; fib-recursive version
(define (fib-r n)
  (cond ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib-r (- n 1))
                 (fib-r (- n 2))))))

; filter
(define (filter-def predicate sequence)
  (define nil '())
  (cond ((null? sequence) nil)
        ((predicate (car sequence))
         (cons (car sequence)
               (filter predicate (cdr sequence))))
        (else (filter predicate (cdr sequence)))))

; accumulate
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))

; enumerate
(define (enumerate-interval low high)
  (define nil '())
  (if (> low high)
      nil
      (cons low (enumerate-interval (+ low 1) high))))


(define (enumerate-tree tree)
  (define nil '())
  (cond ((null? tree) nil)
        ((not (pair? tree)) (list tree))
        (else (append (enumerate-tree (car tree))
                      (enumerate-tree (cdr tree))))))

; testing
(define nil '())
(accumulate + 0 (list 1 2 3 4 5))
(accumulate * 1 (list 1 2 3 4 5))
(display (accumulate cons nil (list 1 2 3 4 5)))
(newline)

; testing for sum-odd-squares
(define (sum-odd-squares tree)
  (define (square x) (* x x))
  (accumulate +
              0
              (map square
                   (filter odd?
                           (enumerate-tree tree)))))
(sum-odd-squares (list (list 1 2) 3 4 (list 5 8 9)))

; testing for even-fibs n
(define (even?-fibs n)
  (accumulate cons
              nil
              (filter even?
                      (map fib-r
                           (enumerate-interval 0 n)))))

  
(define (list-fib-squares n)
  (define nil '())
  (define (square x) (* x x))
  (accumulate cons
              nil
              (map square
                   (map fib-r
                        (enumerate-interval 0 n)))))
(display (list-fib-squares 10))