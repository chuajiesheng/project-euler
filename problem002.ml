let main () =
  let a = ref 0 in
  let b = ref 1 in
  let c = ref (!a + !b) in
  let total = ref 0 in
  let _ = while !c < 4000001 do
            let _ = if (!c mod 2 = 0) then
                      total := !total + !c in
            let _ = a := !b in
            let _ = b := !c in
            c := !a + !b
          done
  in
  print_int !total;
  print_string "\n";;

if !Sys.interactive then () else main ();;
