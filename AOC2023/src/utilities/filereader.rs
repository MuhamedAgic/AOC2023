use std::fs;

pub fn get_file_as_str(path: &str) -> String 
{
    let data = fs::read_to_string(path).expect("Unable to read file");
    return data;
}