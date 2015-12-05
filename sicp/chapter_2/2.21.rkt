(define (square x) (* x x))
(define nil '())

(define (map-def proc items)
  (if (null? items)
      nil
      (cons (proc (car items))
            (map-def proc (cdr items)))))

; version-1
(define (square-list-1 items)
  (if (null? items)
      nil
      (cons (square (car items)) (square-list-1 (cdr items)))))

; version-2
(define (square-list-2 items)
  (map-def (lambda (x) (square x)) items))

; testing for version-1
(display (square-list-1 (list 1 2 3 4 5)))

; testing for version-2
(display (square-list-2 (list 1 2 3 4 5)))