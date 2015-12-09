(define (equal?-def x y)
  (cond ((and (not (pair? x)) (not (pair? y)))
         (eq? x y))
        ((and (pair? x) (pair? y))
         (and (equal?-def (car x) (car y))
              (equal?-def (cdr x) (cdr y))))
        (else false)))

;; testing
(equal?-def 'a 'a)

(equal?-def 'a 'b)

(equal?-def '(1 2 3 (4 5 6)) '(1 2 3 (4 5) 6))

(equal?-def '(1 2 3 (4 5) 6) '(1 2 3 (4 5) 6))