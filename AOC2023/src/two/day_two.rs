use crate::utilities::filereader;
use crate::utilities::stringutils;


fn return_possible_game_id(line: &str) -> Option<i32>
{
    let max_red = 12;
    let max_green = 13;
    let max_blue = 14;

    if let Some((game, game_data)) = stringutils::split_string(line, ':')
    {
        let game_id = game.split(" ").nth(1).unwrap();
        let grabs: Vec<&str> = game_data.split(";").collect();
        println!("{:?}", grabs);

        let mut max_amount_red_detected = 0;
        let mut max_amount_green_detected = 0;
        let mut max_amount_blue_detected = 0;

        for grab in grabs
        {
            // split on , for rgb split
            let rgb: Vec<&str> = grab.split(",").collect();
            //println!("{:?}", rgb);

            for value in rgb
            {
                //println!("{:?}", value);

                // sorry too lazy
                if value.contains("red")
                {
                    let r_val = value.split(" ")
                                               .nth(1)
                                               .unwrap()
                                               .parse::<i32>()
                                               .unwrap();
                    if r_val > max_amount_red_detected
                    {
                        max_amount_red_detected = r_val;
                    }                     
                }
                if value.contains("green")
                {
                    let g_val = value.split(" ")
                                               .nth(1)
                                               .unwrap()
                                               .parse::<i32>()
                                               .unwrap();
                    if g_val > max_amount_green_detected
                    {
                        max_amount_green_detected = g_val;
                    }
                }
                if value.contains("blue")
                {
                    let b_val = value.split(" ")
                                               .nth(1)
                                               .unwrap()
                                               .parse::<i32>()
                                               .unwrap();
                    if b_val > max_amount_blue_detected
                    {
                        max_amount_blue_detected = b_val;
                    }
                }
            }
        }
        
        println!("Max R {}, Max G {}, Max B {}", max_amount_red_detected, max_amount_green_detected, max_amount_blue_detected);

        if max_amount_red_detected <= max_red
        && max_amount_green_detected <= max_green
        && max_amount_blue_detected <= max_blue
        {
            println!("Game: {}", game_id);
            return Some(game_id.parse::<i32>().unwrap());
        }
        println!(" ");
    }
    else
    {
        println!("Something went wrong with loading game data");
    }

    return None;
}

pub fn day_two_part_one(filename: &str) -> i32
{
    let lines = filereader::read_lines(filename).unwrap();

    let mut sum_impossible_game_ids = 0;
    for line in lines
    {
        if let Some(game_id) = return_possible_game_id(line.unwrap().as_str())
        {
            sum_impossible_game_ids += game_id;
        }
    }
    return sum_impossible_game_ids;
}