# SNMP MIB module (ARUBAWIRED-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-PM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:19 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

arubaWiredPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27)
)
if mibBuilder.loadTexts:
    arubaWiredPmMIB.setRevisions(
        ("2024-11-19 00:00",
         "2024-01-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredPmNotificatons_ObjectIdentity = ObjectIdentity
arubaWiredPmNotificatons = _ArubaWiredPmNotificatons_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 0)
)
_ArubaWiredPmObjects_ObjectIdentity = ObjectIdentity
arubaWiredPmObjects = _ArubaWiredPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1)
)
_ArubaWiredPmXcvrInfo_ObjectIdentity = ObjectIdentity
arubaWiredPmXcvrInfo = _ArubaWiredPmXcvrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1)
)
_ArubaWiredPmXcvrTable_Object = MibTable
arubaWiredPmXcvrTable = _ArubaWiredPmXcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPmXcvrTable.setStatus("current")
_ArubaWiredPmXcvrEntry_Object = MibTableRow
arubaWiredPmXcvrEntry = _ArubaWiredPmXcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1)
)
arubaWiredPmXcvrEntry.setIndexNames(
    (0, "ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrPortIfIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredPmXcvrEntry.setStatus("current")
_ArubaWiredPmXcvrPortIfIndex_Type = InterfaceIndex
_ArubaWiredPmXcvrPortIfIndex_Object = MibTableColumn
arubaWiredPmXcvrPortIfIndex = _ArubaWiredPmXcvrPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 1),
    _ArubaWiredPmXcvrPortIfIndex_Type()
)
arubaWiredPmXcvrPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrPortIfIndex.setStatus("current")


class _ArubaWiredPmXcvrPortDesc_Type(DisplayString):
    """Custom type arubaWiredPmXcvrPortDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPmXcvrPortDesc_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrPortDesc_Object = MibTableColumn
arubaWiredPmXcvrPortDesc = _ArubaWiredPmXcvrPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 2),
    _ArubaWiredPmXcvrPortDesc_Type()
)
arubaWiredPmXcvrPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrPortDesc.setStatus("current")


class _ArubaWiredPmXcvrDescription_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArubaWiredPmXcvrDescription_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDescription_Object = MibTableColumn
arubaWiredPmXcvrDescription = _ArubaWiredPmXcvrDescription_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 3),
    _ArubaWiredPmXcvrDescription_Type()
)
arubaWiredPmXcvrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDescription.setStatus("current")


class _ArubaWiredPmXcvrProductNum_Type(DisplayString):
    """Custom type arubaWiredPmXcvrProductNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPmXcvrProductNum_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrProductNum_Object = MibTableColumn
arubaWiredPmXcvrProductNum = _ArubaWiredPmXcvrProductNum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 4),
    _ArubaWiredPmXcvrProductNum_Type()
)
arubaWiredPmXcvrProductNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrProductNum.setStatus("current")


class _ArubaWiredPmXcvrSerialNum_Type(DisplayString):
    """Custom type arubaWiredPmXcvrSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPmXcvrSerialNum_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrSerialNum_Object = MibTableColumn
arubaWiredPmXcvrSerialNum = _ArubaWiredPmXcvrSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 5),
    _ArubaWiredPmXcvrSerialNum_Type()
)
arubaWiredPmXcvrSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrSerialNum.setStatus("current")


class _ArubaWiredPmXcvrPartNum_Type(DisplayString):
    """Custom type arubaWiredPmXcvrPartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPmXcvrPartNum_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrPartNum_Object = MibTableColumn
arubaWiredPmXcvrPartNum = _ArubaWiredPmXcvrPartNum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 6),
    _ArubaWiredPmXcvrPartNum_Type()
)
arubaWiredPmXcvrPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrPartNum.setStatus("current")


class _ArubaWiredPmXcvrType_Type(DisplayString):
    """Custom type arubaWiredPmXcvrType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPmXcvrType_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrType_Object = MibTableColumn
arubaWiredPmXcvrType = _ArubaWiredPmXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 7),
    _ArubaWiredPmXcvrType_Type()
)
arubaWiredPmXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrType.setStatus("current")


class _ArubaWiredPmXcvrConnectorType_Type(DisplayString):
    """Custom type arubaWiredPmXcvrConnectorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPmXcvrConnectorType_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrConnectorType_Object = MibTableColumn
arubaWiredPmXcvrConnectorType = _ArubaWiredPmXcvrConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 8),
    _ArubaWiredPmXcvrConnectorType_Type()
)
arubaWiredPmXcvrConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrConnectorType.setStatus("current")


class _ArubaWiredPmXcvrConnectorStatus_Type(Integer32):
    """Custom type arubaWiredPmXcvrConnectorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("incompatible", 0),
          ("supported", 1),
          ("unrecognized", 2),
          ("unsupported", 3),
          ("unsupportedAllowed", 4))
    )


_ArubaWiredPmXcvrConnectorStatus_Type.__name__ = "Integer32"
_ArubaWiredPmXcvrConnectorStatus_Object = MibTableColumn
arubaWiredPmXcvrConnectorStatus = _ArubaWiredPmXcvrConnectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 9),
    _ArubaWiredPmXcvrConnectorStatus_Type()
)
arubaWiredPmXcvrConnectorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrConnectorStatus.setStatus("current")


class _ArubaWiredPmXcvrConnectorStatusReason_Type(DisplayString):
    """Custom type arubaWiredPmXcvrConnectorStatusReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArubaWiredPmXcvrConnectorStatusReason_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrConnectorStatusReason_Object = MibTableColumn
arubaWiredPmXcvrConnectorStatusReason = _ArubaWiredPmXcvrConnectorStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 10),
    _ArubaWiredPmXcvrConnectorStatusReason_Type()
)
arubaWiredPmXcvrConnectorStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrConnectorStatusReason.setStatus("current")


class _ArubaWiredPmXcvrCableType_Type(DisplayString):
    """Custom type arubaWiredPmXcvrCableType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPmXcvrCableType_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrCableType_Object = MibTableColumn
arubaWiredPmXcvrCableType = _ArubaWiredPmXcvrCableType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 11),
    _ArubaWiredPmXcvrCableType_Type()
)
arubaWiredPmXcvrCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrCableType.setStatus("current")


class _ArubaWiredPmXcvrWavelength_Type(Unsigned32):
    """Custom type arubaWiredPmXcvrWavelength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ArubaWiredPmXcvrWavelength_Type.__name__ = "Unsigned32"
_ArubaWiredPmXcvrWavelength_Object = MibTableColumn
arubaWiredPmXcvrWavelength = _ArubaWiredPmXcvrWavelength_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 12),
    _ArubaWiredPmXcvrWavelength_Type()
)
arubaWiredPmXcvrWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrWavelength.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrWavelength.setUnits("nm")


