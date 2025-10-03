# SNMP MIB module (ARUBAWIRED-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-LLDP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:10 2025
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

(lldpLocPortNum,
 lldpRemIndex,
 lldpRemLocalPortNum,
 lldpRemTimeMark) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "lldpLocPortNum",
    "lldpRemIndex",
    "lldpRemLocalPortNum",
    "lldpRemTimeMark")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arubaWiredLldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    arubaWiredLldpMIB.setRevisions(
        ("2022-11-24 00:00",
         "2020-10-22 00:00",
         "2019-04-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredLldpXdot3Objects_ObjectIdentity = ObjectIdentity
arubaWiredLldpXdot3Objects = _ArubaWiredLldpXdot3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1)
)
_ArubaWiredLldpXdot3LocalData_ObjectIdentity = ObjectIdentity
arubaWiredLldpXdot3LocalData = _ArubaWiredLldpXdot3LocalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1)
)
_ArubaWiredLldpXdot3LocPowerTable_Object = MibTable
arubaWiredLldpXdot3LocPowerTable = _ArubaWiredLldpXdot3LocPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerTable.setStatus("current")
_ArubaWiredLldpXdot3LocPowerEntry_Object = MibTableRow
arubaWiredLldpXdot3LocPowerEntry = _ArubaWiredLldpXdot3LocPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1)
)
arubaWiredLldpXdot3LocPowerEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerEntry.setStatus("current")


class _ArubaWiredLldpXdot3LocPowerPortClass_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPowerPortClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pClassPSE", 1),
          ("pClassPD", 2))
    )


_ArubaWiredLldpXdot3LocPowerPortClass_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPowerPortClass_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerPortClass = _ArubaWiredLldpXdot3LocPowerPortClass_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 1),
    _ArubaWiredLldpXdot3LocPowerPortClass_Type()
)
arubaWiredLldpXdot3LocPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerPortClass.setStatus("current")
_ArubaWiredLldpXdot3LocPowerMDISupported_Type = TruthValue
_ArubaWiredLldpXdot3LocPowerMDISupported_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerMDISupported = _ArubaWiredLldpXdot3LocPowerMDISupported_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 2),
    _ArubaWiredLldpXdot3LocPowerMDISupported_Type()
)
arubaWiredLldpXdot3LocPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerMDISupported.setStatus("current")
_ArubaWiredLldpXdot3LocPowerMDIEnabled_Type = TruthValue
_ArubaWiredLldpXdot3LocPowerMDIEnabled_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerMDIEnabled = _ArubaWiredLldpXdot3LocPowerMDIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 3),
    _ArubaWiredLldpXdot3LocPowerMDIEnabled_Type()
)
arubaWiredLldpXdot3LocPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerMDIEnabled.setStatus("current")
_ArubaWiredLldpXdot3LocPowerPairControlable_Type = TruthValue
_ArubaWiredLldpXdot3LocPowerPairControlable_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerPairControlable = _ArubaWiredLldpXdot3LocPowerPairControlable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 4),
    _ArubaWiredLldpXdot3LocPowerPairControlable_Type()
)
arubaWiredLldpXdot3LocPowerPairControlable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerPairControlable.setStatus("current")


class _ArubaWiredLldpXdot3LocPowerPairs_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPowerPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pairSignal", 1),
          ("pairSpare", 2))
    )


_ArubaWiredLldpXdot3LocPowerPairs_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPowerPairs_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerPairs = _ArubaWiredLldpXdot3LocPowerPairs_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 5),
    _ArubaWiredLldpXdot3LocPowerPairs_Type()
)
arubaWiredLldpXdot3LocPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerPairs.setStatus("current")


class _ArubaWiredLldpXdot3LocPowerClass_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPowerClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_ArubaWiredLldpXdot3LocPowerClass_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPowerClass_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerClass = _ArubaWiredLldpXdot3LocPowerClass_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 6),
    _ArubaWiredLldpXdot3LocPowerClass_Type()
)
arubaWiredLldpXdot3LocPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerClass.setStatus("current")


class _ArubaWiredLldpXdot3LocPowerType_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPowerType based on Integer32"""
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
        *(("type2PSE", 1),
          ("type2PD", 2),
          ("type1PSE", 3),
          ("type1PD", 4))
    )


_ArubaWiredLldpXdot3LocPowerType_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPowerType_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerType = _ArubaWiredLldpXdot3LocPowerType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 7),
    _ArubaWiredLldpXdot3LocPowerType_Type()
)
arubaWiredLldpXdot3LocPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerType.setStatus("current")


class _ArubaWiredLldpXdot3LocPowerSource_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPowerSource based on Integer32"""
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
        *(("unknown", 1),
          ("primary", 2),
          ("backup", 3),
          ("reserved", 4))
    )


_ArubaWiredLldpXdot3LocPowerSource_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPowerSource_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerSource = _ArubaWiredLldpXdot3LocPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 8),
    _ArubaWiredLldpXdot3LocPowerSource_Type()
)
arubaWiredLldpXdot3LocPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerSource.setStatus("current")


