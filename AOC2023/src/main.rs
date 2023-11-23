pub mod utilities 
{
    pub mod filereader;
}

use utilities::filereader;



fn main() {
    println!("Hello, world!");

    let input = "D:/git/magic/aoc2023/aoc2023/src/2022-d14/input.txt";
    let input_as_str = filereader::get_file_as_str(input);
    println!("{}", input_as_str);
}
