# SNMP MIB module (TN-UDLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-UDLD
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:34 2025
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

(TNDisplayString,
 TNInterfaceIndex) = mibBuilder.importSymbols(
    "TN-TC",
    "TNDisplayString",
    "TNInterfaceIndex")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnUdldMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124)
)
if mibBuilder.loadTexts:
    tnUdldMib.setRevisions(
        ("2015-07-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TNUdldDetectionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("inDeterminant", 0),
          ("uniDirectional", 1),
          ("biDirectional", 2),
          ("neighborMismatch", 3),
          ("loopback", 4),
          ("multipleNeighbor", 5))
    )



class TNUdldMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("normal", 1),
          ("aggressive", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TnUdldConfigInterfaceParamTable_Object = MibTable
tnUdldConfigInterfaceParamTable = _TnUdldConfigInterfaceParamTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 1)
)
if mibBuilder.loadTexts:
    tnUdldConfigInterfaceParamTable.setStatus("current")
_TnUdldConfigInterfaceParamEntry_Object = MibTableRow
tnUdldConfigInterfaceParamEntry = _TnUdldConfigInterfaceParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 1, 1)
)
tnUdldConfigInterfaceParamEntry.setIndexNames(
    (0, "TN-UDLD-MIB", "tnUdldConfigInterfaceParamIfIndex"),
)
if mibBuilder.loadTexts:
    tnUdldConfigInterfaceParamEntry.setStatus("current")
_TnUdldConfigInterfaceParamIfIndex_Type = TNInterfaceIndex
_TnUdldConfigInterfaceParamIfIndex_Object = MibTableColumn
tnUdldConfigInterfaceParamIfIndex = _TnUdldConfigInterfaceParamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 1, 1, 1),
    _TnUdldConfigInterfaceParamIfIndex_Type()
)
tnUdldConfigInterfaceParamIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnUdldConfigInterfaceParamIfIndex.setStatus("current")
_TnUdldConfigInterfaceParamUdldMode_Type = TNUdldMode
_TnUdldConfigInterfaceParamUdldMode_Object = MibTableColumn
tnUdldConfigInterfaceParamUdldMode = _TnUdldConfigInterfaceParamUdldMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 1, 1, 2),
    _TnUdldConfigInterfaceParamUdldMode_Type()
)
tnUdldConfigInterfaceParamUdldMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUdldConfigInterfaceParamUdldMode.setStatus("current")


class _TnUdldConfigInterfaceParamProbeMsgInterval_Type(Unsigned32):
    """Custom type tnUdldConfigInterfaceParamProbeMsgInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 90),
    )


_TnUdldConfigInterfaceParamProbeMsgInterval_Type.__name__ = "Unsigned32"
_TnUdldConfigInterfaceParamProbeMsgInterval_Object = MibTableColumn
tnUdldConfigInterfaceParamProbeMsgInterval = _TnUdldConfigInterfaceParamProbeMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 1, 1, 3),
    _TnUdldConfigInterfaceParamProbeMsgInterval_Type()
)
tnUdldConfigInterfaceParamProbeMsgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUdldConfigInterfaceParamProbeMsgInterval.setStatus("current")
_TnUdldStatusInterfaceTable_Object = MibTable
tnUdldStatusInterfaceTable = _TnUdldStatusInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 2)
)
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceTable.setStatus("current")
_TnUdldStatusInterfaceEntry_Object = MibTableRow
tnUdldStatusInterfaceEntry = _TnUdldStatusInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 2, 1)
)
tnUdldStatusInterfaceEntry.setIndexNames(
    (0, "TN-UDLD-MIB", "tnUdldStatusInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceEntry.setStatus("current")
_TnUdldStatusInterfaceIfIndex_Type = TNInterfaceIndex
_TnUdldStatusInterfaceIfIndex_Object = MibTableColumn
tnUdldStatusInterfaceIfIndex = _TnUdldStatusInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 2, 1, 1),
    _TnUdldStatusInterfaceIfIndex_Type()
)
tnUdldStatusInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceIfIndex.setStatus("current")


class _TnUdldStatusInterfaceDeviceID_Type(TNDisplayString):
    """Custom type tnUdldStatusInterfaceDeviceID based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TnUdldStatusInterfaceDeviceID_Type.__name__ = "TNDisplayString"
