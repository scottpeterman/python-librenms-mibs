# SNMP MIB module (ARUBAWIRED-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-POE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:20 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

(pethMainPseEntry,
 pethPsePortEntry) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseEntry",
    "pethPsePortEntry")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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


# MODULE-IDENTITY

arubaWiredPoeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    arubaWiredPoeMIB.setRevisions(
        ("2024-11-27 00:00",
         "2019-06-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredPoePethPsePort_ObjectIdentity = ObjectIdentity
arubaWiredPoePethPsePort = _ArubaWiredPoePethPsePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1)
)
_ArubaWiredPoePethPsePortTable_Object = MibTable
arubaWiredPoePethPsePortTable = _ArubaWiredPoePethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortTable.setStatus("current")
_ArubaWiredPoePethPsePortEntry_Object = MibTableRow
arubaWiredPoePethPsePortEntry = _ArubaWiredPoePethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortEntry.setStatus("current")


class _ArubaWiredPoePethPsePortPowerAllocateBy_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortPowerAllocateBy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("usage", 1),
          ("class", 2))
    )


_ArubaWiredPoePethPsePortPowerAllocateBy_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortPowerAllocateBy_Object = MibTableColumn
arubaWiredPoePethPsePortPowerAllocateBy = _ArubaWiredPoePethPsePortPowerAllocateBy_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 1),
    _ArubaWiredPoePethPsePortPowerAllocateBy_Type()
)
arubaWiredPoePethPsePortPowerAllocateBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPowerAllocateBy.setStatus("current")


class _ArubaWiredPoePethPsePortPreStdDetect_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortPreStdDetect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ArubaWiredPoePethPsePortPreStdDetect_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortPreStdDetect_Object = MibTableColumn
arubaWiredPoePethPsePortPreStdDetect = _ArubaWiredPoePethPsePortPreStdDetect_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 2),
    _ArubaWiredPoePethPsePortPreStdDetect_Type()
)
arubaWiredPoePethPsePortPreStdDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPreStdDetect.setStatus("current")


class _ArubaWiredPoePethPsePortRpd_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortRpd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ArubaWiredPoePethPsePortRpd_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortRpd_Object = MibTableColumn
arubaWiredPoePethPsePortRpd = _ArubaWiredPoePethPsePortRpd_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 3),
    _ArubaWiredPoePethPsePortRpd_Type()
)
arubaWiredPoePethPsePortRpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortRpd.setStatus("current")


class _ArubaWiredPoePethPsePortCurrent_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortCurrent based on Integer32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortCurrent_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortCurrent_Object = MibTableColumn
arubaWiredPoePethPsePortCurrent = _ArubaWiredPoePethPsePortCurrent_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 4),
    _ArubaWiredPoePethPsePortCurrent_Type()
)
arubaWiredPoePethPsePortCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortCurrent.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortCurrent.setUnits("milliamperes")


class _ArubaWiredPoePethPsePortVoltage_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortVoltage based on Integer32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortVoltage_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortVoltage_Object = MibTableColumn
arubaWiredPoePethPsePortVoltage = _ArubaWiredPoePethPsePortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 5),
    _ArubaWiredPoePethPsePortVoltage_Type()
)
arubaWiredPoePethPsePortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortVoltage.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortVoltage.setUnits("deciVolts")


class _ArubaWiredPoePethPsePortReservedPower_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortReservedPower based on Integer32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortReservedPower_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortReservedPower_Object = MibTableColumn
arubaWiredPoePethPsePortReservedPower = _ArubaWiredPoePethPsePortReservedPower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 6),
    _ArubaWiredPoePethPsePortReservedPower_Type()
)
arubaWiredPoePethPsePortReservedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortReservedPower.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortReservedPower.setUnits("milliwatts")


class _ArubaWiredPoePethPsePortPowerDrawn_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortPowerDrawn based on Integer32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortPowerDrawn_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortPowerDrawn_Object = MibTableColumn
arubaWiredPoePethPsePortPowerDrawn = _ArubaWiredPoePethPsePortPowerDrawn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 7),
    _ArubaWiredPoePethPsePortPowerDrawn_Type()
)
arubaWiredPoePethPsePortPowerDrawn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPowerDrawn.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPowerDrawn.setUnits("milliwatts")


