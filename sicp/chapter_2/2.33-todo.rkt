(define nil '())
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))

;; map
(define (map-def proc sequence)
  (accumulate (lambda (x y) (cons (proc x) y))
              nil
              sequence))

;; testing for map
(define test-list (list 1 2 3 4 5 6 7))
(display (map-def (lambda (x) (* x x)) test-list))
(newline)

;; append
(define (append-def seq1 seq2)
  (accumulate (lambda (x y) (cons x y))
              nil
              (cons seq1 seq2)))

;; length
(define (length-def sequence)
  (accumulate (lambda (x y)
                (+ 1 y))
              0 sequence))

(length-def (list -1 0 1 2 3 4 5 6 7 8))