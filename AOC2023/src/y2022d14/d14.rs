use crate::utilities::filereader;

pub fn d14() -> ()
{
    let input = "D:/git/magic/aoc2023/aoc2023/src/y2022d14/input.txt";
    let input_as_str = filereader::get_file_as_str(input);
    println!("{}", input_as_str);
}