class _ArubaWiredPoePethPsePortAveragePower_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortAveragePower based on Integer32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortAveragePower_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortAveragePower_Object = MibTableColumn
arubaWiredPoePethPsePortAveragePower = _ArubaWiredPoePethPsePortAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 8),
    _ArubaWiredPoePethPsePortAveragePower_Type()
)
arubaWiredPoePethPsePortAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortAveragePower.setUnits("milliwatts")


class _ArubaWiredPoePethPsePortPeakPower_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortPeakPower based on Integer32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortPeakPower_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortPeakPower_Object = MibTableColumn
arubaWiredPoePethPsePortPeakPower = _ArubaWiredPoePethPsePortPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 9),
    _ArubaWiredPoePethPsePortPeakPower_Type()
)
arubaWiredPoePethPsePortPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPeakPower.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPeakPower.setUnits("milliwatts")


class _ArubaWiredPoePethPsePortOperStatus_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("off", 2),
          ("on", 3))
    )


_ArubaWiredPoePethPsePortOperStatus_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortOperStatus_Object = MibTableColumn
arubaWiredPoePethPsePortOperStatus = _ArubaWiredPoePethPsePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 10),
    _ArubaWiredPoePethPsePortOperStatus_Type()
)
arubaWiredPoePethPsePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortOperStatus.setStatus("current")


class _ArubaWiredPoePethPsePortPdSignature_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortPdSignature based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknownSignature", 0),
          ("singleSignature", 1),
          ("dualSignature", 2))
    )


_ArubaWiredPoePethPsePortPdSignature_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortPdSignature_Object = MibTableColumn
arubaWiredPoePethPsePortPdSignature = _ArubaWiredPoePethPsePortPdSignature_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 11),
    _ArubaWiredPoePethPsePortPdSignature_Type()
)
arubaWiredPoePethPsePortPdSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPdSignature.setStatus("current")


class _ArubaWiredPoePethPsePortPowerClassification_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortPowerClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6),
          ("class6", 7),
          ("class7", 8),
          ("class8", 9))
    )


_ArubaWiredPoePethPsePortPowerClassification_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortPowerClassification_Object = MibTableColumn
arubaWiredPoePethPsePortPowerClassification = _ArubaWiredPoePethPsePortPowerClassification_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 12),
    _ArubaWiredPoePethPsePortPowerClassification_Type()
)
arubaWiredPoePethPsePortPowerClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPowerClassification.setStatus("current")


class _ArubaWiredPoePethPsePortPseAssignedClass_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortPseAssignedClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6),
          ("class6", 7))
    )


_ArubaWiredPoePethPsePortPseAssignedClass_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortPseAssignedClass_Object = MibTableColumn
arubaWiredPoePethPsePortPseAssignedClass = _ArubaWiredPoePethPsePortPseAssignedClass_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 13),
    _ArubaWiredPoePethPsePortPseAssignedClass_Type()
)
arubaWiredPoePethPsePortPseAssignedClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPseAssignedClass.setStatus("current")


