# SNMP MIB module (GS-GXW42XX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\grandstream\GS-GXW42XX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:57 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Grandstream_ObjectIdentity = ObjectIdentity
grandstream = _Grandstream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397)
)
_ProductFamily_ObjectIdentity = ObjectIdentity
productFamily = _ProductFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1)
)
_Gxw42xx_ObjectIdentity = ObjectIdentity
gxw42xx = _Gxw42xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1)
)


class _PartNo_Type(DisplayString):
    """Custom type partNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PartNo_Type.__name__ = "DisplayString"
_PartNo_Object = MibScalar
partNo = _PartNo_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 1),
    _PartNo_Type()
)
partNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partNo.setStatus("current")
_Ports_ObjectIdentity = ObjectIdentity
ports = _Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2)
)
_HookStatus_ObjectIdentity = ObjectIdentity
hookStatus = _HookStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1)
)


class _HookStatus1_Type(DisplayString):
    """Custom type hookStatus1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus1_Type.__name__ = "DisplayString"
_HookStatus1_Object = MibScalar
hookStatus1 = _HookStatus1_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 1),
    _HookStatus1_Type()
)
hookStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus1.setStatus("current")


class _HookStatus2_Type(DisplayString):
    """Custom type hookStatus2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus2_Type.__name__ = "DisplayString"
_HookStatus2_Object = MibScalar
hookStatus2 = _HookStatus2_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 2),
    _HookStatus2_Type()
)
hookStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus2.setStatus("current")


class _HookStatus3_Type(DisplayString):
    """Custom type hookStatus3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus3_Type.__name__ = "DisplayString"
_HookStatus3_Object = MibScalar
hookStatus3 = _HookStatus3_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 3),
    _HookStatus3_Type()
)
hookStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus3.setStatus("current")


class _HookStatus4_Type(DisplayString):
    """Custom type hookStatus4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus4_Type.__name__ = "DisplayString"
_HookStatus4_Object = MibScalar
hookStatus4 = _HookStatus4_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 4),
    _HookStatus4_Type()
)
hookStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus4.setStatus("current")


class _HookStatus5_Type(DisplayString):
    """Custom type hookStatus5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus5_Type.__name__ = "DisplayString"
_HookStatus5_Object = MibScalar
hookStatus5 = _HookStatus5_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 5),
    _HookStatus5_Type()
)
hookStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus5.setStatus("current")


class _HookStatus6_Type(DisplayString):
    """Custom type hookStatus6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus6_Type.__name__ = "DisplayString"
_HookStatus6_Object = MibScalar
hookStatus6 = _HookStatus6_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 6),
    _HookStatus6_Type()
)
hookStatus6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus6.setStatus("current")


class _HookStatus7_Type(DisplayString):
    """Custom type hookStatus7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus7_Type.__name__ = "DisplayString"
_HookStatus7_Object = MibScalar
hookStatus7 = _HookStatus7_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 7),
    _HookStatus7_Type()
)
hookStatus7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus7.setStatus("current")


class _HookStatus8_Type(DisplayString):
    """Custom type hookStatus8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus8_Type.__name__ = "DisplayString"
_HookStatus8_Object = MibScalar
hookStatus8 = _HookStatus8_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 8),
    _HookStatus8_Type()
)
hookStatus8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus8.setStatus("current")


class _HookStatus9_Type(DisplayString):
    """Custom type hookStatus9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus9_Type.__name__ = "DisplayString"
_HookStatus9_Object = MibScalar
hookStatus9 = _HookStatus9_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 9),
    _HookStatus9_Type()
)
hookStatus9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus9.setStatus("current")


class _HookStatus10_Type(DisplayString):
    """Custom type hookStatus10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus10_Type.__name__ = "DisplayString"
_HookStatus10_Object = MibScalar
hookStatus10 = _HookStatus10_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 10),
    _HookStatus10_Type()
)
hookStatus10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus10.setStatus("current")


class _HookStatus11_Type(DisplayString):
    """Custom type hookStatus11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus11_Type.__name__ = "DisplayString"
_HookStatus11_Object = MibScalar
hookStatus11 = _HookStatus11_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 11),
    _HookStatus11_Type()
)
hookStatus11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus11.setStatus("current")


class _HookStatus12_Type(DisplayString):
    """Custom type hookStatus12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus12_Type.__name__ = "DisplayString"
_HookStatus12_Object = MibScalar
hookStatus12 = _HookStatus12_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 12),
    _HookStatus12_Type()
)
hookStatus12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus12.setStatus("current")


class _HookStatus13_Type(DisplayString):
    """Custom type hookStatus13 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus13_Type.__name__ = "DisplayString"
_HookStatus13_Object = MibScalar
hookStatus13 = _HookStatus13_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 13),
    _HookStatus13_Type()
)
hookStatus13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus13.setStatus("current")


class _HookStatus14_Type(DisplayString):
    """Custom type hookStatus14 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus14_Type.__name__ = "DisplayString"
_HookStatus14_Object = MibScalar
hookStatus14 = _HookStatus14_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 14),
    _HookStatus14_Type()
)
hookStatus14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus14.setStatus("current")


class _HookStatus15_Type(DisplayString):
    """Custom type hookStatus15 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus15_Type.__name__ = "DisplayString"
_HookStatus15_Object = MibScalar
hookStatus15 = _HookStatus15_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 15),
    _HookStatus15_Type()
)
hookStatus15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus15.setStatus("current")


class _HookStatus16_Type(DisplayString):
    """Custom type hookStatus16 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus16_Type.__name__ = "DisplayString"
_HookStatus16_Object = MibScalar
hookStatus16 = _HookStatus16_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 16),
    _HookStatus16_Type()
)
hookStatus16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus16.setStatus("current")


class _HookStatus17_Type(DisplayString):
    """Custom type hookStatus17 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus17_Type.__name__ = "DisplayString"
_HookStatus17_Object = MibScalar
hookStatus17 = _HookStatus17_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 17),
    _HookStatus17_Type()
)
hookStatus17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus17.setStatus("current")


class _HookStatus18_Type(DisplayString):
    """Custom type hookStatus18 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus18_Type.__name__ = "DisplayString"
_HookStatus18_Object = MibScalar
hookStatus18 = _HookStatus18_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 18),
    _HookStatus18_Type()
)
hookStatus18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus18.setStatus("current")


class _HookStatus19_Type(DisplayString):
    """Custom type hookStatus19 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus19_Type.__name__ = "DisplayString"
_HookStatus19_Object = MibScalar
hookStatus19 = _HookStatus19_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 19),
    _HookStatus19_Type()
)
hookStatus19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus19.setStatus("current")


class _HookStatus20_Type(DisplayString):
    """Custom type hookStatus20 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus20_Type.__name__ = "DisplayString"
_HookStatus20_Object = MibScalar
hookStatus20 = _HookStatus20_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 20),
    _HookStatus20_Type()
)
hookStatus20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus20.setStatus("current")


class _HookStatus21_Type(DisplayString):
    """Custom type hookStatus21 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus21_Type.__name__ = "DisplayString"
_HookStatus21_Object = MibScalar
hookStatus21 = _HookStatus21_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 21),
    _HookStatus21_Type()
)
hookStatus21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus21.setStatus("current")


class _HookStatus22_Type(DisplayString):
    """Custom type hookStatus22 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus22_Type.__name__ = "DisplayString"
_HookStatus22_Object = MibScalar
hookStatus22 = _HookStatus22_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 22),
    _HookStatus22_Type()
)
hookStatus22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus22.setStatus("current")


class _HookStatus23_Type(DisplayString):
    """Custom type hookStatus23 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus23_Type.__name__ = "DisplayString"
_HookStatus23_Object = MibScalar
hookStatus23 = _HookStatus23_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 23),
    _HookStatus23_Type()
)
hookStatus23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus23.setStatus("current")


class _HookStatus24_Type(DisplayString):
    """Custom type hookStatus24 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus24_Type.__name__ = "DisplayString"
_HookStatus24_Object = MibScalar
hookStatus24 = _HookStatus24_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 24),
    _HookStatus24_Type()
)
hookStatus24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus24.setStatus("current")


class _HookStatus25_Type(DisplayString):
    """Custom type hookStatus25 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus25_Type.__name__ = "DisplayString"
_HookStatus25_Object = MibScalar
hookStatus25 = _HookStatus25_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 25),
    _HookStatus25_Type()
)
hookStatus25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus25.setStatus("current")


class _HookStatus26_Type(DisplayString):
    """Custom type hookStatus26 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus26_Type.__name__ = "DisplayString"
_HookStatus26_Object = MibScalar
hookStatus26 = _HookStatus26_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 26),
    _HookStatus26_Type()
)
hookStatus26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus26.setStatus("current")


class _HookStatus27_Type(DisplayString):
    """Custom type hookStatus27 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus27_Type.__name__ = "DisplayString"
_HookStatus27_Object = MibScalar
hookStatus27 = _HookStatus27_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 27),
    _HookStatus27_Type()
)
hookStatus27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus27.setStatus("current")


class _HookStatus28_Type(DisplayString):
    """Custom type hookStatus28 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus28_Type.__name__ = "DisplayString"
_HookStatus28_Object = MibScalar
hookStatus28 = _HookStatus28_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 28),
    _HookStatus28_Type()
)
hookStatus28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus28.setStatus("current")


class _HookStatus29_Type(DisplayString):
    """Custom type hookStatus29 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus29_Type.__name__ = "DisplayString"
_HookStatus29_Object = MibScalar
hookStatus29 = _HookStatus29_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 29),
    _HookStatus29_Type()
)
hookStatus29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus29.setStatus("current")


class _HookStatus30_Type(DisplayString):
    """Custom type hookStatus30 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus30_Type.__name__ = "DisplayString"
_HookStatus30_Object = MibScalar
hookStatus30 = _HookStatus30_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 30),
    _HookStatus30_Type()
)
hookStatus30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus30.setStatus("current")


class _HookStatus31_Type(DisplayString):
    """Custom type hookStatus31 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus31_Type.__name__ = "DisplayString"
_HookStatus31_Object = MibScalar
hookStatus31 = _HookStatus31_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 31),
    _HookStatus31_Type()
)
hookStatus31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus31.setStatus("current")


class _HookStatus32_Type(DisplayString):
    """Custom type hookStatus32 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus32_Type.__name__ = "DisplayString"
_HookStatus32_Object = MibScalar
hookStatus32 = _HookStatus32_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 32),
    _HookStatus32_Type()
)
hookStatus32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus32.setStatus("current")


class _HookStatus33_Type(DisplayString):
    """Custom type hookStatus33 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus33_Type.__name__ = "DisplayString"
_HookStatus33_Object = MibScalar
hookStatus33 = _HookStatus33_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 33),
    _HookStatus33_Type()
)
hookStatus33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus33.setStatus("current")


class _HookStatus34_Type(DisplayString):
    """Custom type hookStatus34 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus34_Type.__name__ = "DisplayString"
_HookStatus34_Object = MibScalar
hookStatus34 = _HookStatus34_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 34),
    _HookStatus34_Type()
)
hookStatus34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus34.setStatus("current")


class _HookStatus35_Type(DisplayString):
    """Custom type hookStatus35 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus35_Type.__name__ = "DisplayString"
_HookStatus35_Object = MibScalar
hookStatus35 = _HookStatus35_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 35),
    _HookStatus35_Type()
)
hookStatus35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus35.setStatus("current")


class _HookStatus36_Type(DisplayString):
    """Custom type hookStatus36 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus36_Type.__name__ = "DisplayString"
_HookStatus36_Object = MibScalar
hookStatus36 = _HookStatus36_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 36),
    _HookStatus36_Type()
)
hookStatus36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus36.setStatus("current")


class _HookStatus37_Type(DisplayString):
    """Custom type hookStatus37 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus37_Type.__name__ = "DisplayString"
_HookStatus37_Object = MibScalar
hookStatus37 = _HookStatus37_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 37),
    _HookStatus37_Type()
)
hookStatus37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus37.setStatus("current")


class _HookStatus38_Type(DisplayString):
    """Custom type hookStatus38 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus38_Type.__name__ = "DisplayString"
_HookStatus38_Object = MibScalar
hookStatus38 = _HookStatus38_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 38),
    _HookStatus38_Type()
)
hookStatus38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus38.setStatus("current")


class _HookStatus39_Type(DisplayString):
    """Custom type hookStatus39 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus39_Type.__name__ = "DisplayString"
_HookStatus39_Object = MibScalar
hookStatus39 = _HookStatus39_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 39),
    _HookStatus39_Type()
)
hookStatus39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus39.setStatus("current")


class _HookStatus40_Type(DisplayString):
    """Custom type hookStatus40 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus40_Type.__name__ = "DisplayString"
_HookStatus40_Object = MibScalar
hookStatus40 = _HookStatus40_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 40),
    _HookStatus40_Type()
)
hookStatus40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus40.setStatus("current")


class _HookStatus41_Type(DisplayString):
    """Custom type hookStatus41 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus41_Type.__name__ = "DisplayString"
_HookStatus41_Object = MibScalar
hookStatus41 = _HookStatus41_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 41),
    _HookStatus41_Type()
)
hookStatus41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus41.setStatus("current")


class _HookStatus42_Type(DisplayString):
    """Custom type hookStatus42 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus42_Type.__name__ = "DisplayString"
_HookStatus42_Object = MibScalar
hookStatus42 = _HookStatus42_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 42),
    _HookStatus42_Type()
)
hookStatus42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus42.setStatus("current")


class _HookStatus43_Type(DisplayString):
    """Custom type hookStatus43 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus43_Type.__name__ = "DisplayString"
_HookStatus43_Object = MibScalar
hookStatus43 = _HookStatus43_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 43),
    _HookStatus43_Type()
)
hookStatus43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus43.setStatus("current")


class _HookStatus44_Type(DisplayString):
    """Custom type hookStatus44 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus44_Type.__name__ = "DisplayString"
_HookStatus44_Object = MibScalar
hookStatus44 = _HookStatus44_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 44),
    _HookStatus44_Type()
)
hookStatus44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus44.setStatus("current")


class _HookStatus45_Type(DisplayString):
    """Custom type hookStatus45 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus45_Type.__name__ = "DisplayString"
_HookStatus45_Object = MibScalar
hookStatus45 = _HookStatus45_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 45),
    _HookStatus45_Type()
)
hookStatus45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus45.setStatus("current")


class _HookStatus46_Type(DisplayString):
    """Custom type hookStatus46 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus46_Type.__name__ = "DisplayString"
_HookStatus46_Object = MibScalar
hookStatus46 = _HookStatus46_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 46),
    _HookStatus46_Type()
)
hookStatus46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus46.setStatus("current")


class _HookStatus47_Type(DisplayString):
    """Custom type hookStatus47 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus47_Type.__name__ = "DisplayString"
_HookStatus47_Object = MibScalar
hookStatus47 = _HookStatus47_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 47),
    _HookStatus47_Type()
)
hookStatus47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus47.setStatus("current")


class _HookStatus48_Type(DisplayString):
    """Custom type hookStatus48 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus48_Type.__name__ = "DisplayString"
_HookStatus48_Object = MibScalar
hookStatus48 = _HookStatus48_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 48),
    _HookStatus48_Type()
)
hookStatus48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus48.setStatus("current")


class _HookStatus49_Type(DisplayString):
    """Custom type hookStatus49 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus49_Type.__name__ = "DisplayString"
_HookStatus49_Object = MibScalar
hookStatus49 = _HookStatus49_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 49),
    _HookStatus49_Type()
)
hookStatus49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus49.setStatus("current")


class _HookStatus50_Type(DisplayString):
    """Custom type hookStatus50 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus50_Type.__name__ = "DisplayString"
_HookStatus50_Object = MibScalar
hookStatus50 = _HookStatus50_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 50),
    _HookStatus50_Type()
)
hookStatus50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus50.setStatus("current")


class _HookStatus51_Type(DisplayString):
    """Custom type hookStatus51 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus51_Type.__name__ = "DisplayString"
_HookStatus51_Object = MibScalar
hookStatus51 = _HookStatus51_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 51),
    _HookStatus51_Type()
)
hookStatus51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus51.setStatus("current")


class _HookStatus52_Type(DisplayString):
    """Custom type hookStatus52 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus52_Type.__name__ = "DisplayString"
_HookStatus52_Object = MibScalar
hookStatus52 = _HookStatus52_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 52),
    _HookStatus52_Type()
)
hookStatus52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus52.setStatus("current")


class _HookStatus53_Type(DisplayString):
    """Custom type hookStatus53 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus53_Type.__name__ = "DisplayString"
_HookStatus53_Object = MibScalar
hookStatus53 = _HookStatus53_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 53),
    _HookStatus53_Type()
)
hookStatus53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus53.setStatus("current")


class _HookStatus54_Type(DisplayString):
    """Custom type hookStatus54 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus54_Type.__name__ = "DisplayString"
_HookStatus54_Object = MibScalar
hookStatus54 = _HookStatus54_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 54),
    _HookStatus54_Type()
)
hookStatus54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus54.setStatus("current")


class _HookStatus55_Type(DisplayString):
    """Custom type hookStatus55 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus55_Type.__name__ = "DisplayString"
_HookStatus55_Object = MibScalar
hookStatus55 = _HookStatus55_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 55),
    _HookStatus55_Type()
)
hookStatus55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus55.setStatus("current")


class _HookStatus56_Type(DisplayString):
    """Custom type hookStatus56 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus56_Type.__name__ = "DisplayString"
_HookStatus56_Object = MibScalar
hookStatus56 = _HookStatus56_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 56),
    _HookStatus56_Type()
)
hookStatus56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus56.setStatus("current")


class _HookStatus57_Type(DisplayString):
    """Custom type hookStatus57 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus57_Type.__name__ = "DisplayString"
_HookStatus57_Object = MibScalar
hookStatus57 = _HookStatus57_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 57),
    _HookStatus57_Type()
)
hookStatus57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus57.setStatus("current")


class _HookStatus58_Type(DisplayString):
    """Custom type hookStatus58 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus58_Type.__name__ = "DisplayString"
_HookStatus58_Object = MibScalar
hookStatus58 = _HookStatus58_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 58),
    _HookStatus58_Type()
)
hookStatus58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus58.setStatus("current")


class _HookStatus59_Type(DisplayString):
    """Custom type hookStatus59 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus59_Type.__name__ = "DisplayString"
_HookStatus59_Object = MibScalar
hookStatus59 = _HookStatus59_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 59),
    _HookStatus59_Type()
)
hookStatus59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus59.setStatus("current")


class _HookStatus60_Type(DisplayString):
    """Custom type hookStatus60 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus60_Type.__name__ = "DisplayString"
_HookStatus60_Object = MibScalar
hookStatus60 = _HookStatus60_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 60),
    _HookStatus60_Type()
)
hookStatus60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus60.setStatus("current")


class _HookStatus61_Type(DisplayString):
    """Custom type hookStatus61 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus61_Type.__name__ = "DisplayString"
_HookStatus61_Object = MibScalar
hookStatus61 = _HookStatus61_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 61),
    _HookStatus61_Type()
)
hookStatus61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus61.setStatus("current")


class _HookStatus62_Type(DisplayString):
    """Custom type hookStatus62 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus62_Type.__name__ = "DisplayString"
_HookStatus62_Object = MibScalar
hookStatus62 = _HookStatus62_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 62),
    _HookStatus62_Type()
)
hookStatus62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus62.setStatus("current")


class _HookStatus63_Type(DisplayString):
    """Custom type hookStatus63 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus63_Type.__name__ = "DisplayString"
_HookStatus63_Object = MibScalar
hookStatus63 = _HookStatus63_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 63),
    _HookStatus63_Type()
)
hookStatus63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus63.setStatus("current")


class _HookStatus64_Type(DisplayString):
    """Custom type hookStatus64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus64_Type.__name__ = "DisplayString"
_HookStatus64_Object = MibScalar
hookStatus64 = _HookStatus64_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 64),
    _HookStatus64_Type()
)
hookStatus64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus64.setStatus("current")


class _HookStatus65_Type(DisplayString):
    """Custom type hookStatus65 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus65_Type.__name__ = "DisplayString"
_HookStatus65_Object = MibScalar
hookStatus65 = _HookStatus65_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 65),
    _HookStatus65_Type()
)
hookStatus65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus65.setStatus("current")


class _HookStatus66_Type(DisplayString):
    """Custom type hookStatus66 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus66_Type.__name__ = "DisplayString"
_HookStatus66_Object = MibScalar
hookStatus66 = _HookStatus66_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 66),
    _HookStatus66_Type()
)
hookStatus66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus66.setStatus("current")


class _HookStatus67_Type(DisplayString):
    """Custom type hookStatus67 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus67_Type.__name__ = "DisplayString"
_HookStatus67_Object = MibScalar
hookStatus67 = _HookStatus67_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 67),
    _HookStatus67_Type()
)
hookStatus67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus67.setStatus("current")


class _HookStatus68_Type(DisplayString):
    """Custom type hookStatus68 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus68_Type.__name__ = "DisplayString"
_HookStatus68_Object = MibScalar
hookStatus68 = _HookStatus68_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 68),
    _HookStatus68_Type()
)
hookStatus68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus68.setStatus("current")


class _HookStatus69_Type(DisplayString):
    """Custom type hookStatus69 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus69_Type.__name__ = "DisplayString"
_HookStatus69_Object = MibScalar
hookStatus69 = _HookStatus69_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 69),
    _HookStatus69_Type()
)
hookStatus69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus69.setStatus("current")


class _HookStatus70_Type(DisplayString):
    """Custom type hookStatus70 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus70_Type.__name__ = "DisplayString"
_HookStatus70_Object = MibScalar
hookStatus70 = _HookStatus70_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 70),
    _HookStatus70_Type()
)
hookStatus70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus70.setStatus("current")


class _HookStatus71_Type(DisplayString):
    """Custom type hookStatus71 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus71_Type.__name__ = "DisplayString"
_HookStatus71_Object = MibScalar
hookStatus71 = _HookStatus71_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 71),
    _HookStatus71_Type()
)
hookStatus71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus71.setStatus("current")


class _HookStatus72_Type(DisplayString):
    """Custom type hookStatus72 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus72_Type.__name__ = "DisplayString"
_HookStatus72_Object = MibScalar
hookStatus72 = _HookStatus72_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 72),
    _HookStatus72_Type()
)
hookStatus72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus72.setStatus("current")


class _HookStatus73_Type(DisplayString):
    """Custom type hookStatus73 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus73_Type.__name__ = "DisplayString"
_HookStatus73_Object = MibScalar
hookStatus73 = _HookStatus73_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 73),
    _HookStatus73_Type()
)
hookStatus73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus73.setStatus("current")


class _HookStatus74_Type(DisplayString):
    """Custom type hookStatus74 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus74_Type.__name__ = "DisplayString"
_HookStatus74_Object = MibScalar
hookStatus74 = _HookStatus74_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 74),
    _HookStatus74_Type()
)
hookStatus74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus74.setStatus("current")


class _HookStatus75_Type(DisplayString):
    """Custom type hookStatus75 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus75_Type.__name__ = "DisplayString"
_HookStatus75_Object = MibScalar
hookStatus75 = _HookStatus75_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 75),
    _HookStatus75_Type()
)
hookStatus75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus75.setStatus("current")


class _HookStatus76_Type(DisplayString):
    """Custom type hookStatus76 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus76_Type.__name__ = "DisplayString"
_HookStatus76_Object = MibScalar
hookStatus76 = _HookStatus76_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 76),
    _HookStatus76_Type()
)
hookStatus76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus76.setStatus("current")


class _HookStatus77_Type(DisplayString):
    """Custom type hookStatus77 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus77_Type.__name__ = "DisplayString"
_HookStatus77_Object = MibScalar
hookStatus77 = _HookStatus77_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 77),
    _HookStatus77_Type()
)
hookStatus77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus77.setStatus("current")


class _HookStatus78_Type(DisplayString):
    """Custom type hookStatus78 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus78_Type.__name__ = "DisplayString"
_HookStatus78_Object = MibScalar
hookStatus78 = _HookStatus78_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 78),
    _HookStatus78_Type()
)
hookStatus78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus78.setStatus("current")


class _HookStatus79_Type(DisplayString):
    """Custom type hookStatus79 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus79_Type.__name__ = "DisplayString"
_HookStatus79_Object = MibScalar
hookStatus79 = _HookStatus79_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 79),
    _HookStatus79_Type()
)
hookStatus79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus79.setStatus("current")


class _HookStatus80_Type(DisplayString):
    """Custom type hookStatus80 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus80_Type.__name__ = "DisplayString"
_HookStatus80_Object = MibScalar
hookStatus80 = _HookStatus80_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 80),
    _HookStatus80_Type()
)
hookStatus80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus80.setStatus("current")


class _HookStatus81_Type(DisplayString):
    """Custom type hookStatus81 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus81_Type.__name__ = "DisplayString"
_HookStatus81_Object = MibScalar
hookStatus81 = _HookStatus81_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 81),
    _HookStatus81_Type()
)
hookStatus81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus81.setStatus("current")


class _HookStatus82_Type(DisplayString):
    """Custom type hookStatus82 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus82_Type.__name__ = "DisplayString"
_HookStatus82_Object = MibScalar
hookStatus82 = _HookStatus82_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 82),
    _HookStatus82_Type()
)
hookStatus82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus82.setStatus("current")


class _HookStatus83_Type(DisplayString):
    """Custom type hookStatus83 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus83_Type.__name__ = "DisplayString"
_HookStatus83_Object = MibScalar
hookStatus83 = _HookStatus83_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 83),
    _HookStatus83_Type()
)
hookStatus83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus83.setStatus("current")


class _HookStatus84_Type(DisplayString):
    """Custom type hookStatus84 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus84_Type.__name__ = "DisplayString"
_HookStatus84_Object = MibScalar
hookStatus84 = _HookStatus84_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 84),
    _HookStatus84_Type()
)
hookStatus84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus84.setStatus("current")


class _HookStatus85_Type(DisplayString):
    """Custom type hookStatus85 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus85_Type.__name__ = "DisplayString"
_HookStatus85_Object = MibScalar
hookStatus85 = _HookStatus85_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 85),
    _HookStatus85_Type()
)
hookStatus85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus85.setStatus("current")


class _HookStatus86_Type(DisplayString):
    """Custom type hookStatus86 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus86_Type.__name__ = "DisplayString"
_HookStatus86_Object = MibScalar
hookStatus86 = _HookStatus86_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 86),
    _HookStatus86_Type()
)
hookStatus86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus86.setStatus("current")


class _HookStatus87_Type(DisplayString):
    """Custom type hookStatus87 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus87_Type.__name__ = "DisplayString"
_HookStatus87_Object = MibScalar
hookStatus87 = _HookStatus87_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 87),
    _HookStatus87_Type()
)
hookStatus87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus87.setStatus("current")


class _HookStatus88_Type(DisplayString):
    """Custom type hookStatus88 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus88_Type.__name__ = "DisplayString"
_HookStatus88_Object = MibScalar
hookStatus88 = _HookStatus88_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 88),
    _HookStatus88_Type()
)
hookStatus88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus88.setStatus("current")


class _HookStatus89_Type(DisplayString):
    """Custom type hookStatus89 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus89_Type.__name__ = "DisplayString"
_HookStatus89_Object = MibScalar
hookStatus89 = _HookStatus89_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 89),
    _HookStatus89_Type()
)
hookStatus89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus89.setStatus("current")


class _HookStatus90_Type(DisplayString):
    """Custom type hookStatus90 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus90_Type.__name__ = "DisplayString"
_HookStatus90_Object = MibScalar
hookStatus90 = _HookStatus90_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 90),
    _HookStatus90_Type()
)
hookStatus90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus90.setStatus("current")


class _HookStatus91_Type(DisplayString):
    """Custom type hookStatus91 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus91_Type.__name__ = "DisplayString"