class _ArubaWiredPmXcvrSmfTxDist_Type(Unsigned32):
    """Custom type arubaWiredPmXcvrSmfTxDist based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ArubaWiredPmXcvrSmfTxDist_Type.__name__ = "Unsigned32"
_ArubaWiredPmXcvrSmfTxDist_Object = MibTableColumn
arubaWiredPmXcvrSmfTxDist = _ArubaWiredPmXcvrSmfTxDist_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 13),
    _ArubaWiredPmXcvrSmfTxDist_Type()
)
arubaWiredPmXcvrSmfTxDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrSmfTxDist.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrSmfTxDist.setUnits("km")


class _ArubaWiredPmXcvrMmfOm1TxDist_Type(Unsigned32):
    """Custom type arubaWiredPmXcvrMmfOm1TxDist based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ArubaWiredPmXcvrMmfOm1TxDist_Type.__name__ = "Unsigned32"
_ArubaWiredPmXcvrMmfOm1TxDist_Object = MibTableColumn
arubaWiredPmXcvrMmfOm1TxDist = _ArubaWiredPmXcvrMmfOm1TxDist_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 14),
    _ArubaWiredPmXcvrMmfOm1TxDist_Type()
)
arubaWiredPmXcvrMmfOm1TxDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMmfOm1TxDist.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMmfOm1TxDist.setUnits("m")


class _ArubaWiredPmXcvrMmfOm2TxDist_Type(Unsigned32):
    """Custom type arubaWiredPmXcvrMmfOm2TxDist based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ArubaWiredPmXcvrMmfOm2TxDist_Type.__name__ = "Unsigned32"
_ArubaWiredPmXcvrMmfOm2TxDist_Object = MibTableColumn
arubaWiredPmXcvrMmfOm2TxDist = _ArubaWiredPmXcvrMmfOm2TxDist_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 15),
    _ArubaWiredPmXcvrMmfOm2TxDist_Type()
)
arubaWiredPmXcvrMmfOm2TxDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMmfOm2TxDist.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMmfOm2TxDist.setUnits("m")


class _ArubaWiredPmXcvrMmfOm3TxDist_Type(Unsigned32):
    """Custom type arubaWiredPmXcvrMmfOm3TxDist based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ArubaWiredPmXcvrMmfOm3TxDist_Type.__name__ = "Unsigned32"
_ArubaWiredPmXcvrMmfOm3TxDist_Object = MibTableColumn
arubaWiredPmXcvrMmfOm3TxDist = _ArubaWiredPmXcvrMmfOm3TxDist_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 16),
    _ArubaWiredPmXcvrMmfOm3TxDist_Type()
)
arubaWiredPmXcvrMmfOm3TxDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMmfOm3TxDist.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMmfOm3TxDist.setUnits("m")


class _ArubaWiredPmXcvrMmfOm4TxDist_Type(Unsigned32):
    """Custom type arubaWiredPmXcvrMmfOm4TxDist based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ArubaWiredPmXcvrMmfOm4TxDist_Type.__name__ = "Unsigned32"
_ArubaWiredPmXcvrMmfOm4TxDist_Object = MibTableColumn
arubaWiredPmXcvrMmfOm4TxDist = _ArubaWiredPmXcvrMmfOm4TxDist_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 17),
    _ArubaWiredPmXcvrMmfOm4TxDist_Type()
)
arubaWiredPmXcvrMmfOm4TxDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMmfOm4TxDist.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMmfOm4TxDist.setUnits("m")


class _ArubaWiredPmXcvrMmfOm5TxDist_Type(Unsigned32):
    """Custom type arubaWiredPmXcvrMmfOm5TxDist based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ArubaWiredPmXcvrMmfOm5TxDist_Type.__name__ = "Unsigned32"
_ArubaWiredPmXcvrMmfOm5TxDist_Object = MibTableColumn
arubaWiredPmXcvrMmfOm5TxDist = _ArubaWiredPmXcvrMmfOm5TxDist_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 18),
    _ArubaWiredPmXcvrMmfOm5TxDist_Type()
)
arubaWiredPmXcvrMmfOm5TxDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMmfOm5TxDist.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMmfOm5TxDist.setUnits("m")


class _ArubaWiredPmXcvrCableLength_Type(Unsigned32):
    """Custom type arubaWiredPmXcvrCableLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ArubaWiredPmXcvrCableLength_Type.__name__ = "Unsigned32"
_ArubaWiredPmXcvrCableLength_Object = MibTableColumn
arubaWiredPmXcvrCableLength = _ArubaWiredPmXcvrCableLength_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 19),
    _ArubaWiredPmXcvrCableLength_Type()
)
arubaWiredPmXcvrCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrCableLength.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrCableLength.setUnits("m")


class _ArubaWiredPmXcvrMaxSpeed_Type(Unsigned32):
    """Custom type arubaWiredPmXcvrMaxSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_ArubaWiredPmXcvrMaxSpeed_Type.__name__ = "Unsigned32"
_ArubaWiredPmXcvrMaxSpeed_Object = MibTableColumn
arubaWiredPmXcvrMaxSpeed = _ArubaWiredPmXcvrMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 20),
    _ArubaWiredPmXcvrMaxSpeed_Type()
)
arubaWiredPmXcvrMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMaxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMaxSpeed.setUnits("Mbps")


class _ArubaWiredPmXcvrMaxPower_Type(Unsigned32):
    """Custom type arubaWiredPmXcvrMaxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_ArubaWiredPmXcvrMaxPower_Type.__name__ = "Unsigned32"
_ArubaWiredPmXcvrMaxPower_Object = MibTableColumn
arubaWiredPmXcvrMaxPower = _ArubaWiredPmXcvrMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 21),
    _ArubaWiredPmXcvrMaxPower_Type()
)
arubaWiredPmXcvrMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrMaxPower.setUnits("mW")


class _ArubaWiredPmXcvrAdapterType_Type(DisplayString):
    """Custom type arubaWiredPmXcvrAdapterType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPmXcvrAdapterType_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrAdapterType_Object = MibTableColumn
arubaWiredPmXcvrAdapterType = _ArubaWiredPmXcvrAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 22),
    _ArubaWiredPmXcvrAdapterType_Type()
)
arubaWiredPmXcvrAdapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrAdapterType.setStatus("current")


class _ArubaWiredPmXcvrAdapterStatus_Type(Integer32):
    """Custom type arubaWiredPmXcvrAdapterStatus based on Integer32"""
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
        *(("incompatible", 0),
          ("supported", 1),
          ("unrecognized", 2),
          ("unsupported", 3))
    )


_ArubaWiredPmXcvrAdapterStatus_Type.__name__ = "Integer32"
_ArubaWiredPmXcvrAdapterStatus_Object = MibTableColumn
arubaWiredPmXcvrAdapterStatus = _ArubaWiredPmXcvrAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 23),
    _ArubaWiredPmXcvrAdapterStatus_Type()
)
arubaWiredPmXcvrAdapterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrAdapterStatus.setStatus("current")