class _ArubaWiredPoePethPsePortPoECycle_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortPoECycle based on Integer32"""
    defaultValue = 1


_ArubaWiredPoePethPsePortPoECycle_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortPoECycle_Object = MibTableColumn
arubaWiredPoePethPsePortPoECycle = _ArubaWiredPoePethPsePortPoECycle_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 14),
    _ArubaWiredPoePethPsePortPoECycle_Type()
)
arubaWiredPoePethPsePortPoECycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPoECycle.setStatus("current")
_ArubaWiredPoePethPsePortAveragePoePower_Type = Integer32
_ArubaWiredPoePethPsePortAveragePoePower_Object = MibTableColumn
arubaWiredPoePethPsePortAveragePoePower = _ArubaWiredPoePethPsePortAveragePoePower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 1, 1, 15),
    _ArubaWiredPoePethPsePortAveragePoePower_Type()
)
arubaWiredPoePethPsePortAveragePoePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortAveragePoePower.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortAveragePoePower.setUnits("Watts")
_ArubaWiredPoePethPseFourPairPortTable_Object = MibTable
arubaWiredPoePethPseFourPairPortTable = _ArubaWiredPoePethPseFourPairPortTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2)
)
if mibBuilder.loadTexts:
    arubaWiredPoePethPseFourPairPortTable.setStatus("current")
_ArubaWiredPoePethPseFourPairPortEntry_Object = MibTableRow
arubaWiredPoePethPseFourPairPortEntry = _ArubaWiredPoePethPseFourPairPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPoePethPseFourPairPortEntry.setStatus("current")


class _ArubaWiredPoePethPsePortDetectionStatusPairA_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortDetectionStatusPairA based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("searchingAltA", 1),
          ("deliveringPowerAltA", 2),
          ("faultAltA", 3))
    )


_ArubaWiredPoePethPsePortDetectionStatusPairA_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortDetectionStatusPairA_Object = MibTableColumn
arubaWiredPoePethPsePortDetectionStatusPairA = _ArubaWiredPoePethPsePortDetectionStatusPairA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 1),
    _ArubaWiredPoePethPsePortDetectionStatusPairA_Type()
)
arubaWiredPoePethPsePortDetectionStatusPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortDetectionStatusPairA.setStatus("current")


class _ArubaWiredPoePethPsePortDetectionStatusPairB_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortDetectionStatusPairB based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("searchingAltB", 1),
          ("deliveringPowerAltB", 2),
          ("faultAltB", 3))
    )


_ArubaWiredPoePethPsePortDetectionStatusPairB_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortDetectionStatusPairB_Object = MibTableColumn
arubaWiredPoePethPsePortDetectionStatusPairB = _ArubaWiredPoePethPsePortDetectionStatusPairB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 2),
    _ArubaWiredPoePethPsePortDetectionStatusPairB_Type()
)
arubaWiredPoePethPsePortDetectionStatusPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortDetectionStatusPairB.setStatus("current")


class _ArubaWiredPoePethPsePortPowerClassificationPairA_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortPowerClassificationPairA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("class5", 5))
    )


_ArubaWiredPoePethPsePortPowerClassificationPairA_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortPowerClassificationPairA_Object = MibTableColumn
arubaWiredPoePethPsePortPowerClassificationPairA = _ArubaWiredPoePethPsePortPowerClassificationPairA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 3),
    _ArubaWiredPoePethPsePortPowerClassificationPairA_Type()
)
arubaWiredPoePethPsePortPowerClassificationPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPowerClassificationPairA.setStatus("current")


class _ArubaWiredPoePethPsePortPowerClassificationPairB_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortPowerClassificationPairB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("class5", 5))
    )


_ArubaWiredPoePethPsePortPowerClassificationPairB_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortPowerClassificationPairB_Object = MibTableColumn
arubaWiredPoePethPsePortPowerClassificationPairB = _ArubaWiredPoePethPsePortPowerClassificationPairB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 4),
    _ArubaWiredPoePethPsePortPowerClassificationPairB_Type()
)
arubaWiredPoePethPsePortPowerClassificationPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPowerClassificationPairB.setStatus("current")


class _ArubaWiredPoePethPsePortPseAssignedClassA_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortPseAssignedClassA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4))
    )


_ArubaWiredPoePethPsePortPseAssignedClassA_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortPseAssignedClassA_Object = MibTableColumn
arubaWiredPoePethPsePortPseAssignedClassA = _ArubaWiredPoePethPsePortPseAssignedClassA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 5),
    _ArubaWiredPoePethPsePortPseAssignedClassA_Type()
)
arubaWiredPoePethPsePortPseAssignedClassA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPseAssignedClassA.setStatus("current")


class _ArubaWiredPoePethPsePortPseAssignedClassB_Type(Integer32):
    """Custom type arubaWiredPoePethPsePortPseAssignedClassB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4))
    )


_ArubaWiredPoePethPsePortPseAssignedClassB_Type.__name__ = "Integer32"
_ArubaWiredPoePethPsePortPseAssignedClassB_Object = MibTableColumn
arubaWiredPoePethPsePortPseAssignedClassB = _ArubaWiredPoePethPsePortPseAssignedClassB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 6),
    _ArubaWiredPoePethPsePortPseAssignedClassB_Type()
)
arubaWiredPoePethPsePortPseAssignedClassB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPseAssignedClassB.setStatus("current")


