use std::fs;

pub fn get_file_as_str(path: &str) -> String 
{
    let data = fs::read_to_string(path).expect(format!("Unable to read file '{}'", path).as_str());
    return data;
}