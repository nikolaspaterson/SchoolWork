#lang racket
(require 2htdp/image)
;;PART 1
(define a-red-square (rectangle 100 100 "solid" "red"))
;;PART 2
(define a-blue-circle (circle 50 "solid" "blue"))
;;PART 3
(define outlined-square (rectangle 100 100 "outline" "red"))
(define outlined-circle (circle 50 "outline" "blue"))
;;PART 4
(define row-of-squares (beside (rectangle 100 100 "solid" "red")
                               (rectangle 100 100 "solid" "blue")
                               (rectangle 100 100 "solid" "green")))

(define column-of-squares (above (rectangle 100 100 "solid" "red")
                                 (rectangle 100 100 "solid" "blue")
                                 (rectangle 100 100 "solid" "green")))

(define nested-squares (overlay (rectangle 25 25 "solid" "black")
                                (rectangle 50 50 "solid" "green")
                                (rectangle 75 75 "solid" "blue")
                                (rectangle 100 100 "solid" "red")))
;;PART 5
(define rotated-square (rotate 45 nested-squares))
;;PART 6
(define flag (overlay (rectangle 5 80 "solid" "red")
                      (triangle 50 "solid" "red")
                      (rectangle 50 30 "solid" "red")
                      (rectangle 100 100 "solid" "white")
                      (rectangle 200 100 "solid" "red")))