class _ArubaWiredPmXcvrAdapterStatusReason_Type(DisplayString):
    """Custom type arubaWiredPmXcvrAdapterStatusReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArubaWiredPmXcvrAdapterStatusReason_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrAdapterStatusReason_Object = MibTableColumn
arubaWiredPmXcvrAdapterStatusReason = _ArubaWiredPmXcvrAdapterStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 24),
    _ArubaWiredPmXcvrAdapterStatusReason_Type()
)
arubaWiredPmXcvrAdapterStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrAdapterStatusReason.setStatus("current")


class _ArubaWiredPmXcvrAdapterProductNum_Type(DisplayString):
    """Custom type arubaWiredPmXcvrAdapterProductNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPmXcvrAdapterProductNum_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrAdapterProductNum_Object = MibTableColumn
arubaWiredPmXcvrAdapterProductNum = _ArubaWiredPmXcvrAdapterProductNum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 25),
    _ArubaWiredPmXcvrAdapterProductNum_Type()
)
arubaWiredPmXcvrAdapterProductNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrAdapterProductNum.setStatus("current")


class _ArubaWiredPmXcvrAdapterSerialNum_Type(DisplayString):
    """Custom type arubaWiredPmXcvrAdapterSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPmXcvrAdapterSerialNum_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrAdapterSerialNum_Object = MibTableColumn
arubaWiredPmXcvrAdapterSerialNum = _ArubaWiredPmXcvrAdapterSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 26),
    _ArubaWiredPmXcvrAdapterSerialNum_Type()
)
arubaWiredPmXcvrAdapterSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrAdapterSerialNum.setStatus("current")


class _ArubaWiredPmXcvrThermalClass_Type(DisplayString):
    """Custom type arubaWiredPmXcvrThermalClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArubaWiredPmXcvrThermalClass_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrThermalClass_Object = MibTableColumn
arubaWiredPmXcvrThermalClass = _ArubaWiredPmXcvrThermalClass_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 27),
    _ArubaWiredPmXcvrThermalClass_Type()
)
arubaWiredPmXcvrThermalClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrThermalClass.setStatus("current")
_ArubaWiredPmXcvrDiagnostics_Type = TruthValue
_ArubaWiredPmXcvrDiagnostics_Object = MibTableColumn
arubaWiredPmXcvrDiagnostics = _ArubaWiredPmXcvrDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 1, 1, 1, 28),
    _ArubaWiredPmXcvrDiagnostics_Type()
)
arubaWiredPmXcvrDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDiagnostics.setStatus("current")
_ArubaWiredPmXcvrDomInfo_ObjectIdentity = ObjectIdentity
arubaWiredPmXcvrDomInfo = _ArubaWiredPmXcvrDomInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2)
)
_ArubaWiredPmXcvrDomTable_Object = MibTable
arubaWiredPmXcvrDomTable = _ArubaWiredPmXcvrDomTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTable.setStatus("current")
_ArubaWiredPmXcvrDomEntry_Object = MibTableRow
arubaWiredPmXcvrDomEntry = _ArubaWiredPmXcvrDomEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1)
)
arubaWiredPmXcvrDomEntry.setIndexNames(
    (0, "ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrPortIfIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomEntry.setStatus("current")


class _ArubaWiredPmXcvrDomPortDesc_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomPortDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredPmXcvrDomPortDesc_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomPortDesc_Object = MibTableColumn
arubaWiredPmXcvrDomPortDesc = _ArubaWiredPmXcvrDomPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 1),
    _ArubaWiredPmXcvrDomPortDesc_Type()
)
arubaWiredPmXcvrDomPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomPortDesc.setStatus("current")


class _ArubaWiredPmXcvrDomTemp_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTemp_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTemp_Object = MibTableColumn
arubaWiredPmXcvrDomTemp = _ArubaWiredPmXcvrDomTemp_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 2),
    _ArubaWiredPmXcvrDomTemp_Type()
)
arubaWiredPmXcvrDomTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTemp.setStatus("current")


class _ArubaWiredPmXcvrDomTempHiAlarmThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTempHiAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTempHiAlarmThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTempHiAlarmThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomTempHiAlarmThreshold = _ArubaWiredPmXcvrDomTempHiAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 3),
    _ArubaWiredPmXcvrDomTempHiAlarmThreshold_Type()
)
arubaWiredPmXcvrDomTempHiAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTempHiAlarmThreshold.setStatus("current")
_ArubaWiredPmXcvrDomTempHiAlarm_Type = TruthValue
_ArubaWiredPmXcvrDomTempHiAlarm_Object = MibTableColumn
arubaWiredPmXcvrDomTempHiAlarm = _ArubaWiredPmXcvrDomTempHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 4),
    _ArubaWiredPmXcvrDomTempHiAlarm_Type()
)
arubaWiredPmXcvrDomTempHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTempHiAlarm.setStatus("current")


class _ArubaWiredPmXcvrDomTempLoAlarmThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTempLoAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTempLoAlarmThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTempLoAlarmThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomTempLoAlarmThreshold = _ArubaWiredPmXcvrDomTempLoAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 5),
    _ArubaWiredPmXcvrDomTempLoAlarmThreshold_Type()
)
arubaWiredPmXcvrDomTempLoAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTempLoAlarmThreshold.setStatus("current")
_ArubaWiredPmXcvrDomTempLoAlarm_Type = TruthValue
_ArubaWiredPmXcvrDomTempLoAlarm_Object = MibTableColumn
arubaWiredPmXcvrDomTempLoAlarm = _ArubaWiredPmXcvrDomTempLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 6),
    _ArubaWiredPmXcvrDomTempLoAlarm_Type()
)
arubaWiredPmXcvrDomTempLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTempLoAlarm.setStatus("current")


class _ArubaWiredPmXcvrDomTempHiWarnThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTempHiWarnThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTempHiWarnThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTempHiWarnThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomTempHiWarnThreshold = _ArubaWiredPmXcvrDomTempHiWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 7),
    _ArubaWiredPmXcvrDomTempHiWarnThreshold_Type()
)
arubaWiredPmXcvrDomTempHiWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTempHiWarnThreshold.setStatus("current")
_ArubaWiredPmXcvrDomTempHiWarn_Type = TruthValue
_ArubaWiredPmXcvrDomTempHiWarn_Object = MibTableColumn
arubaWiredPmXcvrDomTempHiWarn = _ArubaWiredPmXcvrDomTempHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 8),
    _ArubaWiredPmXcvrDomTempHiWarn_Type()
)
arubaWiredPmXcvrDomTempHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTempHiWarn.setStatus("current")


