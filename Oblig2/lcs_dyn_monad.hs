import           System.Environment

main :: IO ()
main = do
  args <- getArgs
  if length args < 2 then
    putStrLn "You must provide 2 argument strings!"
  else do
    let x = head args
    let y = args !! 1
    putStrLn ("X = " ++ show x)
    putStrLn ("Y = " ++ show y)
    let (lcs, _) = app (dynamicLcs x y) []
    putStr ("Longest common substring: \"" ++ lcs ++ "\" ")
    putStrLn ("length = " ++ show (length lcs))

type Records = [(String, String, String)]
newtype Memory a = M (Records -> (a, Records))

app :: Memory a -> Records -> (a, Records)
app (M m) = m

instance Functor Memory where
  fmap g mem = M (\r -> let (x, r') = app mem r in (g x, r'))

instance Applicative Memory where
  pure x = M (\r -> (x,r))
  memf <*> memx = M (\r ->
    let (f, r') = app memf r
        (x, r'') = app memx r' in (f x, r''))

instance Monad Memory where
  mem >>= f = M (\r -> let (x,r') = app mem r in app (f x) r')

addResult :: (String, String, String) -> Memory ()
addResult (x, y, res) = M (\r -> ( () , (x,y,res):r))

search :: String -> String -> Memory String
search x y = M (\r -> let res = find r in (res , r))
  where find [] = ""
        find ((a,b,c):rs) = if x == a && y == b || y == a && x == b
          then c
          else find rs

dynamicLcs :: String -> String -> Memory String
dynamicLcs "" _ = return ""
dynamicLcs _ "" = return ""
dynamicLcs x y
  | head x == head y = do
    rest <- dynamicLcs (tail x) (tail y)
    return (head x : rest)
  | otherwise    = do
    res <- search x y
    if res == "" then do
      lans <- dynamicLcs (tail x) y
      rans <- dynamicLcs x (tail y)
      let ans = longest lans rans
      addResult (x, y, ans)
      return ans
    else return res

longest :: String -> String -> String
longest xs ys = if length xs < length ys then ys else xs