_TnUdldStatusInterfaceDeviceID_Object = MibTableColumn
tnUdldStatusInterfaceDeviceID = _TnUdldStatusInterfaceDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 2, 1, 2),
    _TnUdldStatusInterfaceDeviceID_Type()
)
tnUdldStatusInterfaceDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceDeviceID.setStatus("current")


class _TnUdldStatusInterfaceDeviceName_Type(TNDisplayString):
    """Custom type tnUdldStatusInterfaceDeviceName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TnUdldStatusInterfaceDeviceName_Type.__name__ = "TNDisplayString"
_TnUdldStatusInterfaceDeviceName_Object = MibTableColumn
tnUdldStatusInterfaceDeviceName = _TnUdldStatusInterfaceDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 2, 1, 3),
    _TnUdldStatusInterfaceDeviceName_Type()
)
tnUdldStatusInterfaceDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceDeviceName.setStatus("current")
_TnUdldStatusInterfaceLinkState_Type = TNUdldDetectionState
_TnUdldStatusInterfaceLinkState_Object = MibTableColumn
tnUdldStatusInterfaceLinkState = _TnUdldStatusInterfaceLinkState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 2, 1, 4),
    _TnUdldStatusInterfaceLinkState_Type()
)
tnUdldStatusInterfaceLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceLinkState.setStatus("current")
_TnUdldStatusInterfaceNeighborTable_Object = MibTable
tnUdldStatusInterfaceNeighborTable = _TnUdldStatusInterfaceNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 3)
)
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceNeighborTable.setStatus("current")
_TnUdldStatusInterfaceNeighborEntry_Object = MibTableRow
tnUdldStatusInterfaceNeighborEntry = _TnUdldStatusInterfaceNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 3, 1)
)
tnUdldStatusInterfaceNeighborEntry.setIndexNames(
    (0, "TN-UDLD-MIB", "tnUdldStatusInterfaceNeighborIfIndex"),
)
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceNeighborEntry.setStatus("current")
_TnUdldStatusInterfaceNeighborIfIndex_Type = TNInterfaceIndex
_TnUdldStatusInterfaceNeighborIfIndex_Object = MibTableColumn
tnUdldStatusInterfaceNeighborIfIndex = _TnUdldStatusInterfaceNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 3, 1, 1),
    _TnUdldStatusInterfaceNeighborIfIndex_Type()
)
tnUdldStatusInterfaceNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceNeighborIfIndex.setStatus("current")


class _TnUdldStatusInterfaceNeighborNeighborDeviceID_Type(TNDisplayString):
    """Custom type tnUdldStatusInterfaceNeighborNeighborDeviceID based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TnUdldStatusInterfaceNeighborNeighborDeviceID_Type.__name__ = "TNDisplayString"
_TnUdldStatusInterfaceNeighborNeighborDeviceID_Object = MibTableColumn
tnUdldStatusInterfaceNeighborNeighborDeviceID = _TnUdldStatusInterfaceNeighborNeighborDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 3, 1, 2),
    _TnUdldStatusInterfaceNeighborNeighborDeviceID_Type()
)
tnUdldStatusInterfaceNeighborNeighborDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceNeighborNeighborDeviceID.setStatus("current")


