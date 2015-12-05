(define (map-def proc items)
  (define nil '())
  (if (null? items)
      nil
      (cons (proc (car items))
            (map-def proc (cdr items)))))

; testing
(display (map-def (lambda (x) (+ x 1)) (list 1 2 3 4)))
(display (map-def (lambda (x) (* x 2)) (list 2 3 4 5)))