# SNMP MIB module (OPTIX-MISC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\huawei\OPTIX-MISC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:00:01 2025
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

(optixProvisionEqpt,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixProvisionEqpt")

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

optixMisc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39)
)
if mibBuilder.loadTexts:
    optixMisc.setRevisions(
        ("2012-04-24 00:00",
         "2012-04-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OptixMiscGroup_ObjectIdentity = ObjectIdentity
optixMiscGroup = _OptixMiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1)
)


class _OptixFanSpeed_Type(Integer32):
    """Custom type optixFanSpeed based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("mid", 2),
          ("high", 3),
          ("stop", 4),
          ("autolow", 5),
          ("automid", 6),
          ("autohigh", 7),
          ("auto", 9))
    )


_OptixFanSpeed_Type.__name__ = "Integer32"
_OptixFanSpeed_Object = MibScalar
optixFanSpeed = _OptixFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 1),
    _OptixFanSpeed_Type()
)
optixFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixFanSpeed.setStatus("current")
_OptixFanMinDispersion_Type = Unsigned32
_OptixFanMinDispersion_Object = MibScalar
optixFanMinDispersion = _OptixFanMinDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 2),
    _OptixFanMinDispersion_Type()
)
optixFanMinDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixFanMinDispersion.setStatus("current")
_OptixEnvironmentTable_Object = MibTable
optixEnvironmentTable = _OptixEnvironmentTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 3)
)
if mibBuilder.loadTexts:
    optixEnvironmentTable.setStatus("current")
_OptixEnvironmentEntry_Object = MibTableRow
optixEnvironmentEntry = _OptixEnvironmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 3, 1)
)
optixEnvironmentEntry.setIndexNames(
    (0, "OPTIX-MISC-MIB", "optixEnvironmentBdId"),
)
if mibBuilder.loadTexts:
    optixEnvironmentEntry.setStatus("current")
_OptixEnvironmentBdId_Type = Unsigned32
_OptixEnvironmentBdId_Object = MibTableColumn
optixEnvironmentBdId = _OptixEnvironmentBdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 3, 1, 1),
    _OptixEnvironmentBdId_Type()
)
optixEnvironmentBdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixEnvironmentBdId.setStatus("current")


class _OptixRelayControlMode_Type(Integer32):
    """Custom type optixRelayControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pmuauto", 0),
          ("pmumanual", 1))
    )


_OptixRelayControlMode_Type.__name__ = "Integer32"
_OptixRelayControlMode_Object = MibTableColumn
optixRelayControlMode = _OptixRelayControlMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 3, 1, 2),
    _OptixRelayControlMode_Type()
)
optixRelayControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixRelayControlMode.setStatus("current")


class _OptixRelayNormalAlmState_Type(Integer32):
    """Custom type optixRelayNormalAlmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_OptixRelayNormalAlmState_Type.__name__ = "Integer32"
_OptixRelayNormalAlmState_Object = MibTableColumn
optixRelayNormalAlmState = _OptixRelayNormalAlmState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 3, 1, 3),
    _OptixRelayNormalAlmState_Type()
)
optixRelayNormalAlmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixRelayNormalAlmState.setStatus("current")


class _OptixRelaySeriousAlmState_Type(Integer32):
    """Custom type optixRelaySeriousAlmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_OptixRelaySeriousAlmState_Type.__name__ = "Integer32"
_OptixRelaySeriousAlmState_Object = MibTableColumn
optixRelaySeriousAlmState = _OptixRelaySeriousAlmState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 3, 1, 4),
    _OptixRelaySeriousAlmState_Type()
)
optixRelaySeriousAlmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixRelaySeriousAlmState.setStatus("current")
_OptixRelayTable_Object = MibTable
optixRelayTable = _OptixRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4)
)
if mibBuilder.loadTexts:
    optixRelayTable.setStatus("current")
_OptixRelayEntry_Object = MibTableRow
optixRelayEntry = _OptixRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4, 1)
)
optixRelayEntry.setIndexNames(
    (0, "OPTIX-MISC-MIB", "optixEnvironmentBdId"),
    (0, "OPTIX-MISC-MIB", "optixRelayId"),
)
if mibBuilder.loadTexts:
    optixRelayEntry.setStatus("current")
_OptixRelayId_Type = Unsigned32
_OptixRelayId_Object = MibTableColumn
optixRelayId = _OptixRelayId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4, 1, 1),
    _OptixRelayId_Type()
)
optixRelayId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixRelayId.setStatus("current")


