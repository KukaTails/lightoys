(define (memq-def item x)
  (cond ((null? x) false)
        ((eq? item (car x)) x)
        (else (memq item (cdr x)))))

;; testing
(define best-lanuage 'scheme)
(define lanuages '(racket c cpp java scheme python))

(display (memq-def best-lanuage lanuages))

(display (memq-def 'apple '(x (apple sauce) y apple pear)))