class _ArubaWiredLldpXdot3LocPowerPriority_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPowerPriority based on Integer32"""
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
        *(("unknown", 1),
          ("critical", 2),
          ("high", 3),
          ("low", 4))
    )


_ArubaWiredLldpXdot3LocPowerPriority_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPowerPriority_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerPriority = _ArubaWiredLldpXdot3LocPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 9),
    _ArubaWiredLldpXdot3LocPowerPriority_Type()
)
arubaWiredLldpXdot3LocPowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerPriority.setStatus("current")


class _ArubaWiredLldpXdot3LocPDRequestedPowerValue_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPDRequestedPowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_ArubaWiredLldpXdot3LocPDRequestedPowerValue_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPDRequestedPowerValue_Object = MibTableColumn
arubaWiredLldpXdot3LocPDRequestedPowerValue = _ArubaWiredLldpXdot3LocPDRequestedPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 10),
    _ArubaWiredLldpXdot3LocPDRequestedPowerValue_Type()
)
arubaWiredLldpXdot3LocPDRequestedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPDRequestedPowerValue.setStatus("current")


class _ArubaWiredLldpXdot3LocPDRequestedPowerValueA_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPDRequestedPowerValueA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 499),
    )


_ArubaWiredLldpXdot3LocPDRequestedPowerValueA_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPDRequestedPowerValueA_Object = MibTableColumn
arubaWiredLldpXdot3LocPDRequestedPowerValueA = _ArubaWiredLldpXdot3LocPDRequestedPowerValueA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 11),
    _ArubaWiredLldpXdot3LocPDRequestedPowerValueA_Type()
)
arubaWiredLldpXdot3LocPDRequestedPowerValueA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPDRequestedPowerValueA.setStatus("current")


class _ArubaWiredLldpXdot3LocPDRequestedPowerValueB_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPDRequestedPowerValueB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 499),
    )


_ArubaWiredLldpXdot3LocPDRequestedPowerValueB_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPDRequestedPowerValueB_Object = MibTableColumn
arubaWiredLldpXdot3LocPDRequestedPowerValueB = _ArubaWiredLldpXdot3LocPDRequestedPowerValueB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 12),
    _ArubaWiredLldpXdot3LocPDRequestedPowerValueB_Type()
)
arubaWiredLldpXdot3LocPDRequestedPowerValueB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPDRequestedPowerValueB.setStatus("current")


class _ArubaWiredLldpXdot3LocPSEAllocatedPowerValue_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPSEAllocatedPowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_ArubaWiredLldpXdot3LocPSEAllocatedPowerValue_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPSEAllocatedPowerValue_Object = MibTableColumn
arubaWiredLldpXdot3LocPSEAllocatedPowerValue = _ArubaWiredLldpXdot3LocPSEAllocatedPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 13),
    _ArubaWiredLldpXdot3LocPSEAllocatedPowerValue_Type()
)
arubaWiredLldpXdot3LocPSEAllocatedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPSEAllocatedPowerValue.setStatus("current")


class _ArubaWiredLldpXdot3LocPSEAllocatedPowerValueA_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPSEAllocatedPowerValueA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 499),
    )


_ArubaWiredLldpXdot3LocPSEAllocatedPowerValueA_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPSEAllocatedPowerValueA_Object = MibTableColumn
arubaWiredLldpXdot3LocPSEAllocatedPowerValueA = _ArubaWiredLldpXdot3LocPSEAllocatedPowerValueA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 14),
    _ArubaWiredLldpXdot3LocPSEAllocatedPowerValueA_Type()
)
arubaWiredLldpXdot3LocPSEAllocatedPowerValueA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPSEAllocatedPowerValueA.setStatus("current")


class _ArubaWiredLldpXdot3LocPSEAllocatedPowerValueB_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPSEAllocatedPowerValueB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 499),
    )


_ArubaWiredLldpXdot3LocPSEAllocatedPowerValueB_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPSEAllocatedPowerValueB_Object = MibTableColumn
arubaWiredLldpXdot3LocPSEAllocatedPowerValueB = _ArubaWiredLldpXdot3LocPSEAllocatedPowerValueB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 15),
    _ArubaWiredLldpXdot3LocPSEAllocatedPowerValueB_Type()
)
arubaWiredLldpXdot3LocPSEAllocatedPowerValueB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPSEAllocatedPowerValueB.setStatus("current")


class _ArubaWiredLldpXdot3LocPSEPoweringStatus_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPSEPoweringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("twoPair", 1),
          ("fourPsinglesigPD", 2),
          ("fourPdualsigPD", 3))
    )


_ArubaWiredLldpXdot3LocPSEPoweringStatus_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPSEPoweringStatus_Object = MibTableColumn
arubaWiredLldpXdot3LocPSEPoweringStatus = _ArubaWiredLldpXdot3LocPSEPoweringStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 16),
    _ArubaWiredLldpXdot3LocPSEPoweringStatus_Type()
)
arubaWiredLldpXdot3LocPSEPoweringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPSEPoweringStatus.setStatus("current")


class _ArubaWiredLldpXdot3LocPowerPairsExt_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPowerPairsExt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("altA", 1),
          ("altB", 2),
          ("both", 3))
    )


_ArubaWiredLldpXdot3LocPowerPairsExt_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPowerPairsExt_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerPairsExt = _ArubaWiredLldpXdot3LocPowerPairsExt_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 17),
    _ArubaWiredLldpXdot3LocPowerPairsExt_Type()
)
arubaWiredLldpXdot3LocPowerPairsExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerPairsExt.setStatus("current")


class _ArubaWiredLldpXdot3LocPowerClassExtA_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPowerClassExtA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("singlesig", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6))
    )


_ArubaWiredLldpXdot3LocPowerClassExtA_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPowerClassExtA_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerClassExtA = _ArubaWiredLldpXdot3LocPowerClassExtA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 18),
    _ArubaWiredLldpXdot3LocPowerClassExtA_Type()
)
arubaWiredLldpXdot3LocPowerClassExtA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerClassExtA.setStatus("current")


class _ArubaWiredLldpXdot3LocPowerClassExtB_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPowerClassExtB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("singlesig", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6))
    )


_ArubaWiredLldpXdot3LocPowerClassExtB_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPowerClassExtB_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerClassExtB = _ArubaWiredLldpXdot3LocPowerClassExtB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 19),
    _ArubaWiredLldpXdot3LocPowerClassExtB_Type()
)
arubaWiredLldpXdot3LocPowerClassExtB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerClassExtB.setStatus("current")


class _ArubaWiredLldpXdot3LocPowerClassExt_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPowerClassExt based on Integer32"""
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
        *(("dualsig", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6),
          ("class6", 7),
          ("class7", 8),
          ("class8", 9))
    )