class _OptixRelayUseState_Type(Integer32):
    """Custom type optixRelayUseState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OptixRelayUseState_Type.__name__ = "Integer32"
_OptixRelayUseState_Object = MibTableColumn
optixRelayUseState = _OptixRelayUseState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4, 1, 2),
    _OptixRelayUseState_Type()
)
optixRelayUseState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixRelayUseState.setStatus("current")


class _OptixRelayAlmSwitchState_Type(Integer32):
    """Custom type optixRelayAlmSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_OptixRelayAlmSwitchState_Type.__name__ = "Integer32"
_OptixRelayAlmSwitchState_Object = MibTableColumn
optixRelayAlmSwitchState = _OptixRelayAlmSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4, 1, 3),
    _OptixRelayAlmSwitchState_Type()
)
optixRelayAlmSwitchState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixRelayAlmSwitchState.setStatus("current")


class _OptixRelayAlmLevel_Type(Integer32):
    """Custom type optixRelayAlmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("major", 1),
          ("minor", 2),
          ("ignore", 3))
    )


_OptixRelayAlmLevel_Type.__name__ = "Integer32"
_OptixRelayAlmLevel_Object = MibTableColumn
optixRelayAlmLevel = _OptixRelayAlmLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4, 1, 4),
    _OptixRelayAlmLevel_Type()
)
optixRelayAlmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixRelayAlmLevel.setStatus("current")


class _OptixRelayOutState_Type(Integer32):
    """Custom type optixRelayOutState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_OptixRelayOutState_Type.__name__ = "Integer32"
_OptixRelayOutState_Object = MibTableColumn
optixRelayOutState = _OptixRelayOutState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4, 1, 5),
    _OptixRelayOutState_Type()
)
optixRelayOutState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixRelayOutState.setStatus("current")
_OptixAlmOutputTable_Object = MibTable
optixAlmOutputTable = _OptixAlmOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 5)
)
if mibBuilder.loadTexts:
    optixAlmOutputTable.setStatus("current")
_OptixAlmOutputEntry_Object = MibTableRow
optixAlmOutputEntry = _OptixAlmOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 5, 1)
)
optixAlmOutputEntry.setIndexNames(
    (0, "OPTIX-MISC-MIB", "optixEnvironmentBdId"),
    (0, "OPTIX-MISC-MIB", "optixAlmOutputLevel"),
)
if mibBuilder.loadTexts:
    optixAlmOutputEntry.setStatus("current")


class _OptixAlmOutputLevel_Type(Integer32):
    """Custom type optixAlmOutputLevel based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("ignore", 4))
    )


_OptixAlmOutputLevel_Type.__name__ = "Integer32"
_OptixAlmOutputLevel_Object = MibTableColumn
optixAlmOutputLevel = _OptixAlmOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 5, 1, 1),
    _OptixAlmOutputLevel_Type()
)
optixAlmOutputLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixAlmOutputLevel.setStatus("current")
_OptixAlmOutputNum_Type = Unsigned32
_OptixAlmOutputNum_Object = MibTableColumn
optixAlmOutputNum = _OptixAlmOutputNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 5, 1, 2),
    _OptixAlmOutputNum_Type()
)
optixAlmOutputNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixAlmOutputNum.setStatus("current")
_OptixRelayNameTable_Object = MibTable
optixRelayNameTable = _OptixRelayNameTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 6)
)
if mibBuilder.loadTexts:
    optixRelayNameTable.setStatus("current")
_OptixRelayNameEntry_Object = MibTableRow
optixRelayNameEntry = _OptixRelayNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 6, 1)
)
optixRelayNameEntry.setIndexNames(
    (0, "OPTIX-MISC-MIB", "optixEnvironmentBdId"),
    (0, "OPTIX-MISC-MIB", "optixRelayId"),
    (0, "OPTIX-MISC-MIB", "optixRelayType"),
)
if mibBuilder.loadTexts:
    optixRelayNameEntry.setStatus("current")


class _OptixRelayType_Type(Integer32):
    """Custom type optixRelayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("input", 1),
          ("ext", 2))
    )


_OptixRelayType_Type.__name__ = "Integer32"
_OptixRelayType_Object = MibTableColumn
optixRelayType = _OptixRelayType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 6, 1, 1),
    _OptixRelayType_Type()
)
optixRelayType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixRelayType.setStatus("current")