_HookStatus91_Object = MibScalar
hookStatus91 = _HookStatus91_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 91),
    _HookStatus91_Type()
)
hookStatus91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus91.setStatus("current")


class _HookStatus92_Type(DisplayString):
    """Custom type hookStatus92 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus92_Type.__name__ = "DisplayString"
_HookStatus92_Object = MibScalar
hookStatus92 = _HookStatus92_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 92),
    _HookStatus92_Type()
)
hookStatus92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus92.setStatus("current")


class _HookStatus93_Type(DisplayString):
    """Custom type hookStatus93 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus93_Type.__name__ = "DisplayString"
_HookStatus93_Object = MibScalar
hookStatus93 = _HookStatus93_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 93),
    _HookStatus93_Type()
)
hookStatus93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus93.setStatus("current")


class _HookStatus94_Type(DisplayString):
    """Custom type hookStatus94 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus94_Type.__name__ = "DisplayString"
_HookStatus94_Object = MibScalar
hookStatus94 = _HookStatus94_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 94),
    _HookStatus94_Type()
)
hookStatus94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus94.setStatus("current")


class _HookStatus95_Type(DisplayString):
    """Custom type hookStatus95 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus95_Type.__name__ = "DisplayString"
_HookStatus95_Object = MibScalar
hookStatus95 = _HookStatus95_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 95),
    _HookStatus95_Type()
)
hookStatus95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus95.setStatus("current")


class _HookStatus96_Type(DisplayString):
    """Custom type hookStatus96 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HookStatus96_Type.__name__ = "DisplayString"
_HookStatus96_Object = MibScalar
hookStatus96 = _HookStatus96_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 1, 96),
    _HookStatus96_Type()
)
hookStatus96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hookStatus96.setStatus("current")
_RegStatus_ObjectIdentity = ObjectIdentity
regStatus = _RegStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2)
)


class _RegStatus1_Type(DisplayString):
    """Custom type regStatus1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus1_Type.__name__ = "DisplayString"
_RegStatus1_Object = MibScalar
regStatus1 = _RegStatus1_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 1),
    _RegStatus1_Type()
)
regStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus1.setStatus("current")


class _RegStatus2_Type(DisplayString):
    """Custom type regStatus2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus2_Type.__name__ = "DisplayString"
_RegStatus2_Object = MibScalar
regStatus2 = _RegStatus2_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 2),
    _RegStatus2_Type()
)
regStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus2.setStatus("current")


class _RegStatus3_Type(DisplayString):
    """Custom type regStatus3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus3_Type.__name__ = "DisplayString"
_RegStatus3_Object = MibScalar
regStatus3 = _RegStatus3_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 3),
    _RegStatus3_Type()
)
regStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus3.setStatus("current")


class _RegStatus4_Type(DisplayString):
    """Custom type regStatus4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus4_Type.__name__ = "DisplayString"
_RegStatus4_Object = MibScalar
regStatus4 = _RegStatus4_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 4),
    _RegStatus4_Type()
)
regStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus4.setStatus("current")


class _RegStatus5_Type(DisplayString):
    """Custom type regStatus5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus5_Type.__name__ = "DisplayString"
_RegStatus5_Object = MibScalar
regStatus5 = _RegStatus5_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 5),
    _RegStatus5_Type()
)
regStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus5.setStatus("current")


class _RegStatus6_Type(DisplayString):
    """Custom type regStatus6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus6_Type.__name__ = "DisplayString"
_RegStatus6_Object = MibScalar
regStatus6 = _RegStatus6_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 6),
    _RegStatus6_Type()
)
regStatus6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus6.setStatus("current")


class _RegStatus7_Type(DisplayString):
    """Custom type regStatus7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus7_Type.__name__ = "DisplayString"
_RegStatus7_Object = MibScalar
regStatus7 = _RegStatus7_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 7),
    _RegStatus7_Type()
)
regStatus7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus7.setStatus("current")


class _RegStatus8_Type(DisplayString):
    """Custom type regStatus8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus8_Type.__name__ = "DisplayString"
_RegStatus8_Object = MibScalar
regStatus8 = _RegStatus8_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 8),
    _RegStatus8_Type()
)
regStatus8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus8.setStatus("current")


class _RegStatus9_Type(DisplayString):
    """Custom type regStatus9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus9_Type.__name__ = "DisplayString"
_RegStatus9_Object = MibScalar
regStatus9 = _RegStatus9_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 9),
    _RegStatus9_Type()
)
regStatus9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus9.setStatus("current")


class _RegStatus10_Type(DisplayString):
    """Custom type regStatus10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus10_Type.__name__ = "DisplayString"
_RegStatus10_Object = MibScalar
regStatus10 = _RegStatus10_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 10),
    _RegStatus10_Type()
)
regStatus10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus10.setStatus("current")


class _RegStatus11_Type(DisplayString):
    """Custom type regStatus11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus11_Type.__name__ = "DisplayString"
_RegStatus11_Object = MibScalar
regStatus11 = _RegStatus11_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 11),
    _RegStatus11_Type()
)
regStatus11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus11.setStatus("current")


class _RegStatus12_Type(DisplayString):
    """Custom type regStatus12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus12_Type.__name__ = "DisplayString"
_RegStatus12_Object = MibScalar
regStatus12 = _RegStatus12_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 12),
    _RegStatus12_Type()
)
regStatus12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus12.setStatus("current")


class _RegStatus13_Type(DisplayString):
    """Custom type regStatus13 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus13_Type.__name__ = "DisplayString"
_RegStatus13_Object = MibScalar
regStatus13 = _RegStatus13_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 13),
    _RegStatus13_Type()
)
regStatus13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus13.setStatus("current")


class _RegStatus14_Type(DisplayString):
    """Custom type regStatus14 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus14_Type.__name__ = "DisplayString"
_RegStatus14_Object = MibScalar
regStatus14 = _RegStatus14_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 14),
    _RegStatus14_Type()
)
regStatus14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus14.setStatus("current")


class _RegStatus15_Type(DisplayString):
    """Custom type regStatus15 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus15_Type.__name__ = "DisplayString"
_RegStatus15_Object = MibScalar
regStatus15 = _RegStatus15_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 15),
    _RegStatus15_Type()
)
regStatus15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus15.setStatus("current")


class _RegStatus16_Type(DisplayString):
    """Custom type regStatus16 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus16_Type.__name__ = "DisplayString"
_RegStatus16_Object = MibScalar
regStatus16 = _RegStatus16_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 16),
    _RegStatus16_Type()
)
regStatus16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus16.setStatus("current")


class _RegStatus17_Type(DisplayString):
    """Custom type regStatus17 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus17_Type.__name__ = "DisplayString"
_RegStatus17_Object = MibScalar
regStatus17 = _RegStatus17_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 17),
    _RegStatus17_Type()
)
regStatus17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus17.setStatus("current")


class _RegStatus18_Type(DisplayString):
    """Custom type regStatus18 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus18_Type.__name__ = "DisplayString"
_RegStatus18_Object = MibScalar
regStatus18 = _RegStatus18_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 18),
    _RegStatus18_Type()
)
regStatus18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus18.setStatus("current")


class _RegStatus19_Type(DisplayString):
    """Custom type regStatus19 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus19_Type.__name__ = "DisplayString"
_RegStatus19_Object = MibScalar
regStatus19 = _RegStatus19_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 19),
    _RegStatus19_Type()
)
regStatus19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus19.setStatus("current")


class _RegStatus20_Type(DisplayString):
    """Custom type regStatus20 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus20_Type.__name__ = "DisplayString"
_RegStatus20_Object = MibScalar
regStatus20 = _RegStatus20_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 20),
    _RegStatus20_Type()
)
regStatus20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus20.setStatus("current")


class _RegStatus21_Type(DisplayString):
    """Custom type regStatus21 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus21_Type.__name__ = "DisplayString"
_RegStatus21_Object = MibScalar
regStatus21 = _RegStatus21_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 21),
    _RegStatus21_Type()
)
regStatus21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus21.setStatus("current")


class _RegStatus22_Type(DisplayString):
    """Custom type regStatus22 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus22_Type.__name__ = "DisplayString"
_RegStatus22_Object = MibScalar
regStatus22 = _RegStatus22_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 22),
    _RegStatus22_Type()
)
regStatus22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus22.setStatus("current")


class _RegStatus23_Type(DisplayString):
    """Custom type regStatus23 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus23_Type.__name__ = "DisplayString"
_RegStatus23_Object = MibScalar
regStatus23 = _RegStatus23_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 23),
    _RegStatus23_Type()
)
regStatus23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus23.setStatus("current")


class _RegStatus24_Type(DisplayString):
    """Custom type regStatus24 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus24_Type.__name__ = "DisplayString"
_RegStatus24_Object = MibScalar
regStatus24 = _RegStatus24_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 24),
    _RegStatus24_Type()
)
regStatus24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus24.setStatus("current")


class _RegStatus25_Type(DisplayString):
    """Custom type regStatus25 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus25_Type.__name__ = "DisplayString"
_RegStatus25_Object = MibScalar
regStatus25 = _RegStatus25_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 25),
    _RegStatus25_Type()
)
regStatus25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus25.setStatus("current")


class _RegStatus26_Type(DisplayString):
    """Custom type regStatus26 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus26_Type.__name__ = "DisplayString"
_RegStatus26_Object = MibScalar
regStatus26 = _RegStatus26_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 26),
    _RegStatus26_Type()
)
regStatus26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus26.setStatus("current")


class _RegStatus27_Type(DisplayString):
    """Custom type regStatus27 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus27_Type.__name__ = "DisplayString"
_RegStatus27_Object = MibScalar
regStatus27 = _RegStatus27_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 27),
    _RegStatus27_Type()
)
regStatus27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus27.setStatus("current")


class _RegStatus28_Type(DisplayString):
    """Custom type regStatus28 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus28_Type.__name__ = "DisplayString"
_RegStatus28_Object = MibScalar
regStatus28 = _RegStatus28_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 28),
    _RegStatus28_Type()
)
regStatus28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus28.setStatus("current")


class _RegStatus29_Type(DisplayString):
    """Custom type regStatus29 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus29_Type.__name__ = "DisplayString"
_RegStatus29_Object = MibScalar
regStatus29 = _RegStatus29_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 29),
    _RegStatus29_Type()
)
regStatus29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus29.setStatus("current")


class _RegStatus30_Type(DisplayString):
    """Custom type regStatus30 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus30_Type.__name__ = "DisplayString"
_RegStatus30_Object = MibScalar
regStatus30 = _RegStatus30_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 30),
    _RegStatus30_Type()
)
regStatus30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus30.setStatus("current")


class _RegStatus31_Type(DisplayString):
    """Custom type regStatus31 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus31_Type.__name__ = "DisplayString"
_RegStatus31_Object = MibScalar
regStatus31 = _RegStatus31_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 31),
    _RegStatus31_Type()
)
regStatus31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus31.setStatus("current")


class _RegStatus32_Type(DisplayString):
    """Custom type regStatus32 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus32_Type.__name__ = "DisplayString"
_RegStatus32_Object = MibScalar
regStatus32 = _RegStatus32_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 32),
    _RegStatus32_Type()
)
regStatus32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus32.setStatus("current")


class _RegStatus33_Type(DisplayString):
    """Custom type regStatus33 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus33_Type.__name__ = "DisplayString"
_RegStatus33_Object = MibScalar
regStatus33 = _RegStatus33_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 33),
    _RegStatus33_Type()
)
regStatus33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus33.setStatus("current")


class _RegStatus34_Type(DisplayString):
    """Custom type regStatus34 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus34_Type.__name__ = "DisplayString"
_RegStatus34_Object = MibScalar
regStatus34 = _RegStatus34_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 34),
    _RegStatus34_Type()
)
regStatus34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus34.setStatus("current")


class _RegStatus35_Type(DisplayString):
    """Custom type regStatus35 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus35_Type.__name__ = "DisplayString"
_RegStatus35_Object = MibScalar
regStatus35 = _RegStatus35_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 35),
    _RegStatus35_Type()
)
regStatus35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus35.setStatus("current")


class _RegStatus36_Type(DisplayString):
    """Custom type regStatus36 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus36_Type.__name__ = "DisplayString"
_RegStatus36_Object = MibScalar
regStatus36 = _RegStatus36_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 36),
    _RegStatus36_Type()
)
regStatus36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus36.setStatus("current")


class _RegStatus37_Type(DisplayString):
    """Custom type regStatus37 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus37_Type.__name__ = "DisplayString"
_RegStatus37_Object = MibScalar
regStatus37 = _RegStatus37_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 37),
    _RegStatus37_Type()
)
regStatus37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus37.setStatus("current")


class _RegStatus38_Type(DisplayString):
    """Custom type regStatus38 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus38_Type.__name__ = "DisplayString"
_RegStatus38_Object = MibScalar
regStatus38 = _RegStatus38_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 38),
    _RegStatus38_Type()
)
regStatus38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus38.setStatus("current")


class _RegStatus39_Type(DisplayString):
    """Custom type regStatus39 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus39_Type.__name__ = "DisplayString"
_RegStatus39_Object = MibScalar
regStatus39 = _RegStatus39_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 39),
    _RegStatus39_Type()
)
regStatus39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus39.setStatus("current")


class _RegStatus40_Type(DisplayString):
    """Custom type regStatus40 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus40_Type.__name__ = "DisplayString"
_RegStatus40_Object = MibScalar
regStatus40 = _RegStatus40_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 40),
    _RegStatus40_Type()
)
regStatus40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus40.setStatus("current")


class _RegStatus41_Type(DisplayString):
    """Custom type regStatus41 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus41_Type.__name__ = "DisplayString"
_RegStatus41_Object = MibScalar
regStatus41 = _RegStatus41_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 41),
    _RegStatus41_Type()
)
regStatus41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus41.setStatus("current")


class _RegStatus42_Type(DisplayString):
    """Custom type regStatus42 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus42_Type.__name__ = "DisplayString"
_RegStatus42_Object = MibScalar
regStatus42 = _RegStatus42_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 42),
    _RegStatus42_Type()
)
regStatus42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus42.setStatus("current")


class _RegStatus43_Type(DisplayString):
    """Custom type regStatus43 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus43_Type.__name__ = "DisplayString"
_RegStatus43_Object = MibScalar
regStatus43 = _RegStatus43_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 43),
    _RegStatus43_Type()
)
regStatus43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus43.setStatus("current")


class _RegStatus44_Type(DisplayString):
    """Custom type regStatus44 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus44_Type.__name__ = "DisplayString"
_RegStatus44_Object = MibScalar
regStatus44 = _RegStatus44_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 44),
    _RegStatus44_Type()
)
regStatus44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus44.setStatus("current")


class _RegStatus45_Type(DisplayString):
    """Custom type regStatus45 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus45_Type.__name__ = "DisplayString"
_RegStatus45_Object = MibScalar
regStatus45 = _RegStatus45_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 45),
    _RegStatus45_Type()
)
regStatus45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus45.setStatus("current")


class _RegStatus46_Type(DisplayString):
    """Custom type regStatus46 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus46_Type.__name__ = "DisplayString"
_RegStatus46_Object = MibScalar
regStatus46 = _RegStatus46_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 46),
    _RegStatus46_Type()
)
regStatus46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus46.setStatus("current")


class _RegStatus47_Type(DisplayString):
    """Custom type regStatus47 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus47_Type.__name__ = "DisplayString"
_RegStatus47_Object = MibScalar
regStatus47 = _RegStatus47_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 47),
    _RegStatus47_Type()
)
regStatus47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus47.setStatus("current")


class _RegStatus48_Type(DisplayString):
    """Custom type regStatus48 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus48_Type.__name__ = "DisplayString"
_RegStatus48_Object = MibScalar
regStatus48 = _RegStatus48_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 48),
    _RegStatus48_Type()
)
regStatus48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus48.setStatus("current")


class _RegStatus49_Type(DisplayString):
    """Custom type regStatus49 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus49_Type.__name__ = "DisplayString"
_RegStatus49_Object = MibScalar
regStatus49 = _RegStatus49_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 49),
    _RegStatus49_Type()
)
regStatus49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus49.setStatus("current")


class _RegStatus50_Type(DisplayString):
    """Custom type regStatus50 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus50_Type.__name__ = "DisplayString"
_RegStatus50_Object = MibScalar
regStatus50 = _RegStatus50_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 50),
    _RegStatus50_Type()
)
regStatus50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus50.setStatus("current")


class _RegStatus51_Type(DisplayString):
    """Custom type regStatus51 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus51_Type.__name__ = "DisplayString"
_RegStatus51_Object = MibScalar
regStatus51 = _RegStatus51_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 51),
    _RegStatus51_Type()
)
regStatus51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus51.setStatus("current")


class _RegStatus52_Type(DisplayString):
    """Custom type regStatus52 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus52_Type.__name__ = "DisplayString"
_RegStatus52_Object = MibScalar
regStatus52 = _RegStatus52_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 52),
    _RegStatus52_Type()
)
regStatus52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus52.setStatus("current")


class _RegStatus53_Type(DisplayString):
    """Custom type regStatus53 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus53_Type.__name__ = "DisplayString"
_RegStatus53_Object = MibScalar
regStatus53 = _RegStatus53_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 53),
    _RegStatus53_Type()
)
regStatus53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus53.setStatus("current")


class _RegStatus54_Type(DisplayString):
    """Custom type regStatus54 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus54_Type.__name__ = "DisplayString"
_RegStatus54_Object = MibScalar
regStatus54 = _RegStatus54_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 54),
    _RegStatus54_Type()
)
regStatus54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus54.setStatus("current")


class _RegStatus55_Type(DisplayString):
    """Custom type regStatus55 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus55_Type.__name__ = "DisplayString"
_RegStatus55_Object = MibScalar
regStatus55 = _RegStatus55_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 55),
    _RegStatus55_Type()
)
regStatus55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus55.setStatus("current")


class _RegStatus56_Type(DisplayString):
    """Custom type regStatus56 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus56_Type.__name__ = "DisplayString"
_RegStatus56_Object = MibScalar
regStatus56 = _RegStatus56_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 56),
    _RegStatus56_Type()
)
regStatus56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus56.setStatus("current")


class _RegStatus57_Type(DisplayString):
    """Custom type regStatus57 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus57_Type.__name__ = "DisplayString"
_RegStatus57_Object = MibScalar
regStatus57 = _RegStatus57_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 57),
    _RegStatus57_Type()
)
regStatus57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus57.setStatus("current")


class _RegStatus58_Type(DisplayString):
    """Custom type regStatus58 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus58_Type.__name__ = "DisplayString"
_RegStatus58_Object = MibScalar
regStatus58 = _RegStatus58_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 58),
    _RegStatus58_Type()
)
regStatus58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus58.setStatus("current")


class _RegStatus59_Type(DisplayString):
    """Custom type regStatus59 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus59_Type.__name__ = "DisplayString"
_RegStatus59_Object = MibScalar
regStatus59 = _RegStatus59_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 59),
    _RegStatus59_Type()
)
regStatus59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus59.setStatus("current")


class _RegStatus60_Type(DisplayString):
    """Custom type regStatus60 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus60_Type.__name__ = "DisplayString"
_RegStatus60_Object = MibScalar
regStatus60 = _RegStatus60_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 60),
    _RegStatus60_Type()
)
regStatus60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus60.setStatus("current")


class _RegStatus61_Type(DisplayString):
    """Custom type regStatus61 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus61_Type.__name__ = "DisplayString"
_RegStatus61_Object = MibScalar
regStatus61 = _RegStatus61_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 61),
    _RegStatus61_Type()
)
regStatus61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus61.setStatus("current")


class _RegStatus62_Type(DisplayString):
    """Custom type regStatus62 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus62_Type.__name__ = "DisplayString"
_RegStatus62_Object = MibScalar
regStatus62 = _RegStatus62_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 62),
    _RegStatus62_Type()
)
regStatus62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus62.setStatus("current")


class _RegStatus63_Type(DisplayString):
    """Custom type regStatus63 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus63_Type.__name__ = "DisplayString"
_RegStatus63_Object = MibScalar
regStatus63 = _RegStatus63_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 63),
    _RegStatus63_Type()
)
regStatus63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus63.setStatus("current")


class _RegStatus64_Type(DisplayString):
    """Custom type regStatus64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus64_Type.__name__ = "DisplayString"
_RegStatus64_Object = MibScalar
regStatus64 = _RegStatus64_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 64),
    _RegStatus64_Type()
)
regStatus64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus64.setStatus("current")


class _RegStatus65_Type(DisplayString):
    """Custom type regStatus65 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus65_Type.__name__ = "DisplayString"
_RegStatus65_Object = MibScalar
regStatus65 = _RegStatus65_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 65),
    _RegStatus65_Type()
)
regStatus65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus65.setStatus("current")


class _RegStatus66_Type(DisplayString):
    """Custom type regStatus66 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus66_Type.__name__ = "DisplayString"
_RegStatus66_Object = MibScalar
regStatus66 = _RegStatus66_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 66),
    _RegStatus66_Type()
)
regStatus66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus66.setStatus("current")


class _RegStatus67_Type(DisplayString):
    """Custom type regStatus67 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus67_Type.__name__ = "DisplayString"
_RegStatus67_Object = MibScalar
regStatus67 = _RegStatus67_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 67),
    _RegStatus67_Type()
)
regStatus67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus67.setStatus("current")


class _RegStatus68_Type(DisplayString):
    """Custom type regStatus68 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus68_Type.__name__ = "DisplayString"
_RegStatus68_Object = MibScalar
regStatus68 = _RegStatus68_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 68),
    _RegStatus68_Type()
)
regStatus68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus68.setStatus("current")


class _RegStatus69_Type(DisplayString):
    """Custom type regStatus69 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus69_Type.__name__ = "DisplayString"
_RegStatus69_Object = MibScalar
regStatus69 = _RegStatus69_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 69),
    _RegStatus69_Type()
)
regStatus69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus69.setStatus("current")


class _RegStatus70_Type(DisplayString):
    """Custom type regStatus70 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus70_Type.__name__ = "DisplayString"
_RegStatus70_Object = MibScalar
regStatus70 = _RegStatus70_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 70),
    _RegStatus70_Type()
)
regStatus70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus70.setStatus("current")


class _RegStatus71_Type(DisplayString):
    """Custom type regStatus71 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus71_Type.__name__ = "DisplayString"
_RegStatus71_Object = MibScalar
regStatus71 = _RegStatus71_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 71),
    _RegStatus71_Type()
)
regStatus71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus71.setStatus("current")


class _RegStatus72_Type(DisplayString):
    """Custom type regStatus72 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus72_Type.__name__ = "DisplayString"
_RegStatus72_Object = MibScalar
regStatus72 = _RegStatus72_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 72),
    _RegStatus72_Type()
)
regStatus72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus72.setStatus("current")


class _RegStatus73_Type(DisplayString):
    """Custom type regStatus73 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus73_Type.__name__ = "DisplayString"
_RegStatus73_Object = MibScalar
regStatus73 = _RegStatus73_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 73),
    _RegStatus73_Type()
)
regStatus73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus73.setStatus("current")


class _RegStatus74_Type(DisplayString):
    """Custom type regStatus74 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus74_Type.__name__ = "DisplayString"
_RegStatus74_Object = MibScalar
regStatus74 = _RegStatus74_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 74),
    _RegStatus74_Type()
)
regStatus74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus74.setStatus("current")


class _RegStatus75_Type(DisplayString):
    """Custom type regStatus75 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus75_Type.__name__ = "DisplayString"
_RegStatus75_Object = MibScalar
regStatus75 = _RegStatus75_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 75),
    _RegStatus75_Type()
)
regStatus75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus75.setStatus("current")


class _RegStatus76_Type(DisplayString):
    """Custom type regStatus76 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus76_Type.__name__ = "DisplayString"
_RegStatus76_Object = MibScalar
regStatus76 = _RegStatus76_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 76),
    _RegStatus76_Type()
)
regStatus76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus76.setStatus("current")


class _RegStatus77_Type(DisplayString):
    """Custom type regStatus77 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus77_Type.__name__ = "DisplayString"
_RegStatus77_Object = MibScalar
regStatus77 = _RegStatus77_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 77),
    _RegStatus77_Type()
)
regStatus77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus77.setStatus("current")


class _RegStatus78_Type(DisplayString):
    """Custom type regStatus78 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus78_Type.__name__ = "DisplayString"
_RegStatus78_Object = MibScalar
regStatus78 = _RegStatus78_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 78),
    _RegStatus78_Type()
)
regStatus78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus78.setStatus("current")


class _RegStatus79_Type(DisplayString):
    """Custom type regStatus79 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus79_Type.__name__ = "DisplayString"
_RegStatus79_Object = MibScalar
regStatus79 = _RegStatus79_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 79),
    _RegStatus79_Type()
)
regStatus79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus79.setStatus("current")


class _RegStatus80_Type(DisplayString):
    """Custom type regStatus80 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus80_Type.__name__ = "DisplayString"
_RegStatus80_Object = MibScalar
regStatus80 = _RegStatus80_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 80),
    _RegStatus80_Type()
)
regStatus80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus80.setStatus("current")


class _RegStatus81_Type(DisplayString):
    """Custom type regStatus81 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus81_Type.__name__ = "DisplayString"
_RegStatus81_Object = MibScalar
regStatus81 = _RegStatus81_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 81),
    _RegStatus81_Type()
)
regStatus81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus81.setStatus("current")


class _RegStatus82_Type(DisplayString):
    """Custom type regStatus82 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus82_Type.__name__ = "DisplayString"
_RegStatus82_Object = MibScalar
regStatus82 = _RegStatus82_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 82),
    _RegStatus82_Type()
)
regStatus82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus82.setStatus("current")


class _RegStatus83_Type(DisplayString):
    """Custom type regStatus83 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus83_Type.__name__ = "DisplayString"
_RegStatus83_Object = MibScalar
regStatus83 = _RegStatus83_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 83),
    _RegStatus83_Type()
)
regStatus83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus83.setStatus("current")


class _RegStatus84_Type(DisplayString):
    """Custom type regStatus84 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus84_Type.__name__ = "DisplayString"
_RegStatus84_Object = MibScalar
regStatus84 = _RegStatus84_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 84),
    _RegStatus84_Type()
)
regStatus84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus84.setStatus("current")


class _RegStatus85_Type(DisplayString):
    """Custom type regStatus85 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus85_Type.__name__ = "DisplayString"
_RegStatus85_Object = MibScalar
regStatus85 = _RegStatus85_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 85),
    _RegStatus85_Type()
)
regStatus85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus85.setStatus("current")


class _RegStatus86_Type(DisplayString):
    """Custom type regStatus86 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus86_Type.__name__ = "DisplayString"
_RegStatus86_Object = MibScalar
regStatus86 = _RegStatus86_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 86),
    _RegStatus86_Type()
)
regStatus86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus86.setStatus("current")


class _RegStatus87_Type(DisplayString):
    """Custom type regStatus87 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus87_Type.__name__ = "DisplayString"
_RegStatus87_Object = MibScalar
regStatus87 = _RegStatus87_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 87),
    _RegStatus87_Type()
)
regStatus87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus87.setStatus("current")


class _RegStatus88_Type(DisplayString):
    """Custom type regStatus88 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus88_Type.__name__ = "DisplayString"
_RegStatus88_Object = MibScalar
regStatus88 = _RegStatus88_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 88),
    _RegStatus88_Type()
)
regStatus88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus88.setStatus("current")


class _RegStatus89_Type(DisplayString):
    """Custom type regStatus89 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus89_Type.__name__ = "DisplayString"
_RegStatus89_Object = MibScalar
regStatus89 = _RegStatus89_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 89),
    _RegStatus89_Type()
)
regStatus89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus89.setStatus("current")


