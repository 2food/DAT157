import           System.Environment

main :: IO ()
main = do
  args <- getArgs
  if length args < 2 then
    putStrLn "You must provide 2 argument strings!"
  else do
    let xs = head args
    let ys = args !! 1
    putStrLn ("X = " ++ show xs)
    putStrLn ("Y = " ++ show ys)
    let lcs = recursiveLcs xs ys
    putStr ("Longest common substring: \"" ++ lcs ++ "\" ")
    putStrLn ("length = " ++ show (length lcs))

-- starts at beginning of string instead of end because it is faster
recursiveLcs :: String -> String -> String
recursiveLcs [] _ = ""
recursiveLcs _ [] = ""
recursiveLcs (x:xs) (y:ys)
  | x == y    = x : recursiveLcs xs ys
  | otherwise = longest (recursiveLcs xs (y:ys)) (recursiveLcs (x:xs) ys)

longest :: String -> String -> String
longest xs ys = if length xs < length ys then ys else xs
