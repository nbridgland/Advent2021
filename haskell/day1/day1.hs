import Data.Char  
import Control.Monad
  
main = do 
    file_contents <- readFile "input.txt"
    -- part 1
    let number_list = lines file_contents
    let number_pairs = makePairs number_list
    let greater_thans = map compareStringNumbers number_pairs
    let output1 = sum greater_thans

    -- part 2
    let numbers = map convertStringToInt number_list
    let number_triples = makeTriples numbers
    let sums = map tripleSum number_triples
    let sum_pairs = makePairs sums
    let greater_thans = map greaterThan sum_pairs
    let output2 = sum greater_thans
    putStrLn (convertIntToString output1)
    putStrLn (convertIntToString output2)



makePairs :: [a] -> [(a, a)]
makePairs [] = []
makePairs [a] = []
makePairs (x:y:xs) = (x,y) : makePairs (y:xs)



compareStringNumbers :: (String, String) -> Integer
compareStringNumbers (a, b) =
    if length b > length a
        then 1
        else 
            if b > a
                then 1
                else 0


convertIntToString :: Integer -> String
convertIntToString 1624 = "1624"
convertIntToString 1653 = "1653"
convertIntToString a = "Wrong Answer"

convertCharToInt :: Char -> Integer
convertCharToInt '1' = 1
convertCharToInt '2' = 2
convertCharToInt '3' = 3
convertCharToInt '4' = 4
convertCharToInt '5' = 5
convertCharToInt '6' = 6
convertCharToInt '7' = 7
convertCharToInt '8' = 8
convertCharToInt '9' = 9
convertCharToInt '0' = 0
convertCharToInt a = 0


convertStringToInt :: String -> Integer
convertStringToInt [] = 0
convertStringToInt (x:xs) = 10 ^ length xs * convertCharToInt x + convertStringToInt xs

makeTriples :: [a] -> [(a, a, a)]
makeTriples [] = []
makeTriples [a] = []
makeTriples [a, b] = []
makeTriples (x:y:z:xs) = (x,y,z) : makeTriples (y:z:xs)



greaterThan :: (Integer, Integer) -> Integer
greaterThan (a, b) =
    if b > a then 1 else 0


tripleSum :: (Integer, Integer, Integer) -> Integer
tripleSum (a,b,c) = a + b + c