class _RegStatus90_Type(DisplayString):
    """Custom type regStatus90 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus90_Type.__name__ = "DisplayString"
_RegStatus90_Object = MibScalar
regStatus90 = _RegStatus90_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 90),
    _RegStatus90_Type()
)
regStatus90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus90.setStatus("current")


class _RegStatus91_Type(DisplayString):
    """Custom type regStatus91 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus91_Type.__name__ = "DisplayString"
_RegStatus91_Object = MibScalar
regStatus91 = _RegStatus91_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 91),
    _RegStatus91_Type()
)
regStatus91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus91.setStatus("current")


class _RegStatus92_Type(DisplayString):
    """Custom type regStatus92 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus92_Type.__name__ = "DisplayString"
_RegStatus92_Object = MibScalar
regStatus92 = _RegStatus92_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 92),
    _RegStatus92_Type()
)
regStatus92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus92.setStatus("current")


class _RegStatus93_Type(DisplayString):
    """Custom type regStatus93 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus93_Type.__name__ = "DisplayString"
_RegStatus93_Object = MibScalar
regStatus93 = _RegStatus93_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 93),
    _RegStatus93_Type()
)
regStatus93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus93.setStatus("current")


class _RegStatus94_Type(DisplayString):
    """Custom type regStatus94 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus94_Type.__name__ = "DisplayString"
_RegStatus94_Object = MibScalar
regStatus94 = _RegStatus94_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 94),
    _RegStatus94_Type()
)
regStatus94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus94.setStatus("current")


class _RegStatus95_Type(DisplayString):
    """Custom type regStatus95 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus95_Type.__name__ = "DisplayString"
_RegStatus95_Object = MibScalar
regStatus95 = _RegStatus95_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 95),
    _RegStatus95_Type()
)
regStatus95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus95.setStatus("current")


class _RegStatus96_Type(DisplayString):
    """Custom type regStatus96 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RegStatus96_Type.__name__ = "DisplayString"
_RegStatus96_Object = MibScalar
regStatus96 = _RegStatus96_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 2, 96),
    _RegStatus96_Type()
)
regStatus96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatus96.setStatus("current")
_Dnd_ObjectIdentity = ObjectIdentity
dnd = _Dnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3)
)
_Dnd1_Type = Integer32
_Dnd1_Object = MibScalar
dnd1 = _Dnd1_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 1),
    _Dnd1_Type()
)
dnd1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd1.setStatus("current")
_Dnd2_Type = Integer32
_Dnd2_Object = MibScalar
dnd2 = _Dnd2_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 2),
    _Dnd2_Type()
)
dnd2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd2.setStatus("current")
_Dnd3_Type = Integer32
_Dnd3_Object = MibScalar
dnd3 = _Dnd3_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 3),
    _Dnd3_Type()
)
dnd3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd3.setStatus("current")
_Dnd4_Type = Integer32
_Dnd4_Object = MibScalar
dnd4 = _Dnd4_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 4),
    _Dnd4_Type()
)
dnd4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd4.setStatus("current")
_Dnd5_Type = Integer32
_Dnd5_Object = MibScalar
dnd5 = _Dnd5_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 5),
    _Dnd5_Type()
)
dnd5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd5.setStatus("current")
_Dnd6_Type = Integer32
_Dnd6_Object = MibScalar
dnd6 = _Dnd6_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 6),
    _Dnd6_Type()
)
dnd6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd6.setStatus("current")
_Dnd7_Type = Integer32
_Dnd7_Object = MibScalar
dnd7 = _Dnd7_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 7),
    _Dnd7_Type()
)
dnd7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd7.setStatus("current")
_Dnd8_Type = Integer32
_Dnd8_Object = MibScalar
dnd8 = _Dnd8_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 8),
    _Dnd8_Type()
)
dnd8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd8.setStatus("current")
_Dnd9_Type = Integer32
_Dnd9_Object = MibScalar
dnd9 = _Dnd9_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 9),
    _Dnd9_Type()
)
dnd9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd9.setStatus("current")
_Dnd10_Type = Integer32
_Dnd10_Object = MibScalar
dnd10 = _Dnd10_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 10),
    _Dnd10_Type()
)
dnd10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd10.setStatus("current")
_Dnd11_Type = Integer32
_Dnd11_Object = MibScalar
dnd11 = _Dnd11_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 11),
    _Dnd11_Type()
)
dnd11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd11.setStatus("current")
_Dnd12_Type = Integer32
_Dnd12_Object = MibScalar
dnd12 = _Dnd12_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 12),
    _Dnd12_Type()
)
dnd12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd12.setStatus("current")
_Dnd13_Type = Integer32
_Dnd13_Object = MibScalar
dnd13 = _Dnd13_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 13),
    _Dnd13_Type()
)
dnd13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd13.setStatus("current")
_Dnd14_Type = Integer32
_Dnd14_Object = MibScalar
dnd14 = _Dnd14_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 14),
    _Dnd14_Type()
)
dnd14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd14.setStatus("current")
_Dnd15_Type = Integer32
_Dnd15_Object = MibScalar
dnd15 = _Dnd15_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 15),
    _Dnd15_Type()
)
dnd15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd15.setStatus("current")
_Dnd16_Type = Integer32
_Dnd16_Object = MibScalar
dnd16 = _Dnd16_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 16),
    _Dnd16_Type()
)
dnd16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd16.setStatus("current")
_Dnd17_Type = Integer32
_Dnd17_Object = MibScalar
dnd17 = _Dnd17_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 17),
    _Dnd17_Type()
)
dnd17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd17.setStatus("current")
_Dnd18_Type = Integer32
_Dnd18_Object = MibScalar
dnd18 = _Dnd18_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 18),
    _Dnd18_Type()
)
dnd18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd18.setStatus("current")
_Dnd19_Type = Integer32
_Dnd19_Object = MibScalar
dnd19 = _Dnd19_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 19),
    _Dnd19_Type()
)
dnd19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd19.setStatus("current")
_Dnd20_Type = Integer32
_Dnd20_Object = MibScalar
dnd20 = _Dnd20_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 20),
    _Dnd20_Type()
)
dnd20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd20.setStatus("current")
_Dnd21_Type = Integer32
_Dnd21_Object = MibScalar
dnd21 = _Dnd21_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 21),
    _Dnd21_Type()
)
dnd21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd21.setStatus("current")
_Dnd22_Type = Integer32
_Dnd22_Object = MibScalar
dnd22 = _Dnd22_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 22),
    _Dnd22_Type()
)
dnd22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd22.setStatus("current")
_Dnd23_Type = Integer32
_Dnd23_Object = MibScalar
dnd23 = _Dnd23_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 23),
    _Dnd23_Type()
)
dnd23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd23.setStatus("current")
_Dnd24_Type = Integer32
_Dnd24_Object = MibScalar
dnd24 = _Dnd24_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 24),
    _Dnd24_Type()
)
dnd24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd24.setStatus("current")
_Dnd25_Type = Integer32
_Dnd25_Object = MibScalar
dnd25 = _Dnd25_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 25),
    _Dnd25_Type()
)
dnd25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd25.setStatus("current")
_Dnd26_Type = Integer32
_Dnd26_Object = MibScalar
dnd26 = _Dnd26_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 26),
    _Dnd26_Type()
)
dnd26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd26.setStatus("current")
_Dnd27_Type = Integer32
_Dnd27_Object = MibScalar
dnd27 = _Dnd27_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 27),
    _Dnd27_Type()
)
dnd27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd27.setStatus("current")
_Dnd28_Type = Integer32
_Dnd28_Object = MibScalar
dnd28 = _Dnd28_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 28),
    _Dnd28_Type()
)
dnd28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd28.setStatus("current")
_Dnd29_Type = Integer32
_Dnd29_Object = MibScalar
dnd29 = _Dnd29_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 29),
    _Dnd29_Type()
)
dnd29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd29.setStatus("current")
_Dnd30_Type = Integer32
_Dnd30_Object = MibScalar
dnd30 = _Dnd30_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 30),
    _Dnd30_Type()
)
dnd30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd30.setStatus("current")
_Dnd31_Type = Integer32
_Dnd31_Object = MibScalar
dnd31 = _Dnd31_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 31),
    _Dnd31_Type()
)
dnd31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd31.setStatus("current")
_Dnd32_Type = Integer32
_Dnd32_Object = MibScalar
dnd32 = _Dnd32_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 32),
    _Dnd32_Type()
)
dnd32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd32.setStatus("current")
_Dnd33_Type = Integer32
_Dnd33_Object = MibScalar
dnd33 = _Dnd33_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 33),
    _Dnd33_Type()
)
dnd33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd33.setStatus("current")
_Dnd34_Type = Integer32
_Dnd34_Object = MibScalar
dnd34 = _Dnd34_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 34),
    _Dnd34_Type()
)
dnd34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd34.setStatus("current")
_Dnd35_Type = Integer32
_Dnd35_Object = MibScalar
dnd35 = _Dnd35_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 35),
    _Dnd35_Type()
)
dnd35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd35.setStatus("current")
_Dnd36_Type = Integer32
_Dnd36_Object = MibScalar
dnd36 = _Dnd36_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 36),
    _Dnd36_Type()
)
dnd36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd36.setStatus("current")
_Dnd37_Type = Integer32
_Dnd37_Object = MibScalar
dnd37 = _Dnd37_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 37),
    _Dnd37_Type()
)
dnd37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd37.setStatus("current")
_Dnd38_Type = Integer32
_Dnd38_Object = MibScalar
dnd38 = _Dnd38_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 38),
    _Dnd38_Type()
)
dnd38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd38.setStatus("current")
_Dnd39_Type = Integer32
_Dnd39_Object = MibScalar
dnd39 = _Dnd39_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 39),
    _Dnd39_Type()
)
dnd39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd39.setStatus("current")
_Dnd40_Type = Integer32
_Dnd40_Object = MibScalar
dnd40 = _Dnd40_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 40),
    _Dnd40_Type()
)
dnd40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd40.setStatus("current")
_Dnd41_Type = Integer32
_Dnd41_Object = MibScalar
dnd41 = _Dnd41_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 41),
    _Dnd41_Type()
)
dnd41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd41.setStatus("current")
_Dnd42_Type = Integer32
_Dnd42_Object = MibScalar
dnd42 = _Dnd42_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 42),
    _Dnd42_Type()
)
dnd42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd42.setStatus("current")
_Dnd43_Type = Integer32
_Dnd43_Object = MibScalar
dnd43 = _Dnd43_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 43),
    _Dnd43_Type()
)
dnd43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd43.setStatus("current")
_Dnd44_Type = Integer32
_Dnd44_Object = MibScalar
dnd44 = _Dnd44_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 44),
    _Dnd44_Type()
)
dnd44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd44.setStatus("current")
_Dnd45_Type = Integer32
_Dnd45_Object = MibScalar
dnd45 = _Dnd45_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 45),
    _Dnd45_Type()
)
dnd45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd45.setStatus("current")
_Dnd46_Type = Integer32
_Dnd46_Object = MibScalar
dnd46 = _Dnd46_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 46),
    _Dnd46_Type()
)
dnd46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd46.setStatus("current")
_Dnd47_Type = Integer32
_Dnd47_Object = MibScalar
dnd47 = _Dnd47_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 47),
    _Dnd47_Type()
)
dnd47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd47.setStatus("current")
_Dnd48_Type = Integer32
_Dnd48_Object = MibScalar
dnd48 = _Dnd48_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 48),
    _Dnd48_Type()
)
dnd48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd48.setStatus("current")
_Dnd49_Type = Integer32
_Dnd49_Object = MibScalar
dnd49 = _Dnd49_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 49),
    _Dnd49_Type()
)
dnd49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd49.setStatus("current")
_Dnd50_Type = Integer32
_Dnd50_Object = MibScalar
dnd50 = _Dnd50_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 50),
    _Dnd50_Type()
)
dnd50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd50.setStatus("current")
_Dnd51_Type = Integer32
_Dnd51_Object = MibScalar
dnd51 = _Dnd51_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 51),
    _Dnd51_Type()
)
dnd51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd51.setStatus("current")
_Dnd52_Type = Integer32
_Dnd52_Object = MibScalar
dnd52 = _Dnd52_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 52),
    _Dnd52_Type()
)
dnd52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd52.setStatus("current")
_Dnd53_Type = Integer32
_Dnd53_Object = MibScalar
dnd53 = _Dnd53_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 53),
    _Dnd53_Type()
)
dnd53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd53.setStatus("current")
_Dnd54_Type = Integer32
_Dnd54_Object = MibScalar
dnd54 = _Dnd54_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 54),
    _Dnd54_Type()
)
dnd54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd54.setStatus("current")
_Dnd55_Type = Integer32
_Dnd55_Object = MibScalar
dnd55 = _Dnd55_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 55),
    _Dnd55_Type()
)
dnd55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd55.setStatus("current")
_Dnd56_Type = Integer32
_Dnd56_Object = MibScalar
dnd56 = _Dnd56_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 56),
    _Dnd56_Type()
)
dnd56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd56.setStatus("current")
_Dnd57_Type = Integer32
_Dnd57_Object = MibScalar
dnd57 = _Dnd57_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 57),
    _Dnd57_Type()
)
dnd57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd57.setStatus("current")
_Dnd58_Type = Integer32
_Dnd58_Object = MibScalar
dnd58 = _Dnd58_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 58),
    _Dnd58_Type()
)
dnd58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd58.setStatus("current")
_Dnd59_Type = Integer32
_Dnd59_Object = MibScalar
dnd59 = _Dnd59_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 59),
    _Dnd59_Type()
)
dnd59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd59.setStatus("current")
_Dnd60_Type = Integer32
_Dnd60_Object = MibScalar
dnd60 = _Dnd60_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 60),
    _Dnd60_Type()
)
dnd60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd60.setStatus("current")
_Dnd61_Type = Integer32
_Dnd61_Object = MibScalar
dnd61 = _Dnd61_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 61),
    _Dnd61_Type()
)
dnd61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd61.setStatus("current")
_Dnd62_Type = Integer32
_Dnd62_Object = MibScalar
dnd62 = _Dnd62_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 62),
    _Dnd62_Type()
)
dnd62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd62.setStatus("current")
_Dnd63_Type = Integer32
_Dnd63_Object = MibScalar
dnd63 = _Dnd63_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 63),
    _Dnd63_Type()
)
dnd63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd63.setStatus("current")
_Dnd64_Type = Integer32
_Dnd64_Object = MibScalar
dnd64 = _Dnd64_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 64),
    _Dnd64_Type()
)
dnd64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd64.setStatus("current")
_Dnd65_Type = Integer32
_Dnd65_Object = MibScalar
dnd65 = _Dnd65_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 65),
    _Dnd65_Type()
)
dnd65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd65.setStatus("current")
_Dnd66_Type = Integer32
_Dnd66_Object = MibScalar
dnd66 = _Dnd66_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 66),
    _Dnd66_Type()
)
dnd66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd66.setStatus("current")
_Dnd67_Type = Integer32
_Dnd67_Object = MibScalar
dnd67 = _Dnd67_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 67),
    _Dnd67_Type()
)
dnd67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd67.setStatus("current")
_Dnd68_Type = Integer32
_Dnd68_Object = MibScalar
dnd68 = _Dnd68_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 68),
    _Dnd68_Type()
)
dnd68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd68.setStatus("current")
_Dnd69_Type = Integer32
_Dnd69_Object = MibScalar
dnd69 = _Dnd69_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 69),
    _Dnd69_Type()
)
dnd69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd69.setStatus("current")
_Dnd70_Type = Integer32
_Dnd70_Object = MibScalar
dnd70 = _Dnd70_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 70),
    _Dnd70_Type()
)
dnd70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd70.setStatus("current")
_Dnd71_Type = Integer32
_Dnd71_Object = MibScalar
dnd71 = _Dnd71_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 71),
    _Dnd71_Type()
)
dnd71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd71.setStatus("current")
_Dnd72_Type = Integer32
_Dnd72_Object = MibScalar
dnd72 = _Dnd72_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 72),
    _Dnd72_Type()
)
dnd72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd72.setStatus("current")
_Dnd73_Type = Integer32
_Dnd73_Object = MibScalar
dnd73 = _Dnd73_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 73),
    _Dnd73_Type()
)
dnd73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd73.setStatus("current")
_Dnd74_Type = Integer32
_Dnd74_Object = MibScalar
dnd74 = _Dnd74_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 74),
    _Dnd74_Type()
)
dnd74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd74.setStatus("current")
_Dnd75_Type = Integer32
_Dnd75_Object = MibScalar
dnd75 = _Dnd75_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 75),
    _Dnd75_Type()
)
dnd75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd75.setStatus("current")
_Dnd76_Type = Integer32
_Dnd76_Object = MibScalar
dnd76 = _Dnd76_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 76),
    _Dnd76_Type()
)
dnd76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd76.setStatus("current")
_Dnd77_Type = Integer32
_Dnd77_Object = MibScalar
dnd77 = _Dnd77_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 77),
    _Dnd77_Type()
)
dnd77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd77.setStatus("current")
_Dnd78_Type = Integer32
_Dnd78_Object = MibScalar
dnd78 = _Dnd78_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 78),
    _Dnd78_Type()
)
dnd78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd78.setStatus("current")
_Dnd79_Type = Integer32
_Dnd79_Object = MibScalar
dnd79 = _Dnd79_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 79),
    _Dnd79_Type()
)
dnd79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd79.setStatus("current")
_Dnd80_Type = Integer32
_Dnd80_Object = MibScalar
dnd80 = _Dnd80_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 80),
    _Dnd80_Type()
)
dnd80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd80.setStatus("current")
_Dnd81_Type = Integer32
_Dnd81_Object = MibScalar
dnd81 = _Dnd81_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 81),
    _Dnd81_Type()
)
dnd81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd81.setStatus("current")
_Dnd82_Type = Integer32
_Dnd82_Object = MibScalar
dnd82 = _Dnd82_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 82),
    _Dnd82_Type()
)
dnd82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd82.setStatus("current")
_Dnd83_Type = Integer32
_Dnd83_Object = MibScalar
dnd83 = _Dnd83_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 83),
    _Dnd83_Type()
)
dnd83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd83.setStatus("current")
_Dnd84_Type = Integer32
_Dnd84_Object = MibScalar
dnd84 = _Dnd84_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 84),
    _Dnd84_Type()
)
dnd84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd84.setStatus("current")
_Dnd85_Type = Integer32
_Dnd85_Object = MibScalar
dnd85 = _Dnd85_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 85),
    _Dnd85_Type()
)
dnd85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd85.setStatus("current")
_Dnd86_Type = Integer32
_Dnd86_Object = MibScalar
dnd86 = _Dnd86_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 86),
    _Dnd86_Type()
)
dnd86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd86.setStatus("current")
_Dnd87_Type = Integer32
_Dnd87_Object = MibScalar
dnd87 = _Dnd87_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 87),
    _Dnd87_Type()
)
dnd87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd87.setStatus("current")
_Dnd88_Type = Integer32
_Dnd88_Object = MibScalar
dnd88 = _Dnd88_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 88),
    _Dnd88_Type()
)
dnd88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd88.setStatus("current")
_Dnd89_Type = Integer32
_Dnd89_Object = MibScalar
dnd89 = _Dnd89_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 89),
    _Dnd89_Type()
)
dnd89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd89.setStatus("current")
_Dnd90_Type = Integer32
_Dnd90_Object = MibScalar
dnd90 = _Dnd90_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 90),
    _Dnd90_Type()
)
dnd90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd90.setStatus("current")
_Dnd91_Type = Integer32
_Dnd91_Object = MibScalar
dnd91 = _Dnd91_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 91),
    _Dnd91_Type()
)
dnd91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd91.setStatus("current")
_Dnd92_Type = Integer32
_Dnd92_Object = MibScalar
dnd92 = _Dnd92_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 92),
    _Dnd92_Type()
)
dnd92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd92.setStatus("current")
_Dnd93_Type = Integer32
_Dnd93_Object = MibScalar
dnd93 = _Dnd93_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 93),
    _Dnd93_Type()
)
dnd93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd93.setStatus("current")
_Dnd94_Type = Integer32
_Dnd94_Object = MibScalar
dnd94 = _Dnd94_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 94),
    _Dnd94_Type()
)
dnd94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd94.setStatus("current")
_Dnd95_Type = Integer32
_Dnd95_Object = MibScalar
dnd95 = _Dnd95_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 95),
    _Dnd95_Type()
)
dnd95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd95.setStatus("current")
_Dnd96_Type = Integer32
_Dnd96_Object = MibScalar
dnd96 = _Dnd96_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 3, 96),
    _Dnd96_Type()
)
dnd96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnd96.setStatus("current")
_Forward_ObjectIdentity = ObjectIdentity
forward = _Forward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4)
)


class _Forward1_Type(DisplayString):
    """Custom type forward1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward1_Type.__name__ = "DisplayString"
_Forward1_Object = MibScalar
forward1 = _Forward1_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 1),
    _Forward1_Type()
)
forward1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward1.setStatus("current")


class _Forward2_Type(DisplayString):
    """Custom type forward2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward2_Type.__name__ = "DisplayString"
_Forward2_Object = MibScalar
forward2 = _Forward2_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 2),
    _Forward2_Type()
)
forward2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward2.setStatus("current")


class _Forward3_Type(DisplayString):
    """Custom type forward3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward3_Type.__name__ = "DisplayString"
_Forward3_Object = MibScalar
forward3 = _Forward3_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 3),
    _Forward3_Type()
)
forward3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward3.setStatus("current")


class _Forward4_Type(DisplayString):
    """Custom type forward4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward4_Type.__name__ = "DisplayString"
_Forward4_Object = MibScalar
forward4 = _Forward4_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 4),
    _Forward4_Type()
)
forward4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward4.setStatus("current")


class _Forward5_Type(DisplayString):
    """Custom type forward5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward5_Type.__name__ = "DisplayString"
_Forward5_Object = MibScalar
forward5 = _Forward5_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 5),
    _Forward5_Type()
)
forward5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward5.setStatus("current")


class _Forward6_Type(DisplayString):
    """Custom type forward6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward6_Type.__name__ = "DisplayString"
_Forward6_Object = MibScalar
forward6 = _Forward6_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 6),
    _Forward6_Type()
)
forward6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward6.setStatus("current")


class _Forward7_Type(DisplayString):
    """Custom type forward7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward7_Type.__name__ = "DisplayString"
_Forward7_Object = MibScalar
forward7 = _Forward7_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 7),
    _Forward7_Type()
)
forward7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward7.setStatus("current")


class _Forward8_Type(DisplayString):
    """Custom type forward8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward8_Type.__name__ = "DisplayString"
_Forward8_Object = MibScalar
forward8 = _Forward8_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 8),
    _Forward8_Type()
)
forward8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward8.setStatus("current")


class _Forward9_Type(DisplayString):
    """Custom type forward9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward9_Type.__name__ = "DisplayString"
_Forward9_Object = MibScalar
forward9 = _Forward9_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 9),
    _Forward9_Type()
)
forward9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward9.setStatus("current")


class _Forward10_Type(DisplayString):
    """Custom type forward10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward10_Type.__name__ = "DisplayString"
_Forward10_Object = MibScalar
forward10 = _Forward10_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 10),
    _Forward10_Type()
)
forward10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward10.setStatus("current")


class _Forward11_Type(DisplayString):
    """Custom type forward11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward11_Type.__name__ = "DisplayString"
_Forward11_Object = MibScalar
forward11 = _Forward11_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 11),
    _Forward11_Type()
)
forward11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward11.setStatus("current")


class _Forward12_Type(DisplayString):
    """Custom type forward12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward12_Type.__name__ = "DisplayString"
_Forward12_Object = MibScalar
forward12 = _Forward12_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 12),
    _Forward12_Type()
)
forward12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward12.setStatus("current")


class _Forward13_Type(DisplayString):
    """Custom type forward13 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward13_Type.__name__ = "DisplayString"
_Forward13_Object = MibScalar
forward13 = _Forward13_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 13),
    _Forward13_Type()
)
forward13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward13.setStatus("current")


class _Forward14_Type(DisplayString):
    """Custom type forward14 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward14_Type.__name__ = "DisplayString"
_Forward14_Object = MibScalar
forward14 = _Forward14_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 14),
    _Forward14_Type()
)
forward14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward14.setStatus("current")


class _Forward15_Type(DisplayString):
    """Custom type forward15 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward15_Type.__name__ = "DisplayString"
_Forward15_Object = MibScalar
forward15 = _Forward15_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 15),
    _Forward15_Type()
)
forward15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward15.setStatus("current")


class _Forward16_Type(DisplayString):
    """Custom type forward16 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward16_Type.__name__ = "DisplayString"
_Forward16_Object = MibScalar
forward16 = _Forward16_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 16),
    _Forward16_Type()
)
forward16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward16.setStatus("current")


class _Forward17_Type(DisplayString):
    """Custom type forward17 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward17_Type.__name__ = "DisplayString"
_Forward17_Object = MibScalar
forward17 = _Forward17_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 17),
    _Forward17_Type()
)
forward17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward17.setStatus("current")


class _Forward18_Type(DisplayString):
    """Custom type forward18 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward18_Type.__name__ = "DisplayString"
_Forward18_Object = MibScalar
forward18 = _Forward18_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 18),
    _Forward18_Type()
)
forward18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward18.setStatus("current")


class _Forward19_Type(DisplayString):
    """Custom type forward19 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward19_Type.__name__ = "DisplayString"
_Forward19_Object = MibScalar
forward19 = _Forward19_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 19),
    _Forward19_Type()
)
forward19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward19.setStatus("current")


class _Forward20_Type(DisplayString):
    """Custom type forward20 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward20_Type.__name__ = "DisplayString"
_Forward20_Object = MibScalar
forward20 = _Forward20_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 20),
    _Forward20_Type()
)
forward20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward20.setStatus("current")


class _Forward21_Type(DisplayString):
    """Custom type forward21 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward21_Type.__name__ = "DisplayString"
_Forward21_Object = MibScalar
forward21 = _Forward21_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 21),
    _Forward21_Type()
)
forward21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward21.setStatus("current")


class _Forward22_Type(DisplayString):
    """Custom type forward22 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward22_Type.__name__ = "DisplayString"
_Forward22_Object = MibScalar
forward22 = _Forward22_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 22),
    _Forward22_Type()
)
forward22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward22.setStatus("current")


class _Forward23_Type(DisplayString):
    """Custom type forward23 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward23_Type.__name__ = "DisplayString"
_Forward23_Object = MibScalar
forward23 = _Forward23_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 23),
    _Forward23_Type()
)
forward23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward23.setStatus("current")


class _Forward24_Type(DisplayString):
    """Custom type forward24 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward24_Type.__name__ = "DisplayString"
_Forward24_Object = MibScalar
forward24 = _Forward24_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 24),
    _Forward24_Type()
)
forward24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward24.setStatus("current")


class _Forward25_Type(DisplayString):
    """Custom type forward25 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward25_Type.__name__ = "DisplayString"
_Forward25_Object = MibScalar
forward25 = _Forward25_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 25),
    _Forward25_Type()
)
forward25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward25.setStatus("current")


class _Forward26_Type(DisplayString):
    """Custom type forward26 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward26_Type.__name__ = "DisplayString"
_Forward26_Object = MibScalar
forward26 = _Forward26_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 26),
    _Forward26_Type()
)
forward26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward26.setStatus("current")


class _Forward27_Type(DisplayString):
    """Custom type forward27 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward27_Type.__name__ = "DisplayString"
_Forward27_Object = MibScalar
forward27 = _Forward27_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 27),
    _Forward27_Type()
)
forward27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward27.setStatus("current")


