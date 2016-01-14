(define (have-cycle? ls)
  (define encountered (list))
  (define (visit ls)
    (if (not (pair? ls))
        false
        (if (memq ls encountered)
            true
            (begin (set! encountered (cons ls encountered))
                   (or (visit (car ls))
                       (visit (cdr ls)))))))
  (visit ls))


;; testing
(define test (cons 'a 'b))
(set-car! test test)
(have-cycle? test)