_ArubaWiredLldpXdot3LocPowerClassExt_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPowerClassExt_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerClassExt = _ArubaWiredLldpXdot3LocPowerClassExt_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 20),
    _ArubaWiredLldpXdot3LocPowerClassExt_Type()
)
arubaWiredLldpXdot3LocPowerClassExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerClassExt.setStatus("current")


class _ArubaWiredLldpXdot3LocPowerTypeExt_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPowerTypeExt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("type3PSE", 1),
          ("type4PSE", 2),
          ("type3singlesigPD", 3),
          ("type3dualsigPD", 4),
          ("type4singlesigPD", 5),
          ("type4dualsigPD", 6))
    )


_ArubaWiredLldpXdot3LocPowerTypeExt_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPowerTypeExt_Object = MibTableColumn
arubaWiredLldpXdot3LocPowerTypeExt = _ArubaWiredLldpXdot3LocPowerTypeExt_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 21),
    _ArubaWiredLldpXdot3LocPowerTypeExt_Type()
)
arubaWiredLldpXdot3LocPowerTypeExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPowerTypeExt.setStatus("current")
_ArubaWiredLldpXdot3LocPDLoad_Type = TruthValue
_ArubaWiredLldpXdot3LocPDLoad_Object = MibTableColumn
arubaWiredLldpXdot3LocPDLoad = _ArubaWiredLldpXdot3LocPDLoad_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 22),
    _ArubaWiredLldpXdot3LocPDLoad_Type()
)
arubaWiredLldpXdot3LocPDLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPDLoad.setStatus("current")


class _ArubaWiredLldpXdot3LocPSEMaxAvailPower_Type(Integer32):
    """Custom type arubaWiredLldpXdot3LocPSEMaxAvailPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_ArubaWiredLldpXdot3LocPSEMaxAvailPower_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3LocPSEMaxAvailPower_Object = MibTableColumn
arubaWiredLldpXdot3LocPSEMaxAvailPower = _ArubaWiredLldpXdot3LocPSEMaxAvailPower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 23),
    _ArubaWiredLldpXdot3LocPSEMaxAvailPower_Type()
)
arubaWiredLldpXdot3LocPSEMaxAvailPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPSEMaxAvailPower.setStatus("current")
_ArubaWiredLldpXdot3LocPSEAutoclassSupport_Type = TruthValue
_ArubaWiredLldpXdot3LocPSEAutoclassSupport_Object = MibTableColumn
arubaWiredLldpXdot3LocPSEAutoclassSupport = _ArubaWiredLldpXdot3LocPSEAutoclassSupport_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 24),
    _ArubaWiredLldpXdot3LocPSEAutoclassSupport_Type()
)
arubaWiredLldpXdot3LocPSEAutoclassSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocPSEAutoclassSupport.setStatus("current")
_ArubaWiredLldpXdot3LocAutoclassCompleted_Type = TruthValue
_ArubaWiredLldpXdot3LocAutoclassCompleted_Object = MibTableColumn
arubaWiredLldpXdot3LocAutoclassCompleted = _ArubaWiredLldpXdot3LocAutoclassCompleted_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 25),
    _ArubaWiredLldpXdot3LocAutoclassCompleted_Type()
)
arubaWiredLldpXdot3LocAutoclassCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocAutoclassCompleted.setStatus("current")


class _ArubaWiredLldpLocPseTlvSentType_Type(Integer32):
    """Custom type arubaWiredLldpLocPseTlvSentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("med", 1),
          ("dot3", 2),
          ("dot3-ext", 3))
    )


_ArubaWiredLldpLocPseTlvSentType_Type.__name__ = "Integer32"
_ArubaWiredLldpLocPseTlvSentType_Object = MibTableColumn
arubaWiredLldpLocPseTlvSentType = _ArubaWiredLldpLocPseTlvSentType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 26),
    _ArubaWiredLldpLocPseTlvSentType_Type()
)
arubaWiredLldpLocPseTlvSentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpLocPseTlvSentType.setStatus("current")


class _ArubaWiredLldpLocPdTlvSentType_Type(Integer32):
    """Custom type arubaWiredLldpLocPdTlvSentType based on Integer32"""
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
        *(("med", 1),
          ("dot3", 2),
          ("dot3-ext", 3),
          ("medanddot3", 4),
          ("medanddot3-ext", 5))
    )