class _OptixRelayName_Type(OctetString):
    """Custom type optixRelayName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_OptixRelayName_Type.__name__ = "OctetString"
_OptixRelayName_Object = MibTableColumn
optixRelayName = _OptixRelayName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 6, 1, 2),
    _OptixRelayName_Type()
)
optixRelayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixRelayName.setStatus("current")
_OptixOamPortMngTable_Object = MibTable
optixOamPortMngTable = _OptixOamPortMngTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7)
)
if mibBuilder.loadTexts:
    optixOamPortMngTable.setStatus("current")
_OptixOamPortMngEntry_Object = MibTableRow
optixOamPortMngEntry = _OptixOamPortMngEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7, 1)
)
optixOamPortMngEntry.setIndexNames(
    (0, "OPTIX-MISC-MIB", "optixOamBdId"),
    (0, "OPTIX-MISC-MIB", "optixOamSubBdId"),
    (0, "OPTIX-MISC-MIB", "optixOamPortId"),
)
if mibBuilder.loadTexts:
    optixOamPortMngEntry.setStatus("current")
_OptixOamBdId_Type = Unsigned32
_OptixOamBdId_Object = MibTableColumn
optixOamBdId = _OptixOamBdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7, 1, 1),
    _OptixOamBdId_Type()
)
optixOamBdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixOamBdId.setStatus("current")
_OptixOamSubBdId_Type = Unsigned32
_OptixOamSubBdId_Object = MibTableColumn
optixOamSubBdId = _OptixOamSubBdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7, 1, 2),
    _OptixOamSubBdId_Type()
)
optixOamSubBdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixOamSubBdId.setStatus("current")
_OptixOamPortId_Type = Unsigned32
_OptixOamPortId_Object = MibTableColumn
optixOamPortId = _OptixOamPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7, 1, 3),
    _OptixOamPortId_Type()
)
optixOamPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixOamPortId.setStatus("current")


class _OptixOamPortType_Type(Integer32):
    """Custom type optixOamPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("com", 1),
          ("eth", 2),
          ("oam", 3),
          ("fF", 4),
          ("ext", 5),
          ("usb", 6))
    )


_OptixOamPortType_Type.__name__ = "Integer32"
_OptixOamPortType_Object = MibTableColumn
optixOamPortType = _OptixOamPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7, 1, 4),
    _OptixOamPortType_Type()
)
optixOamPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixOamPortType.setStatus("current")


class _OptixOamPortState_Type(Integer32):
    """Custom type optixOamPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_OptixOamPortState_Type.__name__ = "Integer32"
_OptixOamPortState_Object = MibTableColumn
optixOamPortState = _OptixOamPortState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7, 1, 5),
    _OptixOamPortState_Type()
)
optixOamPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixOamPortState.setStatus("current")
_OptixCommuMngTable_Object = MibTable
optixCommuMngTable = _OptixCommuMngTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8)
)
if mibBuilder.loadTexts:
    optixCommuMngTable.setStatus("current")
_OptixCommuMngEntry_Object = MibTableRow
optixCommuMngEntry = _OptixCommuMngEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1)
)
optixCommuMngEntry.setIndexNames(
    (0, "OPTIX-MISC-MIB", "optixCommuBdId"),
    (0, "OPTIX-MISC-MIB", "optixCommuSubBdId"),
    (0, "OPTIX-MISC-MIB", "optixCommuPortId"),
)
if mibBuilder.loadTexts:
    optixCommuMngEntry.setStatus("current")
_OptixCommuBdId_Type = Unsigned32
_OptixCommuBdId_Object = MibTableColumn
optixCommuBdId = _OptixCommuBdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 1),
    _OptixCommuBdId_Type()
)
optixCommuBdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixCommuBdId.setStatus("current")
_OptixCommuSubBdId_Type = Unsigned32
_OptixCommuSubBdId_Object = MibTableColumn
optixCommuSubBdId = _OptixCommuSubBdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 2),
    _OptixCommuSubBdId_Type()
)
optixCommuSubBdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixCommuSubBdId.setStatus("current")
_OptixCommuPortId_Type = Unsigned32
_OptixCommuPortId_Object = MibTableColumn
optixCommuPortId = _OptixCommuPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 3),
    _OptixCommuPortId_Type()
)
optixCommuPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixCommuPortId.setStatus("current")


class _OptixEthPortAdaptMode_Type(Integer32):
    """Custom type optixEthPortAdaptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("adapt", 1))
    )


