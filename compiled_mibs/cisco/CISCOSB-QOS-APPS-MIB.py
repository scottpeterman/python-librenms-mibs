# SNMP MIB module (CISCOSB-QOS-APPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-QOS-APPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:22 2025
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

(rlQosApps,
 switch001) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "rlQosApps",
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlQosApps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232)
)
if mibBuilder.loadTexts:
    rlQosApps.setRevisions(
        ("2016-06-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlIscsiQos_ObjectIdentity = ObjectIdentity
rlIscsiQos = _RlIscsiQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1)
)
_RlIscsiQosEnable_Type = TruthValue
_RlIscsiQosEnable_Object = MibScalar
rlIscsiQosEnable = _RlIscsiQosEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 1),
    _RlIscsiQosEnable_Type()
)
rlIscsiQosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiQosEnable.setStatus("current")
_RlIscsiQosFlowTable_Object = MibTable
rlIscsiQosFlowTable = _RlIscsiQosFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 2)
)
if mibBuilder.loadTexts:
    rlIscsiQosFlowTable.setStatus("current")
_RlIscsiQosFlowEntry_Object = MibTableRow
rlIscsiQosFlowEntry = _RlIscsiQosFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 2, 1)
)
rlIscsiQosFlowEntry.setIndexNames(
    (0, "CISCOSB-QOS-APPS-MIB", "rlIscsiQosFlowDestTcpPort"),
    (0, "CISCOSB-QOS-APPS-MIB", "rlIscsiQosFlowType"),
    (0, "CISCOSB-QOS-APPS-MIB", "rlIscsiQosFlowDestAddressType"),
    (0, "CISCOSB-QOS-APPS-MIB", "rlIscsiQosFlowDestAddress"),
)
if mibBuilder.loadTexts:
    rlIscsiQosFlowEntry.setStatus("current")


class _RlIscsiQosFlowDestTcpPort_Type(Integer32):
    """Custom type rlIscsiQosFlowDestTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlIscsiQosFlowDestTcpPort_Type.__name__ = "Integer32"
_RlIscsiQosFlowDestTcpPort_Object = MibTableColumn
rlIscsiQosFlowDestTcpPort = _RlIscsiQosFlowDestTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 2, 1, 1),
    _RlIscsiQosFlowDestTcpPort_Type()
)
rlIscsiQosFlowDestTcpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiQosFlowDestTcpPort.setStatus("current")


class _RlIscsiQosFlowType_Type(Integer32):
    """Custom type rlIscsiQosFlowType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("both", 3))
    )


_RlIscsiQosFlowType_Type.__name__ = "Integer32"
_RlIscsiQosFlowType_Object = MibTableColumn
rlIscsiQosFlowType = _RlIscsiQosFlowType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 2, 1, 2),
    _RlIscsiQosFlowType_Type()
)
rlIscsiQosFlowType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiQosFlowType.setStatus("current")
_RlIscsiQosFlowDestAddressType_Type = InetAddressType
_RlIscsiQosFlowDestAddressType_Object = MibTableColumn
rlIscsiQosFlowDestAddressType = _RlIscsiQosFlowDestAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 2, 1, 3),
    _RlIscsiQosFlowDestAddressType_Type()
)
rlIscsiQosFlowDestAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiQosFlowDestAddressType.setStatus("current")
_RlIscsiQosFlowDestAddress_Type = InetAddress
_RlIscsiQosFlowDestAddress_Object = MibTableColumn
rlIscsiQosFlowDestAddress = _RlIscsiQosFlowDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 2, 1, 4),
    _RlIscsiQosFlowDestAddress_Type()
)
rlIscsiQosFlowDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiQosFlowDestAddress.setStatus("current")
_RlIscsiQosFlowStatus_Type = RowStatus
_RlIscsiQosFlowStatus_Object = MibTableColumn
rlIscsiQosFlowStatus = _RlIscsiQosFlowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 2, 1, 5),
    _RlIscsiQosFlowStatus_Type()
)
rlIscsiQosFlowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiQosFlowStatus.setStatus("current")
_RlIscsiQosProfileTable_Object = MibTable
rlIscsiQosProfileTable = _RlIscsiQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 3)
)
if mibBuilder.loadTexts:
    rlIscsiQosProfileTable.setStatus("current")