_ArubaWiredLldpLocPdTlvSentType_Type.__name__ = "Integer32"
_ArubaWiredLldpLocPdTlvSentType_Object = MibTableColumn
arubaWiredLldpLocPdTlvSentType = _ArubaWiredLldpLocPdTlvSentType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 1, 1, 1, 27),
    _ArubaWiredLldpLocPdTlvSentType_Type()
)
arubaWiredLldpLocPdTlvSentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpLocPdTlvSentType.setStatus("current")
_ArubaWiredLldpXdot3RemoteData_ObjectIdentity = ObjectIdentity
arubaWiredLldpXdot3RemoteData = _ArubaWiredLldpXdot3RemoteData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2)
)
_ArubaWiredLldpXdot3RemPowerTable_Object = MibTable
arubaWiredLldpXdot3RemPowerTable = _ArubaWiredLldpXdot3RemPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerTable.setStatus("current")
_ArubaWiredLldpXdot3RemPowerEntry_Object = MibTableRow
arubaWiredLldpXdot3RemPowerEntry = _ArubaWiredLldpXdot3RemPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1)
)
arubaWiredLldpXdot3RemPowerEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerEntry.setStatus("current")


class _ArubaWiredLldpXdot3RemPowerPortClass_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPowerPortClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pClassPSE", 1),
          ("pClassPD", 2))
    )


_ArubaWiredLldpXdot3RemPowerPortClass_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPowerPortClass_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerPortClass = _ArubaWiredLldpXdot3RemPowerPortClass_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 1),
    _ArubaWiredLldpXdot3RemPowerPortClass_Type()
)
arubaWiredLldpXdot3RemPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerPortClass.setStatus("current")
_ArubaWiredLldpXdot3RemPowerMDISupported_Type = TruthValue
_ArubaWiredLldpXdot3RemPowerMDISupported_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerMDISupported = _ArubaWiredLldpXdot3RemPowerMDISupported_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 2),
    _ArubaWiredLldpXdot3RemPowerMDISupported_Type()
)
arubaWiredLldpXdot3RemPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerMDISupported.setStatus("current")
_ArubaWiredLldpXdot3RemPowerMDIEnabled_Type = TruthValue
_ArubaWiredLldpXdot3RemPowerMDIEnabled_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerMDIEnabled = _ArubaWiredLldpXdot3RemPowerMDIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 3),
    _ArubaWiredLldpXdot3RemPowerMDIEnabled_Type()
)
arubaWiredLldpXdot3RemPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerMDIEnabled.setStatus("current")
_ArubaWiredLldpXdot3RemPowerPairControlable_Type = TruthValue
_ArubaWiredLldpXdot3RemPowerPairControlable_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerPairControlable = _ArubaWiredLldpXdot3RemPowerPairControlable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 4),
    _ArubaWiredLldpXdot3RemPowerPairControlable_Type()
)
arubaWiredLldpXdot3RemPowerPairControlable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerPairControlable.setStatus("current")


class _ArubaWiredLldpXdot3RemPowerPairs_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPowerPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pairSignal", 1),
          ("pairSpare", 2))
    )


_ArubaWiredLldpXdot3RemPowerPairs_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPowerPairs_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerPairs = _ArubaWiredLldpXdot3RemPowerPairs_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 5),
    _ArubaWiredLldpXdot3RemPowerPairs_Type()
)
arubaWiredLldpXdot3RemPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerPairs.setStatus("current")


class _ArubaWiredLldpXdot3RemPowerClass_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPowerClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_ArubaWiredLldpXdot3RemPowerClass_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPowerClass_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerClass = _ArubaWiredLldpXdot3RemPowerClass_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 6),
    _ArubaWiredLldpXdot3RemPowerClass_Type()
)
arubaWiredLldpXdot3RemPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerClass.setStatus("current")


class _ArubaWiredLldpXdot3RemPowerType_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPowerType based on Integer32"""
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
        *(("type2PSE", 1),
          ("type2PD", 2),
          ("type1PSE", 3),
          ("type1PD", 4))
    )


_ArubaWiredLldpXdot3RemPowerType_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPowerType_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerType = _ArubaWiredLldpXdot3RemPowerType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 7),
    _ArubaWiredLldpXdot3RemPowerType_Type()
)
arubaWiredLldpXdot3RemPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerType.setStatus("current")


class _ArubaWiredLldpXdot3RemPowerSource_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPowerSource based on Integer32"""
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
        *(("unknown", 1),
          ("pse", 2),
          ("local", 3),
          ("pseAndLocal", 4))
    )


_ArubaWiredLldpXdot3RemPowerSource_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPowerSource_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerSource = _ArubaWiredLldpXdot3RemPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 8),
    _ArubaWiredLldpXdot3RemPowerSource_Type()
)
arubaWiredLldpXdot3RemPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerSource.setStatus("current")


