(define (add-interval x y)
  (make-interval (+ (lower-bound x) (lower-bound y))
                 (+ (upper-bound x) (upper-bound y))))

(define (sub-interval x y)
   (make-interval (- (lower-bound x) (upper-bound y)) 
                  (- (upper-bound x) (lower-bound y))))

(define (mul-interval x y)
  (let ((p1 (* (lower-bound x) (lower-bound y)))
        (p2 (* (lower-bound x) (upper-bound y)))
        (p3 (* (upper-bound x) (lower-bound y)))
        (p4 (* (upper-bound x) (upper-bound y))))
    (make-interval (min p1 p2 p3 p4)
                   (max p1 p2 p3 p4))))

(define (div-interval x y)
  (mul-interval x
                (make-interval (/ 1.0 (upper-bound y))
                               (/ 1.0 (lower-bound y)))))

(define (make-interval lower upper)
  (cons lower upper))

(define (lower-bound interval)
  (min (car interval) (cdr interval)))

(define (upper-bound interval)
  (max (car interval) (cdr interval)))

; testing
(define interval-first (make-interval 1 10))
(define interval-second (make-interval 100 1000))

(lower-bound interval-first)
(lower-bound interval-second)

(upper-bound interval-first)
(upper-bound interval-second)

(car (add-interval interval-first interval-second))
(cdr (add-interval interval-first interval-second))

(car (mul-interval interval-first interval-second))
(cdr (mul-interval interval-first interval-second))

(car (div-interval interval-first interval-second))
(cdr (div-interval interval-first interval-second))