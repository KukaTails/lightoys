(define (reverse-def list)
  (define nil '())
  (define (iter list result)
    (if (null? list)
        result
        (iter (cdr list) (cons (car list) result))))
  (iter list nil))


(define (same-parity first . rest)
  (define nil '())
  (define parity (modulo first 2))
  (define (iter items result)
    (cond ((null? items) (reverse result))
          ((= (modulo (car items) 2) parity)
           (iter (cdr items) (cons (car items) result)))
          (else (iter (cdr items) result))))
  (iter rest (list first)))

; testing
(display (same-parity 1 2 3 4 5 6 7 8 9 10))
(display (same-parity 2 1 3 5 7 9))