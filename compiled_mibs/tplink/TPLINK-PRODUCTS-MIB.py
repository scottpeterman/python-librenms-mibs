# SNMP MIB module (TPLINK-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tplink\TPLINK-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:36 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tplinkProducts,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkProducts")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tplink_tlsl5428_ObjectIdentity = ObjectIdentity
tplink_tlsl5428 = _Tplink_tlsl5428_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 1)
)
_Tplink_tlsl3452_ObjectIdentity = ObjectIdentity
tplink_tlsl3452 = _Tplink_tlsl3452_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 2)
)
_Tplink_tlsg3424_ObjectIdentity = ObjectIdentity
tplink_tlsg3424 = _Tplink_tlsg3424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 3)
)
_Tplink_tlsg3216_ObjectIdentity = ObjectIdentity
tplink_tlsg3216 = _Tplink_tlsg3216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 4)
)
_Tplink_tlsg3210_ObjectIdentity = ObjectIdentity
tplink_tlsg3210 = _Tplink_tlsg3210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 5)
)
_Tplink_tlsl3428_ObjectIdentity = ObjectIdentity
tplink_tlsl3428 = _Tplink_tlsl3428_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 6)
)
_Tplink_tlsg5428_ObjectIdentity = ObjectIdentity
tplink_tlsg5428 = _Tplink_tlsg5428_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 7)
)
_Tplink_tlsg3424p_ObjectIdentity = ObjectIdentity
tplink_tlsg3424p = _Tplink_tlsg3424p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 8)
)
_Tplink_tlsg5412f_ObjectIdentity = ObjectIdentity
tplink_tlsg5412f = _Tplink_tlsg5412f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 9)
)
_Tplink_t2700_28tct_ObjectIdentity = ObjectIdentity
tplink_t2700_28tct = _Tplink_t2700_28tct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 10)
)
_Tplink_tlsl2428_ObjectIdentity = ObjectIdentity
tplink_tlsl2428 = _Tplink_tlsl2428_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 11)
)
_Tplink_tlsg2216_ObjectIdentity = ObjectIdentity
tplink_tlsg2216 = _Tplink_tlsg2216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 12)
)
_Tplink_tlsg2424_ObjectIdentity = ObjectIdentity
tplink_tlsg2424 = _Tplink_tlsg2424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 13)
)
_Tplink_tlsg5428cn_ObjectIdentity = ObjectIdentity
tplink_tlsg5428cn = _Tplink_tlsg5428cn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 14)
)
_Tplink_tlsg2452_ObjectIdentity = ObjectIdentity
tplink_tlsg2452 = _Tplink_tlsg2452_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 15)
)
_Tplink_tlsl2218_ObjectIdentity = ObjectIdentity
tplink_tlsl2218 = _Tplink_tlsl2218_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 16)
)
_Tplink_tlsg2424p_ObjectIdentity = ObjectIdentity
tplink_tlsg2424p = _Tplink_tlsg2424p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 17)
)
_Tplink_tlsg2210_ObjectIdentity = ObjectIdentity
tplink_tlsg2210 = _Tplink_tlsg2210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 18)
)
_Tplink_tlsl2210_ObjectIdentity = ObjectIdentity
tplink_tlsl2210 = _Tplink_tlsl2210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 19)
)
_Tplink_t3700g_28tq_ObjectIdentity = ObjectIdentity
tplink_t3700g_28tq = _Tplink_t3700g_28tq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 20)
)
_Tplink_tlsl2226p_ObjectIdentity = ObjectIdentity
tplink_tlsl2226p = _Tplink_tlsl2226p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 21)
)
_Tplink_tlsl2452_ObjectIdentity = ObjectIdentity
tplink_tlsl2452 = _Tplink_tlsl2452_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 22)
)
_Tplink_tlsl2218p_ObjectIdentity = ObjectIdentity
tplink_tlsl2218p = _Tplink_tlsl2218p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 23)
)
_Tplink_tlsg3424_ipv6_ObjectIdentity = ObjectIdentity
tplink_tlsg3424_ipv6 = _Tplink_tlsg3424_ipv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 24)
)
_Tplink_tlsg2008_ObjectIdentity = ObjectIdentity
tplink_tlsg2008 = _Tplink_tlsg2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 25)
)
_Tplink_tlsg2210p_ObjectIdentity = ObjectIdentity
tplink_tlsg2210p = _Tplink_tlsg2210p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 26)
)
_Tplink_t2700g_28tq_ObjectIdentity = ObjectIdentity
tplink_t2700g_28tq = _Tplink_t2700g_28tq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 27)
)
_Tplink_t1600g_28ts_ObjectIdentity = ObjectIdentity
tplink_t1600g_28ts = _Tplink_t1600g_28ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 28)
)
_Tplink_t1600g_52ts_ObjectIdentity = ObjectIdentity
tplink_t1600g_52ts = _Tplink_t1600g_52ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 29)
)
_Tplink_t3700g_54tq_ObjectIdentity = ObjectIdentity
tplink_t3700g_54tq = _Tplink_t3700g_54tq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 30)
)
_Tplink_t1700g_28tq_ObjectIdentity = ObjectIdentity
tplink_t1700g_28tq = _Tplink_t1700g_28tq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 31)
)
_Tplink_t1700g_52tq_ObjectIdentity = ObjectIdentity
tplink_t1700g_52tq = _Tplink_t1700g_52tq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 32)
)
_Tplink_t2600g_28ts_ObjectIdentity = ObjectIdentity
tplink_t2600g_28ts = _Tplink_t2600g_28ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 33)
)
_Tplink_t2600g_52ts_ObjectIdentity = ObjectIdentity
tplink_t2600g_52ts = _Tplink_t2600g_52ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 34)
)
_Tplink_t1600g_28ps_ObjectIdentity = ObjectIdentity
tplink_t1600g_28ps = _Tplink_t1600g_28ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 37)
)
_Tplink_t1600g_52ps_ObjectIdentity = ObjectIdentity
tplink_t1600g_52ps = _Tplink_t1600g_52ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 38)
)
_Tplink_tlsg2224p_ObjectIdentity = ObjectIdentity
tplink_tlsg2224p = _Tplink_tlsg2224p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 39)
)
_Tplink_tlsg3428_ObjectIdentity = ObjectIdentity
tplink_tlsg3428 = _Tplink_tlsg3428_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 40)
)
_Tplink_t1700x_16ts_ObjectIdentity = ObjectIdentity
tplink_t1700x_16ts = _Tplink_t1700x_16ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 41)
)
_Tplink_t2500_28tc_ObjectIdentity = ObjectIdentity
tplink_t2500_28tc = _Tplink_t2500_28tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 44)
)
_Tplink_t2500g_10ts_ObjectIdentity = ObjectIdentity
tplink_t2500g_10ts = _Tplink_t2500g_10ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 59)
)
_Tplink_t2600g_18ts_ObjectIdentity = ObjectIdentity
tplink_t2600g_18ts = _Tplink_t2600g_18ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 72)
)
_Tplink_t2600g_28mps_ObjectIdentity = ObjectIdentity
tplink_t2600g_28mps = _Tplink_t2600g_28mps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 74)
)
_Tplink_t1500g_8t_ObjectIdentity = ObjectIdentity
tplink_t1500g_8t = _Tplink_t1500g_8t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 76)
)
_Tplink_t1500g_10ps_ObjectIdentity = ObjectIdentity
tplink_t1500g_10ps = _Tplink_t1500g_10ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 78)
)
_Tplink_t1500g_10mps_ObjectIdentity = ObjectIdentity
tplink_t1500g_10mps = _Tplink_t1500g_10mps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 80)
)
_Tplink_t1500_28tc_ObjectIdentity = ObjectIdentity
tplink_t1500_28tc = _Tplink_t1500_28tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 82)
)
_Tplink_t1500_28pct_ObjectIdentity = ObjectIdentity
tplink_t1500_28pct = _Tplink_t1500_28pct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 84)
)
_Tplink_t1600g_18ts_ObjectIdentity = ObjectIdentity
tplink_t1600g_18ts = _Tplink_t1600g_18ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 86)
)
_Tplink_t2500g_10mps_ObjectIdentity = ObjectIdentity
tplink_t2500g_10mps = _Tplink_t2500g_10mps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 88)
)
_Tplink_t2600g_28ps_ObjectIdentity = ObjectIdentity
tplink_t2600g_28ps = _Tplink_t2600g_28ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 90)
)
_Tplink_t2600g_28sq_ObjectIdentity = ObjectIdentity
tplink_t2600g_28sq = _Tplink_t2600g_28sq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 5, 92)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-PRODUCTS-MIB",
    **{"tplink-tlsl5428": tplink_tlsl5428,
       "tplink-tlsl3452": tplink_tlsl3452,
       "tplink-tlsg3424": tplink_tlsg3424,
       "tplink-tlsg3216": tplink_tlsg3216,
       "tplink-tlsg3210": tplink_tlsg3210,
       "tplink-tlsl3428": tplink_tlsl3428,
       "tplink-tlsg5428": tplink_tlsg5428,
       "tplink-tlsg3424p": tplink_tlsg3424p,
       "tplink-tlsg5412f": tplink_tlsg5412f,
       "tplink-t2700-28tct": tplink_t2700_28tct,
       "tplink-tlsl2428": tplink_tlsl2428,
       "tplink-tlsg2216": tplink_tlsg2216,
       "tplink-tlsg2424": tplink_tlsg2424,
       "tplink-tlsg5428cn": tplink_tlsg5428cn,
       "tplink-tlsg2452": tplink_tlsg2452,
       "tplink-tlsl2218": tplink_tlsl2218,
       "tplink-tlsg2424p": tplink_tlsg2424p,
       "tplink-tlsg2210": tplink_tlsg2210,
       "tplink-tlsl2210": tplink_tlsl2210,
       "tplink-t3700g-28tq": tplink_t3700g_28tq,
       "tplink-tlsl2226p": tplink_tlsl2226p,
       "tplink-tlsl2452": tplink_tlsl2452,
       "tplink-tlsl2218p": tplink_tlsl2218p,
       "tplink-tlsg3424-ipv6": tplink_tlsg3424_ipv6,
       "tplink-tlsg2008": tplink_tlsg2008,
       "tplink-tlsg2210p": tplink_tlsg2210p,
       "tplink-t2700g-28tq": tplink_t2700g_28tq,
       "tplink-t1600g-28ts": tplink_t1600g_28ts,
       "tplink-t1600g-52ts": tplink_t1600g_52ts,
       "tplink-t3700g-54tq": tplink_t3700g_54tq,
       "tplink-t1700g-28tq": tplink_t1700g_28tq,
       "tplink-t1700g-52tq": tplink_t1700g_52tq,
       "tplink-t2600g-28ts": tplink_t2600g_28ts,
       "tplink-t2600g-52ts": tplink_t2600g_52ts,
       "tplink-t1600g-28ps": tplink_t1600g_28ps,
       "tplink-t1600g-52ps": tplink_t1600g_52ps,
       "tplink-tlsg2224p": tplink_tlsg2224p,
       "tplink-tlsg3428": tplink_tlsg3428,
       "tplink-t1700x-16ts": tplink_t1700x_16ts,
       "tplink-t2500-28tc": tplink_t2500_28tc,
       "tplink-t2500g-10ts": tplink_t2500g_10ts,
       "tplink-t2600g-18ts": tplink_t2600g_18ts,
       "tplink-t2600g-28mps": tplink_t2600g_28mps,
       "tplink-t1500g-8t": tplink_t1500g_8t,
       "tplink-t1500g-10ps": tplink_t1500g_10ps,
       "tplink-t1500g-10mps": tplink_t1500g_10mps,
       "tplink-t1500-28tc": tplink_t1500_28tc,
       "tplink-t1500-28pct": tplink_t1500_28pct,
       "tplink-t1600g-18ts": tplink_t1600g_18ts,
       "tplink-t2500g-10mps": tplink_t2500g_10mps,
       "tplink-t2600g-28ps": tplink_t2600g_28ps,
       "tplink-t2600g-28sq": tplink_t2600g_28sq}
)
