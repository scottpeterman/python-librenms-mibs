# SNMP MIB module (CISCOSB-DEBUGCAPABILITIES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-DEBUGCAPABILITIES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:25 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

rlSna = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229)
)
if mibBuilder.loadTexts:
    rlSna.setRevisions(
        ("2015-05-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlSnaNextFreeSessionId_Type = TestAndIncr
_RlSnaNextFreeSessionId_Object = MibScalar
rlSnaNextFreeSessionId = _RlSnaNextFreeSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229, 1),
    _RlSnaNextFreeSessionId_Type()
)
rlSnaNextFreeSessionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSnaNextFreeSessionId.setStatus("current")
_RlSnaClientAgentPollingTable_Object = MibTable
rlSnaClientAgentPollingTable = _RlSnaClientAgentPollingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229, 2)
)
if mibBuilder.loadTexts:
    rlSnaClientAgentPollingTable.setStatus("current")
_RlSnaClientAgentPollingEntry_Object = MibTableRow
rlSnaClientAgentPollingEntry = _RlSnaClientAgentPollingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229, 2, 1)
)
rlSnaClientAgentPollingEntry.setIndexNames(
    (0, "CISCOSB-DEBUGCAPABILITIES-MIB", "rlSnaClientAgentClientSessionId"),
    (0, "CISCOSB-DEBUGCAPABILITIES-MIB", "rlSnaClientAgentAgentAddressType"),
    (0, "CISCOSB-DEBUGCAPABILITIES-MIB", "rlSnaClientAgentAgentAddress"),
    (1, "CISCOSB-DEBUGCAPABILITIES-MIB", "rlSnaClientAgentMibName"),
)
if mibBuilder.loadTexts:
    rlSnaClientAgentPollingEntry.setStatus("current")
_RlSnaClientAgentClientSessionId_Type = Integer32
_RlSnaClientAgentClientSessionId_Object = MibTableColumn
rlSnaClientAgentClientSessionId = _RlSnaClientAgentClientSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229, 2, 1, 1),
    _RlSnaClientAgentClientSessionId_Type()
)
rlSnaClientAgentClientSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSnaClientAgentClientSessionId.setStatus("current")
_RlSnaClientAgentAgentAddressType_Type = InetAddressType
_RlSnaClientAgentAgentAddressType_Object = MibTableColumn
rlSnaClientAgentAgentAddressType = _RlSnaClientAgentAgentAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229, 2, 1, 2),
    _RlSnaClientAgentAgentAddressType_Type()
)
rlSnaClientAgentAgentAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSnaClientAgentAgentAddressType.setStatus("current")
_RlSnaClientAgentAgentAddress_Type = InetAddress
_RlSnaClientAgentAgentAddress_Object = MibTableColumn
rlSnaClientAgentAgentAddress = _RlSnaClientAgentAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229, 2, 1, 3),
    _RlSnaClientAgentAgentAddress_Type()
)
rlSnaClientAgentAgentAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSnaClientAgentAgentAddress.setStatus("current")


class _RlSnaClientAgentMibName_Type(DisplayString):
    """Custom type rlSnaClientAgentMibName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RlSnaClientAgentMibName_Type.__name__ = "DisplayString"
_RlSnaClientAgentMibName_Object = MibTableColumn
rlSnaClientAgentMibName = _RlSnaClientAgentMibName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229, 2, 1, 4),
    _RlSnaClientAgentMibName_Type()
)
rlSnaClientAgentMibName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSnaClientAgentMibName.setStatus("current")


class _RlSnaClientAgentMibFieldsMask_Type(OctetString):
    """Custom type rlSnaClientAgentMibFieldsMask based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlSnaClientAgentMibFieldsMask_Type.__name__ = "OctetString"
_RlSnaClientAgentMibFieldsMask_Object = MibTableColumn
rlSnaClientAgentMibFieldsMask = _RlSnaClientAgentMibFieldsMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229, 2, 1, 5),
    _RlSnaClientAgentMibFieldsMask_Type()
)
rlSnaClientAgentMibFieldsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSnaClientAgentMibFieldsMask.setStatus("current")


class _RlSnaClientAgentSecondaryMibName_Type(DisplayString):
    """Custom type rlSnaClientAgentSecondaryMibName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RlSnaClientAgentSecondaryMibName_Type.__name__ = "DisplayString"
_RlSnaClientAgentSecondaryMibName_Object = MibTableColumn
rlSnaClientAgentSecondaryMibName = _RlSnaClientAgentSecondaryMibName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229, 2, 1, 6),
    _RlSnaClientAgentSecondaryMibName_Type()
)
rlSnaClientAgentSecondaryMibName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSnaClientAgentSecondaryMibName.setStatus("current")


class _RlSnaClientAgentPollingEnable_Type(TruthValue):
    """Custom type rlSnaClientAgentPollingEnable based on TruthValue"""
    defaultValue = 2


_RlSnaClientAgentPollingEnable_Type.__name__ = "TruthValue"
_RlSnaClientAgentPollingEnable_Object = MibTableColumn
rlSnaClientAgentPollingEnable = _RlSnaClientAgentPollingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229, 2, 1, 7),
    _RlSnaClientAgentPollingEnable_Type()
)
rlSnaClientAgentPollingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSnaClientAgentPollingEnable.setStatus("current")


class _RlSnaClientAgentPollingInterval_Type(TimeInterval):
    """Custom type rlSnaClientAgentPollingInterval based on TimeInterval"""
    defaultValue = 12000


_RlSnaClientAgentPollingInterval_Type.__name__ = "TimeInterval"
_RlSnaClientAgentPollingInterval_Object = MibTableColumn
rlSnaClientAgentPollingInterval = _RlSnaClientAgentPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229, 2, 1, 8),
    _RlSnaClientAgentPollingInterval_Type()
)
rlSnaClientAgentPollingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSnaClientAgentPollingInterval.setStatus("current")
_RlSnaClientAgentStatus_Type = RowStatus
_RlSnaClientAgentStatus_Object = MibTableColumn
rlSnaClientAgentStatus = _RlSnaClientAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 229, 2, 1, 9),
    _RlSnaClientAgentStatus_Type()
)
rlSnaClientAgentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSnaClientAgentStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-DEBUGCAPABILITIES-MIB",
    **{"rlSna": rlSna,
       "rlSnaNextFreeSessionId": rlSnaNextFreeSessionId,
       "rlSnaClientAgentPollingTable": rlSnaClientAgentPollingTable,
       "rlSnaClientAgentPollingEntry": rlSnaClientAgentPollingEntry,
       "rlSnaClientAgentClientSessionId": rlSnaClientAgentClientSessionId,
       "rlSnaClientAgentAgentAddressType": rlSnaClientAgentAgentAddressType,
       "rlSnaClientAgentAgentAddress": rlSnaClientAgentAgentAddress,
       "rlSnaClientAgentMibName": rlSnaClientAgentMibName,
       "rlSnaClientAgentMibFieldsMask": rlSnaClientAgentMibFieldsMask,
       "rlSnaClientAgentSecondaryMibName": rlSnaClientAgentSecondaryMibName,
       "rlSnaClientAgentPollingEnable": rlSnaClientAgentPollingEnable,
       "rlSnaClientAgentPollingInterval": rlSnaClientAgentPollingInterval,
       "rlSnaClientAgentStatus": rlSnaClientAgentStatus}
)