class _Forward28_Type(DisplayString):
    """Custom type forward28 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward28_Type.__name__ = "DisplayString"
_Forward28_Object = MibScalar
forward28 = _Forward28_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 28),
    _Forward28_Type()
)
forward28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward28.setStatus("current")


class _Forward29_Type(DisplayString):
    """Custom type forward29 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward29_Type.__name__ = "DisplayString"
_Forward29_Object = MibScalar
forward29 = _Forward29_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 29),
    _Forward29_Type()
)
forward29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward29.setStatus("current")


class _Forward30_Type(DisplayString):
    """Custom type forward30 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward30_Type.__name__ = "DisplayString"
_Forward30_Object = MibScalar
forward30 = _Forward30_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 30),
    _Forward30_Type()
)
forward30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward30.setStatus("current")


class _Forward31_Type(DisplayString):
    """Custom type forward31 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward31_Type.__name__ = "DisplayString"
_Forward31_Object = MibScalar
forward31 = _Forward31_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 31),
    _Forward31_Type()
)
forward31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward31.setStatus("current")


class _Forward32_Type(DisplayString):
    """Custom type forward32 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward32_Type.__name__ = "DisplayString"
_Forward32_Object = MibScalar
forward32 = _Forward32_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 32),
    _Forward32_Type()
)
forward32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward32.setStatus("current")


class _Forward33_Type(DisplayString):
    """Custom type forward33 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward33_Type.__name__ = "DisplayString"
_Forward33_Object = MibScalar
forward33 = _Forward33_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 33),
    _Forward33_Type()
)
forward33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward33.setStatus("current")


class _Forward34_Type(DisplayString):
    """Custom type forward34 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward34_Type.__name__ = "DisplayString"
_Forward34_Object = MibScalar
forward34 = _Forward34_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 34),
    _Forward34_Type()
)
forward34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward34.setStatus("current")


class _Forward35_Type(DisplayString):
    """Custom type forward35 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward35_Type.__name__ = "DisplayString"
_Forward35_Object = MibScalar
forward35 = _Forward35_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 35),
    _Forward35_Type()
)
forward35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward35.setStatus("current")


class _Forward36_Type(DisplayString):
    """Custom type forward36 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward36_Type.__name__ = "DisplayString"
_Forward36_Object = MibScalar
forward36 = _Forward36_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 36),
    _Forward36_Type()
)
forward36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward36.setStatus("current")


class _Forward37_Type(DisplayString):
    """Custom type forward37 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward37_Type.__name__ = "DisplayString"
_Forward37_Object = MibScalar
forward37 = _Forward37_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 37),
    _Forward37_Type()
)
forward37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward37.setStatus("current")


class _Forward38_Type(DisplayString):
    """Custom type forward38 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward38_Type.__name__ = "DisplayString"
_Forward38_Object = MibScalar
forward38 = _Forward38_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 38),
    _Forward38_Type()
)
forward38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward38.setStatus("current")


class _Forward39_Type(DisplayString):
    """Custom type forward39 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward39_Type.__name__ = "DisplayString"
_Forward39_Object = MibScalar
forward39 = _Forward39_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 39),
    _Forward39_Type()
)
forward39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward39.setStatus("current")


class _Forward40_Type(DisplayString):
    """Custom type forward40 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward40_Type.__name__ = "DisplayString"
_Forward40_Object = MibScalar
forward40 = _Forward40_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 40),
    _Forward40_Type()
)
forward40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward40.setStatus("current")


class _Forward41_Type(DisplayString):
    """Custom type forward41 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward41_Type.__name__ = "DisplayString"
_Forward41_Object = MibScalar
forward41 = _Forward41_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 41),
    _Forward41_Type()
)
forward41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward41.setStatus("current")


class _Forward42_Type(DisplayString):
    """Custom type forward42 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward42_Type.__name__ = "DisplayString"
_Forward42_Object = MibScalar
forward42 = _Forward42_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 42),
    _Forward42_Type()
)
forward42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward42.setStatus("current")


class _Forward43_Type(DisplayString):
    """Custom type forward43 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward43_Type.__name__ = "DisplayString"
_Forward43_Object = MibScalar
forward43 = _Forward43_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 43),
    _Forward43_Type()
)
forward43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward43.setStatus("current")


class _Forward44_Type(DisplayString):
    """Custom type forward44 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward44_Type.__name__ = "DisplayString"
_Forward44_Object = MibScalar
forward44 = _Forward44_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 44),
    _Forward44_Type()
)
forward44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward44.setStatus("current")


class _Forward45_Type(DisplayString):
    """Custom type forward45 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward45_Type.__name__ = "DisplayString"
_Forward45_Object = MibScalar
forward45 = _Forward45_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 45),
    _Forward45_Type()
)
forward45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward45.setStatus("current")


class _Forward46_Type(DisplayString):
    """Custom type forward46 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward46_Type.__name__ = "DisplayString"
_Forward46_Object = MibScalar
forward46 = _Forward46_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 46),
    _Forward46_Type()
)
forward46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward46.setStatus("current")


class _Forward47_Type(DisplayString):
    """Custom type forward47 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward47_Type.__name__ = "DisplayString"
_Forward47_Object = MibScalar
forward47 = _Forward47_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 47),
    _Forward47_Type()
)
forward47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward47.setStatus("current")


class _Forward48_Type(DisplayString):
    """Custom type forward48 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward48_Type.__name__ = "DisplayString"
_Forward48_Object = MibScalar
forward48 = _Forward48_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 48),
    _Forward48_Type()
)
forward48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward48.setStatus("current")


class _Forward49_Type(DisplayString):
    """Custom type forward49 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward49_Type.__name__ = "DisplayString"
_Forward49_Object = MibScalar
forward49 = _Forward49_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 49),
    _Forward49_Type()
)
forward49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward49.setStatus("current")


class _Forward50_Type(DisplayString):
    """Custom type forward50 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward50_Type.__name__ = "DisplayString"
_Forward50_Object = MibScalar
forward50 = _Forward50_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 50),
    _Forward50_Type()
)
forward50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward50.setStatus("current")


class _Forward51_Type(DisplayString):
    """Custom type forward51 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward51_Type.__name__ = "DisplayString"
_Forward51_Object = MibScalar
forward51 = _Forward51_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 51),
    _Forward51_Type()
)
forward51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward51.setStatus("current")


class _Forward52_Type(DisplayString):
    """Custom type forward52 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward52_Type.__name__ = "DisplayString"
_Forward52_Object = MibScalar
forward52 = _Forward52_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 52),
    _Forward52_Type()
)
forward52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward52.setStatus("current")


class _Forward53_Type(DisplayString):
    """Custom type forward53 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward53_Type.__name__ = "DisplayString"
_Forward53_Object = MibScalar
forward53 = _Forward53_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 53),
    _Forward53_Type()
)
forward53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward53.setStatus("current")


class _Forward54_Type(DisplayString):
    """Custom type forward54 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward54_Type.__name__ = "DisplayString"
_Forward54_Object = MibScalar
forward54 = _Forward54_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 54),
    _Forward54_Type()
)
forward54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward54.setStatus("current")


class _Forward55_Type(DisplayString):
    """Custom type forward55 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward55_Type.__name__ = "DisplayString"
_Forward55_Object = MibScalar
forward55 = _Forward55_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 55),
    _Forward55_Type()
)
forward55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward55.setStatus("current")


class _Forward56_Type(DisplayString):
    """Custom type forward56 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward56_Type.__name__ = "DisplayString"
_Forward56_Object = MibScalar
forward56 = _Forward56_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 56),
    _Forward56_Type()
)
forward56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward56.setStatus("current")


class _Forward57_Type(DisplayString):
    """Custom type forward57 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward57_Type.__name__ = "DisplayString"
_Forward57_Object = MibScalar
forward57 = _Forward57_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 57),
    _Forward57_Type()
)
forward57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward57.setStatus("current")


class _Forward58_Type(DisplayString):
    """Custom type forward58 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward58_Type.__name__ = "DisplayString"
_Forward58_Object = MibScalar
forward58 = _Forward58_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 58),
    _Forward58_Type()
)
forward58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward58.setStatus("current")


class _Forward59_Type(DisplayString):
    """Custom type forward59 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward59_Type.__name__ = "DisplayString"
_Forward59_Object = MibScalar
forward59 = _Forward59_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 59),
    _Forward59_Type()
)
forward59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward59.setStatus("current")


class _Forward60_Type(DisplayString):
    """Custom type forward60 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward60_Type.__name__ = "DisplayString"
_Forward60_Object = MibScalar
forward60 = _Forward60_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 60),
    _Forward60_Type()
)
forward60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward60.setStatus("current")


class _Forward61_Type(DisplayString):
    """Custom type forward61 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward61_Type.__name__ = "DisplayString"
_Forward61_Object = MibScalar
forward61 = _Forward61_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 61),
    _Forward61_Type()
)
forward61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward61.setStatus("current")


class _Forward62_Type(DisplayString):
    """Custom type forward62 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward62_Type.__name__ = "DisplayString"
_Forward62_Object = MibScalar
forward62 = _Forward62_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 62),
    _Forward62_Type()
)
forward62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward62.setStatus("current")


class _Forward63_Type(DisplayString):
    """Custom type forward63 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward63_Type.__name__ = "DisplayString"
_Forward63_Object = MibScalar
forward63 = _Forward63_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 63),
    _Forward63_Type()
)
forward63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward63.setStatus("current")


class _Forward64_Type(DisplayString):
    """Custom type forward64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward64_Type.__name__ = "DisplayString"
_Forward64_Object = MibScalar
forward64 = _Forward64_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 64),
    _Forward64_Type()
)
forward64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward64.setStatus("current")


class _Forward65_Type(DisplayString):
    """Custom type forward65 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward65_Type.__name__ = "DisplayString"
_Forward65_Object = MibScalar
forward65 = _Forward65_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 65),
    _Forward65_Type()
)
forward65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward65.setStatus("current")


class _Forward66_Type(DisplayString):
    """Custom type forward66 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward66_Type.__name__ = "DisplayString"
_Forward66_Object = MibScalar
forward66 = _Forward66_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 66),
    _Forward66_Type()
)
forward66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward66.setStatus("current")


class _Forward67_Type(DisplayString):
    """Custom type forward67 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward67_Type.__name__ = "DisplayString"
_Forward67_Object = MibScalar
forward67 = _Forward67_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 67),
    _Forward67_Type()
)
forward67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward67.setStatus("current")


class _Forward68_Type(DisplayString):
    """Custom type forward68 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward68_Type.__name__ = "DisplayString"
_Forward68_Object = MibScalar
forward68 = _Forward68_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 68),
    _Forward68_Type()
)
forward68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward68.setStatus("current")


class _Forward69_Type(DisplayString):
    """Custom type forward69 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward69_Type.__name__ = "DisplayString"
_Forward69_Object = MibScalar
forward69 = _Forward69_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 69),
    _Forward69_Type()
)
forward69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward69.setStatus("current")


class _Forward70_Type(DisplayString):
    """Custom type forward70 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward70_Type.__name__ = "DisplayString"
_Forward70_Object = MibScalar
forward70 = _Forward70_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 70),
    _Forward70_Type()
)
forward70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward70.setStatus("current")


class _Forward71_Type(DisplayString):
    """Custom type forward71 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward71_Type.__name__ = "DisplayString"
_Forward71_Object = MibScalar
forward71 = _Forward71_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 71),
    _Forward71_Type()
)
forward71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward71.setStatus("current")


class _Forward72_Type(DisplayString):
    """Custom type forward72 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward72_Type.__name__ = "DisplayString"
_Forward72_Object = MibScalar
forward72 = _Forward72_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 72),
    _Forward72_Type()
)
forward72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward72.setStatus("current")


class _Forward73_Type(DisplayString):
    """Custom type forward73 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward73_Type.__name__ = "DisplayString"
_Forward73_Object = MibScalar
forward73 = _Forward73_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 73),
    _Forward73_Type()
)
forward73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward73.setStatus("current")


class _Forward74_Type(DisplayString):
    """Custom type forward74 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward74_Type.__name__ = "DisplayString"
_Forward74_Object = MibScalar
forward74 = _Forward74_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 74),
    _Forward74_Type()
)
forward74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward74.setStatus("current")


class _Forward75_Type(DisplayString):
    """Custom type forward75 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward75_Type.__name__ = "DisplayString"
_Forward75_Object = MibScalar
forward75 = _Forward75_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 75),
    _Forward75_Type()
)
forward75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward75.setStatus("current")


class _Forward76_Type(DisplayString):
    """Custom type forward76 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward76_Type.__name__ = "DisplayString"
_Forward76_Object = MibScalar
forward76 = _Forward76_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 76),
    _Forward76_Type()
)
forward76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward76.setStatus("current")


class _Forward77_Type(DisplayString):
    """Custom type forward77 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward77_Type.__name__ = "DisplayString"
_Forward77_Object = MibScalar
forward77 = _Forward77_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 77),
    _Forward77_Type()
)
forward77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward77.setStatus("current")


class _Forward78_Type(DisplayString):
    """Custom type forward78 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward78_Type.__name__ = "DisplayString"
_Forward78_Object = MibScalar
forward78 = _Forward78_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 78),
    _Forward78_Type()
)
forward78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward78.setStatus("current")


class _Forward79_Type(DisplayString):
    """Custom type forward79 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward79_Type.__name__ = "DisplayString"
_Forward79_Object = MibScalar
forward79 = _Forward79_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 79),
    _Forward79_Type()
)
forward79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward79.setStatus("current")


class _Forward80_Type(DisplayString):
    """Custom type forward80 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward80_Type.__name__ = "DisplayString"
_Forward80_Object = MibScalar
forward80 = _Forward80_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 80),
    _Forward80_Type()
)
forward80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward80.setStatus("current")


class _Forward81_Type(DisplayString):
    """Custom type forward81 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward81_Type.__name__ = "DisplayString"
_Forward81_Object = MibScalar
forward81 = _Forward81_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 81),
    _Forward81_Type()
)
forward81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward81.setStatus("current")


class _Forward82_Type(DisplayString):
    """Custom type forward82 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward82_Type.__name__ = "DisplayString"
_Forward82_Object = MibScalar
forward82 = _Forward82_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 82),
    _Forward82_Type()
)
forward82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward82.setStatus("current")


class _Forward83_Type(DisplayString):
    """Custom type forward83 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward83_Type.__name__ = "DisplayString"
_Forward83_Object = MibScalar
forward83 = _Forward83_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 83),
    _Forward83_Type()
)
forward83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward83.setStatus("current")


class _Forward84_Type(DisplayString):
    """Custom type forward84 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward84_Type.__name__ = "DisplayString"
_Forward84_Object = MibScalar
forward84 = _Forward84_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 84),
    _Forward84_Type()
)
forward84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward84.setStatus("current")


class _Forward85_Type(DisplayString):
    """Custom type forward85 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward85_Type.__name__ = "DisplayString"
_Forward85_Object = MibScalar
forward85 = _Forward85_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 85),
    _Forward85_Type()
)
forward85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward85.setStatus("current")


class _Forward86_Type(DisplayString):
    """Custom type forward86 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward86_Type.__name__ = "DisplayString"
_Forward86_Object = MibScalar
forward86 = _Forward86_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 86),
    _Forward86_Type()
)
forward86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward86.setStatus("current")


class _Forward87_Type(DisplayString):
    """Custom type forward87 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward87_Type.__name__ = "DisplayString"
_Forward87_Object = MibScalar
forward87 = _Forward87_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 87),
    _Forward87_Type()
)
forward87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward87.setStatus("current")


class _Forward88_Type(DisplayString):
    """Custom type forward88 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward88_Type.__name__ = "DisplayString"
_Forward88_Object = MibScalar
forward88 = _Forward88_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 88),
    _Forward88_Type()
)
forward88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward88.setStatus("current")


class _Forward89_Type(DisplayString):
    """Custom type forward89 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward89_Type.__name__ = "DisplayString"
_Forward89_Object = MibScalar
forward89 = _Forward89_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 89),
    _Forward89_Type()
)
forward89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward89.setStatus("current")


class _Forward90_Type(DisplayString):
    """Custom type forward90 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward90_Type.__name__ = "DisplayString"
_Forward90_Object = MibScalar
forward90 = _Forward90_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 90),
    _Forward90_Type()
)
forward90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward90.setStatus("current")


class _Forward91_Type(DisplayString):
    """Custom type forward91 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward91_Type.__name__ = "DisplayString"
_Forward91_Object = MibScalar
forward91 = _Forward91_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 91),
    _Forward91_Type()
)
forward91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward91.setStatus("current")


class _Forward92_Type(DisplayString):
    """Custom type forward92 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward92_Type.__name__ = "DisplayString"
_Forward92_Object = MibScalar
forward92 = _Forward92_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 92),
    _Forward92_Type()
)
forward92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward92.setStatus("current")


class _Forward93_Type(DisplayString):
    """Custom type forward93 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward93_Type.__name__ = "DisplayString"
_Forward93_Object = MibScalar
forward93 = _Forward93_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 93),
    _Forward93_Type()
)
forward93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward93.setStatus("current")


class _Forward94_Type(DisplayString):
    """Custom type forward94 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward94_Type.__name__ = "DisplayString"
_Forward94_Object = MibScalar
forward94 = _Forward94_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 94),
    _Forward94_Type()
)
forward94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward94.setStatus("current")


class _Forward95_Type(DisplayString):
    """Custom type forward95 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward95_Type.__name__ = "DisplayString"
_Forward95_Object = MibScalar
forward95 = _Forward95_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 95),
    _Forward95_Type()
)
forward95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward95.setStatus("current")


class _Forward96_Type(DisplayString):
    """Custom type forward96 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Forward96_Type.__name__ = "DisplayString"
_Forward96_Object = MibScalar
forward96 = _Forward96_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 4, 96),
    _Forward96_Type()
)
forward96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forward96.setStatus("current")
_BusyForward_ObjectIdentity = ObjectIdentity
busyForward = _BusyForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5)
)


class _BusyForward1_Type(DisplayString):
    """Custom type busyForward1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward1_Type.__name__ = "DisplayString"
_BusyForward1_Object = MibScalar
busyForward1 = _BusyForward1_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 1),
    _BusyForward1_Type()
)
busyForward1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward1.setStatus("current")


class _BusyForward2_Type(DisplayString):
    """Custom type busyForward2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward2_Type.__name__ = "DisplayString"
_BusyForward2_Object = MibScalar
busyForward2 = _BusyForward2_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 2),
    _BusyForward2_Type()
)
busyForward2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward2.setStatus("current")


class _BusyForward3_Type(DisplayString):
    """Custom type busyForward3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward3_Type.__name__ = "DisplayString"
_BusyForward3_Object = MibScalar
busyForward3 = _BusyForward3_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 3),
    _BusyForward3_Type()
)
busyForward3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward3.setStatus("current")


class _BusyForward4_Type(DisplayString):
    """Custom type busyForward4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward4_Type.__name__ = "DisplayString"
_BusyForward4_Object = MibScalar
busyForward4 = _BusyForward4_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 4),
    _BusyForward4_Type()
)
busyForward4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward4.setStatus("current")


class _BusyForward5_Type(DisplayString):
    """Custom type busyForward5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward5_Type.__name__ = "DisplayString"
_BusyForward5_Object = MibScalar
busyForward5 = _BusyForward5_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 5),
    _BusyForward5_Type()
)
busyForward5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward5.setStatus("current")


class _BusyForward6_Type(DisplayString):
    """Custom type busyForward6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward6_Type.__name__ = "DisplayString"
_BusyForward6_Object = MibScalar
busyForward6 = _BusyForward6_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 6),
    _BusyForward6_Type()
)
busyForward6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward6.setStatus("current")


class _BusyForward7_Type(DisplayString):
    """Custom type busyForward7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward7_Type.__name__ = "DisplayString"
_BusyForward7_Object = MibScalar
busyForward7 = _BusyForward7_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 7),
    _BusyForward7_Type()
)
busyForward7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward7.setStatus("current")


class _BusyForward8_Type(DisplayString):
    """Custom type busyForward8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward8_Type.__name__ = "DisplayString"
_BusyForward8_Object = MibScalar
busyForward8 = _BusyForward8_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 8),
    _BusyForward8_Type()
)
busyForward8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward8.setStatus("current")


class _BusyForward9_Type(DisplayString):
    """Custom type busyForward9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward9_Type.__name__ = "DisplayString"
_BusyForward9_Object = MibScalar
busyForward9 = _BusyForward9_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 9),
    _BusyForward9_Type()
)
busyForward9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward9.setStatus("current")


class _BusyForward10_Type(DisplayString):
    """Custom type busyForward10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward10_Type.__name__ = "DisplayString"
_BusyForward10_Object = MibScalar
busyForward10 = _BusyForward10_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 10),
    _BusyForward10_Type()
)
busyForward10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward10.setStatus("current")


class _BusyForward11_Type(DisplayString):
    """Custom type busyForward11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward11_Type.__name__ = "DisplayString"
_BusyForward11_Object = MibScalar
busyForward11 = _BusyForward11_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 11),
    _BusyForward11_Type()
)
busyForward11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward11.setStatus("current")


class _BusyForward12_Type(DisplayString):
    """Custom type busyForward12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward12_Type.__name__ = "DisplayString"
_BusyForward12_Object = MibScalar
busyForward12 = _BusyForward12_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 12),
    _BusyForward12_Type()
)
busyForward12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward12.setStatus("current")


class _BusyForward13_Type(DisplayString):
    """Custom type busyForward13 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward13_Type.__name__ = "DisplayString"
_BusyForward13_Object = MibScalar
busyForward13 = _BusyForward13_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 13),
    _BusyForward13_Type()
)
busyForward13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward13.setStatus("current")


class _BusyForward14_Type(DisplayString):
    """Custom type busyForward14 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward14_Type.__name__ = "DisplayString"
_BusyForward14_Object = MibScalar
busyForward14 = _BusyForward14_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 14),
    _BusyForward14_Type()
)
busyForward14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward14.setStatus("current")


class _BusyForward15_Type(DisplayString):
    """Custom type busyForward15 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward15_Type.__name__ = "DisplayString"
_BusyForward15_Object = MibScalar
busyForward15 = _BusyForward15_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 15),
    _BusyForward15_Type()
)
busyForward15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward15.setStatus("current")


class _BusyForward16_Type(DisplayString):
    """Custom type busyForward16 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward16_Type.__name__ = "DisplayString"
_BusyForward16_Object = MibScalar
busyForward16 = _BusyForward16_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 16),
    _BusyForward16_Type()
)
busyForward16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward16.setStatus("current")


class _BusyForward17_Type(DisplayString):
    """Custom type busyForward17 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward17_Type.__name__ = "DisplayString"
_BusyForward17_Object = MibScalar
busyForward17 = _BusyForward17_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 17),
    _BusyForward17_Type()
)
busyForward17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward17.setStatus("current")


class _BusyForward18_Type(DisplayString):
    """Custom type busyForward18 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward18_Type.__name__ = "DisplayString"
_BusyForward18_Object = MibScalar
busyForward18 = _BusyForward18_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 18),
    _BusyForward18_Type()
)
busyForward18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward18.setStatus("current")


class _BusyForward19_Type(DisplayString):
    """Custom type busyForward19 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward19_Type.__name__ = "DisplayString"
_BusyForward19_Object = MibScalar
busyForward19 = _BusyForward19_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 19),
    _BusyForward19_Type()
)
busyForward19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward19.setStatus("current")


class _BusyForward20_Type(DisplayString):
    """Custom type busyForward20 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward20_Type.__name__ = "DisplayString"
_BusyForward20_Object = MibScalar
busyForward20 = _BusyForward20_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 20),
    _BusyForward20_Type()
)
busyForward20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward20.setStatus("current")


class _BusyForward21_Type(DisplayString):
    """Custom type busyForward21 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward21_Type.__name__ = "DisplayString"
_BusyForward21_Object = MibScalar
busyForward21 = _BusyForward21_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 21),
    _BusyForward21_Type()
)
busyForward21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward21.setStatus("current")


class _BusyForward22_Type(DisplayString):
    """Custom type busyForward22 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward22_Type.__name__ = "DisplayString"
_BusyForward22_Object = MibScalar
busyForward22 = _BusyForward22_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 22),
    _BusyForward22_Type()
)
busyForward22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward22.setStatus("current")


class _BusyForward23_Type(DisplayString):
    """Custom type busyForward23 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward23_Type.__name__ = "DisplayString"
_BusyForward23_Object = MibScalar
busyForward23 = _BusyForward23_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 23),
    _BusyForward23_Type()
)
busyForward23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward23.setStatus("current")


class _BusyForward24_Type(DisplayString):
    """Custom type busyForward24 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward24_Type.__name__ = "DisplayString"
_BusyForward24_Object = MibScalar
busyForward24 = _BusyForward24_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 24),
    _BusyForward24_Type()
)
busyForward24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward24.setStatus("current")


class _BusyForward25_Type(DisplayString):
    """Custom type busyForward25 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward25_Type.__name__ = "DisplayString"
_BusyForward25_Object = MibScalar
busyForward25 = _BusyForward25_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 25),
    _BusyForward25_Type()
)
busyForward25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward25.setStatus("current")


class _BusyForward26_Type(DisplayString):
    """Custom type busyForward26 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward26_Type.__name__ = "DisplayString"
_BusyForward26_Object = MibScalar
busyForward26 = _BusyForward26_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 26),
    _BusyForward26_Type()
)
busyForward26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward26.setStatus("current")


class _BusyForward27_Type(DisplayString):
    """Custom type busyForward27 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward27_Type.__name__ = "DisplayString"
_BusyForward27_Object = MibScalar
busyForward27 = _BusyForward27_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 27),
    _BusyForward27_Type()
)
busyForward27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward27.setStatus("current")


class _BusyForward28_Type(DisplayString):
    """Custom type busyForward28 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward28_Type.__name__ = "DisplayString"
_BusyForward28_Object = MibScalar
busyForward28 = _BusyForward28_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 28),
    _BusyForward28_Type()
)
busyForward28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward28.setStatus("current")


class _BusyForward29_Type(DisplayString):
    """Custom type busyForward29 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward29_Type.__name__ = "DisplayString"
_BusyForward29_Object = MibScalar
busyForward29 = _BusyForward29_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 29),
    _BusyForward29_Type()
)
busyForward29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward29.setStatus("current")


class _BusyForward30_Type(DisplayString):
    """Custom type busyForward30 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward30_Type.__name__ = "DisplayString"
_BusyForward30_Object = MibScalar
busyForward30 = _BusyForward30_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 30),
    _BusyForward30_Type()
)
busyForward30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward30.setStatus("current")


class _BusyForward31_Type(DisplayString):
    """Custom type busyForward31 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward31_Type.__name__ = "DisplayString"
_BusyForward31_Object = MibScalar
busyForward31 = _BusyForward31_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 31),
    _BusyForward31_Type()
)
busyForward31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward31.setStatus("current")


class _BusyForward32_Type(DisplayString):
    """Custom type busyForward32 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward32_Type.__name__ = "DisplayString"
_BusyForward32_Object = MibScalar
busyForward32 = _BusyForward32_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 32),
    _BusyForward32_Type()
)
busyForward32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward32.setStatus("current")


class _BusyForward33_Type(DisplayString):
    """Custom type busyForward33 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward33_Type.__name__ = "DisplayString"