class _ArubaWiredLldpXdot3RemPowerPriority_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPowerPriority based on Integer32"""
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
        *(("unknown", 1),
          ("critical", 2),
          ("high", 3),
          ("low", 4))
    )


_ArubaWiredLldpXdot3RemPowerPriority_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPowerPriority_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerPriority = _ArubaWiredLldpXdot3RemPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 9),
    _ArubaWiredLldpXdot3RemPowerPriority_Type()
)
arubaWiredLldpXdot3RemPowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerPriority.setStatus("current")


class _ArubaWiredLldpXdot3RemPDRequestedPowerValue_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPDRequestedPowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_ArubaWiredLldpXdot3RemPDRequestedPowerValue_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPDRequestedPowerValue_Object = MibTableColumn
arubaWiredLldpXdot3RemPDRequestedPowerValue = _ArubaWiredLldpXdot3RemPDRequestedPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 10),
    _ArubaWiredLldpXdot3RemPDRequestedPowerValue_Type()
)
arubaWiredLldpXdot3RemPDRequestedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPDRequestedPowerValue.setStatus("current")


class _ArubaWiredLldpXdot3RemPDRequestedPowerValueA_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPDRequestedPowerValueA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 499),
    )


_ArubaWiredLldpXdot3RemPDRequestedPowerValueA_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPDRequestedPowerValueA_Object = MibTableColumn
arubaWiredLldpXdot3RemPDRequestedPowerValueA = _ArubaWiredLldpXdot3RemPDRequestedPowerValueA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 11),
    _ArubaWiredLldpXdot3RemPDRequestedPowerValueA_Type()
)
arubaWiredLldpXdot3RemPDRequestedPowerValueA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPDRequestedPowerValueA.setStatus("current")


class _ArubaWiredLldpXdot3RemPDRequestedPowerValueB_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPDRequestedPowerValueB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 499),
    )


_ArubaWiredLldpXdot3RemPDRequestedPowerValueB_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPDRequestedPowerValueB_Object = MibTableColumn
arubaWiredLldpXdot3RemPDRequestedPowerValueB = _ArubaWiredLldpXdot3RemPDRequestedPowerValueB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 12),
    _ArubaWiredLldpXdot3RemPDRequestedPowerValueB_Type()
)
arubaWiredLldpXdot3RemPDRequestedPowerValueB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPDRequestedPowerValueB.setStatus("current")


class _ArubaWiredLldpXdot3RemPSEAllocatedPowerValue_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPSEAllocatedPowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_ArubaWiredLldpXdot3RemPSEAllocatedPowerValue_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPSEAllocatedPowerValue_Object = MibTableColumn
arubaWiredLldpXdot3RemPSEAllocatedPowerValue = _ArubaWiredLldpXdot3RemPSEAllocatedPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 13),
    _ArubaWiredLldpXdot3RemPSEAllocatedPowerValue_Type()
)
arubaWiredLldpXdot3RemPSEAllocatedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPSEAllocatedPowerValue.setStatus("current")


class _ArubaWiredLldpXdot3RemPSEAllocatedPowerValueA_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPSEAllocatedPowerValueA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 499),
    )


_ArubaWiredLldpXdot3RemPSEAllocatedPowerValueA_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPSEAllocatedPowerValueA_Object = MibTableColumn
arubaWiredLldpXdot3RemPSEAllocatedPowerValueA = _ArubaWiredLldpXdot3RemPSEAllocatedPowerValueA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 14),
    _ArubaWiredLldpXdot3RemPSEAllocatedPowerValueA_Type()
)
arubaWiredLldpXdot3RemPSEAllocatedPowerValueA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPSEAllocatedPowerValueA.setStatus("current")


class _ArubaWiredLldpXdot3RemPSEAllocatedPowerValueB_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPSEAllocatedPowerValueB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 499),
    )


_ArubaWiredLldpXdot3RemPSEAllocatedPowerValueB_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPSEAllocatedPowerValueB_Object = MibTableColumn
arubaWiredLldpXdot3RemPSEAllocatedPowerValueB = _ArubaWiredLldpXdot3RemPSEAllocatedPowerValueB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 15),
    _ArubaWiredLldpXdot3RemPSEAllocatedPowerValueB_Type()
)
arubaWiredLldpXdot3RemPSEAllocatedPowerValueB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPSEAllocatedPowerValueB.setStatus("current")


class _ArubaWiredLldpXdot3RemPDPoweredStatus_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPDPoweredStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("singlesigPD", 1),
          ("twoPdualsigPD", 2),
          ("fourPdualsigPD", 3))
    )


_ArubaWiredLldpXdot3RemPDPoweredStatus_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPDPoweredStatus_Object = MibTableColumn
arubaWiredLldpXdot3RemPDPoweredStatus = _ArubaWiredLldpXdot3RemPDPoweredStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 16),
    _ArubaWiredLldpXdot3RemPDPoweredStatus_Type()
)
arubaWiredLldpXdot3RemPDPoweredStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPDPoweredStatus.setStatus("current")


class _ArubaWiredLldpXdot3RemPowerClassExtA_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPowerClassExtA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("singlesig", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6))
    )


_ArubaWiredLldpXdot3RemPowerClassExtA_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPowerClassExtA_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerClassExtA = _ArubaWiredLldpXdot3RemPowerClassExtA_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 17),
    _ArubaWiredLldpXdot3RemPowerClassExtA_Type()
)
arubaWiredLldpXdot3RemPowerClassExtA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerClassExtA.setStatus("current")


class _ArubaWiredLldpXdot3RemPowerClassExtB_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPowerClassExtB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("singlesig", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6))
    )


_ArubaWiredLldpXdot3RemPowerClassExtB_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPowerClassExtB_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerClassExtB = _ArubaWiredLldpXdot3RemPowerClassExtB_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 18),
    _ArubaWiredLldpXdot3RemPowerClassExtB_Type()
)
arubaWiredLldpXdot3RemPowerClassExtB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerClassExtB.setStatus("current")


class _ArubaWiredLldpXdot3RemPowerClassExt_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPowerClassExt based on Integer32"""
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
        *(("dualsig", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6),
          ("class6", 7),
          ("class7", 8),
          ("class8", 9))
    )


_ArubaWiredLldpXdot3RemPowerClassExt_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPowerClassExt_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerClassExt = _ArubaWiredLldpXdot3RemPowerClassExt_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 19),
    _ArubaWiredLldpXdot3RemPowerClassExt_Type()
)
arubaWiredLldpXdot3RemPowerClassExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerClassExt.setStatus("current")