class _TnUdldStatusInterfaceNeighborNeighborPortID_Type(TNDisplayString):
    """Custom type tnUdldStatusInterfaceNeighborNeighborPortID based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TnUdldStatusInterfaceNeighborNeighborPortID_Type.__name__ = "TNDisplayString"
_TnUdldStatusInterfaceNeighborNeighborPortID_Object = MibTableColumn
tnUdldStatusInterfaceNeighborNeighborPortID = _TnUdldStatusInterfaceNeighborNeighborPortID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 3, 1, 3),
    _TnUdldStatusInterfaceNeighborNeighborPortID_Type()
)
tnUdldStatusInterfaceNeighborNeighborPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceNeighborNeighborPortID.setStatus("current")


class _TnUdldStatusInterfaceNeighborNeighborDeviceName_Type(TNDisplayString):
    """Custom type tnUdldStatusInterfaceNeighborNeighborDeviceName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TnUdldStatusInterfaceNeighborNeighborDeviceName_Type.__name__ = "TNDisplayString"
_TnUdldStatusInterfaceNeighborNeighborDeviceName_Object = MibTableColumn
tnUdldStatusInterfaceNeighborNeighborDeviceName = _TnUdldStatusInterfaceNeighborNeighborDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 3, 1, 4),
    _TnUdldStatusInterfaceNeighborNeighborDeviceName_Type()
)
tnUdldStatusInterfaceNeighborNeighborDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceNeighborNeighborDeviceName.setStatus("current")
_TnUdldStatusInterfaceNeighborLinkDetectionState_Type = TNUdldDetectionState
_TnUdldStatusInterfaceNeighborLinkDetectionState_Object = MibTableColumn
tnUdldStatusInterfaceNeighborLinkDetectionState = _TnUdldStatusInterfaceNeighborLinkDetectionState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 124, 3, 1, 5),
    _TnUdldStatusInterfaceNeighborLinkDetectionState_Type()
)
tnUdldStatusInterfaceNeighborLinkDetectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUdldStatusInterfaceNeighborLinkDetectionState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-UDLD-MIB",
    **{"TNUdldDetectionState": TNUdldDetectionState,
       "TNUdldMode": TNUdldMode,
       "tnUdldMib": tnUdldMib,
       "tnUdldConfigInterfaceParamTable": tnUdldConfigInterfaceParamTable,
       "tnUdldConfigInterfaceParamEntry": tnUdldConfigInterfaceParamEntry,
       "tnUdldConfigInterfaceParamIfIndex": tnUdldConfigInterfaceParamIfIndex,
       "tnUdldConfigInterfaceParamUdldMode": tnUdldConfigInterfaceParamUdldMode,
       "tnUdldConfigInterfaceParamProbeMsgInterval": tnUdldConfigInterfaceParamProbeMsgInterval,
       "tnUdldStatusInterfaceTable": tnUdldStatusInterfaceTable,
       "tnUdldStatusInterfaceEntry": tnUdldStatusInterfaceEntry,
       "tnUdldStatusInterfaceIfIndex": tnUdldStatusInterfaceIfIndex,
       "tnUdldStatusInterfaceDeviceID": tnUdldStatusInterfaceDeviceID,
       "tnUdldStatusInterfaceDeviceName": tnUdldStatusInterfaceDeviceName,
       "tnUdldStatusInterfaceLinkState": tnUdldStatusInterfaceLinkState,
       "tnUdldStatusInterfaceNeighborTable": tnUdldStatusInterfaceNeighborTable,
       "tnUdldStatusInterfaceNeighborEntry": tnUdldStatusInterfaceNeighborEntry,
       "tnUdldStatusInterfaceNeighborIfIndex": tnUdldStatusInterfaceNeighborIfIndex,
       "tnUdldStatusInterfaceNeighborNeighborDeviceID": tnUdldStatusInterfaceNeighborNeighborDeviceID,
       "tnUdldStatusInterfaceNeighborNeighborPortID": tnUdldStatusInterfaceNeighborNeighborPortID,
       "tnUdldStatusInterfaceNeighborNeighborDeviceName": tnUdldStatusInterfaceNeighborNeighborDeviceName,
       "tnUdldStatusInterfaceNeighborLinkDetectionState": tnUdldStatusInterfaceNeighborLinkDetectionState}
)