_BusyForward33_Object = MibScalar
busyForward33 = _BusyForward33_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 33),
    _BusyForward33_Type()
)
busyForward33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward33.setStatus("current")


class _BusyForward34_Type(DisplayString):
    """Custom type busyForward34 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward34_Type.__name__ = "DisplayString"
_BusyForward34_Object = MibScalar
busyForward34 = _BusyForward34_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 34),
    _BusyForward34_Type()
)
busyForward34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward34.setStatus("current")


class _BusyForward35_Type(DisplayString):
    """Custom type busyForward35 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward35_Type.__name__ = "DisplayString"
_BusyForward35_Object = MibScalar
busyForward35 = _BusyForward35_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 35),
    _BusyForward35_Type()
)
busyForward35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward35.setStatus("current")


class _BusyForward36_Type(DisplayString):
    """Custom type busyForward36 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward36_Type.__name__ = "DisplayString"
_BusyForward36_Object = MibScalar
busyForward36 = _BusyForward36_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 36),
    _BusyForward36_Type()
)
busyForward36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward36.setStatus("current")


class _BusyForward37_Type(DisplayString):
    """Custom type busyForward37 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward37_Type.__name__ = "DisplayString"
_BusyForward37_Object = MibScalar
busyForward37 = _BusyForward37_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 37),
    _BusyForward37_Type()
)
busyForward37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward37.setStatus("current")


class _BusyForward38_Type(DisplayString):
    """Custom type busyForward38 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward38_Type.__name__ = "DisplayString"
_BusyForward38_Object = MibScalar
busyForward38 = _BusyForward38_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 38),
    _BusyForward38_Type()
)
busyForward38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward38.setStatus("current")


class _BusyForward39_Type(DisplayString):
    """Custom type busyForward39 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward39_Type.__name__ = "DisplayString"
_BusyForward39_Object = MibScalar
busyForward39 = _BusyForward39_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 39),
    _BusyForward39_Type()
)
busyForward39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward39.setStatus("current")


class _BusyForward40_Type(DisplayString):
    """Custom type busyForward40 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward40_Type.__name__ = "DisplayString"
_BusyForward40_Object = MibScalar
busyForward40 = _BusyForward40_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 40),
    _BusyForward40_Type()
)
busyForward40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward40.setStatus("current")


class _BusyForward41_Type(DisplayString):
    """Custom type busyForward41 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward41_Type.__name__ = "DisplayString"
_BusyForward41_Object = MibScalar
busyForward41 = _BusyForward41_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 41),
    _BusyForward41_Type()
)
busyForward41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward41.setStatus("current")


class _BusyForward42_Type(DisplayString):
    """Custom type busyForward42 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward42_Type.__name__ = "DisplayString"
_BusyForward42_Object = MibScalar
busyForward42 = _BusyForward42_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 42),
    _BusyForward42_Type()
)
busyForward42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward42.setStatus("current")


class _BusyForward43_Type(DisplayString):
    """Custom type busyForward43 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward43_Type.__name__ = "DisplayString"
_BusyForward43_Object = MibScalar
busyForward43 = _BusyForward43_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 43),
    _BusyForward43_Type()
)
busyForward43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward43.setStatus("current")


class _BusyForward44_Type(DisplayString):
    """Custom type busyForward44 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward44_Type.__name__ = "DisplayString"
_BusyForward44_Object = MibScalar
busyForward44 = _BusyForward44_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 44),
    _BusyForward44_Type()
)
busyForward44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward44.setStatus("current")


class _BusyForward45_Type(DisplayString):
    """Custom type busyForward45 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward45_Type.__name__ = "DisplayString"
_BusyForward45_Object = MibScalar
busyForward45 = _BusyForward45_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 45),
    _BusyForward45_Type()
)
busyForward45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward45.setStatus("current")


class _BusyForward46_Type(DisplayString):
    """Custom type busyForward46 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward46_Type.__name__ = "DisplayString"
_BusyForward46_Object = MibScalar
busyForward46 = _BusyForward46_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 46),
    _BusyForward46_Type()
)
busyForward46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward46.setStatus("current")


class _BusyForward47_Type(DisplayString):
    """Custom type busyForward47 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward47_Type.__name__ = "DisplayString"
_BusyForward47_Object = MibScalar
busyForward47 = _BusyForward47_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 47),
    _BusyForward47_Type()
)
busyForward47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward47.setStatus("current")


class _BusyForward48_Type(DisplayString):
    """Custom type busyForward48 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward48_Type.__name__ = "DisplayString"
_BusyForward48_Object = MibScalar
busyForward48 = _BusyForward48_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 48),
    _BusyForward48_Type()
)
busyForward48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward48.setStatus("current")


class _BusyForward49_Type(DisplayString):
    """Custom type busyForward49 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward49_Type.__name__ = "DisplayString"
_BusyForward49_Object = MibScalar
busyForward49 = _BusyForward49_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 49),
    _BusyForward49_Type()
)
busyForward49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward49.setStatus("current")


class _BusyForward50_Type(DisplayString):
    """Custom type busyForward50 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward50_Type.__name__ = "DisplayString"
_BusyForward50_Object = MibScalar
busyForward50 = _BusyForward50_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 50),
    _BusyForward50_Type()
)
busyForward50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward50.setStatus("current")


class _BusyForward51_Type(DisplayString):
    """Custom type busyForward51 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward51_Type.__name__ = "DisplayString"
_BusyForward51_Object = MibScalar
busyForward51 = _BusyForward51_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 51),
    _BusyForward51_Type()
)
busyForward51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward51.setStatus("current")


class _BusyForward52_Type(DisplayString):
    """Custom type busyForward52 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward52_Type.__name__ = "DisplayString"
_BusyForward52_Object = MibScalar
busyForward52 = _BusyForward52_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 52),
    _BusyForward52_Type()
)
busyForward52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward52.setStatus("current")


class _BusyForward53_Type(DisplayString):
    """Custom type busyForward53 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward53_Type.__name__ = "DisplayString"
_BusyForward53_Object = MibScalar
busyForward53 = _BusyForward53_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 53),
    _BusyForward53_Type()
)
busyForward53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward53.setStatus("current")


class _BusyForward54_Type(DisplayString):
    """Custom type busyForward54 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward54_Type.__name__ = "DisplayString"
_BusyForward54_Object = MibScalar
busyForward54 = _BusyForward54_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 54),
    _BusyForward54_Type()
)
busyForward54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward54.setStatus("current")


class _BusyForward55_Type(DisplayString):
    """Custom type busyForward55 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward55_Type.__name__ = "DisplayString"
_BusyForward55_Object = MibScalar
busyForward55 = _BusyForward55_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 55),
    _BusyForward55_Type()
)
busyForward55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward55.setStatus("current")


class _BusyForward56_Type(DisplayString):
    """Custom type busyForward56 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward56_Type.__name__ = "DisplayString"
_BusyForward56_Object = MibScalar
busyForward56 = _BusyForward56_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 56),
    _BusyForward56_Type()
)
busyForward56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward56.setStatus("current")


class _BusyForward57_Type(DisplayString):
    """Custom type busyForward57 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward57_Type.__name__ = "DisplayString"
_BusyForward57_Object = MibScalar
busyForward57 = _BusyForward57_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 57),
    _BusyForward57_Type()
)
busyForward57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward57.setStatus("current")


class _BusyForward58_Type(DisplayString):
    """Custom type busyForward58 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward58_Type.__name__ = "DisplayString"
_BusyForward58_Object = MibScalar
busyForward58 = _BusyForward58_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 58),
    _BusyForward58_Type()
)
busyForward58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward58.setStatus("current")


class _BusyForward59_Type(DisplayString):
    """Custom type busyForward59 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward59_Type.__name__ = "DisplayString"
_BusyForward59_Object = MibScalar
busyForward59 = _BusyForward59_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 59),
    _BusyForward59_Type()
)
busyForward59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward59.setStatus("current")


class _BusyForward60_Type(DisplayString):
    """Custom type busyForward60 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward60_Type.__name__ = "DisplayString"
_BusyForward60_Object = MibScalar
busyForward60 = _BusyForward60_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 60),
    _BusyForward60_Type()
)
busyForward60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward60.setStatus("current")


class _BusyForward61_Type(DisplayString):
    """Custom type busyForward61 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward61_Type.__name__ = "DisplayString"
_BusyForward61_Object = MibScalar
busyForward61 = _BusyForward61_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 61),
    _BusyForward61_Type()
)
busyForward61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward61.setStatus("current")


class _BusyForward62_Type(DisplayString):
    """Custom type busyForward62 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward62_Type.__name__ = "DisplayString"
_BusyForward62_Object = MibScalar
busyForward62 = _BusyForward62_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 62),
    _BusyForward62_Type()
)
busyForward62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward62.setStatus("current")


class _BusyForward63_Type(DisplayString):
    """Custom type busyForward63 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward63_Type.__name__ = "DisplayString"
_BusyForward63_Object = MibScalar
busyForward63 = _BusyForward63_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 63),
    _BusyForward63_Type()
)
busyForward63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward63.setStatus("current")


class _BusyForward64_Type(DisplayString):
    """Custom type busyForward64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward64_Type.__name__ = "DisplayString"
_BusyForward64_Object = MibScalar
busyForward64 = _BusyForward64_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 64),
    _BusyForward64_Type()
)
busyForward64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward64.setStatus("current")


class _BusyForward65_Type(DisplayString):
    """Custom type busyForward65 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward65_Type.__name__ = "DisplayString"
_BusyForward65_Object = MibScalar
busyForward65 = _BusyForward65_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 65),
    _BusyForward65_Type()
)
busyForward65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward65.setStatus("current")


class _BusyForward66_Type(DisplayString):
    """Custom type busyForward66 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward66_Type.__name__ = "DisplayString"
_BusyForward66_Object = MibScalar
busyForward66 = _BusyForward66_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 66),
    _BusyForward66_Type()
)
busyForward66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward66.setStatus("current")


class _BusyForward67_Type(DisplayString):
    """Custom type busyForward67 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward67_Type.__name__ = "DisplayString"
_BusyForward67_Object = MibScalar
busyForward67 = _BusyForward67_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 67),
    _BusyForward67_Type()
)
busyForward67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward67.setStatus("current")


class _BusyForward68_Type(DisplayString):
    """Custom type busyForward68 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward68_Type.__name__ = "DisplayString"
_BusyForward68_Object = MibScalar
busyForward68 = _BusyForward68_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 68),
    _BusyForward68_Type()
)
busyForward68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward68.setStatus("current")


class _BusyForward69_Type(DisplayString):
    """Custom type busyForward69 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward69_Type.__name__ = "DisplayString"
_BusyForward69_Object = MibScalar
busyForward69 = _BusyForward69_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 69),
    _BusyForward69_Type()
)
busyForward69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward69.setStatus("current")


class _BusyForward70_Type(DisplayString):
    """Custom type busyForward70 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward70_Type.__name__ = "DisplayString"
_BusyForward70_Object = MibScalar
busyForward70 = _BusyForward70_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 70),
    _BusyForward70_Type()
)
busyForward70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward70.setStatus("current")


class _BusyForward71_Type(DisplayString):
    """Custom type busyForward71 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward71_Type.__name__ = "DisplayString"
_BusyForward71_Object = MibScalar
busyForward71 = _BusyForward71_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 71),
    _BusyForward71_Type()
)
busyForward71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward71.setStatus("current")


class _BusyForward72_Type(DisplayString):
    """Custom type busyForward72 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward72_Type.__name__ = "DisplayString"
_BusyForward72_Object = MibScalar
busyForward72 = _BusyForward72_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 72),
    _BusyForward72_Type()
)
busyForward72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward72.setStatus("current")


class _BusyForward73_Type(DisplayString):
    """Custom type busyForward73 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward73_Type.__name__ = "DisplayString"
_BusyForward73_Object = MibScalar
busyForward73 = _BusyForward73_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 73),
    _BusyForward73_Type()
)
busyForward73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward73.setStatus("current")


class _BusyForward74_Type(DisplayString):
    """Custom type busyForward74 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward74_Type.__name__ = "DisplayString"
_BusyForward74_Object = MibScalar
busyForward74 = _BusyForward74_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 74),
    _BusyForward74_Type()
)
busyForward74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward74.setStatus("current")


class _BusyForward75_Type(DisplayString):
    """Custom type busyForward75 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward75_Type.__name__ = "DisplayString"
_BusyForward75_Object = MibScalar
busyForward75 = _BusyForward75_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 75),
    _BusyForward75_Type()
)
busyForward75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward75.setStatus("current")


class _BusyForward76_Type(DisplayString):
    """Custom type busyForward76 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward76_Type.__name__ = "DisplayString"
_BusyForward76_Object = MibScalar
busyForward76 = _BusyForward76_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 76),
    _BusyForward76_Type()
)
busyForward76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward76.setStatus("current")


class _BusyForward77_Type(DisplayString):
    """Custom type busyForward77 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward77_Type.__name__ = "DisplayString"
_BusyForward77_Object = MibScalar
busyForward77 = _BusyForward77_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 77),
    _BusyForward77_Type()
)
busyForward77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward77.setStatus("current")


class _BusyForward78_Type(DisplayString):
    """Custom type busyForward78 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward78_Type.__name__ = "DisplayString"
_BusyForward78_Object = MibScalar
busyForward78 = _BusyForward78_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 78),
    _BusyForward78_Type()
)
busyForward78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward78.setStatus("current")


class _BusyForward79_Type(DisplayString):
    """Custom type busyForward79 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward79_Type.__name__ = "DisplayString"
_BusyForward79_Object = MibScalar
busyForward79 = _BusyForward79_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 79),
    _BusyForward79_Type()
)
busyForward79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward79.setStatus("current")


class _BusyForward80_Type(DisplayString):
    """Custom type busyForward80 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward80_Type.__name__ = "DisplayString"
_BusyForward80_Object = MibScalar
busyForward80 = _BusyForward80_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 80),
    _BusyForward80_Type()
)
busyForward80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward80.setStatus("current")


class _BusyForward81_Type(DisplayString):
    """Custom type busyForward81 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward81_Type.__name__ = "DisplayString"
_BusyForward81_Object = MibScalar
busyForward81 = _BusyForward81_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 81),
    _BusyForward81_Type()
)
busyForward81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward81.setStatus("current")


class _BusyForward82_Type(DisplayString):
    """Custom type busyForward82 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward82_Type.__name__ = "DisplayString"
_BusyForward82_Object = MibScalar
busyForward82 = _BusyForward82_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 82),
    _BusyForward82_Type()
)
busyForward82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward82.setStatus("current")


class _BusyForward83_Type(DisplayString):
    """Custom type busyForward83 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward83_Type.__name__ = "DisplayString"
_BusyForward83_Object = MibScalar
busyForward83 = _BusyForward83_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 83),
    _BusyForward83_Type()
)
busyForward83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward83.setStatus("current")


class _BusyForward84_Type(DisplayString):
    """Custom type busyForward84 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward84_Type.__name__ = "DisplayString"
_BusyForward84_Object = MibScalar
busyForward84 = _BusyForward84_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 84),
    _BusyForward84_Type()
)
busyForward84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward84.setStatus("current")


class _BusyForward85_Type(DisplayString):
    """Custom type busyForward85 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward85_Type.__name__ = "DisplayString"
_BusyForward85_Object = MibScalar
busyForward85 = _BusyForward85_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 85),
    _BusyForward85_Type()
)
busyForward85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward85.setStatus("current")


class _BusyForward86_Type(DisplayString):
    """Custom type busyForward86 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward86_Type.__name__ = "DisplayString"
_BusyForward86_Object = MibScalar
busyForward86 = _BusyForward86_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 86),
    _BusyForward86_Type()
)
busyForward86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward86.setStatus("current")


class _BusyForward87_Type(DisplayString):
    """Custom type busyForward87 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward87_Type.__name__ = "DisplayString"
_BusyForward87_Object = MibScalar
busyForward87 = _BusyForward87_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 87),
    _BusyForward87_Type()
)
busyForward87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward87.setStatus("current")


class _BusyForward88_Type(DisplayString):
    """Custom type busyForward88 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward88_Type.__name__ = "DisplayString"
_BusyForward88_Object = MibScalar
busyForward88 = _BusyForward88_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 88),
    _BusyForward88_Type()
)
busyForward88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward88.setStatus("current")


class _BusyForward89_Type(DisplayString):
    """Custom type busyForward89 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward89_Type.__name__ = "DisplayString"
_BusyForward89_Object = MibScalar
busyForward89 = _BusyForward89_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 89),
    _BusyForward89_Type()
)
busyForward89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward89.setStatus("current")


class _BusyForward90_Type(DisplayString):
    """Custom type busyForward90 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward90_Type.__name__ = "DisplayString"
_BusyForward90_Object = MibScalar
busyForward90 = _BusyForward90_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 90),
    _BusyForward90_Type()
)
busyForward90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward90.setStatus("current")


class _BusyForward91_Type(DisplayString):
    """Custom type busyForward91 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward91_Type.__name__ = "DisplayString"
_BusyForward91_Object = MibScalar
busyForward91 = _BusyForward91_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 91),
    _BusyForward91_Type()
)
busyForward91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward91.setStatus("current")


class _BusyForward92_Type(DisplayString):
    """Custom type busyForward92 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward92_Type.__name__ = "DisplayString"
_BusyForward92_Object = MibScalar
busyForward92 = _BusyForward92_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 92),
    _BusyForward92_Type()
)
busyForward92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward92.setStatus("current")


class _BusyForward93_Type(DisplayString):
    """Custom type busyForward93 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward93_Type.__name__ = "DisplayString"
_BusyForward93_Object = MibScalar
busyForward93 = _BusyForward93_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 93),
    _BusyForward93_Type()
)
busyForward93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward93.setStatus("current")


class _BusyForward94_Type(DisplayString):
    """Custom type busyForward94 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward94_Type.__name__ = "DisplayString"
_BusyForward94_Object = MibScalar
busyForward94 = _BusyForward94_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 94),
    _BusyForward94_Type()
)
busyForward94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward94.setStatus("current")


class _BusyForward95_Type(DisplayString):
    """Custom type busyForward95 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward95_Type.__name__ = "DisplayString"
_BusyForward95_Object = MibScalar
busyForward95 = _BusyForward95_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 95),
    _BusyForward95_Type()
)
busyForward95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward95.setStatus("current")


class _BusyForward96_Type(DisplayString):
    """Custom type busyForward96 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusyForward96_Type.__name__ = "DisplayString"
_BusyForward96_Object = MibScalar
busyForward96 = _BusyForward96_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 5, 96),
    _BusyForward96_Type()
)
busyForward96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyForward96.setStatus("current")
_DelayedForward_ObjectIdentity = ObjectIdentity
delayedForward = _DelayedForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6)
)


class _DelayedForward1_Type(DisplayString):
    """Custom type delayedForward1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward1_Type.__name__ = "DisplayString"
_DelayedForward1_Object = MibScalar
delayedForward1 = _DelayedForward1_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 1),
    _DelayedForward1_Type()
)
delayedForward1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward1.setStatus("current")


class _DelayedForward2_Type(DisplayString):
    """Custom type delayedForward2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward2_Type.__name__ = "DisplayString"
_DelayedForward2_Object = MibScalar
delayedForward2 = _DelayedForward2_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 2),
    _DelayedForward2_Type()
)
delayedForward2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward2.setStatus("current")


class _DelayedForward3_Type(DisplayString):
    """Custom type delayedForward3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward3_Type.__name__ = "DisplayString"
_DelayedForward3_Object = MibScalar
delayedForward3 = _DelayedForward3_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 3),
    _DelayedForward3_Type()
)
delayedForward3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward3.setStatus("current")


class _DelayedForward4_Type(DisplayString):
    """Custom type delayedForward4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward4_Type.__name__ = "DisplayString"
_DelayedForward4_Object = MibScalar
delayedForward4 = _DelayedForward4_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 4),
    _DelayedForward4_Type()
)
delayedForward4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward4.setStatus("current")


class _DelayedForward5_Type(DisplayString):
    """Custom type delayedForward5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward5_Type.__name__ = "DisplayString"
_DelayedForward5_Object = MibScalar
delayedForward5 = _DelayedForward5_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 5),
    _DelayedForward5_Type()
)
delayedForward5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward5.setStatus("current")


class _DelayedForward6_Type(DisplayString):
    """Custom type delayedForward6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward6_Type.__name__ = "DisplayString"
_DelayedForward6_Object = MibScalar
delayedForward6 = _DelayedForward6_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 6),
    _DelayedForward6_Type()
)
delayedForward6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward6.setStatus("current")


class _DelayedForward7_Type(DisplayString):
    """Custom type delayedForward7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward7_Type.__name__ = "DisplayString"
_DelayedForward7_Object = MibScalar
delayedForward7 = _DelayedForward7_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 7),
    _DelayedForward7_Type()
)
delayedForward7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward7.setStatus("current")


class _DelayedForward8_Type(DisplayString):
    """Custom type delayedForward8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward8_Type.__name__ = "DisplayString"
_DelayedForward8_Object = MibScalar
delayedForward8 = _DelayedForward8_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 8),
    _DelayedForward8_Type()
)
delayedForward8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward8.setStatus("current")


class _DelayedForward9_Type(DisplayString):
    """Custom type delayedForward9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward9_Type.__name__ = "DisplayString"
_DelayedForward9_Object = MibScalar
delayedForward9 = _DelayedForward9_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 9),
    _DelayedForward9_Type()
)
delayedForward9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward9.setStatus("current")


class _DelayedForward10_Type(DisplayString):
    """Custom type delayedForward10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward10_Type.__name__ = "DisplayString"
_DelayedForward10_Object = MibScalar
delayedForward10 = _DelayedForward10_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 10),
    _DelayedForward10_Type()
)
delayedForward10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward10.setStatus("current")


class _DelayedForward11_Type(DisplayString):
    """Custom type delayedForward11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward11_Type.__name__ = "DisplayString"
_DelayedForward11_Object = MibScalar
delayedForward11 = _DelayedForward11_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 11),
    _DelayedForward11_Type()
)
delayedForward11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward11.setStatus("current")


class _DelayedForward12_Type(DisplayString):
    """Custom type delayedForward12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward12_Type.__name__ = "DisplayString"
_DelayedForward12_Object = MibScalar
delayedForward12 = _DelayedForward12_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 12),
    _DelayedForward12_Type()
)
delayedForward12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward12.setStatus("current")


class _DelayedForward13_Type(DisplayString):
    """Custom type delayedForward13 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward13_Type.__name__ = "DisplayString"
_DelayedForward13_Object = MibScalar
delayedForward13 = _DelayedForward13_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 13),
    _DelayedForward13_Type()
)
delayedForward13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward13.setStatus("current")


class _DelayedForward14_Type(DisplayString):
    """Custom type delayedForward14 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward14_Type.__name__ = "DisplayString"
_DelayedForward14_Object = MibScalar
delayedForward14 = _DelayedForward14_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 14),
    _DelayedForward14_Type()
)
delayedForward14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward14.setStatus("current")


class _DelayedForward15_Type(DisplayString):
    """Custom type delayedForward15 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward15_Type.__name__ = "DisplayString"
_DelayedForward15_Object = MibScalar
delayedForward15 = _DelayedForward15_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 15),
    _DelayedForward15_Type()
)
delayedForward15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward15.setStatus("current")


class _DelayedForward16_Type(DisplayString):
    """Custom type delayedForward16 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward16_Type.__name__ = "DisplayString"
_DelayedForward16_Object = MibScalar
delayedForward16 = _DelayedForward16_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 16),
    _DelayedForward16_Type()
)
delayedForward16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward16.setStatus("current")


class _DelayedForward17_Type(DisplayString):
    """Custom type delayedForward17 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward17_Type.__name__ = "DisplayString"
_DelayedForward17_Object = MibScalar
delayedForward17 = _DelayedForward17_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 17),
    _DelayedForward17_Type()
)
delayedForward17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward17.setStatus("current")


class _DelayedForward18_Type(DisplayString):
    """Custom type delayedForward18 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward18_Type.__name__ = "DisplayString"
_DelayedForward18_Object = MibScalar
delayedForward18 = _DelayedForward18_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 18),
    _DelayedForward18_Type()
)
delayedForward18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward18.setStatus("current")


class _DelayedForward19_Type(DisplayString):
    """Custom type delayedForward19 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward19_Type.__name__ = "DisplayString"
_DelayedForward19_Object = MibScalar
delayedForward19 = _DelayedForward19_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 19),
    _DelayedForward19_Type()
)
delayedForward19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward19.setStatus("current")


class _DelayedForward20_Type(DisplayString):
    """Custom type delayedForward20 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward20_Type.__name__ = "DisplayString"
_DelayedForward20_Object = MibScalar
delayedForward20 = _DelayedForward20_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 20),
    _DelayedForward20_Type()
)
delayedForward20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward20.setStatus("current")


class _DelayedForward21_Type(DisplayString):
    """Custom type delayedForward21 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward21_Type.__name__ = "DisplayString"
_DelayedForward21_Object = MibScalar
delayedForward21 = _DelayedForward21_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 21),
    _DelayedForward21_Type()
)
delayedForward21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward21.setStatus("current")


class _DelayedForward22_Type(DisplayString):
    """Custom type delayedForward22 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward22_Type.__name__ = "DisplayString"
_DelayedForward22_Object = MibScalar
delayedForward22 = _DelayedForward22_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 22),
    _DelayedForward22_Type()
)
delayedForward22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward22.setStatus("current")


class _DelayedForward23_Type(DisplayString):
    """Custom type delayedForward23 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward23_Type.__name__ = "DisplayString"
_DelayedForward23_Object = MibScalar
delayedForward23 = _DelayedForward23_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 23),
    _DelayedForward23_Type()
)
delayedForward23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward23.setStatus("current")


class _DelayedForward24_Type(DisplayString):
    """Custom type delayedForward24 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward24_Type.__name__ = "DisplayString"
_DelayedForward24_Object = MibScalar
delayedForward24 = _DelayedForward24_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 24),
    _DelayedForward24_Type()
)
delayedForward24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward24.setStatus("current")


class _DelayedForward25_Type(DisplayString):
    """Custom type delayedForward25 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward25_Type.__name__ = "DisplayString"
_DelayedForward25_Object = MibScalar
delayedForward25 = _DelayedForward25_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 25),
    _DelayedForward25_Type()
)
delayedForward25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward25.setStatus("current")


class _DelayedForward26_Type(DisplayString):
    """Custom type delayedForward26 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward26_Type.__name__ = "DisplayString"
_DelayedForward26_Object = MibScalar
delayedForward26 = _DelayedForward26_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 26),
    _DelayedForward26_Type()
)
delayedForward26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward26.setStatus("current")


class _DelayedForward27_Type(DisplayString):
    """Custom type delayedForward27 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward27_Type.__name__ = "DisplayString"
_DelayedForward27_Object = MibScalar
delayedForward27 = _DelayedForward27_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 27),
    _DelayedForward27_Type()
)
delayedForward27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward27.setStatus("current")


class _DelayedForward28_Type(DisplayString):
    """Custom type delayedForward28 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward28_Type.__name__ = "DisplayString"
_DelayedForward28_Object = MibScalar
delayedForward28 = _DelayedForward28_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 28),
    _DelayedForward28_Type()
)
delayedForward28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward28.setStatus("current")


class _DelayedForward29_Type(DisplayString):
    """Custom type delayedForward29 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward29_Type.__name__ = "DisplayString"