class _ArubaWiredPmXcvrDomTempLoWarnThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTempLoWarnThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTempLoWarnThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTempLoWarnThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomTempLoWarnThreshold = _ArubaWiredPmXcvrDomTempLoWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 9),
    _ArubaWiredPmXcvrDomTempLoWarnThreshold_Type()
)
arubaWiredPmXcvrDomTempLoWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTempLoWarnThreshold.setStatus("current")
_ArubaWiredPmXcvrDomTempLoWarn_Type = TruthValue
_ArubaWiredPmXcvrDomTempLoWarn_Object = MibTableColumn
arubaWiredPmXcvrDomTempLoWarn = _ArubaWiredPmXcvrDomTempLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 10),
    _ArubaWiredPmXcvrDomTempLoWarn_Type()
)
arubaWiredPmXcvrDomTempLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTempLoWarn.setStatus("current")


class _ArubaWiredPmXcvrDomVoltage_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomVoltage_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomVoltage_Object = MibTableColumn
arubaWiredPmXcvrDomVoltage = _ArubaWiredPmXcvrDomVoltage_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 11),
    _ArubaWiredPmXcvrDomVoltage_Type()
)
arubaWiredPmXcvrDomVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomVoltage.setStatus("current")


class _ArubaWiredPmXcvrDomVccHiAlarmThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomVccHiAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomVccHiAlarmThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomVccHiAlarmThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomVccHiAlarmThreshold = _ArubaWiredPmXcvrDomVccHiAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 12),
    _ArubaWiredPmXcvrDomVccHiAlarmThreshold_Type()
)
arubaWiredPmXcvrDomVccHiAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomVccHiAlarmThreshold.setStatus("current")
_ArubaWiredPmXcvrDomVccHiAlarm_Type = TruthValue
_ArubaWiredPmXcvrDomVccHiAlarm_Object = MibTableColumn
arubaWiredPmXcvrDomVccHiAlarm = _ArubaWiredPmXcvrDomVccHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 13),
    _ArubaWiredPmXcvrDomVccHiAlarm_Type()
)
arubaWiredPmXcvrDomVccHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomVccHiAlarm.setStatus("current")


class _ArubaWiredPmXcvrDomVccLoAlarmThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomVccLoAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomVccLoAlarmThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomVccLoAlarmThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomVccLoAlarmThreshold = _ArubaWiredPmXcvrDomVccLoAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 14),
    _ArubaWiredPmXcvrDomVccLoAlarmThreshold_Type()
)
arubaWiredPmXcvrDomVccLoAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomVccLoAlarmThreshold.setStatus("current")
_ArubaWiredPmXcvrDomVccLoAlarm_Type = TruthValue
_ArubaWiredPmXcvrDomVccLoAlarm_Object = MibTableColumn
arubaWiredPmXcvrDomVccLoAlarm = _ArubaWiredPmXcvrDomVccLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 15),
    _ArubaWiredPmXcvrDomVccLoAlarm_Type()
)
arubaWiredPmXcvrDomVccLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomVccLoAlarm.setStatus("current")


class _ArubaWiredPmXcvrDomVccHiWarnThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomVccHiWarnThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomVccHiWarnThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomVccHiWarnThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomVccHiWarnThreshold = _ArubaWiredPmXcvrDomVccHiWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 16),
    _ArubaWiredPmXcvrDomVccHiWarnThreshold_Type()
)
arubaWiredPmXcvrDomVccHiWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomVccHiWarnThreshold.setStatus("current")
_ArubaWiredPmXcvrDomVccHiWarn_Type = TruthValue
_ArubaWiredPmXcvrDomVccHiWarn_Object = MibTableColumn
arubaWiredPmXcvrDomVccHiWarn = _ArubaWiredPmXcvrDomVccHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 17),
    _ArubaWiredPmXcvrDomVccHiWarn_Type()
)
arubaWiredPmXcvrDomVccHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomVccHiWarn.setStatus("current")


class _ArubaWiredPmXcvrDomVccLoWarnThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomVccLoWarnThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomVccLoWarnThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomVccLoWarnThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomVccLoWarnThreshold = _ArubaWiredPmXcvrDomVccLoWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 18),
    _ArubaWiredPmXcvrDomVccLoWarnThreshold_Type()
)
arubaWiredPmXcvrDomVccLoWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomVccLoWarnThreshold.setStatus("current")
_ArubaWiredPmXcvrDomVccLoWarn_Type = TruthValue
_ArubaWiredPmXcvrDomVccLoWarn_Object = MibTableColumn
arubaWiredPmXcvrDomVccLoWarn = _ArubaWiredPmXcvrDomVccLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 19),
    _ArubaWiredPmXcvrDomVccLoWarn_Type()
)
arubaWiredPmXcvrDomVccLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomVccLoWarn.setStatus("current")


class _ArubaWiredPmXcvrDomTxBiasHiAlarmThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTxBiasHiAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTxBiasHiAlarmThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTxBiasHiAlarmThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomTxBiasHiAlarmThreshold = _ArubaWiredPmXcvrDomTxBiasHiAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 20),
    _ArubaWiredPmXcvrDomTxBiasHiAlarmThreshold_Type()
)
arubaWiredPmXcvrDomTxBiasHiAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTxBiasHiAlarmThreshold.setStatus("current")


class _ArubaWiredPmXcvrDomTxBiasLoAlarmThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTxBiasLoAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTxBiasLoAlarmThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTxBiasLoAlarmThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomTxBiasLoAlarmThreshold = _ArubaWiredPmXcvrDomTxBiasLoAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 21),
    _ArubaWiredPmXcvrDomTxBiasLoAlarmThreshold_Type()
)
arubaWiredPmXcvrDomTxBiasLoAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTxBiasLoAlarmThreshold.setStatus("current")


class _ArubaWiredPmXcvrDomTxBiasHiWarnThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTxBiasHiWarnThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTxBiasHiWarnThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTxBiasHiWarnThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomTxBiasHiWarnThreshold = _ArubaWiredPmXcvrDomTxBiasHiWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 22),
    _ArubaWiredPmXcvrDomTxBiasHiWarnThreshold_Type()
)
arubaWiredPmXcvrDomTxBiasHiWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTxBiasHiWarnThreshold.setStatus("current")


class _ArubaWiredPmXcvrDomTxBiasLoWarnThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTxBiasLoWarnThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTxBiasLoWarnThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTxBiasLoWarnThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomTxBiasLoWarnThreshold = _ArubaWiredPmXcvrDomTxBiasLoWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 23),
    _ArubaWiredPmXcvrDomTxBiasLoWarnThreshold_Type()
)
arubaWiredPmXcvrDomTxBiasLoWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTxBiasLoWarnThreshold.setStatus("current")


class _ArubaWiredPmXcvrDomTxPwrHiAlarmThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTxPwrHiAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTxPwrHiAlarmThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTxPwrHiAlarmThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomTxPwrHiAlarmThreshold = _ArubaWiredPmXcvrDomTxPwrHiAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 24),
    _ArubaWiredPmXcvrDomTxPwrHiAlarmThreshold_Type()
)
arubaWiredPmXcvrDomTxPwrHiAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTxPwrHiAlarmThreshold.setStatus("current")