_OptixEthPortAdaptMode_Type.__name__ = "Integer32"
_OptixEthPortAdaptMode_Object = MibTableColumn
optixEthPortAdaptMode = _OptixEthPortAdaptMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 4),
    _OptixEthPortAdaptMode_Type()
)
optixEthPortAdaptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixEthPortAdaptMode.setStatus("current")


class _OptixEthPortAdaptSpeed_Type(Integer32):
    """Custom type optixEthPortAdaptSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("snmp10m", 0),
          ("snmp100m", 1),
          ("commufail", 254),
          ("inautonego", 255))
    )


_OptixEthPortAdaptSpeed_Type.__name__ = "Integer32"
_OptixEthPortAdaptSpeed_Object = MibTableColumn
optixEthPortAdaptSpeed = _OptixEthPortAdaptSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 5),
    _OptixEthPortAdaptSpeed_Type()
)
optixEthPortAdaptSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixEthPortAdaptSpeed.setStatus("current")


class _OptixEthPortAdaptDuplex_Type(Integer32):
    """Custom type optixEthPortAdaptDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("half", 0),
          ("full", 1),
          ("commufail", 254),
          ("inautonego", 255))
    )


_OptixEthPortAdaptDuplex_Type.__name__ = "Integer32"
_OptixEthPortAdaptDuplex_Object = MibTableColumn
optixEthPortAdaptDuplex = _OptixEthPortAdaptDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 6),
    _OptixEthPortAdaptDuplex_Type()
)
optixEthPortAdaptDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixEthPortAdaptDuplex.setStatus("current")


class _OptixCommuRealMode_Type(Integer32):
    """Custom type optixCommuRealMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("adapt", 1))
    )


_OptixCommuRealMode_Type.__name__ = "Integer32"
_OptixCommuRealMode_Object = MibTableColumn
optixCommuRealMode = _OptixCommuRealMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 7),
    _OptixCommuRealMode_Type()
)
optixCommuRealMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixCommuRealMode.setStatus("current")


class _OptixCommuRealSpeed_Type(Integer32):
    """Custom type optixCommuRealSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("snmp10m", 0),
          ("snmp100m", 1),
          ("commufail", 254),
          ("inautonego", 255))
    )


_OptixCommuRealSpeed_Type.__name__ = "Integer32"
_OptixCommuRealSpeed_Object = MibTableColumn
optixCommuRealSpeed = _OptixCommuRealSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 8),
    _OptixCommuRealSpeed_Type()
)
optixCommuRealSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixCommuRealSpeed.setStatus("current")


class _OptixCommuRealDuplex_Type(Integer32):
    """Custom type optixCommuRealDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("half", 0),
          ("full", 1),
          ("commufail", 254),
          ("inautonego", 255))
    )


_OptixCommuRealDuplex_Type.__name__ = "Integer32"
_OptixCommuRealDuplex_Object = MibTableColumn
optixCommuRealDuplex = _OptixCommuRealDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 9),
    _OptixCommuRealDuplex_Type()
)
optixCommuRealDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixCommuRealDuplex.setStatus("current")
_OptixPowerMonstateTable_Object = MibTable
optixPowerMonstateTable = _OptixPowerMonstateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 9)
)
if mibBuilder.loadTexts:
    optixPowerMonstateTable.setStatus("current")
_OptixPowerMonstateEntry_Object = MibTableRow
optixPowerMonstateEntry = _OptixPowerMonstateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 9, 1)
)
optixPowerMonstateEntry.setIndexNames(
    (0, "OPTIX-MISC-MIB", "optixPowerMonstateSlotId"),
    (0, "OPTIX-MISC-MIB", "optixPowerMonstatePort"),
)
if mibBuilder.loadTexts:
    optixPowerMonstateEntry.setStatus("current")


class _OptixPowerMonstateSlotId_Type(Unsigned32):
    """Custom type optixPowerMonstateSlotId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_OptixPowerMonstateSlotId_Type.__name__ = "Unsigned32"
_OptixPowerMonstateSlotId_Object = MibTableColumn
optixPowerMonstateSlotId = _OptixPowerMonstateSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 9, 1, 1),
    _OptixPowerMonstateSlotId_Type()
)
optixPowerMonstateSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixPowerMonstateSlotId.setStatus("current")