_RlIscsiQosProfileEntry_Object = MibTableRow
rlIscsiQosProfileEntry = _RlIscsiQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 3, 1)
)
rlIscsiQosProfileEntry.setIndexNames(
    (0, "CISCOSB-QOS-APPS-MIB", "rlIscsiQosProfileIndex"),
)
if mibBuilder.loadTexts:
    rlIscsiQosProfileEntry.setStatus("current")


class _RlIscsiQosProfileIndex_Type(Integer32):
    """Custom type rlIscsiQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlIscsiQosProfileIndex_Type.__name__ = "Integer32"
_RlIscsiQosProfileIndex_Object = MibTableColumn
rlIscsiQosProfileIndex = _RlIscsiQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 3, 1, 1),
    _RlIscsiQosProfileIndex_Type()
)
rlIscsiQosProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiQosProfileIndex.setStatus("current")


class _RlIscsiQosProfileVpt_Type(Integer32):
    """Custom type rlIscsiQosProfileVpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlIscsiQosProfileVpt_Type.__name__ = "Integer32"
_RlIscsiQosProfileVpt_Object = MibTableColumn
rlIscsiQosProfileVpt = _RlIscsiQosProfileVpt_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 3, 1, 2),
    _RlIscsiQosProfileVpt_Type()
)
rlIscsiQosProfileVpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiQosProfileVpt.setStatus("current")


class _RlIscsiQosProfileDscp_Type(Integer32):
    """Custom type rlIscsiQosProfileDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlIscsiQosProfileDscp_Type.__name__ = "Integer32"
_RlIscsiQosProfileDscp_Object = MibTableColumn
rlIscsiQosProfileDscp = _RlIscsiQosProfileDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 3, 1, 3),
    _RlIscsiQosProfileDscp_Type()
)
rlIscsiQosProfileDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiQosProfileDscp.setStatus("current")


class _RlIscsiQosProfileQueue_Type(Integer32):
    """Custom type rlIscsiQosProfileQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlIscsiQosProfileQueue_Type.__name__ = "Integer32"
_RlIscsiQosProfileQueue_Object = MibTableColumn
rlIscsiQosProfileQueue = _RlIscsiQosProfileQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 3, 1, 4),
    _RlIscsiQosProfileQueue_Type()
)
rlIscsiQosProfileQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiQosProfileQueue.setStatus("current")
_RlIscsiQosProfileStatus_Type = RowStatus
_RlIscsiQosProfileStatus_Object = MibTableColumn
rlIscsiQosProfileStatus = _RlIscsiQosProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 232, 1, 3, 1, 5),
    _RlIscsiQosProfileStatus_Type()
)
rlIscsiQosProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiQosProfileStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-QOS-APPS-MIB",
    **{"rlQosApps": rlQosApps,
       "rlIscsiQos": rlIscsiQos,
       "rlIscsiQosEnable": rlIscsiQosEnable,
       "rlIscsiQosFlowTable": rlIscsiQosFlowTable,
       "rlIscsiQosFlowEntry": rlIscsiQosFlowEntry,
       "rlIscsiQosFlowDestTcpPort": rlIscsiQosFlowDestTcpPort,
       "rlIscsiQosFlowType": rlIscsiQosFlowType,
       "rlIscsiQosFlowDestAddressType": rlIscsiQosFlowDestAddressType,
       "rlIscsiQosFlowDestAddress": rlIscsiQosFlowDestAddress,
       "rlIscsiQosFlowStatus": rlIscsiQosFlowStatus,
       "rlIscsiQosProfileTable": rlIscsiQosProfileTable,
       "rlIscsiQosProfileEntry": rlIscsiQosProfileEntry,
       "rlIscsiQosProfileIndex": rlIscsiQosProfileIndex,
       "rlIscsiQosProfileVpt": rlIscsiQosProfileVpt,
       "rlIscsiQosProfileDscp": rlIscsiQosProfileDscp,
       "rlIscsiQosProfileQueue": rlIscsiQosProfileQueue,
       "rlIscsiQosProfileStatus": rlIscsiQosProfileStatus}
)
