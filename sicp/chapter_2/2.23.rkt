(define nil '())
(define (for-each-def proc items)
  (let ((items-rest (cdr items)))
    (proc (car items))
    (if (null? items-rest)
        true
        (for-each-def proc items-rest))))

; testing
(for-each-def (lambda (x) (newline) (display x))
          (list 57 321 88))