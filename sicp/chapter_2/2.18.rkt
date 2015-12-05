(define (reverse-def list)
  (define nil '())
  (define (iter list result)
    (if (null? list)
        result
        (iter (cdr list) (cons (car list) result))))
  (iter list nil))

; testing
(define list-a (list 1 2 3 4 5))
(reverse-def list-a)