_DelayedForward29_Object = MibScalar
delayedForward29 = _DelayedForward29_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 29),
    _DelayedForward29_Type()
)
delayedForward29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward29.setStatus("current")


class _DelayedForward30_Type(DisplayString):
    """Custom type delayedForward30 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward30_Type.__name__ = "DisplayString"
_DelayedForward30_Object = MibScalar
delayedForward30 = _DelayedForward30_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 30),
    _DelayedForward30_Type()
)
delayedForward30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward30.setStatus("current")


class _DelayedForward31_Type(DisplayString):
    """Custom type delayedForward31 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward31_Type.__name__ = "DisplayString"
_DelayedForward31_Object = MibScalar
delayedForward31 = _DelayedForward31_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 31),
    _DelayedForward31_Type()
)
delayedForward31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward31.setStatus("current")


class _DelayedForward32_Type(DisplayString):
    """Custom type delayedForward32 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward32_Type.__name__ = "DisplayString"
_DelayedForward32_Object = MibScalar
delayedForward32 = _DelayedForward32_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 32),
    _DelayedForward32_Type()
)
delayedForward32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward32.setStatus("current")


class _DelayedForward33_Type(DisplayString):
    """Custom type delayedForward33 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward33_Type.__name__ = "DisplayString"
_DelayedForward33_Object = MibScalar
delayedForward33 = _DelayedForward33_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 33),
    _DelayedForward33_Type()
)
delayedForward33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward33.setStatus("current")


class _DelayedForward34_Type(DisplayString):
    """Custom type delayedForward34 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward34_Type.__name__ = "DisplayString"
_DelayedForward34_Object = MibScalar
delayedForward34 = _DelayedForward34_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 34),
    _DelayedForward34_Type()
)
delayedForward34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward34.setStatus("current")


class _DelayedForward35_Type(DisplayString):
    """Custom type delayedForward35 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward35_Type.__name__ = "DisplayString"
_DelayedForward35_Object = MibScalar
delayedForward35 = _DelayedForward35_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 35),
    _DelayedForward35_Type()
)
delayedForward35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward35.setStatus("current")


class _DelayedForward36_Type(DisplayString):
    """Custom type delayedForward36 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward36_Type.__name__ = "DisplayString"
_DelayedForward36_Object = MibScalar
delayedForward36 = _DelayedForward36_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 36),
    _DelayedForward36_Type()
)
delayedForward36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward36.setStatus("current")


class _DelayedForward37_Type(DisplayString):
    """Custom type delayedForward37 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward37_Type.__name__ = "DisplayString"
_DelayedForward37_Object = MibScalar
delayedForward37 = _DelayedForward37_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 37),
    _DelayedForward37_Type()
)
delayedForward37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward37.setStatus("current")


class _DelayedForward38_Type(DisplayString):
    """Custom type delayedForward38 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward38_Type.__name__ = "DisplayString"
_DelayedForward38_Object = MibScalar
delayedForward38 = _DelayedForward38_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 38),
    _DelayedForward38_Type()
)
delayedForward38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward38.setStatus("current")


class _DelayedForward39_Type(DisplayString):
    """Custom type delayedForward39 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward39_Type.__name__ = "DisplayString"
_DelayedForward39_Object = MibScalar
delayedForward39 = _DelayedForward39_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 39),
    _DelayedForward39_Type()
)
delayedForward39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward39.setStatus("current")


class _DelayedForward40_Type(DisplayString):
    """Custom type delayedForward40 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward40_Type.__name__ = "DisplayString"
_DelayedForward40_Object = MibScalar
delayedForward40 = _DelayedForward40_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 40),
    _DelayedForward40_Type()
)
delayedForward40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward40.setStatus("current")


class _DelayedForward41_Type(DisplayString):
    """Custom type delayedForward41 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward41_Type.__name__ = "DisplayString"
_DelayedForward41_Object = MibScalar
delayedForward41 = _DelayedForward41_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 41),
    _DelayedForward41_Type()
)
delayedForward41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward41.setStatus("current")


class _DelayedForward42_Type(DisplayString):
    """Custom type delayedForward42 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward42_Type.__name__ = "DisplayString"
_DelayedForward42_Object = MibScalar
delayedForward42 = _DelayedForward42_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 42),
    _DelayedForward42_Type()
)
delayedForward42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward42.setStatus("current")


class _DelayedForward43_Type(DisplayString):
    """Custom type delayedForward43 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward43_Type.__name__ = "DisplayString"
_DelayedForward43_Object = MibScalar
delayedForward43 = _DelayedForward43_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 43),
    _DelayedForward43_Type()
)
delayedForward43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward43.setStatus("current")


class _DelayedForward44_Type(DisplayString):
    """Custom type delayedForward44 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward44_Type.__name__ = "DisplayString"
_DelayedForward44_Object = MibScalar
delayedForward44 = _DelayedForward44_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 44),
    _DelayedForward44_Type()
)
delayedForward44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward44.setStatus("current")


class _DelayedForward45_Type(DisplayString):
    """Custom type delayedForward45 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward45_Type.__name__ = "DisplayString"
_DelayedForward45_Object = MibScalar
delayedForward45 = _DelayedForward45_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 45),
    _DelayedForward45_Type()
)
delayedForward45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward45.setStatus("current")


class _DelayedForward46_Type(DisplayString):
    """Custom type delayedForward46 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward46_Type.__name__ = "DisplayString"
_DelayedForward46_Object = MibScalar
delayedForward46 = _DelayedForward46_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 46),
    _DelayedForward46_Type()
)
delayedForward46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward46.setStatus("current")


class _DelayedForward47_Type(DisplayString):
    """Custom type delayedForward47 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward47_Type.__name__ = "DisplayString"
_DelayedForward47_Object = MibScalar
delayedForward47 = _DelayedForward47_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 47),
    _DelayedForward47_Type()
)
delayedForward47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward47.setStatus("current")


class _DelayedForward48_Type(DisplayString):
    """Custom type delayedForward48 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward48_Type.__name__ = "DisplayString"
_DelayedForward48_Object = MibScalar
delayedForward48 = _DelayedForward48_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 48),
    _DelayedForward48_Type()
)
delayedForward48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward48.setStatus("current")


class _DelayedForward49_Type(DisplayString):
    """Custom type delayedForward49 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward49_Type.__name__ = "DisplayString"
_DelayedForward49_Object = MibScalar
delayedForward49 = _DelayedForward49_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 49),
    _DelayedForward49_Type()
)
delayedForward49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward49.setStatus("current")


class _DelayedForward50_Type(DisplayString):
    """Custom type delayedForward50 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward50_Type.__name__ = "DisplayString"
_DelayedForward50_Object = MibScalar
delayedForward50 = _DelayedForward50_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 50),
    _DelayedForward50_Type()
)
delayedForward50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward50.setStatus("current")


class _DelayedForward51_Type(DisplayString):
    """Custom type delayedForward51 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward51_Type.__name__ = "DisplayString"
_DelayedForward51_Object = MibScalar
delayedForward51 = _DelayedForward51_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 51),
    _DelayedForward51_Type()
)
delayedForward51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward51.setStatus("current")


class _DelayedForward52_Type(DisplayString):
    """Custom type delayedForward52 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward52_Type.__name__ = "DisplayString"
_DelayedForward52_Object = MibScalar
delayedForward52 = _DelayedForward52_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 52),
    _DelayedForward52_Type()
)
delayedForward52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward52.setStatus("current")


class _DelayedForward53_Type(DisplayString):
    """Custom type delayedForward53 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward53_Type.__name__ = "DisplayString"
_DelayedForward53_Object = MibScalar
delayedForward53 = _DelayedForward53_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 53),
    _DelayedForward53_Type()
)
delayedForward53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward53.setStatus("current")


class _DelayedForward54_Type(DisplayString):
    """Custom type delayedForward54 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward54_Type.__name__ = "DisplayString"
_DelayedForward54_Object = MibScalar
delayedForward54 = _DelayedForward54_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 54),
    _DelayedForward54_Type()
)
delayedForward54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward54.setStatus("current")


class _DelayedForward55_Type(DisplayString):
    """Custom type delayedForward55 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward55_Type.__name__ = "DisplayString"
_DelayedForward55_Object = MibScalar
delayedForward55 = _DelayedForward55_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 55),
    _DelayedForward55_Type()
)
delayedForward55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward55.setStatus("current")


class _DelayedForward56_Type(DisplayString):
    """Custom type delayedForward56 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward56_Type.__name__ = "DisplayString"
_DelayedForward56_Object = MibScalar
delayedForward56 = _DelayedForward56_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 56),
    _DelayedForward56_Type()
)
delayedForward56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward56.setStatus("current")


class _DelayedForward57_Type(DisplayString):
    """Custom type delayedForward57 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward57_Type.__name__ = "DisplayString"
_DelayedForward57_Object = MibScalar
delayedForward57 = _DelayedForward57_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 57),
    _DelayedForward57_Type()
)
delayedForward57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward57.setStatus("current")


class _DelayedForward58_Type(DisplayString):
    """Custom type delayedForward58 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward58_Type.__name__ = "DisplayString"
_DelayedForward58_Object = MibScalar
delayedForward58 = _DelayedForward58_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 58),
    _DelayedForward58_Type()
)
delayedForward58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward58.setStatus("current")


class _DelayedForward59_Type(DisplayString):
    """Custom type delayedForward59 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward59_Type.__name__ = "DisplayString"
_DelayedForward59_Object = MibScalar
delayedForward59 = _DelayedForward59_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 59),
    _DelayedForward59_Type()
)
delayedForward59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward59.setStatus("current")


class _DelayedForward60_Type(DisplayString):
    """Custom type delayedForward60 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward60_Type.__name__ = "DisplayString"
_DelayedForward60_Object = MibScalar
delayedForward60 = _DelayedForward60_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 60),
    _DelayedForward60_Type()
)
delayedForward60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward60.setStatus("current")


class _DelayedForward61_Type(DisplayString):
    """Custom type delayedForward61 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward61_Type.__name__ = "DisplayString"
_DelayedForward61_Object = MibScalar
delayedForward61 = _DelayedForward61_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 61),
    _DelayedForward61_Type()
)
delayedForward61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward61.setStatus("current")


class _DelayedForward62_Type(DisplayString):
    """Custom type delayedForward62 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward62_Type.__name__ = "DisplayString"
_DelayedForward62_Object = MibScalar
delayedForward62 = _DelayedForward62_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 62),
    _DelayedForward62_Type()
)
delayedForward62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward62.setStatus("current")


class _DelayedForward63_Type(DisplayString):
    """Custom type delayedForward63 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward63_Type.__name__ = "DisplayString"
_DelayedForward63_Object = MibScalar
delayedForward63 = _DelayedForward63_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 63),
    _DelayedForward63_Type()
)
delayedForward63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward63.setStatus("current")


class _DelayedForward64_Type(DisplayString):
    """Custom type delayedForward64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward64_Type.__name__ = "DisplayString"
_DelayedForward64_Object = MibScalar
delayedForward64 = _DelayedForward64_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 64),
    _DelayedForward64_Type()
)
delayedForward64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward64.setStatus("current")


class _DelayedForward65_Type(DisplayString):
    """Custom type delayedForward65 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward65_Type.__name__ = "DisplayString"
_DelayedForward65_Object = MibScalar
delayedForward65 = _DelayedForward65_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 65),
    _DelayedForward65_Type()
)
delayedForward65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward65.setStatus("current")


class _DelayedForward66_Type(DisplayString):
    """Custom type delayedForward66 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward66_Type.__name__ = "DisplayString"
_DelayedForward66_Object = MibScalar
delayedForward66 = _DelayedForward66_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 66),
    _DelayedForward66_Type()
)
delayedForward66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward66.setStatus("current")


class _DelayedForward67_Type(DisplayString):
    """Custom type delayedForward67 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward67_Type.__name__ = "DisplayString"
_DelayedForward67_Object = MibScalar
delayedForward67 = _DelayedForward67_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 67),
    _DelayedForward67_Type()
)
delayedForward67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward67.setStatus("current")


class _DelayedForward68_Type(DisplayString):
    """Custom type delayedForward68 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward68_Type.__name__ = "DisplayString"
_DelayedForward68_Object = MibScalar
delayedForward68 = _DelayedForward68_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 68),
    _DelayedForward68_Type()
)
delayedForward68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward68.setStatus("current")


class _DelayedForward69_Type(DisplayString):
    """Custom type delayedForward69 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward69_Type.__name__ = "DisplayString"
_DelayedForward69_Object = MibScalar
delayedForward69 = _DelayedForward69_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 69),
    _DelayedForward69_Type()
)
delayedForward69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward69.setStatus("current")


class _DelayedForward70_Type(DisplayString):
    """Custom type delayedForward70 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward70_Type.__name__ = "DisplayString"
_DelayedForward70_Object = MibScalar
delayedForward70 = _DelayedForward70_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 70),
    _DelayedForward70_Type()
)
delayedForward70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward70.setStatus("current")


class _DelayedForward71_Type(DisplayString):
    """Custom type delayedForward71 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward71_Type.__name__ = "DisplayString"
_DelayedForward71_Object = MibScalar
delayedForward71 = _DelayedForward71_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 71),
    _DelayedForward71_Type()
)
delayedForward71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward71.setStatus("current")


class _DelayedForward72_Type(DisplayString):
    """Custom type delayedForward72 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward72_Type.__name__ = "DisplayString"
_DelayedForward72_Object = MibScalar
delayedForward72 = _DelayedForward72_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 72),
    _DelayedForward72_Type()
)
delayedForward72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward72.setStatus("current")


class _DelayedForward73_Type(DisplayString):
    """Custom type delayedForward73 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward73_Type.__name__ = "DisplayString"
_DelayedForward73_Object = MibScalar
delayedForward73 = _DelayedForward73_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 73),
    _DelayedForward73_Type()
)
delayedForward73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward73.setStatus("current")


class _DelayedForward74_Type(DisplayString):
    """Custom type delayedForward74 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward74_Type.__name__ = "DisplayString"
_DelayedForward74_Object = MibScalar
delayedForward74 = _DelayedForward74_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 74),
    _DelayedForward74_Type()
)
delayedForward74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward74.setStatus("current")


class _DelayedForward75_Type(DisplayString):
    """Custom type delayedForward75 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward75_Type.__name__ = "DisplayString"
_DelayedForward75_Object = MibScalar
delayedForward75 = _DelayedForward75_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 75),
    _DelayedForward75_Type()
)
delayedForward75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward75.setStatus("current")


class _DelayedForward76_Type(DisplayString):
    """Custom type delayedForward76 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward76_Type.__name__ = "DisplayString"
_DelayedForward76_Object = MibScalar
delayedForward76 = _DelayedForward76_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 76),
    _DelayedForward76_Type()
)
delayedForward76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward76.setStatus("current")


class _DelayedForward77_Type(DisplayString):
    """Custom type delayedForward77 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward77_Type.__name__ = "DisplayString"
_DelayedForward77_Object = MibScalar
delayedForward77 = _DelayedForward77_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 77),
    _DelayedForward77_Type()
)
delayedForward77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward77.setStatus("current")


class _DelayedForward78_Type(DisplayString):
    """Custom type delayedForward78 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward78_Type.__name__ = "DisplayString"
_DelayedForward78_Object = MibScalar
delayedForward78 = _DelayedForward78_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 78),
    _DelayedForward78_Type()
)
delayedForward78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward78.setStatus("current")


class _DelayedForward79_Type(DisplayString):
    """Custom type delayedForward79 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward79_Type.__name__ = "DisplayString"
_DelayedForward79_Object = MibScalar
delayedForward79 = _DelayedForward79_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 79),
    _DelayedForward79_Type()
)
delayedForward79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward79.setStatus("current")


class _DelayedForward80_Type(DisplayString):
    """Custom type delayedForward80 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward80_Type.__name__ = "DisplayString"
_DelayedForward80_Object = MibScalar
delayedForward80 = _DelayedForward80_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 80),
    _DelayedForward80_Type()
)
delayedForward80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward80.setStatus("current")


class _DelayedForward81_Type(DisplayString):
    """Custom type delayedForward81 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward81_Type.__name__ = "DisplayString"
_DelayedForward81_Object = MibScalar
delayedForward81 = _DelayedForward81_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 81),
    _DelayedForward81_Type()
)
delayedForward81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward81.setStatus("current")


class _DelayedForward82_Type(DisplayString):
    """Custom type delayedForward82 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward82_Type.__name__ = "DisplayString"
_DelayedForward82_Object = MibScalar
delayedForward82 = _DelayedForward82_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 82),
    _DelayedForward82_Type()
)
delayedForward82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward82.setStatus("current")


class _DelayedForward83_Type(DisplayString):
    """Custom type delayedForward83 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward83_Type.__name__ = "DisplayString"
_DelayedForward83_Object = MibScalar
delayedForward83 = _DelayedForward83_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 83),
    _DelayedForward83_Type()
)
delayedForward83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward83.setStatus("current")


class _DelayedForward84_Type(DisplayString):
    """Custom type delayedForward84 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward84_Type.__name__ = "DisplayString"
_DelayedForward84_Object = MibScalar
delayedForward84 = _DelayedForward84_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 84),
    _DelayedForward84_Type()
)
delayedForward84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward84.setStatus("current")


class _DelayedForward85_Type(DisplayString):
    """Custom type delayedForward85 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward85_Type.__name__ = "DisplayString"
_DelayedForward85_Object = MibScalar
delayedForward85 = _DelayedForward85_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 85),
    _DelayedForward85_Type()
)
delayedForward85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward85.setStatus("current")


class _DelayedForward86_Type(DisplayString):
    """Custom type delayedForward86 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward86_Type.__name__ = "DisplayString"
_DelayedForward86_Object = MibScalar
delayedForward86 = _DelayedForward86_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 86),
    _DelayedForward86_Type()
)
delayedForward86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward86.setStatus("current")


class _DelayedForward87_Type(DisplayString):
    """Custom type delayedForward87 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward87_Type.__name__ = "DisplayString"
_DelayedForward87_Object = MibScalar
delayedForward87 = _DelayedForward87_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 87),
    _DelayedForward87_Type()
)
delayedForward87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward87.setStatus("current")


class _DelayedForward88_Type(DisplayString):
    """Custom type delayedForward88 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward88_Type.__name__ = "DisplayString"
_DelayedForward88_Object = MibScalar
delayedForward88 = _DelayedForward88_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 88),
    _DelayedForward88_Type()
)
delayedForward88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward88.setStatus("current")


class _DelayedForward89_Type(DisplayString):
    """Custom type delayedForward89 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward89_Type.__name__ = "DisplayString"
_DelayedForward89_Object = MibScalar
delayedForward89 = _DelayedForward89_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 89),
    _DelayedForward89_Type()
)
delayedForward89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward89.setStatus("current")


class _DelayedForward90_Type(DisplayString):
    """Custom type delayedForward90 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward90_Type.__name__ = "DisplayString"
_DelayedForward90_Object = MibScalar
delayedForward90 = _DelayedForward90_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 90),
    _DelayedForward90_Type()
)
delayedForward90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward90.setStatus("current")


class _DelayedForward91_Type(DisplayString):
    """Custom type delayedForward91 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward91_Type.__name__ = "DisplayString"
_DelayedForward91_Object = MibScalar
delayedForward91 = _DelayedForward91_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 91),
    _DelayedForward91_Type()
)
delayedForward91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward91.setStatus("current")


class _DelayedForward92_Type(DisplayString):
    """Custom type delayedForward92 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward92_Type.__name__ = "DisplayString"
_DelayedForward92_Object = MibScalar
delayedForward92 = _DelayedForward92_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 92),
    _DelayedForward92_Type()
)
delayedForward92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward92.setStatus("current")


class _DelayedForward93_Type(DisplayString):
    """Custom type delayedForward93 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward93_Type.__name__ = "DisplayString"
_DelayedForward93_Object = MibScalar
delayedForward93 = _DelayedForward93_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 93),
    _DelayedForward93_Type()
)
delayedForward93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward93.setStatus("current")


class _DelayedForward94_Type(DisplayString):
    """Custom type delayedForward94 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward94_Type.__name__ = "DisplayString"
_DelayedForward94_Object = MibScalar
delayedForward94 = _DelayedForward94_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 94),
    _DelayedForward94_Type()
)
delayedForward94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward94.setStatus("current")


class _DelayedForward95_Type(DisplayString):
    """Custom type delayedForward95 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward95_Type.__name__ = "DisplayString"
_DelayedForward95_Object = MibScalar
delayedForward95 = _DelayedForward95_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 95),
    _DelayedForward95_Type()
)
delayedForward95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward95.setStatus("current")


class _DelayedForward96_Type(DisplayString):
    """Custom type delayedForward96 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DelayedForward96_Type.__name__ = "DisplayString"
_DelayedForward96_Object = MibScalar
delayedForward96 = _DelayedForward96_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 2, 6, 96),
    _DelayedForward96_Type()
)
delayedForward96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedForward96.setStatus("current")
_Firmware_ObjectIdentity = ObjectIdentity
firmware = _Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3)
)


class _VersionBoot_Type(DisplayString):
    """Custom type versionBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VersionBoot_Type.__name__ = "DisplayString"
_VersionBoot_Object = MibScalar
versionBoot = _VersionBoot_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 1),
    _VersionBoot_Type()
)
versionBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionBoot.setStatus("current")


class _VersionCore_Type(DisplayString):
    """Custom type versionCore based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VersionCore_Type.__name__ = "DisplayString"
_VersionCore_Object = MibScalar
versionCore = _VersionCore_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 2),
    _VersionCore_Type()
)
versionCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionCore.setStatus("current")


class _VersionBase_Type(DisplayString):
    """Custom type versionBase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VersionBase_Type.__name__ = "DisplayString"
_VersionBase_Object = MibScalar
versionBase = _VersionBase_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 3),
    _VersionBase_Type()
)
versionBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionBase.setStatus("current")