class _ArubaWiredPmXcvrDomTxPwrLoAlarmThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTxPwrLoAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTxPwrLoAlarmThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTxPwrLoAlarmThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomTxPwrLoAlarmThreshold = _ArubaWiredPmXcvrDomTxPwrLoAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 25),
    _ArubaWiredPmXcvrDomTxPwrLoAlarmThreshold_Type()
)
arubaWiredPmXcvrDomTxPwrLoAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTxPwrLoAlarmThreshold.setStatus("current")


class _ArubaWiredPmXcvrDomTxPwrHiWarnThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTxPwrHiWarnThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTxPwrHiWarnThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTxPwrHiWarnThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomTxPwrHiWarnThreshold = _ArubaWiredPmXcvrDomTxPwrHiWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 26),
    _ArubaWiredPmXcvrDomTxPwrHiWarnThreshold_Type()
)
arubaWiredPmXcvrDomTxPwrHiWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTxPwrHiWarnThreshold.setStatus("current")


class _ArubaWiredPmXcvrDomTxPwrLoWarnThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomTxPwrLoWarnThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomTxPwrLoWarnThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomTxPwrLoWarnThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomTxPwrLoWarnThreshold = _ArubaWiredPmXcvrDomTxPwrLoWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 27),
    _ArubaWiredPmXcvrDomTxPwrLoWarnThreshold_Type()
)
arubaWiredPmXcvrDomTxPwrLoWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTxPwrLoWarnThreshold.setStatus("current")


class _ArubaWiredPmXcvrDomRxPwrHiAlarmThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomRxPwrHiAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomRxPwrHiAlarmThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomRxPwrHiAlarmThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomRxPwrHiAlarmThreshold = _ArubaWiredPmXcvrDomRxPwrHiAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 28),
    _ArubaWiredPmXcvrDomRxPwrHiAlarmThreshold_Type()
)
arubaWiredPmXcvrDomRxPwrHiAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomRxPwrHiAlarmThreshold.setStatus("current")


class _ArubaWiredPmXcvrDomRxPwrLoAlarmThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomRxPwrLoAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomRxPwrLoAlarmThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomRxPwrLoAlarmThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomRxPwrLoAlarmThreshold = _ArubaWiredPmXcvrDomRxPwrLoAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 29),
    _ArubaWiredPmXcvrDomRxPwrLoAlarmThreshold_Type()
)
arubaWiredPmXcvrDomRxPwrLoAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomRxPwrLoAlarmThreshold.setStatus("current")


class _ArubaWiredPmXcvrDomRxPwrHiWarnThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomRxPwrHiWarnThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomRxPwrHiWarnThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomRxPwrHiWarnThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomRxPwrHiWarnThreshold = _ArubaWiredPmXcvrDomRxPwrHiWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 30),
    _ArubaWiredPmXcvrDomRxPwrHiWarnThreshold_Type()
)
arubaWiredPmXcvrDomRxPwrHiWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomRxPwrHiWarnThreshold.setStatus("current")


class _ArubaWiredPmXcvrDomRxPwrLoWarnThreshold_Type(DisplayString):
    """Custom type arubaWiredPmXcvrDomRxPwrLoWarnThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrDomRxPwrLoWarnThreshold_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrDomRxPwrLoWarnThreshold_Object = MibTableColumn
arubaWiredPmXcvrDomRxPwrLoWarnThreshold = _ArubaWiredPmXcvrDomRxPwrLoWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 31),
    _ArubaWiredPmXcvrDomRxPwrLoWarnThreshold_Type()
)
arubaWiredPmXcvrDomRxPwrLoWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomRxPwrLoWarnThreshold.setStatus("current")
_ArubaWiredPmXcvrDomTimeStamp_Type = TimeTicks
_ArubaWiredPmXcvrDomTimeStamp_Object = MibTableColumn
arubaWiredPmXcvrDomTimeStamp = _ArubaWiredPmXcvrDomTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 1, 1, 32),
    _ArubaWiredPmXcvrDomTimeStamp_Type()
)
arubaWiredPmXcvrDomTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomTimeStamp.setStatus("current")
_ArubaWiredPmXcvrLaneDomTable_Object = MibTable
arubaWiredPmXcvrLaneDomTable = _ArubaWiredPmXcvrLaneDomTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2)
)
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomTable.setStatus("current")
_ArubaWiredPmXcvrLaneDomEntry_Object = MibTableRow
arubaWiredPmXcvrLaneDomEntry = _ArubaWiredPmXcvrLaneDomEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1)
)
arubaWiredPmXcvrLaneDomEntry.setIndexNames(
    (0, "ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrPortIfIndex"),
    (0, "ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomEntry.setStatus("current")


class _ArubaWiredPmXcvrLaneDomIndex_Type(Unsigned32):
    """Custom type arubaWiredPmXcvrLaneDomIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ArubaWiredPmXcvrLaneDomIndex_Type.__name__ = "Unsigned32"
_ArubaWiredPmXcvrLaneDomIndex_Object = MibTableColumn
arubaWiredPmXcvrLaneDomIndex = _ArubaWiredPmXcvrLaneDomIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 1),
    _ArubaWiredPmXcvrLaneDomIndex_Type()
)
arubaWiredPmXcvrLaneDomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomIndex.setStatus("current")


class _ArubaWiredPmXcvrLaneDomTxBias_Type(DisplayString):
    """Custom type arubaWiredPmXcvrLaneDomTxBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrLaneDomTxBias_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrLaneDomTxBias_Object = MibTableColumn
arubaWiredPmXcvrLaneDomTxBias = _ArubaWiredPmXcvrLaneDomTxBias_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 2),
    _ArubaWiredPmXcvrLaneDomTxBias_Type()
)
arubaWiredPmXcvrLaneDomTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomTxBias.setStatus("current")
_ArubaWiredPmXcvrLaneDomTxBiasHiAlarm_Type = TruthValue
_ArubaWiredPmXcvrLaneDomTxBiasHiAlarm_Object = MibTableColumn
arubaWiredPmXcvrLaneDomTxBiasHiAlarm = _ArubaWiredPmXcvrLaneDomTxBiasHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 3),
    _ArubaWiredPmXcvrLaneDomTxBiasHiAlarm_Type()
)
arubaWiredPmXcvrLaneDomTxBiasHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomTxBiasHiAlarm.setStatus("current")
_ArubaWiredPmXcvrLaneDomTxBiasLoAlarm_Type = TruthValue
_ArubaWiredPmXcvrLaneDomTxBiasLoAlarm_Object = MibTableColumn
arubaWiredPmXcvrLaneDomTxBiasLoAlarm = _ArubaWiredPmXcvrLaneDomTxBiasLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 4),
    _ArubaWiredPmXcvrLaneDomTxBiasLoAlarm_Type()
)
arubaWiredPmXcvrLaneDomTxBiasLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomTxBiasLoAlarm.setStatus("current")
_ArubaWiredPmXcvrLaneDomTxBiasHiWarn_Type = TruthValue
_ArubaWiredPmXcvrLaneDomTxBiasHiWarn_Object = MibTableColumn
arubaWiredPmXcvrLaneDomTxBiasHiWarn = _ArubaWiredPmXcvrLaneDomTxBiasHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 5),
    _ArubaWiredPmXcvrLaneDomTxBiasHiWarn_Type()
)
arubaWiredPmXcvrLaneDomTxBiasHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomTxBiasHiWarn.setStatus("current")
_ArubaWiredPmXcvrLaneDomTxBiasLoWarn_Type = TruthValue
_ArubaWiredPmXcvrLaneDomTxBiasLoWarn_Object = MibTableColumn
arubaWiredPmXcvrLaneDomTxBiasLoWarn = _ArubaWiredPmXcvrLaneDomTxBiasLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 6),
    _ArubaWiredPmXcvrLaneDomTxBiasLoWarn_Type()
)
arubaWiredPmXcvrLaneDomTxBiasLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomTxBiasLoWarn.setStatus("current")


class _ArubaWiredPmXcvrLaneDomTxPower_Type(DisplayString):
    """Custom type arubaWiredPmXcvrLaneDomTxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrLaneDomTxPower_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrLaneDomTxPower_Object = MibTableColumn