class _ArubaWiredPoePethPsePortInvalidSignatureCounterPairA_Type(Counter32):
    """Custom type arubaWiredPoePethPsePortInvalidSignatureCounterPairA based on Counter32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortInvalidSignatureCounterPairA_Type.__name__ = "Counter32"
_ArubaWiredPoePethPsePortInvalidSignatureCounterPairA_Object = MibTableColumn
arubaWiredPoePethPsePortInvalidSignatureCounterPairA = _ArubaWiredPoePethPsePortInvalidSignatureCounterPairA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 7),
    _ArubaWiredPoePethPsePortInvalidSignatureCounterPairA_Type()
)
arubaWiredPoePethPsePortInvalidSignatureCounterPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortInvalidSignatureCounterPairA.setStatus("current")


class _ArubaWiredPoePethPsePortInvalidSignatureCounterPairB_Type(Counter32):
    """Custom type arubaWiredPoePethPsePortInvalidSignatureCounterPairB based on Counter32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortInvalidSignatureCounterPairB_Type.__name__ = "Counter32"
_ArubaWiredPoePethPsePortInvalidSignatureCounterPairB_Object = MibTableColumn
arubaWiredPoePethPsePortInvalidSignatureCounterPairB = _ArubaWiredPoePethPsePortInvalidSignatureCounterPairB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 8),
    _ArubaWiredPoePethPsePortInvalidSignatureCounterPairB_Type()
)
arubaWiredPoePethPsePortInvalidSignatureCounterPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortInvalidSignatureCounterPairB.setStatus("current")


class _ArubaWiredPoePethPsePortPowerDeniedCounterPairA_Type(Counter32):
    """Custom type arubaWiredPoePethPsePortPowerDeniedCounterPairA based on Counter32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortPowerDeniedCounterPairA_Type.__name__ = "Counter32"
_ArubaWiredPoePethPsePortPowerDeniedCounterPairA_Object = MibTableColumn
arubaWiredPoePethPsePortPowerDeniedCounterPairA = _ArubaWiredPoePethPsePortPowerDeniedCounterPairA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 9),
    _ArubaWiredPoePethPsePortPowerDeniedCounterPairA_Type()
)
arubaWiredPoePethPsePortPowerDeniedCounterPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPowerDeniedCounterPairA.setStatus("current")


class _ArubaWiredPoePethPsePortPowerDeniedCounterPairB_Type(Counter32):
    """Custom type arubaWiredPoePethPsePortPowerDeniedCounterPairB based on Counter32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortPowerDeniedCounterPairB_Type.__name__ = "Counter32"
_ArubaWiredPoePethPsePortPowerDeniedCounterPairB_Object = MibTableColumn
arubaWiredPoePethPsePortPowerDeniedCounterPairB = _ArubaWiredPoePethPsePortPowerDeniedCounterPairB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 10),
    _ArubaWiredPoePethPsePortPowerDeniedCounterPairB_Type()
)
arubaWiredPoePethPsePortPowerDeniedCounterPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortPowerDeniedCounterPairB.setStatus("current")


class _ArubaWiredPoePethPsePortOverLoadCounterPairA_Type(Counter32):
    """Custom type arubaWiredPoePethPsePortOverLoadCounterPairA based on Counter32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortOverLoadCounterPairA_Type.__name__ = "Counter32"
_ArubaWiredPoePethPsePortOverLoadCounterPairA_Object = MibTableColumn
arubaWiredPoePethPsePortOverLoadCounterPairA = _ArubaWiredPoePethPsePortOverLoadCounterPairA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 11),
    _ArubaWiredPoePethPsePortOverLoadCounterPairA_Type()
)
arubaWiredPoePethPsePortOverLoadCounterPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortOverLoadCounterPairA.setStatus("current")


class _ArubaWiredPoePethPsePortOverLoadCounterPairB_Type(Counter32):
    """Custom type arubaWiredPoePethPsePortOverLoadCounterPairB based on Counter32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortOverLoadCounterPairB_Type.__name__ = "Counter32"
_ArubaWiredPoePethPsePortOverLoadCounterPairB_Object = MibTableColumn
arubaWiredPoePethPsePortOverLoadCounterPairB = _ArubaWiredPoePethPsePortOverLoadCounterPairB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 12),
    _ArubaWiredPoePethPsePortOverLoadCounterPairB_Type()
)
arubaWiredPoePethPsePortOverLoadCounterPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortOverLoadCounterPairB.setStatus("current")


