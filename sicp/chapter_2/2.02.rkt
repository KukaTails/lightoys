; ADT of point
(define (make-point x y)
  (cons x y))

(define (x-point p) (car p))

(define (y-point p) (cdr p))

(define (add-point p-a p-b)
  (make-point (+ (x-point p-a) (x-point p-b))
              (+ (y-point p-a) (y-point p-b))))

(define (div-point p n)
  (make-point (/ (x-point p) n)
              (/ (y-point p) n)))

(define (print-point p)
  (newline)
  (display "(")
  (display (x-point p))
  (display ",")
  (display (y-point p))
  (display ")"))

; testing for point
(print-point (make-point 1 3))
(print-point (make-point 3 3))

; ADT of segment
(define (make-segment start-p end-p)
  (cons start-p end-p))

(define (start-segment segment) (car segment))

(define (end-segment segment) (cdr segment))

(define (print-segment segment)
  (define (print-point p)
    (display "(")
    (display (x-point p))
    (display ",")
    (display (y-point p))
    (display ")"))
  (newline)
  (print-point (start-segment segment))
  (display "->")
  (print-point (end-segment segment)))

; testing for segment
(print-segment (make-segment (make-point 0 0) (make-point 1 1)))


; mid-point of segment
(define (midpoint-segment segment)
  (div-point (add-point (start-segment segment)
                        (end-segment segment))
             2))

; testing for mid-point procedure
(define seg (make-segment (make-point 0 0) (make-point 2 2)))
(print-point (midpoint-segment seg))

(define seg (make-segment (make-point 0 0) (make-point -2 4)))
(print-point (midpoint-segment seg))