arubaWiredPmXcvrLaneDomTxPower = _ArubaWiredPmXcvrLaneDomTxPower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 7),
    _ArubaWiredPmXcvrLaneDomTxPower_Type()
)
arubaWiredPmXcvrLaneDomTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomTxPower.setStatus("current")
_ArubaWiredPmXcvrLaneDomTxPwrHiAlarm_Type = TruthValue
_ArubaWiredPmXcvrLaneDomTxPwrHiAlarm_Object = MibTableColumn
arubaWiredPmXcvrLaneDomTxPwrHiAlarm = _ArubaWiredPmXcvrLaneDomTxPwrHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 8),
    _ArubaWiredPmXcvrLaneDomTxPwrHiAlarm_Type()
)
arubaWiredPmXcvrLaneDomTxPwrHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomTxPwrHiAlarm.setStatus("current")
_ArubaWiredPmXcvrLaneDomTxPwrLoAlarm_Type = TruthValue
_ArubaWiredPmXcvrLaneDomTxPwrLoAlarm_Object = MibTableColumn
arubaWiredPmXcvrLaneDomTxPwrLoAlarm = _ArubaWiredPmXcvrLaneDomTxPwrLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 9),
    _ArubaWiredPmXcvrLaneDomTxPwrLoAlarm_Type()
)
arubaWiredPmXcvrLaneDomTxPwrLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomTxPwrLoAlarm.setStatus("current")
_ArubaWiredPmXcvrLaneDomTxPwrHiWarn_Type = TruthValue
_ArubaWiredPmXcvrLaneDomTxPwrHiWarn_Object = MibTableColumn
arubaWiredPmXcvrLaneDomTxPwrHiWarn = _ArubaWiredPmXcvrLaneDomTxPwrHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 10),
    _ArubaWiredPmXcvrLaneDomTxPwrHiWarn_Type()
)
arubaWiredPmXcvrLaneDomTxPwrHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomTxPwrHiWarn.setStatus("current")
_ArubaWiredPmXcvrLaneDomTxPwrLoWarn_Type = TruthValue
_ArubaWiredPmXcvrLaneDomTxPwrLoWarn_Object = MibTableColumn
arubaWiredPmXcvrLaneDomTxPwrLoWarn = _ArubaWiredPmXcvrLaneDomTxPwrLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 11),
    _ArubaWiredPmXcvrLaneDomTxPwrLoWarn_Type()
)
arubaWiredPmXcvrLaneDomTxPwrLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomTxPwrLoWarn.setStatus("current")


