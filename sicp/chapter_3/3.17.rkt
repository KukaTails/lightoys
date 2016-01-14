(define (count-pairs x)
  (let ((encountered '()))
    (define (helper x)
      (if (or (not (pair? x)) (memq x encountered))
          0
          (begin
            (set! encountered (cons x encountered))
            (+ (helper (car x))
               (helper (cdr x))
               1))))
    (helper x)))

;; testing
(define third-list (list 'd))
(define second-list (cons third-list third-list))
(define first-list (cons 'b second-list))
(count-pairs first-list)