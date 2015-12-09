(define (reverse-def list)
  (define nil '())
  (define (iter list result)
    (if (null? list)
        result
        (iter (cdr list) (cons (car list) result))))
  (iter list nil))

(define (deep-reverse items)
  (define nil '())
  (define (iter items result)
    (cond ((null? items) result)
           ((pair? (car items))
            (iter (cdr items) (cons (deep-reverse (car items)) result)))
           (else (iter (cdr items) (cons (car items) result)))))
  (iter items nil))

; testing
(define (display-list items)
  (display items)
  (newline))

(define list-a (list 1 2 3 4 5))
(define list-b (list (list 1 2) (list 3 4)))
(define list-c (list 1 (list 2 3) (list 5 (list 6 7 8) 9)))

(display-list (reverse-def list-a))
(display-list (reverse-def list-b))
(display-list (reverse-def list-c))
(display-list (deep-reverse list-a))
(display-list (deep-reverse list-b))
(display-list (deep-reverse list-c))