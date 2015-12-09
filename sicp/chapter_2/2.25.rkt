(define tree-a (list 1 3 (list 5 7) 9))
(define tree-b (list (list 7)))
(define tree-c (list 1 (list 2 (list 3 (list 4 (list 5 (list 6 7)))))))

(display tree-a)
(newline)
(display tree-b)
(newline)
(display tree-c)
(newline)

; testing
(cdr (car (cdr (cdr tree-a))))
(car (car tree-b))
(display (cdr (car (cdr (car (cdr (car (cdr (car (cdr (car (cdr tree-c))))))))))))