class _OptixPowerMonstatePort_Type(Unsigned32):
    """Custom type optixPowerMonstatePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_OptixPowerMonstatePort_Type.__name__ = "Unsigned32"
_OptixPowerMonstatePort_Object = MibTableColumn
optixPowerMonstatePort = _OptixPowerMonstatePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 9, 1, 2),
    _OptixPowerMonstatePort_Type()
)
optixPowerMonstatePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optixPowerMonstatePort.setStatus("current")


class _OptixPowerMonstateState_Type(Integer32):
    """Custom type optixPowerMonstateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OptixPowerMonstateState_Type.__name__ = "Integer32"
_OptixPowerMonstateState_Object = MibTableColumn
optixPowerMonstateState = _OptixPowerMonstateState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 9, 1, 3),
    _OptixPowerMonstateState_Type()
)
optixPowerMonstateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixPowerMonstateState.setStatus("current")
_OptixMiscextGroup_ObjectIdentity = ObjectIdentity
optixMiscextGroup = _OptixMiscextGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 2)
)


class _OptixFanSpeedext_Type(OctetString):
    """Custom type optixFanSpeedext based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OptixFanSpeedext_Type.__name__ = "OctetString"
_OptixFanSpeedext_Object = MibScalar
optixFanSpeedext = _OptixFanSpeedext_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 2, 1),
    _OptixFanSpeedext_Type()
)
optixFanSpeedext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optixFanSpeedext.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-MISC-MIB",
    **{"optixMisc": optixMisc,
       "optixMiscGroup": optixMiscGroup,
       "optixFanSpeed": optixFanSpeed,
       "optixFanMinDispersion": optixFanMinDispersion,
       "optixEnvironmentTable": optixEnvironmentTable,
       "optixEnvironmentEntry": optixEnvironmentEntry,
       "optixEnvironmentBdId": optixEnvironmentBdId,
       "optixRelayControlMode": optixRelayControlMode,
       "optixRelayNormalAlmState": optixRelayNormalAlmState,
       "optixRelaySeriousAlmState": optixRelaySeriousAlmState,
       "optixRelayTable": optixRelayTable,
       "optixRelayEntry": optixRelayEntry,
       "optixRelayId": optixRelayId,
       "optixRelayUseState": optixRelayUseState,
       "optixRelayAlmSwitchState": optixRelayAlmSwitchState,
       "optixRelayAlmLevel": optixRelayAlmLevel,
       "optixRelayOutState": optixRelayOutState,
       "optixAlmOutputTable": optixAlmOutputTable,
       "optixAlmOutputEntry": optixAlmOutputEntry,
       "optixAlmOutputLevel": optixAlmOutputLevel,
       "optixAlmOutputNum": optixAlmOutputNum,
       "optixRelayNameTable": optixRelayNameTable,
       "optixRelayNameEntry": optixRelayNameEntry,
       "optixRelayType": optixRelayType,
       "optixRelayName": optixRelayName,
       "optixOamPortMngTable": optixOamPortMngTable,
       "optixOamPortMngEntry": optixOamPortMngEntry,
       "optixOamBdId": optixOamBdId,
       "optixOamSubBdId": optixOamSubBdId,
       "optixOamPortId": optixOamPortId,
       "optixOamPortType": optixOamPortType,
       "optixOamPortState": optixOamPortState,
       "optixCommuMngTable": optixCommuMngTable,
       "optixCommuMngEntry": optixCommuMngEntry,
       "optixCommuBdId": optixCommuBdId,
       "optixCommuSubBdId": optixCommuSubBdId,
       "optixCommuPortId": optixCommuPortId,
       "optixEthPortAdaptMode": optixEthPortAdaptMode,
       "optixEthPortAdaptSpeed": optixEthPortAdaptSpeed,
       "optixEthPortAdaptDuplex": optixEthPortAdaptDuplex,
       "optixCommuRealMode": optixCommuRealMode,
       "optixCommuRealSpeed": optixCommuRealSpeed,
       "optixCommuRealDuplex": optixCommuRealDuplex,
       "optixPowerMonstateTable": optixPowerMonstateTable,
       "optixPowerMonstateEntry": optixPowerMonstateEntry,
       "optixPowerMonstateSlotId": optixPowerMonstateSlotId,
       "optixPowerMonstatePort": optixPowerMonstatePort,
       "optixPowerMonstateState": optixPowerMonstateState,
       "optixMiscextGroup": optixMiscextGroup,
       "optixFanSpeedext": optixFanSpeedext}
)