class _ArubaWiredLldpXdot3RemPowerTypeExt_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPowerTypeExt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("type3PSE", 1),
          ("type4PSE", 2),
          ("type3singlesigPD", 3),
          ("type3dualsigPD", 4),
          ("type4singlesigPD", 5),
          ("type4dualsigPD", 6))
    )


_ArubaWiredLldpXdot3RemPowerTypeExt_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPowerTypeExt_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerTypeExt = _ArubaWiredLldpXdot3RemPowerTypeExt_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 20),
    _ArubaWiredLldpXdot3RemPowerTypeExt_Type()
)
arubaWiredLldpXdot3RemPowerTypeExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerTypeExt.setStatus("current")
_ArubaWiredLldpXdot3RemPDLoad_Type = TruthValue
_ArubaWiredLldpXdot3RemPDLoad_Object = MibTableColumn
arubaWiredLldpXdot3RemPDLoad = _ArubaWiredLldpXdot3RemPDLoad_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 21),
    _ArubaWiredLldpXdot3RemPDLoad_Type()
)
arubaWiredLldpXdot3RemPDLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPDLoad.setStatus("current")
_ArubaWiredLldpXdot3RemPD4PID_Type = TruthValue
_ArubaWiredLldpXdot3RemPD4PID_Object = MibTableColumn
arubaWiredLldpXdot3RemPD4PID = _ArubaWiredLldpXdot3RemPD4PID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 22),
    _ArubaWiredLldpXdot3RemPD4PID_Type()
)
arubaWiredLldpXdot3RemPD4PID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPD4PID.setStatus("current")


class _ArubaWiredLldpXdot3RemPSEMaxAvailPower_Type(Integer32):
    """Custom type arubaWiredLldpXdot3RemPSEMaxAvailPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_ArubaWiredLldpXdot3RemPSEMaxAvailPower_Type.__name__ = "Integer32"
_ArubaWiredLldpXdot3RemPSEMaxAvailPower_Object = MibTableColumn
arubaWiredLldpXdot3RemPSEMaxAvailPower = _ArubaWiredLldpXdot3RemPSEMaxAvailPower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 23),
    _ArubaWiredLldpXdot3RemPSEMaxAvailPower_Type()
)
arubaWiredLldpXdot3RemPSEMaxAvailPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPSEMaxAvailPower.setStatus("current")
_ArubaWiredLldpXdot3RemAutoclassRequest_Type = TruthValue
_ArubaWiredLldpXdot3RemAutoclassRequest_Object = MibTableColumn
arubaWiredLldpXdot3RemAutoclassRequest = _ArubaWiredLldpXdot3RemAutoclassRequest_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 24),
    _ArubaWiredLldpXdot3RemAutoclassRequest_Type()
)
arubaWiredLldpXdot3RemAutoclassRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemAutoclassRequest.setStatus("current")
_ArubaWiredLldpXdot3RemPowerDownRequest_Type = Integer32
_ArubaWiredLldpXdot3RemPowerDownRequest_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerDownRequest = _ArubaWiredLldpXdot3RemPowerDownRequest_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 25),
    _ArubaWiredLldpXdot3RemPowerDownRequest_Type()
)
arubaWiredLldpXdot3RemPowerDownRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerDownRequest.setStatus("current")
_ArubaWiredLldpXdot3RemPowerDownTime_Type = Integer32
_ArubaWiredLldpXdot3RemPowerDownTime_Object = MibTableColumn
arubaWiredLldpXdot3RemPowerDownTime = _ArubaWiredLldpXdot3RemPowerDownTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 1, 2, 1, 1, 26),
    _ArubaWiredLldpXdot3RemPowerDownTime_Type()
)
arubaWiredLldpXdot3RemPowerDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemPowerDownTime.setStatus("current")
_ArubaWiredLldpConformance_ObjectIdentity = ObjectIdentity
arubaWiredLldpConformance = _ArubaWiredLldpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 2)
)
_ArubaWiredLldpCompliances_ObjectIdentity = ObjectIdentity
arubaWiredLldpCompliances = _ArubaWiredLldpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 2, 1)
)
_ArubaWiredLldpGroups_ObjectIdentity = ObjectIdentity
arubaWiredLldpGroups = _ArubaWiredLldpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 2, 2)
)
_ArubaWiredLldpScalarConfig_ObjectIdentity = ObjectIdentity
arubaWiredLldpScalarConfig = _ArubaWiredLldpScalarConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 3)
)


class _ArubaWiredLldpMgmtAddrVlanId_Type(Integer32):
    """Custom type arubaWiredLldpMgmtAddrVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ArubaWiredLldpMgmtAddrVlanId_Type.__name__ = "Integer32"
_ArubaWiredLldpMgmtAddrVlanId_Object = MibScalar
arubaWiredLldpMgmtAddrVlanId = _ArubaWiredLldpMgmtAddrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 3, 1),
    _ArubaWiredLldpMgmtAddrVlanId_Type()
)
arubaWiredLldpMgmtAddrVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLldpMgmtAddrVlanId.setStatus("current")

# Managed Objects groups

