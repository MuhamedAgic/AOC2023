pub mod utilities { pub mod filereader; }
pub mod one {pub mod day_one; }

use crate::utilities::filereader;
use crate::one::day_one;



fn main() 
{
    let input = "D:/git/magic/aoc2023/aoc2023/src/one/input.txt";
    let lines = filereader::read_lines(input).unwrap();
    
    let d1p1 = day_one::day_one_part_one(input);
    println!("{}", d1p1);

    let d1p2 = day_one::day_one_part_two(input);
    println!("{}", d1p2);

    // let input_as_str = filereader::get_file_as_str(input);
    // println!("{}", input_as_str);

    // d14::d14();

    //let lines = d14::input_to_2d_list(input);
}