class _ArubaWiredPmXcvrLaneDomRxPower_Type(DisplayString):
    """Custom type arubaWiredPmXcvrLaneDomRxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredPmXcvrLaneDomRxPower_Type.__name__ = "DisplayString"
_ArubaWiredPmXcvrLaneDomRxPower_Object = MibTableColumn
arubaWiredPmXcvrLaneDomRxPower = _ArubaWiredPmXcvrLaneDomRxPower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 12),
    _ArubaWiredPmXcvrLaneDomRxPower_Type()
)
arubaWiredPmXcvrLaneDomRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomRxPower.setStatus("current")
_ArubaWiredPmXcvrLaneDomRxPwrHiAlarm_Type = TruthValue
_ArubaWiredPmXcvrLaneDomRxPwrHiAlarm_Object = MibTableColumn
arubaWiredPmXcvrLaneDomRxPwrHiAlarm = _ArubaWiredPmXcvrLaneDomRxPwrHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 13),
    _ArubaWiredPmXcvrLaneDomRxPwrHiAlarm_Type()
)
arubaWiredPmXcvrLaneDomRxPwrHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomRxPwrHiAlarm.setStatus("current")
_ArubaWiredPmXcvrLaneDomRxPwrLoAlarm_Type = TruthValue
_ArubaWiredPmXcvrLaneDomRxPwrLoAlarm_Object = MibTableColumn
arubaWiredPmXcvrLaneDomRxPwrLoAlarm = _ArubaWiredPmXcvrLaneDomRxPwrLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 14),
    _ArubaWiredPmXcvrLaneDomRxPwrLoAlarm_Type()
)
arubaWiredPmXcvrLaneDomRxPwrLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomRxPwrLoAlarm.setStatus("current")
_ArubaWiredPmXcvrLaneDomRxPwrHiWarn_Type = TruthValue
_ArubaWiredPmXcvrLaneDomRxPwrHiWarn_Object = MibTableColumn
arubaWiredPmXcvrLaneDomRxPwrHiWarn = _ArubaWiredPmXcvrLaneDomRxPwrHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 15),
    _ArubaWiredPmXcvrLaneDomRxPwrHiWarn_Type()
)
arubaWiredPmXcvrLaneDomRxPwrHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomRxPwrHiWarn.setStatus("current")
_ArubaWiredPmXcvrLaneDomRxPwrLoWarn_Type = TruthValue
_ArubaWiredPmXcvrLaneDomRxPwrLoWarn_Object = MibTableColumn
arubaWiredPmXcvrLaneDomRxPwrLoWarn = _ArubaWiredPmXcvrLaneDomRxPwrLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 1, 2, 2, 1, 16),
    _ArubaWiredPmXcvrLaneDomRxPwrLoWarn_Type()
)
arubaWiredPmXcvrLaneDomRxPwrLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPmXcvrLaneDomRxPwrLoWarn.setStatus("current")
_ArubaWiredPmConformance_ObjectIdentity = ObjectIdentity
arubaWiredPmConformance = _ArubaWiredPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 2)
)
_ArubaWiredPmGroups_ObjectIdentity = ObjectIdentity
arubaWiredPmGroups = _ArubaWiredPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 2, 1)
)
_ArubaWiredPmCompliances_ObjectIdentity = ObjectIdentity
arubaWiredPmCompliances = _ArubaWiredPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 2, 2)
)

# Managed Objects groups

arubaWiredPmXcvrInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 2, 1, 1)
)
arubaWiredPmXcvrInfoGroup.setObjects(
      *(("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrPortDesc"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDescription"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrProductNum"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrSerialNum"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrPartNum"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrType"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrConnectorType"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrConnectorStatus"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrConnectorStatusReason"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrCableType"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrWavelength"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrSmfTxDist"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrMmfOm1TxDist"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrMmfOm2TxDist"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrMmfOm3TxDist"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrMmfOm4TxDist"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrMmfOm5TxDist"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrCableLength"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrMaxSpeed"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrMaxPower"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrAdapterType"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrAdapterStatus"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrAdapterStatusReason"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrAdapterProductNum"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrAdapterSerialNum"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrThermalClass"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDiagnostics"))
)
if mibBuilder.loadTexts:
    arubaWiredPmXcvrInfoGroup.setStatus("current")

arubaWiredPmXcvrDomInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 2, 1, 2)
)
arubaWiredPmXcvrDomInfoGroup.setObjects(
      *(("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomPortDesc"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTemp"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTempHiAlarmThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTempHiAlarm"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTempLoAlarmThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTempLoAlarm"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTempHiWarnThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTempHiWarn"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTempLoWarnThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTempLoWarn"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomVoltage"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomVccHiAlarmThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomVccHiAlarm"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomVccLoAlarmThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomVccLoAlarm"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomVccHiWarnThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomVccHiWarn"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomVccLoWarnThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomVccLoWarn"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTxBiasHiAlarmThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTxBiasLoAlarmThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTxBiasHiWarnThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTxBiasLoWarnThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTxPwrHiAlarmThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTxPwrLoAlarmThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTxPwrHiWarnThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTxPwrLoWarnThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomRxPwrHiAlarmThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomRxPwrLoAlarmThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomRxPwrHiWarnThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomRxPwrLoWarnThreshold"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomTimeStamp"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomTxBias"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomTxBiasHiAlarm"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomTxBiasLoAlarm"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomTxBiasHiWarn"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomTxBiasLoWarn"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomTxPower"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomTxPwrHiAlarm"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomTxPwrLoAlarm"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomTxPwrHiWarn"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomTxPwrLoWarn"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomRxPower"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomRxPwrHiAlarm"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomRxPwrLoAlarm"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomRxPwrHiWarn"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrLaneDomRxPwrLoWarn"))
)
if mibBuilder.loadTexts:
    arubaWiredPmXcvrDomInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27, 2, 2, 1)
)
arubaWiredPmCompliance.setObjects(
      *(("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrInfoGroup"),
        ("ARUBAWIRED-PM-MIB", "arubaWiredPmXcvrDomInfoGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredPmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-PM-MIB",
    **{"arubaWiredPmMIB": arubaWiredPmMIB,
       "arubaWiredPmNotificatons": arubaWiredPmNotificatons,
       "arubaWiredPmObjects": arubaWiredPmObjects,
       "arubaWiredPmXcvrInfo": arubaWiredPmXcvrInfo,
       "arubaWiredPmXcvrTable": arubaWiredPmXcvrTable,
       "arubaWiredPmXcvrEntry": arubaWiredPmXcvrEntry,
       "arubaWiredPmXcvrPortIfIndex": arubaWiredPmXcvrPortIfIndex,
       "arubaWiredPmXcvrPortDesc": arubaWiredPmXcvrPortDesc,
       "arubaWiredPmXcvrDescription": arubaWiredPmXcvrDescription,
       "arubaWiredPmXcvrProductNum": arubaWiredPmXcvrProductNum,
       "arubaWiredPmXcvrSerialNum": arubaWiredPmXcvrSerialNum,
       "arubaWiredPmXcvrPartNum": arubaWiredPmXcvrPartNum,
       "arubaWiredPmXcvrType": arubaWiredPmXcvrType,
       "arubaWiredPmXcvrConnectorType": arubaWiredPmXcvrConnectorType,
       "arubaWiredPmXcvrConnectorStatus": arubaWiredPmXcvrConnectorStatus,
       "arubaWiredPmXcvrConnectorStatusReason": arubaWiredPmXcvrConnectorStatusReason,
       "arubaWiredPmXcvrCableType": arubaWiredPmXcvrCableType,
       "arubaWiredPmXcvrWavelength": arubaWiredPmXcvrWavelength,
       "arubaWiredPmXcvrSmfTxDist": arubaWiredPmXcvrSmfTxDist,
       "arubaWiredPmXcvrMmfOm1TxDist": arubaWiredPmXcvrMmfOm1TxDist,
       "arubaWiredPmXcvrMmfOm2TxDist": arubaWiredPmXcvrMmfOm2TxDist,
       "arubaWiredPmXcvrMmfOm3TxDist": arubaWiredPmXcvrMmfOm3TxDist,
       "arubaWiredPmXcvrMmfOm4TxDist": arubaWiredPmXcvrMmfOm4TxDist,
       "arubaWiredPmXcvrMmfOm5TxDist": arubaWiredPmXcvrMmfOm5TxDist,
       "arubaWiredPmXcvrCableLength": arubaWiredPmXcvrCableLength,
       "arubaWiredPmXcvrMaxSpeed": arubaWiredPmXcvrMaxSpeed,
       "arubaWiredPmXcvrMaxPower": arubaWiredPmXcvrMaxPower,
       "arubaWiredPmXcvrAdapterType": arubaWiredPmXcvrAdapterType,
       "arubaWiredPmXcvrAdapterStatus": arubaWiredPmXcvrAdapterStatus,
       "arubaWiredPmXcvrAdapterStatusReason": arubaWiredPmXcvrAdapterStatusReason,
       "arubaWiredPmXcvrAdapterProductNum": arubaWiredPmXcvrAdapterProductNum,
       "arubaWiredPmXcvrAdapterSerialNum": arubaWiredPmXcvrAdapterSerialNum,
       "arubaWiredPmXcvrThermalClass": arubaWiredPmXcvrThermalClass,
       "arubaWiredPmXcvrDiagnostics": arubaWiredPmXcvrDiagnostics,
       "arubaWiredPmXcvrDomInfo": arubaWiredPmXcvrDomInfo,
       "arubaWiredPmXcvrDomTable": arubaWiredPmXcvrDomTable,
       "arubaWiredPmXcvrDomEntry": arubaWiredPmXcvrDomEntry,
       "arubaWiredPmXcvrDomPortDesc": arubaWiredPmXcvrDomPortDesc,
       "arubaWiredPmXcvrDomTemp": arubaWiredPmXcvrDomTemp,
       "arubaWiredPmXcvrDomTempHiAlarmThreshold": arubaWiredPmXcvrDomTempHiAlarmThreshold,
       "arubaWiredPmXcvrDomTempHiAlarm": arubaWiredPmXcvrDomTempHiAlarm,
       "arubaWiredPmXcvrDomTempLoAlarmThreshold": arubaWiredPmXcvrDomTempLoAlarmThreshold,
       "arubaWiredPmXcvrDomTempLoAlarm": arubaWiredPmXcvrDomTempLoAlarm,
       "arubaWiredPmXcvrDomTempHiWarnThreshold": arubaWiredPmXcvrDomTempHiWarnThreshold,
       "arubaWiredPmXcvrDomTempHiWarn": arubaWiredPmXcvrDomTempHiWarn,
       "arubaWiredPmXcvrDomTempLoWarnThreshold": arubaWiredPmXcvrDomTempLoWarnThreshold,
       "arubaWiredPmXcvrDomTempLoWarn": arubaWiredPmXcvrDomTempLoWarn,
       "arubaWiredPmXcvrDomVoltage": arubaWiredPmXcvrDomVoltage,
       "arubaWiredPmXcvrDomVccHiAlarmThreshold": arubaWiredPmXcvrDomVccHiAlarmThreshold,
       "arubaWiredPmXcvrDomVccHiAlarm": arubaWiredPmXcvrDomVccHiAlarm,
       "arubaWiredPmXcvrDomVccLoAlarmThreshold": arubaWiredPmXcvrDomVccLoAlarmThreshold,
       "arubaWiredPmXcvrDomVccLoAlarm": arubaWiredPmXcvrDomVccLoAlarm,
       "arubaWiredPmXcvrDomVccHiWarnThreshold": arubaWiredPmXcvrDomVccHiWarnThreshold,
       "arubaWiredPmXcvrDomVccHiWarn": arubaWiredPmXcvrDomVccHiWarn,
       "arubaWiredPmXcvrDomVccLoWarnThreshold": arubaWiredPmXcvrDomVccLoWarnThreshold,
       "arubaWiredPmXcvrDomVccLoWarn": arubaWiredPmXcvrDomVccLoWarn,
       "arubaWiredPmXcvrDomTxBiasHiAlarmThreshold": arubaWiredPmXcvrDomTxBiasHiAlarmThreshold,
       "arubaWiredPmXcvrDomTxBiasLoAlarmThreshold": arubaWiredPmXcvrDomTxBiasLoAlarmThreshold,
       "arubaWiredPmXcvrDomTxBiasHiWarnThreshold": arubaWiredPmXcvrDomTxBiasHiWarnThreshold,
       "arubaWiredPmXcvrDomTxBiasLoWarnThreshold": arubaWiredPmXcvrDomTxBiasLoWarnThreshold,
       "arubaWiredPmXcvrDomTxPwrHiAlarmThreshold": arubaWiredPmXcvrDomTxPwrHiAlarmThreshold,
       "arubaWiredPmXcvrDomTxPwrLoAlarmThreshold": arubaWiredPmXcvrDomTxPwrLoAlarmThreshold,
       "arubaWiredPmXcvrDomTxPwrHiWarnThreshold": arubaWiredPmXcvrDomTxPwrHiWarnThreshold,
       "arubaWiredPmXcvrDomTxPwrLoWarnThreshold": arubaWiredPmXcvrDomTxPwrLoWarnThreshold,
       "arubaWiredPmXcvrDomRxPwrHiAlarmThreshold": arubaWiredPmXcvrDomRxPwrHiAlarmThreshold,
       "arubaWiredPmXcvrDomRxPwrLoAlarmThreshold": arubaWiredPmXcvrDomRxPwrLoAlarmThreshold,
       "arubaWiredPmXcvrDomRxPwrHiWarnThreshold": arubaWiredPmXcvrDomRxPwrHiWarnThreshold,
       "arubaWiredPmXcvrDomRxPwrLoWarnThreshold": arubaWiredPmXcvrDomRxPwrLoWarnThreshold,
       "arubaWiredPmXcvrDomTimeStamp": arubaWiredPmXcvrDomTimeStamp,
       "arubaWiredPmXcvrLaneDomTable": arubaWiredPmXcvrLaneDomTable,
       "arubaWiredPmXcvrLaneDomEntry": arubaWiredPmXcvrLaneDomEntry,
       "arubaWiredPmXcvrLaneDomIndex": arubaWiredPmXcvrLaneDomIndex,
       "arubaWiredPmXcvrLaneDomTxBias": arubaWiredPmXcvrLaneDomTxBias,
       "arubaWiredPmXcvrLaneDomTxBiasHiAlarm": arubaWiredPmXcvrLaneDomTxBiasHiAlarm,
       "arubaWiredPmXcvrLaneDomTxBiasLoAlarm": arubaWiredPmXcvrLaneDomTxBiasLoAlarm,
       "arubaWiredPmXcvrLaneDomTxBiasHiWarn": arubaWiredPmXcvrLaneDomTxBiasHiWarn,
       "arubaWiredPmXcvrLaneDomTxBiasLoWarn": arubaWiredPmXcvrLaneDomTxBiasLoWarn,
       "arubaWiredPmXcvrLaneDomTxPower": arubaWiredPmXcvrLaneDomTxPower,
       "arubaWiredPmXcvrLaneDomTxPwrHiAlarm": arubaWiredPmXcvrLaneDomTxPwrHiAlarm,
       "arubaWiredPmXcvrLaneDomTxPwrLoAlarm": arubaWiredPmXcvrLaneDomTxPwrLoAlarm,
       "arubaWiredPmXcvrLaneDomTxPwrHiWarn": arubaWiredPmXcvrLaneDomTxPwrHiWarn,
       "arubaWiredPmXcvrLaneDomTxPwrLoWarn": arubaWiredPmXcvrLaneDomTxPwrLoWarn,
       "arubaWiredPmXcvrLaneDomRxPower": arubaWiredPmXcvrLaneDomRxPower,
       "arubaWiredPmXcvrLaneDomRxPwrHiAlarm": arubaWiredPmXcvrLaneDomRxPwrHiAlarm,
       "arubaWiredPmXcvrLaneDomRxPwrLoAlarm": arubaWiredPmXcvrLaneDomRxPwrLoAlarm,
       "arubaWiredPmXcvrLaneDomRxPwrHiWarn": arubaWiredPmXcvrLaneDomRxPwrHiWarn,
       "arubaWiredPmXcvrLaneDomRxPwrLoWarn": arubaWiredPmXcvrLaneDomRxPwrLoWarn,
       "arubaWiredPmConformance": arubaWiredPmConformance,
       "arubaWiredPmGroups": arubaWiredPmGroups,
       "arubaWiredPmXcvrInfoGroup": arubaWiredPmXcvrInfoGroup,
       "arubaWiredPmXcvrDomInfoGroup": arubaWiredPmXcvrDomInfoGroup,
       "arubaWiredPmCompliances": arubaWiredPmCompliances,
       "arubaWiredPmCompliance": arubaWiredPmCompliance}
)
