nasa_string = "nasa_rwanda_field_boundary_competition_source_train_51_2021_08"

dataset_id = 'nasa_rwanda_field_boundary_competition'

def clean_string(s):
    """
    extract the tile id and timestamp from a source image folder
    e.g extract 'ID_YYYY_MM' from 'nasa_rwanda_field_boundary_competition_source_train_ID_YYYY_MM'
    """
    s = s.replace(f"{dataset_id}_source_","").split("_")[1:]
    return "_".join(s)


print(clean_string(nasa_string))
