import sys
import glob
import xarray as xr
import intake
import click
from framework import src_header
from framework import src_footer
import os
@click.command()
@click.argument('file_path_name')
@click.argument('dataset_sub_name')
@click.argument('parent_page')
@click.argument('tags')

def generate_catalog(file_path_name, dataset_sub_name, parent_page, tags):
    """
    FILE_NAME: If there are more than one file, FILE_NAME is the pattern for the NetCDF files, otherwise, Name of the NetCDF file. e.g.: 'air.mon.mean.nc' 

    DATASET_SUB_NAME: Name of the directory containing the NetCDf data files, e.g.: 'GHCN_CAMS'. If there is subdirectory like monthly, daily, etc., it should also be included and separated by "_".

    PARENT_PAGE: Name of the parent directory in the dataset type hierarchy, e.g.: Temperature

    TAG: A dataset may need to be catalogued into multiple child catalogs, e.g.: "Atmosphere", "Temperature". Please keep the format consistent
    """
    file_path_name = file_path_name.strip('""')
    path, fileName = os.path.split(file_path_name)
    print("1 :"+ file_path_name)
    print("2 :"+ dataset_sub_name)
    print("3 :"+ parent_page)
    print("4: "+ tags)
    nfiles = len(glob.glob(file_path_name))
    # Set is_combine based on number of files
    if (nfiles > 1):
        is_combine= True
        print("More than one file###")
    else:
        print("one file###")
        is_combine= False

    temp = dataset_sub_name

    #print("file path name is "+ file_path_name)

    #print("dataset_sub_name is "+ dataset_sub_name)

    #print("parent page is " + parent_page)

    if int(is_combine) == True:
        # Read with xarray
        source = xr.open_mfdataset(file_path_name,combine='nested',concat_dim='time')
        src = source
        # Use intake with xarray kwargs
        source = intake.open_netcdf(file_path_name,concat_dim='time',xarray_kwargs={'combine':'nested','decode_times':True})
    else:
        source = intake.open_netcdf(file_path_name)
        src = xr.open_dataset(file_path_name)
        source.discover()
    #print('subname' + dataset_sub_name)
    dataset_sub_name = open(dataset_sub_name.strip('""')+ '.yaml', 'w')
    dataset_sub_name.write(source.yaml())
    dataset_sub_name.close()
    print(str(dataset_sub_name.name) + " was cataloged")
    
    #############################################

    # CATALOG_DIR: Github repository containing the master catalog
    # NOTE: It will be more accurate later
    catalog_dir = "https://raw.githubusercontent.com/kpegion/COLA-DATASETS-CATALOG/gh-pages/intake-catalogs/"


    print(type(path))
    print(path)
            
    open_catalog = catalog_dir + temp +".yaml"

    #print("Here is: {0}".format(open_catalog))
    try:
        title = src.attrs['title'] 
    except:
        title = dataset_sub_name
    try:
        url = src.attrs['References']
    except:
        url =""
    # Here url roles as the location
    url = path
    html_repr =xr.core.formatting_html.dataset_repr(src).replace('\\n', '\n')
    _header = src_header(title, parent_page,  open_catalog, url, tags, open_catalog)

    tags =tags.split(',')
    _footer = src_footer()
    html_src = _header + html_repr + _footer
    page_name = fileName.replace('*','').replace('..','.')
    html_page = page_name +".html" 
    with open(html_page , "w") as file:
        file.write(html_src)

    print( html_page + " was created\n")
if __name__ == "__main__":
    generate_catalog()