arubaWiredLldpXdot3LocSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 2, 2, 1)
)
arubaWiredLldpXdot3LocSysGroup.setObjects(
      *(("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerPortClass"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerMDISupported"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerMDIEnabled"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerPairControlable"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerPairs"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerClass"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerType"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerSource"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerPriority"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPDRequestedPowerValue"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPDRequestedPowerValueA"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPDRequestedPowerValueB"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPSEAllocatedPowerValue"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPSEAllocatedPowerValueA"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPSEAllocatedPowerValueB"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPSEPoweringStatus"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerPairsExt"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerClassExtA"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerClassExtB"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerClassExt"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPowerTypeExt"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPDLoad"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPSEMaxAvailPower"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocPSEAutoclassSupport"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocAutoclassCompleted"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpLocPseTlvSentType"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpLocPdTlvSentType"))
)
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3LocSysGroup.setStatus("current")

arubaWiredLldpXdot3RemSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 2, 2, 2)
)
arubaWiredLldpXdot3RemSysGroup.setObjects(
      *(("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerPortClass"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerMDISupported"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerMDIEnabled"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerPairControlable"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerPairs"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerClass"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerType"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerSource"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerPriority"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPDRequestedPowerValue"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPDRequestedPowerValueA"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPDRequestedPowerValueB"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPSEAllocatedPowerValue"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPSEAllocatedPowerValueA"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPSEAllocatedPowerValueB"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPDPoweredStatus"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerClassExtA"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerClassExtB"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerClassExt"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerTypeExt"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPDLoad"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPD4PID"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPSEMaxAvailPower"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemAutoclassRequest"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerDownRequest"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemPowerDownTime"))
)
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3RemSysGroup.setStatus("current")

arubaWiredLldpScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 2, 2, 3)
)
arubaWiredLldpScalarGroup.setObjects(
    ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpMgmtAddrVlanId")
)
if mibBuilder.loadTexts:
    arubaWiredLldpScalarGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredLldpXdot3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 2, 1, 1)
)
arubaWiredLldpXdot3Compliance.setObjects(
      *(("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3LocSysGroup"),
        ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpXdot3RemSysGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredLldpXdot3Compliance.setStatus(
        "current"
    )

arubaWiredLldpScalarCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9, 2, 1, 2)
)
arubaWiredLldpScalarCompliance.setObjects(
    ("ARUBAWIRED-LLDP-MIB", "arubaWiredLldpScalarGroup")
)
if mibBuilder.loadTexts:
    arubaWiredLldpScalarCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-LLDP-MIB",
    **{"arubaWiredLldpMIB": arubaWiredLldpMIB,
       "arubaWiredLldpXdot3Objects": arubaWiredLldpXdot3Objects,
       "arubaWiredLldpXdot3LocalData": arubaWiredLldpXdot3LocalData,
       "arubaWiredLldpXdot3LocPowerTable": arubaWiredLldpXdot3LocPowerTable,
       "arubaWiredLldpXdot3LocPowerEntry": arubaWiredLldpXdot3LocPowerEntry,
       "arubaWiredLldpXdot3LocPowerPortClass": arubaWiredLldpXdot3LocPowerPortClass,
       "arubaWiredLldpXdot3LocPowerMDISupported": arubaWiredLldpXdot3LocPowerMDISupported,
       "arubaWiredLldpXdot3LocPowerMDIEnabled": arubaWiredLldpXdot3LocPowerMDIEnabled,
       "arubaWiredLldpXdot3LocPowerPairControlable": arubaWiredLldpXdot3LocPowerPairControlable,
       "arubaWiredLldpXdot3LocPowerPairs": arubaWiredLldpXdot3LocPowerPairs,
       "arubaWiredLldpXdot3LocPowerClass": arubaWiredLldpXdot3LocPowerClass,
       "arubaWiredLldpXdot3LocPowerType": arubaWiredLldpXdot3LocPowerType,
       "arubaWiredLldpXdot3LocPowerSource": arubaWiredLldpXdot3LocPowerSource,
       "arubaWiredLldpXdot3LocPowerPriority": arubaWiredLldpXdot3LocPowerPriority,
       "arubaWiredLldpXdot3LocPDRequestedPowerValue": arubaWiredLldpXdot3LocPDRequestedPowerValue,
       "arubaWiredLldpXdot3LocPDRequestedPowerValueA": arubaWiredLldpXdot3LocPDRequestedPowerValueA,
       "arubaWiredLldpXdot3LocPDRequestedPowerValueB": arubaWiredLldpXdot3LocPDRequestedPowerValueB,
       "arubaWiredLldpXdot3LocPSEAllocatedPowerValue": arubaWiredLldpXdot3LocPSEAllocatedPowerValue,
       "arubaWiredLldpXdot3LocPSEAllocatedPowerValueA": arubaWiredLldpXdot3LocPSEAllocatedPowerValueA,
       "arubaWiredLldpXdot3LocPSEAllocatedPowerValueB": arubaWiredLldpXdot3LocPSEAllocatedPowerValueB,
       "arubaWiredLldpXdot3LocPSEPoweringStatus": arubaWiredLldpXdot3LocPSEPoweringStatus,
       "arubaWiredLldpXdot3LocPowerPairsExt": arubaWiredLldpXdot3LocPowerPairsExt,
       "arubaWiredLldpXdot3LocPowerClassExtA": arubaWiredLldpXdot3LocPowerClassExtA,
       "arubaWiredLldpXdot3LocPowerClassExtB": arubaWiredLldpXdot3LocPowerClassExtB,
       "arubaWiredLldpXdot3LocPowerClassExt": arubaWiredLldpXdot3LocPowerClassExt,
       "arubaWiredLldpXdot3LocPowerTypeExt": arubaWiredLldpXdot3LocPowerTypeExt,
       "arubaWiredLldpXdot3LocPDLoad": arubaWiredLldpXdot3LocPDLoad,
       "arubaWiredLldpXdot3LocPSEMaxAvailPower": arubaWiredLldpXdot3LocPSEMaxAvailPower,
       "arubaWiredLldpXdot3LocPSEAutoclassSupport": arubaWiredLldpXdot3LocPSEAutoclassSupport,
       "arubaWiredLldpXdot3LocAutoclassCompleted": arubaWiredLldpXdot3LocAutoclassCompleted,
       "arubaWiredLldpLocPseTlvSentType": arubaWiredLldpLocPseTlvSentType,
       "arubaWiredLldpLocPdTlvSentType": arubaWiredLldpLocPdTlvSentType,
       "arubaWiredLldpXdot3RemoteData": arubaWiredLldpXdot3RemoteData,
       "arubaWiredLldpXdot3RemPowerTable": arubaWiredLldpXdot3RemPowerTable,
       "arubaWiredLldpXdot3RemPowerEntry": arubaWiredLldpXdot3RemPowerEntry,
       "arubaWiredLldpXdot3RemPowerPortClass": arubaWiredLldpXdot3RemPowerPortClass,
       "arubaWiredLldpXdot3RemPowerMDISupported": arubaWiredLldpXdot3RemPowerMDISupported,
       "arubaWiredLldpXdot3RemPowerMDIEnabled": arubaWiredLldpXdot3RemPowerMDIEnabled,
       "arubaWiredLldpXdot3RemPowerPairControlable": arubaWiredLldpXdot3RemPowerPairControlable,
       "arubaWiredLldpXdot3RemPowerPairs": arubaWiredLldpXdot3RemPowerPairs,
       "arubaWiredLldpXdot3RemPowerClass": arubaWiredLldpXdot3RemPowerClass,
       "arubaWiredLldpXdot3RemPowerType": arubaWiredLldpXdot3RemPowerType,
       "arubaWiredLldpXdot3RemPowerSource": arubaWiredLldpXdot3RemPowerSource,
       "arubaWiredLldpXdot3RemPowerPriority": arubaWiredLldpXdot3RemPowerPriority,
       "arubaWiredLldpXdot3RemPDRequestedPowerValue": arubaWiredLldpXdot3RemPDRequestedPowerValue,
       "arubaWiredLldpXdot3RemPDRequestedPowerValueA": arubaWiredLldpXdot3RemPDRequestedPowerValueA,
       "arubaWiredLldpXdot3RemPDRequestedPowerValueB": arubaWiredLldpXdot3RemPDRequestedPowerValueB,
       "arubaWiredLldpXdot3RemPSEAllocatedPowerValue": arubaWiredLldpXdot3RemPSEAllocatedPowerValue,
       "arubaWiredLldpXdot3RemPSEAllocatedPowerValueA": arubaWiredLldpXdot3RemPSEAllocatedPowerValueA,
       "arubaWiredLldpXdot3RemPSEAllocatedPowerValueB": arubaWiredLldpXdot3RemPSEAllocatedPowerValueB,
       "arubaWiredLldpXdot3RemPDPoweredStatus": arubaWiredLldpXdot3RemPDPoweredStatus,
       "arubaWiredLldpXdot3RemPowerClassExtA": arubaWiredLldpXdot3RemPowerClassExtA,
       "arubaWiredLldpXdot3RemPowerClassExtB": arubaWiredLldpXdot3RemPowerClassExtB,
       "arubaWiredLldpXdot3RemPowerClassExt": arubaWiredLldpXdot3RemPowerClassExt,
       "arubaWiredLldpXdot3RemPowerTypeExt": arubaWiredLldpXdot3RemPowerTypeExt,
       "arubaWiredLldpXdot3RemPDLoad": arubaWiredLldpXdot3RemPDLoad,
       "arubaWiredLldpXdot3RemPD4PID": arubaWiredLldpXdot3RemPD4PID,
       "arubaWiredLldpXdot3RemPSEMaxAvailPower": arubaWiredLldpXdot3RemPSEMaxAvailPower,
       "arubaWiredLldpXdot3RemAutoclassRequest": arubaWiredLldpXdot3RemAutoclassRequest,
       "arubaWiredLldpXdot3RemPowerDownRequest": arubaWiredLldpXdot3RemPowerDownRequest,
       "arubaWiredLldpXdot3RemPowerDownTime": arubaWiredLldpXdot3RemPowerDownTime,
       "arubaWiredLldpConformance": arubaWiredLldpConformance,
       "arubaWiredLldpCompliances": arubaWiredLldpCompliances,
       "arubaWiredLldpXdot3Compliance": arubaWiredLldpXdot3Compliance,
       "arubaWiredLldpScalarCompliance": arubaWiredLldpScalarCompliance,
       "arubaWiredLldpGroups": arubaWiredLldpGroups,
       "arubaWiredLldpXdot3LocSysGroup": arubaWiredLldpXdot3LocSysGroup,
       "arubaWiredLldpXdot3RemSysGroup": arubaWiredLldpXdot3RemSysGroup,
       "arubaWiredLldpScalarGroup": arubaWiredLldpScalarGroup,
       "arubaWiredLldpScalarConfig": arubaWiredLldpScalarConfig,
       "arubaWiredLldpMgmtAddrVlanId": arubaWiredLldpMgmtAddrVlanId}
)