class _ArubaWiredPoePethPsePortMPSAbsentCounterPairA_Type(Counter32):
    """Custom type arubaWiredPoePethPsePortMPSAbsentCounterPairA based on Counter32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortMPSAbsentCounterPairA_Type.__name__ = "Counter32"
_ArubaWiredPoePethPsePortMPSAbsentCounterPairA_Object = MibTableColumn
arubaWiredPoePethPsePortMPSAbsentCounterPairA = _ArubaWiredPoePethPsePortMPSAbsentCounterPairA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 13),
    _ArubaWiredPoePethPsePortMPSAbsentCounterPairA_Type()
)
arubaWiredPoePethPsePortMPSAbsentCounterPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortMPSAbsentCounterPairA.setStatus("current")


class _ArubaWiredPoePethPsePortMPSAbsentCounterPairB_Type(Counter32):
    """Custom type arubaWiredPoePethPsePortMPSAbsentCounterPairB based on Counter32"""
    defaultValue = 0


_ArubaWiredPoePethPsePortMPSAbsentCounterPairB_Type.__name__ = "Counter32"
_ArubaWiredPoePethPsePortMPSAbsentCounterPairB_Object = MibTableColumn
arubaWiredPoePethPsePortMPSAbsentCounterPairB = _ArubaWiredPoePethPsePortMPSAbsentCounterPairB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 1, 2, 1, 14),
    _ArubaWiredPoePethPsePortMPSAbsentCounterPairB_Type()
)
arubaWiredPoePethPsePortMPSAbsentCounterPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortMPSAbsentCounterPairB.setStatus("current")
_ArubaWiredPoeConformance_ObjectIdentity = ObjectIdentity
arubaWiredPoeConformance = _ArubaWiredPoeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 2)
)
_ArubaWiredPoeCompliances_ObjectIdentity = ObjectIdentity
arubaWiredPoeCompliances = _ArubaWiredPoeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 2, 1)
)
_ArubaWiredPoeGroups_ObjectIdentity = ObjectIdentity
arubaWiredPoeGroups = _ArubaWiredPoeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 2, 2)
)
_ArubaWiredPoePethMainPse_ObjectIdentity = ObjectIdentity
arubaWiredPoePethMainPse = _ArubaWiredPoePethMainPse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 3)
)
_ArubaWiredPoePethMainPseTable_Object = MibTable
arubaWiredPoePethMainPseTable = _ArubaWiredPoePethMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 3, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPoePethMainPseTable.setStatus("current")
_ArubaWiredPoePethMainPseEntry_Object = MibTableRow
arubaWiredPoePethMainPseEntry = _ArubaWiredPoePethMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPoePethMainPseEntry.setStatus("current")


class _ArubaWiredPoePethMainPseReservedPower_Type(Integer32):
    """Custom type arubaWiredPoePethMainPseReservedPower based on Integer32"""
    defaultValue = 0


_ArubaWiredPoePethMainPseReservedPower_Type.__name__ = "Integer32"
_ArubaWiredPoePethMainPseReservedPower_Object = MibTableColumn
arubaWiredPoePethMainPseReservedPower = _ArubaWiredPoePethMainPseReservedPower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 3, 1, 1, 1),
    _ArubaWiredPoePethMainPseReservedPower_Type()
)
arubaWiredPoePethMainPseReservedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethMainPseReservedPower.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPoePethMainPseReservedPower.setUnits("Watts")


class _ArubaWiredPoePethMainPseFailoverPower_Type(Integer32):
    """Custom type arubaWiredPoePethMainPseFailoverPower based on Integer32"""
    defaultValue = 0


_ArubaWiredPoePethMainPseFailoverPower_Type.__name__ = "Integer32"
_ArubaWiredPoePethMainPseFailoverPower_Object = MibTableColumn
arubaWiredPoePethMainPseFailoverPower = _ArubaWiredPoePethMainPseFailoverPower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 3, 1, 1, 2),
    _ArubaWiredPoePethMainPseFailoverPower_Type()
)
arubaWiredPoePethMainPseFailoverPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethMainPseFailoverPower.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPoePethMainPseFailoverPower.setUnits("Watts")


class _ArubaWiredPoePethMainPseRedundantPower_Type(Integer32):
    """Custom type arubaWiredPoePethMainPseRedundantPower based on Integer32"""
    defaultValue = 0


_ArubaWiredPoePethMainPseRedundantPower_Type.__name__ = "Integer32"
_ArubaWiredPoePethMainPseRedundantPower_Object = MibTableColumn
arubaWiredPoePethMainPseRedundantPower = _ArubaWiredPoePethMainPseRedundantPower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 3, 1, 1, 3),
    _ArubaWiredPoePethMainPseRedundantPower_Type()
)
arubaWiredPoePethMainPseRedundantPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethMainPseRedundantPower.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPoePethMainPseRedundantPower.setUnits("Watts")
_ArubaWiredPoePethMainPseAveragePoePower_Type = Integer32
_ArubaWiredPoePethMainPseAveragePoePower_Object = MibTableColumn
arubaWiredPoePethMainPseAveragePoePower = _ArubaWiredPoePethMainPseAveragePoePower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 3, 1, 1, 4),
    _ArubaWiredPoePethMainPseAveragePoePower_Type()
)
arubaWiredPoePethMainPseAveragePoePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethMainPseAveragePoePower.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPoePethMainPseAveragePoePower.setUnits("Watts")
_ArubaWiredPoePethPseModule_ObjectIdentity = ObjectIdentity
arubaWiredPoePethPseModule = _ArubaWiredPoePethPseModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 4)
)
_ArubaWiredPoePethPseModuleTable_Object = MibTable
arubaWiredPoePethPseModuleTable = _ArubaWiredPoePethPseModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 4, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPoePethPseModuleTable.setStatus("current")
_ArubaWiredPoePethPseModuleEntry_Object = MibTableRow
arubaWiredPoePethPseModuleEntry = _ArubaWiredPoePethPseModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 4, 1, 1)
)
arubaWiredPoePethPseModuleEntry.setIndexNames(
    (0, "ARUBAWIRED-POE-MIB", "arubaWiredPoePethPseModuleGroupIndex"),
    (0, "ARUBAWIRED-POE-MIB", "arubaWiredPoePethPseModuleSlotIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredPoePethPseModuleEntry.setStatus("current")


class _ArubaWiredPoePethPseModuleGroupIndex_Type(Integer32):
    """Custom type arubaWiredPoePethPseModuleGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredPoePethPseModuleGroupIndex_Type.__name__ = "Integer32"