class _VersionProg_Type(DisplayString):
    """Custom type versionProg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VersionProg_Type.__name__ = "DisplayString"
_VersionProg_Object = MibScalar
versionProg = _VersionProg_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 3, 4),
    _VersionProg_Type()
)
versionProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionProg.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 4)
)
_NetworkMode_Type = Integer32
_NetworkMode_Object = MibScalar
networkMode = _NetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 4, 1),
    _NetworkMode_Type()
)
networkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkMode.setStatus("current")
_PppoeLink_Type = Integer32
_PppoeLink_Object = MibScalar
pppoeLink = _PppoeLink_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 4, 2),
    _PppoeLink_Type()
)
pppoeLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeLink.setStatus("current")
_NatTraversal1_Type = Integer32
_NatTraversal1_Object = MibScalar
natTraversal1 = _NatTraversal1_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 4, 3),
    _NatTraversal1_Type()
)
natTraversal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natTraversal1.setStatus("current")
_NatTraversal2_Type = Integer32
_NatTraversal2_Object = MibScalar
natTraversal2 = _NatTraversal2_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 4, 4),
    _NatTraversal2_Type()
)
natTraversal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natTraversal2.setStatus("current")
_NatTraversal3_Type = Integer32
_NatTraversal3_Object = MibScalar
natTraversal3 = _NatTraversal3_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 4, 5),
    _NatTraversal3_Type()
)
natTraversal3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natTraversal3.setStatus("current")
_NatTraversal4_Type = Integer32
_NatTraversal4_Object = MibScalar
natTraversal4 = _NatTraversal4_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 4, 6),
    _NatTraversal4_Type()
)
natTraversal4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natTraversal4.setStatus("current")
_Gxw42xxNotifications_ObjectIdentity = ObjectIdentity
gxw42xxNotifications = _Gxw42xxNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 5)
)
_Gxw4216_ObjectIdentity = ObjectIdentity
gxw4216 = _Gxw4216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 16)
)
_Gxw4224_ObjectIdentity = ObjectIdentity
gxw4224 = _Gxw4224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 24)
)
_Gxw4232_ObjectIdentity = ObjectIdentity
gxw4232 = _Gxw4232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 32)
)
_Gxw4248_ObjectIdentity = ObjectIdentity
gxw4248 = _Gxw4248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 48)
)
_Gxw4296_ObjectIdentity = ObjectIdentity
gxw4296 = _Gxw4296_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 96)
)

# Managed Objects groups


# Notification objects

timedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1, 5, 1)
)
timedTrap.setObjects(
      *(("GS-GXW42XX-MIB", "partNo"),
        ("GS-GXW42XX-MIB", "networkMode"),
        ("GS-GXW42XX-MIB", "pppoeLink"),
        ("GS-GXW42XX-MIB", "natTraversal1"),
        ("GS-GXW42XX-MIB", "natTraversal2"),
        ("GS-GXW42XX-MIB", "natTraversal3"),
        ("GS-GXW42XX-MIB", "natTraversal4"),
        ("GS-GXW42XX-MIB", "versionBoot"),
        ("GS-GXW42XX-MIB", "versionCore"),
        ("GS-GXW42XX-MIB", "versionBase"),
        ("GS-GXW42XX-MIB", "versionProg"),
        ("GS-GXW42XX-MIB", "hookStatus1"),
        ("GS-GXW42XX-MIB", "hookStatus2"),
        ("GS-GXW42XX-MIB", "hookStatus3"),
        ("GS-GXW42XX-MIB", "hookStatus4"),
        ("GS-GXW42XX-MIB", "hookStatus5"),
        ("GS-GXW42XX-MIB", "hookStatus6"),
        ("GS-GXW42XX-MIB", "hookStatus7"),
        ("GS-GXW42XX-MIB", "hookStatus8"),
        ("GS-GXW42XX-MIB", "hookStatus9"),
        ("GS-GXW42XX-MIB", "hookStatus10"),
        ("GS-GXW42XX-MIB", "hookStatus11"),
        ("GS-GXW42XX-MIB", "hookStatus12"),
        ("GS-GXW42XX-MIB", "hookStatus13"),
        ("GS-GXW42XX-MIB", "hookStatus14"),
        ("GS-GXW42XX-MIB", "hookStatus15"),
        ("GS-GXW42XX-MIB", "hookStatus16"),
        ("GS-GXW42XX-MIB", "hookStatus17"),
        ("GS-GXW42XX-MIB", "hookStatus18"),
        ("GS-GXW42XX-MIB", "hookStatus19"),
        ("GS-GXW42XX-MIB", "hookStatus20"),
        ("GS-GXW42XX-MIB", "hookStatus21"),
        ("GS-GXW42XX-MIB", "hookStatus22"),
        ("GS-GXW42XX-MIB", "hookStatus23"),
        ("GS-GXW42XX-MIB", "hookStatus24"),
        ("GS-GXW42XX-MIB", "hookStatus25"),
        ("GS-GXW42XX-MIB", "hookStatus26"),
        ("GS-GXW42XX-MIB", "hookStatus27"),
        ("GS-GXW42XX-MIB", "hookStatus28"),
        ("GS-GXW42XX-MIB", "hookStatus29"),
        ("GS-GXW42XX-MIB", "hookStatus30"),
        ("GS-GXW42XX-MIB", "hookStatus31"),
        ("GS-GXW42XX-MIB", "hookStatus32"),
        ("GS-GXW42XX-MIB", "hookStatus33"),
        ("GS-GXW42XX-MIB", "hookStatus34"),
        ("GS-GXW42XX-MIB", "hookStatus35"),
        ("GS-GXW42XX-MIB", "hookStatus36"),
        ("GS-GXW42XX-MIB", "hookStatus37"),
        ("GS-GXW42XX-MIB", "hookStatus38"),
        ("GS-GXW42XX-MIB", "hookStatus39"),
        ("GS-GXW42XX-MIB", "hookStatus40"),
        ("GS-GXW42XX-MIB", "hookStatus41"),
        ("GS-GXW42XX-MIB", "hookStatus42"),
        ("GS-GXW42XX-MIB", "hookStatus43"),
        ("GS-GXW42XX-MIB", "hookStatus44"),
        ("GS-GXW42XX-MIB", "hookStatus45"),
        ("GS-GXW42XX-MIB", "hookStatus46"),
        ("GS-GXW42XX-MIB", "hookStatus47"),
        ("GS-GXW42XX-MIB", "hookStatus48"),
        ("GS-GXW42XX-MIB", "hookStatus49"),
        ("GS-GXW42XX-MIB", "hookStatus50"),
        ("GS-GXW42XX-MIB", "hookStatus51"),
        ("GS-GXW42XX-MIB", "hookStatus52"),
        ("GS-GXW42XX-MIB", "hookStatus53"),
        ("GS-GXW42XX-MIB", "hookStatus54"),
        ("GS-GXW42XX-MIB", "hookStatus55"),
        ("GS-GXW42XX-MIB", "hookStatus56"),
        ("GS-GXW42XX-MIB", "hookStatus57"),
        ("GS-GXW42XX-MIB", "hookStatus58"),
        ("GS-GXW42XX-MIB", "hookStatus59"),
        ("GS-GXW42XX-MIB", "hookStatus60"),
        ("GS-GXW42XX-MIB", "hookStatus61"),
        ("GS-GXW42XX-MIB", "hookStatus62"),
        ("GS-GXW42XX-MIB", "hookStatus63"),
        ("GS-GXW42XX-MIB", "hookStatus64"),
        ("GS-GXW42XX-MIB", "hookStatus65"),
        ("GS-GXW42XX-MIB", "hookStatus66"),
        ("GS-GXW42XX-MIB", "hookStatus67"),
        ("GS-GXW42XX-MIB", "hookStatus68"),
        ("GS-GXW42XX-MIB", "hookStatus69"),
        ("GS-GXW42XX-MIB", "hookStatus70"),
        ("GS-GXW42XX-MIB", "hookStatus71"),
        ("GS-GXW42XX-MIB", "hookStatus72"),
        ("GS-GXW42XX-MIB", "hookStatus73"),
        ("GS-GXW42XX-MIB", "hookStatus74"),
        ("GS-GXW42XX-MIB", "hookStatus75"),
        ("GS-GXW42XX-MIB", "hookStatus76"),
        ("GS-GXW42XX-MIB", "hookStatus77"),
        ("GS-GXW42XX-MIB", "hookStatus78"),
        ("GS-GXW42XX-MIB", "hookStatus79"),
        ("GS-GXW42XX-MIB", "hookStatus80"),
        ("GS-GXW42XX-MIB", "hookStatus81"),
        ("GS-GXW42XX-MIB", "hookStatus82"),
        ("GS-GXW42XX-MIB", "hookStatus83"),
        ("GS-GXW42XX-MIB", "hookStatus84"),
        ("GS-GXW42XX-MIB", "hookStatus85"),
        ("GS-GXW42XX-MIB", "hookStatus86"),
        ("GS-GXW42XX-MIB", "hookStatus87"),
        ("GS-GXW42XX-MIB", "hookStatus88"),
        ("GS-GXW42XX-MIB", "hookStatus89"),
        ("GS-GXW42XX-MIB", "hookStatus90"),
        ("GS-GXW42XX-MIB", "hookStatus91"),
        ("GS-GXW42XX-MIB", "hookStatus92"),
        ("GS-GXW42XX-MIB", "hookStatus93"),
        ("GS-GXW42XX-MIB", "hookStatus94"),
        ("GS-GXW42XX-MIB", "hookStatus95"),
        ("GS-GXW42XX-MIB", "hookStatus96"),
        ("GS-GXW42XX-MIB", "regStatus1"),
        ("GS-GXW42XX-MIB", "regStatus2"),
        ("GS-GXW42XX-MIB", "regStatus3"),
        ("GS-GXW42XX-MIB", "regStatus4"),
        ("GS-GXW42XX-MIB", "regStatus5"),
        ("GS-GXW42XX-MIB", "regStatus6"),
        ("GS-GXW42XX-MIB", "regStatus7"),
        ("GS-GXW42XX-MIB", "regStatus8"),
        ("GS-GXW42XX-MIB", "regStatus9"),
        ("GS-GXW42XX-MIB", "regStatus10"),
        ("GS-GXW42XX-MIB", "regStatus11"),
        ("GS-GXW42XX-MIB", "regStatus12"),
        ("GS-GXW42XX-MIB", "regStatus13"),
        ("GS-GXW42XX-MIB", "regStatus14"),
        ("GS-GXW42XX-MIB", "regStatus15"),
        ("GS-GXW42XX-MIB", "regStatus16"),
        ("GS-GXW42XX-MIB", "regStatus17"),
        ("GS-GXW42XX-MIB", "regStatus18"),
        ("GS-GXW42XX-MIB", "regStatus19"),
        ("GS-GXW42XX-MIB", "regStatus20"),
        ("GS-GXW42XX-MIB", "regStatus21"),
        ("GS-GXW42XX-MIB", "regStatus22"),
        ("GS-GXW42XX-MIB", "regStatus23"),
        ("GS-GXW42XX-MIB", "regStatus24"),
        ("GS-GXW42XX-MIB", "regStatus25"),
        ("GS-GXW42XX-MIB", "regStatus26"),
        ("GS-GXW42XX-MIB", "regStatus27"),
        ("GS-GXW42XX-MIB", "regStatus28"),
        ("GS-GXW42XX-MIB", "regStatus29"),
        ("GS-GXW42XX-MIB", "regStatus30"),
        ("GS-GXW42XX-MIB", "regStatus31"),
        ("GS-GXW42XX-MIB", "regStatus32"),
        ("GS-GXW42XX-MIB", "regStatus33"),
        ("GS-GXW42XX-MIB", "regStatus34"),
        ("GS-GXW42XX-MIB", "regStatus35"),
        ("GS-GXW42XX-MIB", "regStatus36"),
        ("GS-GXW42XX-MIB", "regStatus37"),
        ("GS-GXW42XX-MIB", "regStatus38"),
        ("GS-GXW42XX-MIB", "regStatus39"),
        ("GS-GXW42XX-MIB", "regStatus40"),
        ("GS-GXW42XX-MIB", "regStatus41"),
        ("GS-GXW42XX-MIB", "regStatus42"),
        ("GS-GXW42XX-MIB", "regStatus43"),
        ("GS-GXW42XX-MIB", "regStatus44"),
        ("GS-GXW42XX-MIB", "regStatus45"),
        ("GS-GXW42XX-MIB", "regStatus46"),
        ("GS-GXW42XX-MIB", "regStatus47"),
        ("GS-GXW42XX-MIB", "regStatus48"),
        ("GS-GXW42XX-MIB", "regStatus49"),
        ("GS-GXW42XX-MIB", "regStatus50"),
        ("GS-GXW42XX-MIB", "regStatus51"),
        ("GS-GXW42XX-MIB", "regStatus52"),
        ("GS-GXW42XX-MIB", "regStatus53"),
        ("GS-GXW42XX-MIB", "regStatus54"),
        ("GS-GXW42XX-MIB", "regStatus55"),
        ("GS-GXW42XX-MIB", "regStatus56"),
        ("GS-GXW42XX-MIB", "regStatus57"),
        ("GS-GXW42XX-MIB", "regStatus58"),
        ("GS-GXW42XX-MIB", "regStatus59"),
        ("GS-GXW42XX-MIB", "regStatus60"),
        ("GS-GXW42XX-MIB", "regStatus61"),
        ("GS-GXW42XX-MIB", "regStatus62"),
        ("GS-GXW42XX-MIB", "regStatus63"),
        ("GS-GXW42XX-MIB", "regStatus64"),
        ("GS-GXW42XX-MIB", "regStatus65"),
        ("GS-GXW42XX-MIB", "regStatus66"),
        ("GS-GXW42XX-MIB", "regStatus67"),
        ("GS-GXW42XX-MIB", "regStatus68"),
        ("GS-GXW42XX-MIB", "regStatus69"),
        ("GS-GXW42XX-MIB", "regStatus70"),
        ("GS-GXW42XX-MIB", "regStatus71"),
        ("GS-GXW42XX-MIB", "regStatus72"),
        ("GS-GXW42XX-MIB", "regStatus73"),
        ("GS-GXW42XX-MIB", "regStatus74"),
        ("GS-GXW42XX-MIB", "regStatus75"),
        ("GS-GXW42XX-MIB", "regStatus76"),
        ("GS-GXW42XX-MIB", "regStatus77"),
        ("GS-GXW42XX-MIB", "regStatus78"),
        ("GS-GXW42XX-MIB", "regStatus79"),
        ("GS-GXW42XX-MIB", "regStatus80"),
        ("GS-GXW42XX-MIB", "regStatus81"),
        ("GS-GXW42XX-MIB", "regStatus82"),
        ("GS-GXW42XX-MIB", "regStatus83"),
        ("GS-GXW42XX-MIB", "regStatus84"),
        ("GS-GXW42XX-MIB", "regStatus85"),
        ("GS-GXW42XX-MIB", "regStatus86"),
        ("GS-GXW42XX-MIB", "regStatus87"),
        ("GS-GXW42XX-MIB", "regStatus88"),
        ("GS-GXW42XX-MIB", "regStatus89"),
        ("GS-GXW42XX-MIB", "regStatus90"),
        ("GS-GXW42XX-MIB", "regStatus91"),
        ("GS-GXW42XX-MIB", "regStatus92"),
        ("GS-GXW42XX-MIB", "regStatus93"),
        ("GS-GXW42XX-MIB", "regStatus94"),
        ("GS-GXW42XX-MIB", "regStatus95"),
        ("GS-GXW42XX-MIB", "regStatus96"),
        ("GS-GXW42XX-MIB", "dnd1"),
        ("GS-GXW42XX-MIB", "dnd2"),
        ("GS-GXW42XX-MIB", "dnd3"),
        ("GS-GXW42XX-MIB", "dnd4"),
        ("GS-GXW42XX-MIB", "dnd5"),
        ("GS-GXW42XX-MIB", "dnd6"),
        ("GS-GXW42XX-MIB", "dnd7"),
        ("GS-GXW42XX-MIB", "dnd8"),
        ("GS-GXW42XX-MIB", "dnd9"),
        ("GS-GXW42XX-MIB", "dnd10"),
        ("GS-GXW42XX-MIB", "dnd11"),
        ("GS-GXW42XX-MIB", "dnd12"),
        ("GS-GXW42XX-MIB", "dnd13"),
        ("GS-GXW42XX-MIB", "dnd14"),
        ("GS-GXW42XX-MIB", "dnd15"),
        ("GS-GXW42XX-MIB", "dnd16"),
        ("GS-GXW42XX-MIB", "dnd17"),
        ("GS-GXW42XX-MIB", "dnd18"),
        ("GS-GXW42XX-MIB", "dnd19"),
        ("GS-GXW42XX-MIB", "dnd20"),
        ("GS-GXW42XX-MIB", "dnd21"),
        ("GS-GXW42XX-MIB", "dnd22"),
        ("GS-GXW42XX-MIB", "dnd23"),
        ("GS-GXW42XX-MIB", "dnd24"),
        ("GS-GXW42XX-MIB", "dnd25"),
        ("GS-GXW42XX-MIB", "dnd26"),
        ("GS-GXW42XX-MIB", "dnd27"),
        ("GS-GXW42XX-MIB", "dnd28"),
        ("GS-GXW42XX-MIB", "dnd29"),
        ("GS-GXW42XX-MIB", "dnd30"),
        ("GS-GXW42XX-MIB", "dnd31"),
        ("GS-GXW42XX-MIB", "dnd32"),
        ("GS-GXW42XX-MIB", "dnd33"),
        ("GS-GXW42XX-MIB", "dnd34"),
        ("GS-GXW42XX-MIB", "dnd35"),
        ("GS-GXW42XX-MIB", "dnd36"),
        ("GS-GXW42XX-MIB", "dnd37"),
        ("GS-GXW42XX-MIB", "dnd38"),
        ("GS-GXW42XX-MIB", "dnd39"),
        ("GS-GXW42XX-MIB", "dnd40"),
        ("GS-GXW42XX-MIB", "dnd41"),
        ("GS-GXW42XX-MIB", "dnd42"),
        ("GS-GXW42XX-MIB", "dnd43"),
        ("GS-GXW42XX-MIB", "dnd44"),
        ("GS-GXW42XX-MIB", "dnd45"),
        ("GS-GXW42XX-MIB", "dnd46"),
        ("GS-GXW42XX-MIB", "dnd47"),
        ("GS-GXW42XX-MIB", "dnd48"),
        ("GS-GXW42XX-MIB", "dnd49"),
        ("GS-GXW42XX-MIB", "dnd50"),
        ("GS-GXW42XX-MIB", "dnd51"),
        ("GS-GXW42XX-MIB", "dnd52"),
        ("GS-GXW42XX-MIB", "dnd53"),
        ("GS-GXW42XX-MIB", "dnd54"),
        ("GS-GXW42XX-MIB", "dnd55"),
        ("GS-GXW42XX-MIB", "dnd56"),
        ("GS-GXW42XX-MIB", "dnd57"),
        ("GS-GXW42XX-MIB", "dnd58"),
        ("GS-GXW42XX-MIB", "dnd59"),
        ("GS-GXW42XX-MIB", "dnd60"),
        ("GS-GXW42XX-MIB", "dnd61"),
        ("GS-GXW42XX-MIB", "dnd62"),
        ("GS-GXW42XX-MIB", "dnd63"),
        ("GS-GXW42XX-MIB", "dnd64"),
        ("GS-GXW42XX-MIB", "dnd65"),
        ("GS-GXW42XX-MIB", "dnd66"),
        ("GS-GXW42XX-MIB", "dnd67"),
        ("GS-GXW42XX-MIB", "dnd68"),
        ("GS-GXW42XX-MIB", "dnd69"),
        ("GS-GXW42XX-MIB", "dnd70"),
        ("GS-GXW42XX-MIB", "dnd71"),
        ("GS-GXW42XX-MIB", "dnd72"),
        ("GS-GXW42XX-MIB", "dnd73"),
        ("GS-GXW42XX-MIB", "dnd74"),
        ("GS-GXW42XX-MIB", "dnd75"),
        ("GS-GXW42XX-MIB", "dnd76"),
        ("GS-GXW42XX-MIB", "dnd77"),
        ("GS-GXW42XX-MIB", "dnd78"),
        ("GS-GXW42XX-MIB", "dnd79"),
        ("GS-GXW42XX-MIB", "dnd80"),
        ("GS-GXW42XX-MIB", "dnd81"),
        ("GS-GXW42XX-MIB", "dnd82"),
        ("GS-GXW42XX-MIB", "dnd83"),
        ("GS-GXW42XX-MIB", "dnd84"),
        ("GS-GXW42XX-MIB", "dnd85"),
        ("GS-GXW42XX-MIB", "dnd86"),
        ("GS-GXW42XX-MIB", "dnd87"),
        ("GS-GXW42XX-MIB", "dnd88"),
        ("GS-GXW42XX-MIB", "dnd89"),
        ("GS-GXW42XX-MIB", "dnd90"),
        ("GS-GXW42XX-MIB", "dnd91"),
        ("GS-GXW42XX-MIB", "dnd92"),
        ("GS-GXW42XX-MIB", "dnd93"),
        ("GS-GXW42XX-MIB", "dnd94"),
        ("GS-GXW42XX-MIB", "dnd95"),
        ("GS-GXW42XX-MIB", "dnd96"),
        ("GS-GXW42XX-MIB", "forward1"),
        ("GS-GXW42XX-MIB", "forward2"),
        ("GS-GXW42XX-MIB", "forward3"),
        ("GS-GXW42XX-MIB", "forward4"),
        ("GS-GXW42XX-MIB", "forward5"),
        ("GS-GXW42XX-MIB", "forward6"),
        ("GS-GXW42XX-MIB", "forward7"),
        ("GS-GXW42XX-MIB", "forward8"),
        ("GS-GXW42XX-MIB", "forward9"),
        ("GS-GXW42XX-MIB", "forward10"),
        ("GS-GXW42XX-MIB", "forward11"),
        ("GS-GXW42XX-MIB", "forward12"),
        ("GS-GXW42XX-MIB", "forward13"),
        ("GS-GXW42XX-MIB", "forward14"),
        ("GS-GXW42XX-MIB", "forward15"),
        ("GS-GXW42XX-MIB", "forward16"),
        ("GS-GXW42XX-MIB", "forward17"),
        ("GS-GXW42XX-MIB", "forward18"),
        ("GS-GXW42XX-MIB", "forward19"),
        ("GS-GXW42XX-MIB", "forward20"),
        ("GS-GXW42XX-MIB", "forward21"),
        ("GS-GXW42XX-MIB", "forward22"),
        ("GS-GXW42XX-MIB", "forward23"),
        ("GS-GXW42XX-MIB", "forward24"),
        ("GS-GXW42XX-MIB", "forward25"),
        ("GS-GXW42XX-MIB", "forward26"),
        ("GS-GXW42XX-MIB", "forward27"),
        ("GS-GXW42XX-MIB", "forward28"),
        ("GS-GXW42XX-MIB", "forward29"),
        ("GS-GXW42XX-MIB", "forward30"),
        ("GS-GXW42XX-MIB", "forward31"),
        ("GS-GXW42XX-MIB", "forward32"),
        ("GS-GXW42XX-MIB", "forward33"),
        ("GS-GXW42XX-MIB", "forward34"),
        ("GS-GXW42XX-MIB", "forward35"),
        ("GS-GXW42XX-MIB", "forward36"),
        ("GS-GXW42XX-MIB", "forward37"),
        ("GS-GXW42XX-MIB", "forward38"),
        ("GS-GXW42XX-MIB", "forward39"),
        ("GS-GXW42XX-MIB", "forward40"),
        ("GS-GXW42XX-MIB", "forward41"),
        ("GS-GXW42XX-MIB", "forward42"),
        ("GS-GXW42XX-MIB", "forward43"),
        ("GS-GXW42XX-MIB", "forward44"),
        ("GS-GXW42XX-MIB", "forward45"),
        ("GS-GXW42XX-MIB", "forward46"),
        ("GS-GXW42XX-MIB", "forward47"),
        ("GS-GXW42XX-MIB", "forward48"),
        ("GS-GXW42XX-MIB", "forward49"),
        ("GS-GXW42XX-MIB", "forward50"),
        ("GS-GXW42XX-MIB", "forward51"),
        ("GS-GXW42XX-MIB", "forward52"),
        ("GS-GXW42XX-MIB", "forward53"),
        ("GS-GXW42XX-MIB", "forward54"),
        ("GS-GXW42XX-MIB", "forward55"),
        ("GS-GXW42XX-MIB", "forward56"),
        ("GS-GXW42XX-MIB", "forward57"),
        ("GS-GXW42XX-MIB", "forward58"),
        ("GS-GXW42XX-MIB", "forward59"),
        ("GS-GXW42XX-MIB", "forward60"),
        ("GS-GXW42XX-MIB", "forward61"),
        ("GS-GXW42XX-MIB", "forward62"),
        ("GS-GXW42XX-MIB", "forward63"),
        ("GS-GXW42XX-MIB", "forward64"),
        ("GS-GXW42XX-MIB", "forward65"),
        ("GS-GXW42XX-MIB", "forward66"),
        ("GS-GXW42XX-MIB", "forward67"),
        ("GS-GXW42XX-MIB", "forward68"),
        ("GS-GXW42XX-MIB", "forward69"),
        ("GS-GXW42XX-MIB", "forward70"),
        ("GS-GXW42XX-MIB", "forward71"),
        ("GS-GXW42XX-MIB", "forward72"),
        ("GS-GXW42XX-MIB", "forward73"),
        ("GS-GXW42XX-MIB", "forward74"),
        ("GS-GXW42XX-MIB", "forward75"),
        ("GS-GXW42XX-MIB", "forward76"),
        ("GS-GXW42XX-MIB", "forward77"),
        ("GS-GXW42XX-MIB", "forward78"),
        ("GS-GXW42XX-MIB", "forward79"),
        ("GS-GXW42XX-MIB", "forward80"),
        ("GS-GXW42XX-MIB", "forward81"),
        ("GS-GXW42XX-MIB", "forward82"),
        ("GS-GXW42XX-MIB", "forward83"),
        ("GS-GXW42XX-MIB", "forward84"),
        ("GS-GXW42XX-MIB", "forward85"),
        ("GS-GXW42XX-MIB", "forward86"),
        ("GS-GXW42XX-MIB", "forward87"),
        ("GS-GXW42XX-MIB", "forward88"),
        ("GS-GXW42XX-MIB", "forward89"),
        ("GS-GXW42XX-MIB", "forward90"),
        ("GS-GXW42XX-MIB", "forward91"),
        ("GS-GXW42XX-MIB", "forward92"),
        ("GS-GXW42XX-MIB", "forward93"),
        ("GS-GXW42XX-MIB", "forward94"),
        ("GS-GXW42XX-MIB", "forward95"),
        ("GS-GXW42XX-MIB", "forward96"),
        ("GS-GXW42XX-MIB", "busyForward1"),
        ("GS-GXW42XX-MIB", "busyForward2"),
        ("GS-GXW42XX-MIB", "busyForward3"),
        ("GS-GXW42XX-MIB", "busyForward4"),
        ("GS-GXW42XX-MIB", "busyForward5"),
        ("GS-GXW42XX-MIB", "busyForward6"),
        ("GS-GXW42XX-MIB", "busyForward7"),
        ("GS-GXW42XX-MIB", "busyForward8"),
        ("GS-GXW42XX-MIB", "busyForward9"),
        ("GS-GXW42XX-MIB", "busyForward10"),
        ("GS-GXW42XX-MIB", "busyForward11"),
        ("GS-GXW42XX-MIB", "busyForward12"),
        ("GS-GXW42XX-MIB", "busyForward13"),
        ("GS-GXW42XX-MIB", "busyForward14"),
        ("GS-GXW42XX-MIB", "busyForward15"),
        ("GS-GXW42XX-MIB", "busyForward16"),
        ("GS-GXW42XX-MIB", "busyForward17"),
        ("GS-GXW42XX-MIB", "busyForward18"),
        ("GS-GXW42XX-MIB", "busyForward19"),
        ("GS-GXW42XX-MIB", "busyForward20"),
        ("GS-GXW42XX-MIB", "busyForward21"),
        ("GS-GXW42XX-MIB", "busyForward22"),
        ("GS-GXW42XX-MIB", "busyForward23"),
        ("GS-GXW42XX-MIB", "busyForward24"),
        ("GS-GXW42XX-MIB", "busyForward25"),
        ("GS-GXW42XX-MIB", "busyForward26"),
        ("GS-GXW42XX-MIB", "busyForward27"),
        ("GS-GXW42XX-MIB", "busyForward28"),
        ("GS-GXW42XX-MIB", "busyForward29"),
        ("GS-GXW42XX-MIB", "busyForward30"),
        ("GS-GXW42XX-MIB", "busyForward31"),
        ("GS-GXW42XX-MIB", "busyForward32"),
        ("GS-GXW42XX-MIB", "busyForward33"),
        ("GS-GXW42XX-MIB", "busyForward34"),
        ("GS-GXW42XX-MIB", "busyForward35"),
        ("GS-GXW42XX-MIB", "busyForward36"),
        ("GS-GXW42XX-MIB", "busyForward37"),
        ("GS-GXW42XX-MIB", "busyForward38"),
        ("GS-GXW42XX-MIB", "busyForward39"),
        ("GS-GXW42XX-MIB", "busyForward40"),
        ("GS-GXW42XX-MIB", "busyForward41"),
        ("GS-GXW42XX-MIB", "busyForward42"),
        ("GS-GXW42XX-MIB", "busyForward43"),
        ("GS-GXW42XX-MIB", "busyForward44"),
        ("GS-GXW42XX-MIB", "busyForward45"),
        ("GS-GXW42XX-MIB", "busyForward46"),
        ("GS-GXW42XX-MIB", "busyForward47"),
        ("GS-GXW42XX-MIB", "busyForward48"),
        ("GS-GXW42XX-MIB", "busyForward49"),
        ("GS-GXW42XX-MIB", "busyForward50"),
        ("GS-GXW42XX-MIB", "busyForward51"),
        ("GS-GXW42XX-MIB", "busyForward52"),
        ("GS-GXW42XX-MIB", "busyForward53"),
        ("GS-GXW42XX-MIB", "busyForward54"),
        ("GS-GXW42XX-MIB", "busyForward55"),
        ("GS-GXW42XX-MIB", "busyForward56"),
        ("GS-GXW42XX-MIB", "busyForward57"),
        ("GS-GXW42XX-MIB", "busyForward58"),
        ("GS-GXW42XX-MIB", "busyForward59"),
        ("GS-GXW42XX-MIB", "busyForward60"),
        ("GS-GXW42XX-MIB", "busyForward61"),
        ("GS-GXW42XX-MIB", "busyForward62"),
        ("GS-GXW42XX-MIB", "busyForward63"),
        ("GS-GXW42XX-MIB", "busyForward64"),
        ("GS-GXW42XX-MIB", "busyForward65"),
        ("GS-GXW42XX-MIB", "busyForward66"),
        ("GS-GXW42XX-MIB", "busyForward67"),
        ("GS-GXW42XX-MIB", "busyForward68"),
        ("GS-GXW42XX-MIB", "busyForward69"),
        ("GS-GXW42XX-MIB", "busyForward70"),
        ("GS-GXW42XX-MIB", "busyForward71"),
        ("GS-GXW42XX-MIB", "busyForward72"),
        ("GS-GXW42XX-MIB", "busyForward73"),
        ("GS-GXW42XX-MIB", "busyForward74"),
        ("GS-GXW42XX-MIB", "busyForward75"),
        ("GS-GXW42XX-MIB", "busyForward76"),
        ("GS-GXW42XX-MIB", "busyForward77"),
        ("GS-GXW42XX-MIB", "busyForward78"),
        ("GS-GXW42XX-MIB", "busyForward79"),
        ("GS-GXW42XX-MIB", "busyForward80"),
        ("GS-GXW42XX-MIB", "busyForward81"),
        ("GS-GXW42XX-MIB", "busyForward82"),
        ("GS-GXW42XX-MIB", "busyForward83"),
        ("GS-GXW42XX-MIB", "busyForward84"),
        ("GS-GXW42XX-MIB", "busyForward85"),
        ("GS-GXW42XX-MIB", "busyForward86"),
        ("GS-GXW42XX-MIB", "busyForward87"),
        ("GS-GXW42XX-MIB", "busyForward88"),
        ("GS-GXW42XX-MIB", "busyForward89"),
        ("GS-GXW42XX-MIB", "busyForward90"),
        ("GS-GXW42XX-MIB", "busyForward91"),
        ("GS-GXW42XX-MIB", "busyForward92"),
        ("GS-GXW42XX-MIB", "busyForward93"),
        ("GS-GXW42XX-MIB", "busyForward94"),
        ("GS-GXW42XX-MIB", "busyForward95"),
        ("GS-GXW42XX-MIB", "busyForward96"),
        ("GS-GXW42XX-MIB", "delayedForward1"),
        ("GS-GXW42XX-MIB", "delayedForward2"),
        ("GS-GXW42XX-MIB", "delayedForward3"),
        ("GS-GXW42XX-MIB", "delayedForward4"),
        ("GS-GXW42XX-MIB", "delayedForward5"),
        ("GS-GXW42XX-MIB", "delayedForward6"),
        ("GS-GXW42XX-MIB", "delayedForward7"),
        ("GS-GXW42XX-MIB", "delayedForward8"),
        ("GS-GXW42XX-MIB", "delayedForward9"),
        ("GS-GXW42XX-MIB", "delayedForward10"),
        ("GS-GXW42XX-MIB", "delayedForward11"),
        ("GS-GXW42XX-MIB", "delayedForward12"),
        ("GS-GXW42XX-MIB", "delayedForward13"),
        ("GS-GXW42XX-MIB", "delayedForward14"),
        ("GS-GXW42XX-MIB", "delayedForward15"),
        ("GS-GXW42XX-MIB", "delayedForward16"),
        ("GS-GXW42XX-MIB", "delayedForward17"),
        ("GS-GXW42XX-MIB", "delayedForward18"),
        ("GS-GXW42XX-MIB", "delayedForward19"),
        ("GS-GXW42XX-MIB", "delayedForward20"),
        ("GS-GXW42XX-MIB", "delayedForward21"),
        ("GS-GXW42XX-MIB", "delayedForward22"),
        ("GS-GXW42XX-MIB", "delayedForward23"),
        ("GS-GXW42XX-MIB", "delayedForward24"),
        ("GS-GXW42XX-MIB", "delayedForward25"),
        ("GS-GXW42XX-MIB", "delayedForward26"),
        ("GS-GXW42XX-MIB", "delayedForward27"),
        ("GS-GXW42XX-MIB", "delayedForward28"),
        ("GS-GXW42XX-MIB", "delayedForward29"),
        ("GS-GXW42XX-MIB", "delayedForward30"),
        ("GS-GXW42XX-MIB", "delayedForward31"),
        ("GS-GXW42XX-MIB", "delayedForward32"),
        ("GS-GXW42XX-MIB", "delayedForward33"),
        ("GS-GXW42XX-MIB", "delayedForward34"),
        ("GS-GXW42XX-MIB", "delayedForward35"),
        ("GS-GXW42XX-MIB", "delayedForward36"),
        ("GS-GXW42XX-MIB", "delayedForward37"),
        ("GS-GXW42XX-MIB", "delayedForward38"),
        ("GS-GXW42XX-MIB", "delayedForward39"),
        ("GS-GXW42XX-MIB", "delayedForward40"),
        ("GS-GXW42XX-MIB", "delayedForward41"),
        ("GS-GXW42XX-MIB", "delayedForward42"),
        ("GS-GXW42XX-MIB", "delayedForward43"),
        ("GS-GXW42XX-MIB", "delayedForward44"),
        ("GS-GXW42XX-MIB", "delayedForward45"),
        ("GS-GXW42XX-MIB", "delayedForward46"),
        ("GS-GXW42XX-MIB", "delayedForward47"),
        ("GS-GXW42XX-MIB", "delayedForward48"),
        ("GS-GXW42XX-MIB", "delayedForward49"),
        ("GS-GXW42XX-MIB", "delayedForward50"),
        ("GS-GXW42XX-MIB", "delayedForward51"),
        ("GS-GXW42XX-MIB", "delayedForward52"),
        ("GS-GXW42XX-MIB", "delayedForward53"),
        ("GS-GXW42XX-MIB", "delayedForward54"),
        ("GS-GXW42XX-MIB", "delayedForward55"),
        ("GS-GXW42XX-MIB", "delayedForward56"),
        ("GS-GXW42XX-MIB", "delayedForward57"),
        ("GS-GXW42XX-MIB", "delayedForward58"),
        ("GS-GXW42XX-MIB", "delayedForward59"),
        ("GS-GXW42XX-MIB", "delayedForward60"),
        ("GS-GXW42XX-MIB", "delayedForward61"),
        ("GS-GXW42XX-MIB", "delayedForward62"),
        ("GS-GXW42XX-MIB", "delayedForward63"),
        ("GS-GXW42XX-MIB", "delayedForward64"),
        ("GS-GXW42XX-MIB", "delayedForward65"),
        ("GS-GXW42XX-MIB", "delayedForward66"),
        ("GS-GXW42XX-MIB", "delayedForward67"),
        ("GS-GXW42XX-MIB", "delayedForward68"),
        ("GS-GXW42XX-MIB", "delayedForward69"),
        ("GS-GXW42XX-MIB", "delayedForward70"),
        ("GS-GXW42XX-MIB", "delayedForward71"),
        ("GS-GXW42XX-MIB", "delayedForward72"),
        ("GS-GXW42XX-MIB", "delayedForward73"),
        ("GS-GXW42XX-MIB", "delayedForward74"),
        ("GS-GXW42XX-MIB", "delayedForward75"),
        ("GS-GXW42XX-MIB", "delayedForward76"),
        ("GS-GXW42XX-MIB", "delayedForward77"),
        ("GS-GXW42XX-MIB", "delayedForward78"),
        ("GS-GXW42XX-MIB", "delayedForward79"),
        ("GS-GXW42XX-MIB", "delayedForward80"),
        ("GS-GXW42XX-MIB", "delayedForward81"),
        ("GS-GXW42XX-MIB", "delayedForward82"),
        ("GS-GXW42XX-MIB", "delayedForward83"),
        ("GS-GXW42XX-MIB", "delayedForward84"),
        ("GS-GXW42XX-MIB", "delayedForward85"),
        ("GS-GXW42XX-MIB", "delayedForward86"),
        ("GS-GXW42XX-MIB", "delayedForward87"),
        ("GS-GXW42XX-MIB", "delayedForward88"),
        ("GS-GXW42XX-MIB", "delayedForward89"),
        ("GS-GXW42XX-MIB", "delayedForward90"),
        ("GS-GXW42XX-MIB", "delayedForward91"),
        ("GS-GXW42XX-MIB", "delayedForward92"),
        ("GS-GXW42XX-MIB", "delayedForward93"),
        ("GS-GXW42XX-MIB", "delayedForward94"),
        ("GS-GXW42XX-MIB", "delayedForward95"),
        ("GS-GXW42XX-MIB", "delayedForward96"))
)
if mibBuilder.loadTexts:
    timedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GS-GXW42XX-MIB",
    **{"grandstream": grandstream,
       "productFamily": productFamily,
       "gxw42xx": gxw42xx,
       "partNo": partNo,
       "ports": ports,
       "hookStatus": hookStatus,
       "hookStatus1": hookStatus1,
       "hookStatus2": hookStatus2,
       "hookStatus3": hookStatus3,
       "hookStatus4": hookStatus4,
       "hookStatus5": hookStatus5,
       "hookStatus6": hookStatus6,
       "hookStatus7": hookStatus7,
       "hookStatus8": hookStatus8,
       "hookStatus9": hookStatus9,
       "hookStatus10": hookStatus10,
       "hookStatus11": hookStatus11,
       "hookStatus12": hookStatus12,
       "hookStatus13": hookStatus13,
       "hookStatus14": hookStatus14,
       "hookStatus15": hookStatus15,
       "hookStatus16": hookStatus16,
       "hookStatus17": hookStatus17,
       "hookStatus18": hookStatus18,
       "hookStatus19": hookStatus19,
       "hookStatus20": hookStatus20,
       "hookStatus21": hookStatus21,
       "hookStatus22": hookStatus22,
       "hookStatus23": hookStatus23,
       "hookStatus24": hookStatus24,
       "hookStatus25": hookStatus25,
       "hookStatus26": hookStatus26,
       "hookStatus27": hookStatus27,
       "hookStatus28": hookStatus28,
       "hookStatus29": hookStatus29,
       "hookStatus30": hookStatus30,
       "hookStatus31": hookStatus31,
       "hookStatus32": hookStatus32,
       "hookStatus33": hookStatus33,
       "hookStatus34": hookStatus34,
       "hookStatus35": hookStatus35,
       "hookStatus36": hookStatus36,
       "hookStatus37": hookStatus37,
       "hookStatus38": hookStatus38,
       "hookStatus39": hookStatus39,
       "hookStatus40": hookStatus40,
       "hookStatus41": hookStatus41,
       "hookStatus42": hookStatus42,
       "hookStatus43": hookStatus43,
       "hookStatus44": hookStatus44,
       "hookStatus45": hookStatus45,
       "hookStatus46": hookStatus46,
       "hookStatus47": hookStatus47,
       "hookStatus48": hookStatus48,
       "hookStatus49": hookStatus49,
       "hookStatus50": hookStatus50,
       "hookStatus51": hookStatus51,
       "hookStatus52": hookStatus52,
       "hookStatus53": hookStatus53,
       "hookStatus54": hookStatus54,
       "hookStatus55": hookStatus55,
       "hookStatus56": hookStatus56,
       "hookStatus57": hookStatus57,
       "hookStatus58": hookStatus58,
       "hookStatus59": hookStatus59,
       "hookStatus60": hookStatus60,
       "hookStatus61": hookStatus61,
       "hookStatus62": hookStatus62,
       "hookStatus63": hookStatus63,
       "hookStatus64": hookStatus64,
       "hookStatus65": hookStatus65,
       "hookStatus66": hookStatus66,
       "hookStatus67": hookStatus67,
       "hookStatus68": hookStatus68,
       "hookStatus69": hookStatus69,
       "hookStatus70": hookStatus70,
       "hookStatus71": hookStatus71,
       "hookStatus72": hookStatus72,
       "hookStatus73": hookStatus73,
       "hookStatus74": hookStatus74,
       "hookStatus75": hookStatus75,
       "hookStatus76": hookStatus76,
       "hookStatus77": hookStatus77,
       "hookStatus78": hookStatus78,
       "hookStatus79": hookStatus79,
       "hookStatus80": hookStatus80,
       "hookStatus81": hookStatus81,
       "hookStatus82": hookStatus82,
       "hookStatus83": hookStatus83,
       "hookStatus84": hookStatus84,
       "hookStatus85": hookStatus85,
       "hookStatus86": hookStatus86,
       "hookStatus87": hookStatus87,
       "hookStatus88": hookStatus88,
       "hookStatus89": hookStatus89,
       "hookStatus90": hookStatus90,
       "hookStatus91": hookStatus91,
       "hookStatus92": hookStatus92,
       "hookStatus93": hookStatus93,
       "hookStatus94": hookStatus94,
       "hookStatus95": hookStatus95,
       "hookStatus96": hookStatus96,
       "regStatus": regStatus,
       "regStatus1": regStatus1,
       "regStatus2": regStatus2,
       "regStatus3": regStatus3,
       "regStatus4": regStatus4,
       "regStatus5": regStatus5,
       "regStatus6": regStatus6,
       "regStatus7": regStatus7,
       "regStatus8": regStatus8,
       "regStatus9": regStatus9,
       "regStatus10": regStatus10,
       "regStatus11": regStatus11,
       "regStatus12": regStatus12,
       "regStatus13": regStatus13,
       "regStatus14": regStatus14,
       "regStatus15": regStatus15,
       "regStatus16": regStatus16,
       "regStatus17": regStatus17,
       "regStatus18": regStatus18,
       "regStatus19": regStatus19,
       "regStatus20": regStatus20,
       "regStatus21": regStatus21,
       "regStatus22": regStatus22,
       "regStatus23": regStatus23,
       "regStatus24": regStatus24,
       "regStatus25": regStatus25,
       "regStatus26": regStatus26,
       "regStatus27": regStatus27,
       "regStatus28": regStatus28,
       "regStatus29": regStatus29,
       "regStatus30": regStatus30,
       "regStatus31": regStatus31,
       "regStatus32": regStatus32,
       "regStatus33": regStatus33,
       "regStatus34": regStatus34,
       "regStatus35": regStatus35,
       "regStatus36": regStatus36,
       "regStatus37": regStatus37,
       "regStatus38": regStatus38,
       "regStatus39": regStatus39,
       "regStatus40": regStatus40,
       "regStatus41": regStatus41,
       "regStatus42": regStatus42,
       "regStatus43": regStatus43,
       "regStatus44": regStatus44,
       "regStatus45": regStatus45,
       "regStatus46": regStatus46,
       "regStatus47": regStatus47,
       "regStatus48": regStatus48,
       "regStatus49": regStatus49,
       "regStatus50": regStatus50,
       "regStatus51": regStatus51,
       "regStatus52": regStatus52,
       "regStatus53": regStatus53,
       "regStatus54": regStatus54,
       "regStatus55": regStatus55,
       "regStatus56": regStatus56,
       "regStatus57": regStatus57,
       "regStatus58": regStatus58,
       "regStatus59": regStatus59,
       "regStatus60": regStatus60,
       "regStatus61": regStatus61,
       "regStatus62": regStatus62,
       "regStatus63": regStatus63,
       "regStatus64": regStatus64,
       "regStatus65": regStatus65,
       "regStatus66": regStatus66,
       "regStatus67": regStatus67,
       "regStatus68": regStatus68,
       "regStatus69": regStatus69,
       "regStatus70": regStatus70,
       "regStatus71": regStatus71,
       "regStatus72": regStatus72,
       "regStatus73": regStatus73,
       "regStatus74": regStatus74,
       "regStatus75": regStatus75,
       "regStatus76": regStatus76,
       "regStatus77": regStatus77,
       "regStatus78": regStatus78,
       "regStatus79": regStatus79,
       "regStatus80": regStatus80,
       "regStatus81": regStatus81,
       "regStatus82": regStatus82,
       "regStatus83": regStatus83,
       "regStatus84": regStatus84,
       "regStatus85": regStatus85,
       "regStatus86": regStatus86,
       "regStatus87": regStatus87,
       "regStatus88": regStatus88,
       "regStatus89": regStatus89,
       "regStatus90": regStatus90,
       "regStatus91": regStatus91,
       "regStatus92": regStatus92,
       "regStatus93": regStatus93,
       "regStatus94": regStatus94,
       "regStatus95": regStatus95,
       "regStatus96": regStatus96,
       "dnd": dnd,
       "dnd1": dnd1,
       "dnd2": dnd2,
       "dnd3": dnd3,
       "dnd4": dnd4,
       "dnd5": dnd5,
       "dnd6": dnd6,
       "dnd7": dnd7,
       "dnd8": dnd8,
       "dnd9": dnd9,
       "dnd10": dnd10,
       "dnd11": dnd11,
       "dnd12": dnd12,
       "dnd13": dnd13,
       "dnd14": dnd14,
       "dnd15": dnd15,
       "dnd16": dnd16,
       "dnd17": dnd17,
       "dnd18": dnd18,
       "dnd19": dnd19,
       "dnd20": dnd20,
       "dnd21": dnd21,
       "dnd22": dnd22,
       "dnd23": dnd23,
       "dnd24": dnd24,
       "dnd25": dnd25,
       "dnd26": dnd26,
       "dnd27": dnd27,
       "dnd28": dnd28,
       "dnd29": dnd29,
       "dnd30": dnd30,
       "dnd31": dnd31,
       "dnd32": dnd32,
       "dnd33": dnd33,
       "dnd34": dnd34,
       "dnd35": dnd35,
       "dnd36": dnd36,
       "dnd37": dnd37,
       "dnd38": dnd38,
       "dnd39": dnd39,
       "dnd40": dnd40,
       "dnd41": dnd41,
       "dnd42": dnd42,
       "dnd43": dnd43,
       "dnd44": dnd44,
       "dnd45": dnd45,
       "dnd46": dnd46,
       "dnd47": dnd47,
       "dnd48": dnd48,
       "dnd49": dnd49,
       "dnd50": dnd50,
       "dnd51": dnd51,
       "dnd52": dnd52,
       "dnd53": dnd53,
       "dnd54": dnd54,
       "dnd55": dnd55,
       "dnd56": dnd56,
       "dnd57": dnd57,
       "dnd58": dnd58,
       "dnd59": dnd59,
       "dnd60": dnd60,
       "dnd61": dnd61,
       "dnd62": dnd62,
       "dnd63": dnd63,
       "dnd64": dnd64,
       "dnd65": dnd65,
       "dnd66": dnd66,
       "dnd67": dnd67,
       "dnd68": dnd68,
       "dnd69": dnd69,
       "dnd70": dnd70,
       "dnd71": dnd71,
       "dnd72": dnd72,
       "dnd73": dnd73,
       "dnd74": dnd74,
       "dnd75": dnd75,
       "dnd76": dnd76,
       "dnd77": dnd77,
       "dnd78": dnd78,
       "dnd79": dnd79,
       "dnd80": dnd80,
       "dnd81": dnd81,
       "dnd82": dnd82,
       "dnd83": dnd83,
       "dnd84": dnd84,
       "dnd85": dnd85,
       "dnd86": dnd86,
       "dnd87": dnd87,
       "dnd88": dnd88,
       "dnd89": dnd89,
       "dnd90": dnd90,
       "dnd91": dnd91,
       "dnd92": dnd92,
       "dnd93": dnd93,
       "dnd94": dnd94,
       "dnd95": dnd95,
       "dnd96": dnd96,
       "forward": forward,
       "forward1": forward1,
       "forward2": forward2,
       "forward3": forward3,
       "forward4": forward4,
       "forward5": forward5,
       "forward6": forward6,
       "forward7": forward7,
       "forward8": forward8,
       "forward9": forward9,
       "forward10": forward10,
       "forward11": forward11,
       "forward12": forward12,
       "forward13": forward13,
       "forward14": forward14,
       "forward15": forward15,
       "forward16": forward16,
       "forward17": forward17,
       "forward18": forward18,
       "forward19": forward19,
       "forward20": forward20,
       "forward21": forward21,
       "forward22": forward22,
       "forward23": forward23,
       "forward24": forward24,
       "forward25": forward25,
       "forward26": forward26,
       "forward27": forward27,
       "forward28": forward28,
       "forward29": forward29,
       "forward30": forward30,
       "forward31": forward31,
       "forward32": forward32,
       "forward33": forward33,
       "forward34": forward34,
       "forward35": forward35,
       "forward36": forward36,
       "forward37": forward37,
       "forward38": forward38,
       "forward39": forward39,
       "forward40": forward40,
       "forward41": forward41,
       "forward42": forward42,
       "forward43": forward43,
       "forward44": forward44,
       "forward45": forward45,
       "forward46": forward46,
       "forward47": forward47,
       "forward48": forward48,
       "forward49": forward49,
       "forward50": forward50,
       "forward51": forward51,
       "forward52": forward52,
       "forward53": forward53,
       "forward54": forward54,
       "forward55": forward55,
       "forward56": forward56,
       "forward57": forward57,
       "forward58": forward58,
       "forward59": forward59,
       "forward60": forward60,
       "forward61": forward61,
       "forward62": forward62,
       "forward63": forward63,
       "forward64": forward64,
       "forward65": forward65,
       "forward66": forward66,
       "forward67": forward67,
       "forward68": forward68,
       "forward69": forward69,
       "forward70": forward70,
       "forward71": forward71,
       "forward72": forward72,
       "forward73": forward73,
       "forward74": forward74,
       "forward75": forward75,
       "forward76": forward76,
       "forward77": forward77,
       "forward78": forward78,
       "forward79": forward79,
       "forward80": forward80,
       "forward81": forward81,
       "forward82": forward82,
       "forward83": forward83,
       "forward84": forward84,
       "forward85": forward85,
       "forward86": forward86,
       "forward87": forward87,
       "forward88": forward88,
       "forward89": forward89,
       "forward90": forward90,
       "forward91": forward91,
       "forward92": forward92,
       "forward93": forward93,
       "forward94": forward94,
       "forward95": forward95,
       "forward96": forward96,
       "busyForward": busyForward,
       "busyForward1": busyForward1,
       "busyForward2": busyForward2,
       "busyForward3": busyForward3,
       "busyForward4": busyForward4,
       "busyForward5": busyForward5,
       "busyForward6": busyForward6,
       "busyForward7": busyForward7,
       "busyForward8": busyForward8,
       "busyForward9": busyForward9,
       "busyForward10": busyForward10,
       "busyForward11": busyForward11,
       "busyForward12": busyForward12,
       "busyForward13": busyForward13,
       "busyForward14": busyForward14,
       "busyForward15": busyForward15,
       "busyForward16": busyForward16,
       "busyForward17": busyForward17,
       "busyForward18": busyForward18,
       "busyForward19": busyForward19,
       "busyForward20": busyForward20,
       "busyForward21": busyForward21,
       "busyForward22": busyForward22,
       "busyForward23": busyForward23,
       "busyForward24": busyForward24,
       "busyForward25": busyForward25,
       "busyForward26": busyForward26,
       "busyForward27": busyForward27,
       "busyForward28": busyForward28,
       "busyForward29": busyForward29,
       "busyForward30": busyForward30,
       "busyForward31": busyForward31,
       "busyForward32": busyForward32,
       "busyForward33": busyForward33,
       "busyForward34": busyForward34,
       "busyForward35": busyForward35,
       "busyForward36": busyForward36,
       "busyForward37": busyForward37,
       "busyForward38": busyForward38,
       "busyForward39": busyForward39,
       "busyForward40": busyForward40,
       "busyForward41": busyForward41,
       "busyForward42": busyForward42,
       "busyForward43": busyForward43,
       "busyForward44": busyForward44,
       "busyForward45": busyForward45,
       "busyForward46": busyForward46,
       "busyForward47": busyForward47,
       "busyForward48": busyForward48,
       "busyForward49": busyForward49,
       "busyForward50": busyForward50,
       "busyForward51": busyForward51,
       "busyForward52": busyForward52,
       "busyForward53": busyForward53,
       "busyForward54": busyForward54,
       "busyForward55": busyForward55,
       "busyForward56": busyForward56,
       "busyForward57": busyForward57,
       "busyForward58": busyForward58,
       "busyForward59": busyForward59,
       "busyForward60": busyForward60,
       "busyForward61": busyForward61,
       "busyForward62": busyForward62,
       "busyForward63": busyForward63,
       "busyForward64": busyForward64,
       "busyForward65": busyForward65,
       "busyForward66": busyForward66,
       "busyForward67": busyForward67,
       "busyForward68": busyForward68,
       "busyForward69": busyForward69,
       "busyForward70": busyForward70,
       "busyForward71": busyForward71,
       "busyForward72": busyForward72,
       "busyForward73": busyForward73,
       "busyForward74": busyForward74,
       "busyForward75": busyForward75,
       "busyForward76": busyForward76,
       "busyForward77": busyForward77,
       "busyForward78": busyForward78,
       "busyForward79": busyForward79,
       "busyForward80": busyForward80,
       "busyForward81": busyForward81,
       "busyForward82": busyForward82,
       "busyForward83": busyForward83,
       "busyForward84": busyForward84,
       "busyForward85": busyForward85,
       "busyForward86": busyForward86,
       "busyForward87": busyForward87,
       "busyForward88": busyForward88,
       "busyForward89": busyForward89,
       "busyForward90": busyForward90,
       "busyForward91": busyForward91,
       "busyForward92": busyForward92,
       "busyForward93": busyForward93,
       "busyForward94": busyForward94,
       "busyForward95": busyForward95,
       "busyForward96": busyForward96,
       "delayedForward": delayedForward,
       "delayedForward1": delayedForward1,
       "delayedForward2": delayedForward2,
       "delayedForward3": delayedForward3,
       "delayedForward4": delayedForward4,
       "delayedForward5": delayedForward5,
       "delayedForward6": delayedForward6,
       "delayedForward7": delayedForward7,
       "delayedForward8": delayedForward8,
       "delayedForward9": delayedForward9,
       "delayedForward10": delayedForward10,
       "delayedForward11": delayedForward11,
       "delayedForward12": delayedForward12,
       "delayedForward13": delayedForward13,
       "delayedForward14": delayedForward14,
       "delayedForward15": delayedForward15,
       "delayedForward16": delayedForward16,
       "delayedForward17": delayedForward17,
       "delayedForward18": delayedForward18,
       "delayedForward19": delayedForward19,
       "delayedForward20": delayedForward20,
       "delayedForward21": delayedForward21,
       "delayedForward22": delayedForward22,
       "delayedForward23": delayedForward23,
       "delayedForward24": delayedForward24,
       "delayedForward25": delayedForward25,
       "delayedForward26": delayedForward26,
       "delayedForward27": delayedForward27,
       "delayedForward28": delayedForward28,
       "delayedForward29": delayedForward29,
       "delayedForward30": delayedForward30,
       "delayedForward31": delayedForward31,
       "delayedForward32": delayedForward32,
       "delayedForward33": delayedForward33,
       "delayedForward34": delayedForward34,
       "delayedForward35": delayedForward35,
       "delayedForward36": delayedForward36,
       "delayedForward37": delayedForward37,
       "delayedForward38": delayedForward38,
       "delayedForward39": delayedForward39,
       "delayedForward40": delayedForward40,
       "delayedForward41": delayedForward41,
       "delayedForward42": delayedForward42,
       "delayedForward43": delayedForward43,
       "delayedForward44": delayedForward44,
       "delayedForward45": delayedForward45,
       "delayedForward46": delayedForward46,
       "delayedForward47": delayedForward47,
       "delayedForward48": delayedForward48,
       "delayedForward49": delayedForward49,
       "delayedForward50": delayedForward50,
       "delayedForward51": delayedForward51,
       "delayedForward52": delayedForward52,
       "delayedForward53": delayedForward53,
       "delayedForward54": delayedForward54,
       "delayedForward55": delayedForward55,
       "delayedForward56": delayedForward56,
       "delayedForward57": delayedForward57,
       "delayedForward58": delayedForward58,
       "delayedForward59": delayedForward59,
       "delayedForward60": delayedForward60,
       "delayedForward61": delayedForward61,
       "delayedForward62": delayedForward62,
       "delayedForward63": delayedForward63,
       "delayedForward64": delayedForward64,
       "delayedForward65": delayedForward65,
       "delayedForward66": delayedForward66,
       "delayedForward67": delayedForward67,
       "delayedForward68": delayedForward68,
       "delayedForward69": delayedForward69,
       "delayedForward70": delayedForward70,
       "delayedForward71": delayedForward71,
       "delayedForward72": delayedForward72,
       "delayedForward73": delayedForward73,
       "delayedForward74": delayedForward74,
       "delayedForward75": delayedForward75,
       "delayedForward76": delayedForward76,
       "delayedForward77": delayedForward77,
       "delayedForward78": delayedForward78,
       "delayedForward79": delayedForward79,
       "delayedForward80": delayedForward80,
       "delayedForward81": delayedForward81,
       "delayedForward82": delayedForward82,
       "delayedForward83": delayedForward83,
       "delayedForward84": delayedForward84,
       "delayedForward85": delayedForward85,
       "delayedForward86": delayedForward86,
       "delayedForward87": delayedForward87,
       "delayedForward88": delayedForward88,
       "delayedForward89": delayedForward89,
       "delayedForward90": delayedForward90,
       "delayedForward91": delayedForward91,
       "delayedForward92": delayedForward92,
       "delayedForward93": delayedForward93,
       "delayedForward94": delayedForward94,
       "delayedForward95": delayedForward95,
       "delayedForward96": delayedForward96,
       "firmware": firmware,
       "versionBoot": versionBoot,
       "versionCore": versionCore,
       "versionBase": versionBase,
       "versionProg": versionProg,
       "network": network,
       "networkMode": networkMode,
       "pppoeLink": pppoeLink,
       "natTraversal1": natTraversal1,
       "natTraversal2": natTraversal2,
       "natTraversal3": natTraversal3,
       "natTraversal4": natTraversal4,
       "gxw42xxNotifications": gxw42xxNotifications,
       "timedTrap": timedTrap,
       "gxw4216": gxw4216,
       "gxw4224": gxw4224,
       "gxw4232": gxw4232,
       "gxw4248": gxw4248,
       "gxw4296": gxw4296}
)
