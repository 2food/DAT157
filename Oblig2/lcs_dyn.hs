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
    let (_, lcs) = dynamicLcs xs ys []
    putStr ("Longest common substring: \"" ++ lcs ++ "\" ")
    putStrLn ("length = " ++ show (length lcs))

-- on the form (x, y, answer)
type Record = (String, String, String)

-- starts at beginning of string instead of end because it is faster
dynamicLcs :: String -> String -> [Record] -> ([Record], String)
dynamicLcs "" _ rs = (rs, "")
dynamicLcs _ "" rs = (rs, "")
dynamicLcs x y rs
  | find x y rs /= "" = (rs, find x y rs)
  | head x == head y  = let (drs, ans) = dynamicLcs (tail x) (tail y) rs in
    let newans = head x : ans in
    ((x, y, newans) : drs, newans)
  | otherwise    =
    let (lrs, lans) = dynamicLcs (tail x) y rs in
    let (rrs, rans) = dynamicLcs x (tail y) lrs in
    let ans = longest lans rans in
    ((x, y, ans) : rrs, ans)

longest :: String -> String -> String
longest xs ys = if length xs < length ys then ys else xs


find :: String -> String -> [Record] -> String
find _ _ []     = ""
find x y (r:rs) = case r of
  (f, s, l) -> if x == f && y == s || y == f && x == s
    then l
    else find x y rs