_ArubaWiredPoePethPseModuleGroupIndex_Object = MibTableColumn
arubaWiredPoePethPseModuleGroupIndex = _ArubaWiredPoePethPseModuleGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 4, 1, 1, 1),
    _ArubaWiredPoePethPseModuleGroupIndex_Type()
)
arubaWiredPoePethPseModuleGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredPoePethPseModuleGroupIndex.setStatus("current")


class _ArubaWiredPoePethPseModuleSlotIndex_Type(Integer32):
    """Custom type arubaWiredPoePethPseModuleSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredPoePethPseModuleSlotIndex_Type.__name__ = "Integer32"
_ArubaWiredPoePethPseModuleSlotIndex_Object = MibTableColumn
arubaWiredPoePethPseModuleSlotIndex = _ArubaWiredPoePethPseModuleSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 4, 1, 1, 2),
    _ArubaWiredPoePethPseModuleSlotIndex_Type()
)
arubaWiredPoePethPseModuleSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredPoePethPseModuleSlotIndex.setStatus("current")


class _ArubaWiredPoePethPseModuleAlwaysOnPoe_Type(Integer32):
    """Custom type arubaWiredPoePethPseModuleAlwaysOnPoe based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ArubaWiredPoePethPseModuleAlwaysOnPoe_Type.__name__ = "Integer32"
_ArubaWiredPoePethPseModuleAlwaysOnPoe_Object = MibTableColumn
arubaWiredPoePethPseModuleAlwaysOnPoe = _ArubaWiredPoePethPseModuleAlwaysOnPoe_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 4, 1, 1, 3),
    _ArubaWiredPoePethPseModuleAlwaysOnPoe_Type()
)
arubaWiredPoePethPseModuleAlwaysOnPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPoePethPseModuleAlwaysOnPoe.setStatus("current")
pethPsePortEntry.registerAugmentions(
    ("ARUBAWIRED-POE-MIB",
     "arubaWiredPoePethPsePortEntry")
)
arubaWiredPoePethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethPsePortEntry.registerAugmentions(
    ("ARUBAWIRED-POE-MIB",
     "arubaWiredPoePethPseFourPairPortEntry")
)
arubaWiredPoePethPseFourPairPortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethMainPseEntry.registerAugmentions(
    ("ARUBAWIRED-POE-MIB",
     "arubaWiredPoePethMainPseEntry")
)
arubaWiredPoePethMainPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())

# Managed Objects groups

arubaWiredPoePethPsePortTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 2, 2, 1)
)
arubaWiredPoePethPsePortTableGroup.setObjects(
      *(("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPowerAllocateBy"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPreStdDetect"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortRpd"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortCurrent"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortVoltage"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortReservedPower"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPowerDrawn"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortAveragePower"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPeakPower"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortOperStatus"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPdSignature"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPowerClassification"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPseAssignedClass"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPoECycle"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortAveragePoePower"))
)
if mibBuilder.loadTexts:
    arubaWiredPoePethPsePortTableGroup.setStatus("current")

arubaWiredPoePethPseFourPairPortTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 2, 2, 2)
)
arubaWiredPoePethPseFourPairPortTableGroup.setObjects(
      *(("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortDetectionStatusPairA"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortDetectionStatusPairB"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPowerClassificationPairA"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPowerClassificationPairB"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPseAssignedClassA"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPseAssignedClassB"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortInvalidSignatureCounterPairA"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortInvalidSignatureCounterPairB"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPowerDeniedCounterPairA"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortPowerDeniedCounterPairB"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortOverLoadCounterPairA"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortOverLoadCounterPairB"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortMPSAbsentCounterPairA"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortMPSAbsentCounterPairB"))
)
if mibBuilder.loadTexts:
    arubaWiredPoePethPseFourPairPortTableGroup.setStatus("current")

arubaWiredPoePethMainPseTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 2, 2, 3)
)
arubaWiredPoePethMainPseTableGroup.setObjects(
      *(("ARUBAWIRED-POE-MIB", "arubaWiredPoePethMainPseReservedPower"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethMainPseFailoverPower"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethMainPseRedundantPower"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethMainPseAveragePoePower"))
)
if mibBuilder.loadTexts:
    arubaWiredPoePethMainPseTableGroup.setStatus("current")

arubaWiredPoePethPseModuleTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 2, 2, 4)
)
arubaWiredPoePethPseModuleTableGroup.setObjects(
    ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPseModuleAlwaysOnPoe")
)
if mibBuilder.loadTexts:
    arubaWiredPoePethPseModuleTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredPoeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8, 2, 1, 1)
)
arubaWiredPoeCompliance.setObjects(
      *(("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortTable"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethMainPseTable"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPseModuleTable"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPsePortTableGroup"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPseFourPairPortTableGroup"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethMainPseTableGroup"),
        ("ARUBAWIRED-POE-MIB", "arubaWiredPoePethPseModuleTableGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredPoeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-POE-MIB",
    **{"arubaWiredPoeMIB": arubaWiredPoeMIB,
       "arubaWiredPoePethPsePort": arubaWiredPoePethPsePort,
       "arubaWiredPoePethPsePortTable": arubaWiredPoePethPsePortTable,
       "arubaWiredPoePethPsePortEntry": arubaWiredPoePethPsePortEntry,
       "arubaWiredPoePethPsePortPowerAllocateBy": arubaWiredPoePethPsePortPowerAllocateBy,
       "arubaWiredPoePethPsePortPreStdDetect": arubaWiredPoePethPsePortPreStdDetect,
       "arubaWiredPoePethPsePortRpd": arubaWiredPoePethPsePortRpd,
       "arubaWiredPoePethPsePortCurrent": arubaWiredPoePethPsePortCurrent,
       "arubaWiredPoePethPsePortVoltage": arubaWiredPoePethPsePortVoltage,
       "arubaWiredPoePethPsePortReservedPower": arubaWiredPoePethPsePortReservedPower,
       "arubaWiredPoePethPsePortPowerDrawn": arubaWiredPoePethPsePortPowerDrawn,
       "arubaWiredPoePethPsePortAveragePower": arubaWiredPoePethPsePortAveragePower,
       "arubaWiredPoePethPsePortPeakPower": arubaWiredPoePethPsePortPeakPower,
       "arubaWiredPoePethPsePortOperStatus": arubaWiredPoePethPsePortOperStatus,
       "arubaWiredPoePethPsePortPdSignature": arubaWiredPoePethPsePortPdSignature,
       "arubaWiredPoePethPsePortPowerClassification": arubaWiredPoePethPsePortPowerClassification,
       "arubaWiredPoePethPsePortPseAssignedClass": arubaWiredPoePethPsePortPseAssignedClass,
       "arubaWiredPoePethPsePortPoECycle": arubaWiredPoePethPsePortPoECycle,
       "arubaWiredPoePethPsePortAveragePoePower": arubaWiredPoePethPsePortAveragePoePower,
       "arubaWiredPoePethPseFourPairPortTable": arubaWiredPoePethPseFourPairPortTable,
       "arubaWiredPoePethPseFourPairPortEntry": arubaWiredPoePethPseFourPairPortEntry,
       "arubaWiredPoePethPsePortDetectionStatusPairA": arubaWiredPoePethPsePortDetectionStatusPairA,
       "arubaWiredPoePethPsePortDetectionStatusPairB": arubaWiredPoePethPsePortDetectionStatusPairB,
       "arubaWiredPoePethPsePortPowerClassificationPairA": arubaWiredPoePethPsePortPowerClassificationPairA,
       "arubaWiredPoePethPsePortPowerClassificationPairB": arubaWiredPoePethPsePortPowerClassificationPairB,
       "arubaWiredPoePethPsePortPseAssignedClassA": arubaWiredPoePethPsePortPseAssignedClassA,
       "arubaWiredPoePethPsePortPseAssignedClassB": arubaWiredPoePethPsePortPseAssignedClassB,
       "arubaWiredPoePethPsePortInvalidSignatureCounterPairA": arubaWiredPoePethPsePortInvalidSignatureCounterPairA,
       "arubaWiredPoePethPsePortInvalidSignatureCounterPairB": arubaWiredPoePethPsePortInvalidSignatureCounterPairB,
       "arubaWiredPoePethPsePortPowerDeniedCounterPairA": arubaWiredPoePethPsePortPowerDeniedCounterPairA,
       "arubaWiredPoePethPsePortPowerDeniedCounterPairB": arubaWiredPoePethPsePortPowerDeniedCounterPairB,
       "arubaWiredPoePethPsePortOverLoadCounterPairA": arubaWiredPoePethPsePortOverLoadCounterPairA,
       "arubaWiredPoePethPsePortOverLoadCounterPairB": arubaWiredPoePethPsePortOverLoadCounterPairB,
       "arubaWiredPoePethPsePortMPSAbsentCounterPairA": arubaWiredPoePethPsePortMPSAbsentCounterPairA,
       "arubaWiredPoePethPsePortMPSAbsentCounterPairB": arubaWiredPoePethPsePortMPSAbsentCounterPairB,
       "arubaWiredPoeConformance": arubaWiredPoeConformance,
       "arubaWiredPoeCompliances": arubaWiredPoeCompliances,
       "arubaWiredPoeCompliance": arubaWiredPoeCompliance,
       "arubaWiredPoeGroups": arubaWiredPoeGroups,
       "arubaWiredPoePethPsePortTableGroup": arubaWiredPoePethPsePortTableGroup,
       "arubaWiredPoePethPseFourPairPortTableGroup": arubaWiredPoePethPseFourPairPortTableGroup,
       "arubaWiredPoePethMainPseTableGroup": arubaWiredPoePethMainPseTableGroup,
       "arubaWiredPoePethPseModuleTableGroup": arubaWiredPoePethPseModuleTableGroup,
       "arubaWiredPoePethMainPse": arubaWiredPoePethMainPse,
       "arubaWiredPoePethMainPseTable": arubaWiredPoePethMainPseTable,
       "arubaWiredPoePethMainPseEntry": arubaWiredPoePethMainPseEntry,
       "arubaWiredPoePethMainPseReservedPower": arubaWiredPoePethMainPseReservedPower,
       "arubaWiredPoePethMainPseFailoverPower": arubaWiredPoePethMainPseFailoverPower,
       "arubaWiredPoePethMainPseRedundantPower": arubaWiredPoePethMainPseRedundantPower,
       "arubaWiredPoePethMainPseAveragePoePower": arubaWiredPoePethMainPseAveragePoePower,
       "arubaWiredPoePethPseModule": arubaWiredPoePethPseModule,
       "arubaWiredPoePethPseModuleTable": arubaWiredPoePethPseModuleTable,
       "arubaWiredPoePethPseModuleEntry": arubaWiredPoePethPseModuleEntry,
       "arubaWiredPoePethPseModuleGroupIndex": arubaWiredPoePethPseModuleGroupIndex,
       "arubaWiredPoePethPseModuleSlotIndex": arubaWiredPoePethPseModuleSlotIndex,
       "arubaWiredPoePethPseModuleAlwaysOnPoe": arubaWiredPoePethPseModuleAlwaysOnPoe}
)
