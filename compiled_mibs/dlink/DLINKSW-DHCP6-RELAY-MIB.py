# SNMP MIB module (DLINKSW-DHCP6-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DHCP6-RELAY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:56 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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

dlinkSwDhcp6RelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 88)
)
if mibBuilder.loadTexts:
    dlinkSwDhcp6RelayMIB.setRevisions(
        ("2013-01-18 00:00",
         "2013-09-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RemoteIdType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("cidWithUserDefine", 2),
          ("userDefine", 3))
    )



# MIB Managed Objects in the order of their OIDs

_DDhcp6RelayMIBNotifications_ObjectIdentity = ObjectIdentity
dDhcp6RelayMIBNotifications = _DDhcp6RelayMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 0)
)
_DDhcp6RelayMIBObjects_ObjectIdentity = ObjectIdentity
dDhcp6RelayMIBObjects = _DDhcp6RelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1)
)
_DDhcp6RelayGeneral_ObjectIdentity = ObjectIdentity
dDhcp6RelayGeneral = _DDhcp6RelayGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 1)
)


class _DDhcp6RRemoteIdInsertEnabled_Type(TruthValue):
    """Custom type dDhcp6RRemoteIdInsertEnabled based on TruthValue"""
    defaultValue = 2


_DDhcp6RRemoteIdInsertEnabled_Type.__name__ = "TruthValue"
_DDhcp6RRemoteIdInsertEnabled_Object = MibScalar
dDhcp6RRemoteIdInsertEnabled = _DDhcp6RRemoteIdInsertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 1, 1),
    _DDhcp6RRemoteIdInsertEnabled_Type()
)
dDhcp6RRemoteIdInsertEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcp6RRemoteIdInsertEnabled.setStatus("current")


class _DDhcp6RRemoteIdPolicy_Type(Integer32):
    """Custom type dDhcp6RRemoteIdPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("keep", 2))
    )


_DDhcp6RRemoteIdPolicy_Type.__name__ = "Integer32"
_DDhcp6RRemoteIdPolicy_Object = MibScalar
dDhcp6RRemoteIdPolicy = _DDhcp6RRemoteIdPolicy_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 1, 2),
    _DDhcp6RRemoteIdPolicy_Type()
)
dDhcp6RRemoteIdPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcp6RRemoteIdPolicy.setStatus("current")
_DDhcp6RRemoteIdFormat_Type = RemoteIdType
_DDhcp6RRemoteIdFormat_Object = MibScalar
dDhcp6RRemoteIdFormat = _DDhcp6RRemoteIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 1, 3),
    _DDhcp6RRemoteIdFormat_Type()
)
dDhcp6RRemoteIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcp6RRemoteIdFormat.setStatus("current")


class _DDhcp6RRemoteIdUdfType_Type(Integer32):
    """Custom type dDhcp6RRemoteIdUdfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("string", 1),
          ("hex", 2))
    )


_DDhcp6RRemoteIdUdfType_Type.__name__ = "Integer32"
_DDhcp6RRemoteIdUdfType_Object = MibScalar
dDhcp6RRemoteIdUdfType = _DDhcp6RRemoteIdUdfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 1, 4),
    _DDhcp6RRemoteIdUdfType_Type()
)
dDhcp6RRemoteIdUdfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcp6RRemoteIdUdfType.setStatus("current")
_DDhcp6RRemoteIdUdfValue_Type = DisplayString
_DDhcp6RRemoteIdUdfValue_Object = MibScalar
dDhcp6RRemoteIdUdfValue = _DDhcp6RRemoteIdUdfValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 1, 5),
    _DDhcp6RRemoteIdUdfValue_Type()
)
dDhcp6RRemoteIdUdfValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcp6RRemoteIdUdfValue.setStatus("current")
_DDhcp6RelayIfObjects_ObjectIdentity = ObjectIdentity
dDhcp6RelayIfObjects = _DDhcp6RelayIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2)
)
_DDhcp6RIfRelayDestTable_Object = MibTable
dDhcp6RIfRelayDestTable = _DDhcp6RIfRelayDestTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dDhcp6RIfRelayDestTable.setStatus("current")
_DDhcp6RIfRelayDestEntry_Object = MibTableRow
dDhcp6RIfRelayDestEntry = _DDhcp6RIfRelayDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2, 1, 1)
)
dDhcp6RIfRelayDestEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RIfRelayDestIndex"),
    (0, "DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RIfRelayDestDestAddr"),
    (0, "DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RIfRelayDestOutIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcp6RIfRelayDestEntry.setStatus("current")
_DDhcp6RIfRelayDestIndex_Type = InterfaceIndex
_DDhcp6RIfRelayDestIndex_Object = MibTableColumn
dDhcp6RIfRelayDestIndex = _DDhcp6RIfRelayDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2, 1, 1, 1),
    _DDhcp6RIfRelayDestIndex_Type()
)
dDhcp6RIfRelayDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6RIfRelayDestIndex.setStatus("current")
_DDhcp6RIfRelayDestDestAddr_Type = InetAddressIPv6
_DDhcp6RIfRelayDestDestAddr_Object = MibTableColumn
dDhcp6RIfRelayDestDestAddr = _DDhcp6RIfRelayDestDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2, 1, 1, 2),
    _DDhcp6RIfRelayDestDestAddr_Type()
)
dDhcp6RIfRelayDestDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6RIfRelayDestDestAddr.setStatus("current")
_DDhcp6RIfRelayDestOutIfIndex_Type = InterfaceIndexOrZero
_DDhcp6RIfRelayDestOutIfIndex_Object = MibTableColumn
dDhcp6RIfRelayDestOutIfIndex = _DDhcp6RIfRelayDestOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2, 1, 1, 3),
    _DDhcp6RIfRelayDestOutIfIndex_Type()
)
dDhcp6RIfRelayDestOutIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6RIfRelayDestOutIfIndex.setStatus("current")
_DDhcp6RIfRelayDestRowStatus_Type = RowStatus
_DDhcp6RIfRelayDestRowStatus_Object = MibTableColumn
dDhcp6RIfRelayDestRowStatus = _DDhcp6RIfRelayDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2, 1, 1, 4),
    _DDhcp6RIfRelayDestRowStatus_Type()
)
dDhcp6RIfRelayDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6RIfRelayDestRowStatus.setStatus("current")
_DDhcp6RelayMIBConformance_ObjectIdentity = ObjectIdentity
dDhcp6RelayMIBConformance = _DDhcp6RelayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 2)
)
_DDhcp6RelayCompliances_ObjectIdentity = ObjectIdentity
dDhcp6RelayCompliances = _DDhcp6RelayCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 2, 1)
)
_DDhcp6RelayGroups_ObjectIdentity = ObjectIdentity
dDhcp6RelayGroups = _DDhcp6RelayGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 2, 2)
)

# Managed Objects groups

dDhcp6RBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 2, 2, 1)
)
dDhcp6RBasicGroup.setObjects(
    ("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RIfRelayDestRowStatus")
)
if mibBuilder.loadTexts:
    dDhcp6RBasicGroup.setStatus("current")

dDhcp6RelayOption37Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 2, 2, 2)
)
dDhcp6RelayOption37Group.setObjects(
      *(("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RRemoteIdInsertEnabled"),
        ("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RRemoteIdPolicy"),
        ("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RRemoteIdFormat"),
        ("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RRemoteIdUdfType"),
        ("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RRemoteIdUdfValue"))
)
if mibBuilder.loadTexts:
    dDhcp6RelayOption37Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dDhcp6RelayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 88, 2, 1, 1)
)
dDhcp6RelayCompliance.setObjects(
      *(("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RBasicGroup"),
        ("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RelayOption37Group"))
)
if mibBuilder.loadTexts:
    dDhcp6RelayCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DHCP6-RELAY-MIB",
    **{"RemoteIdType": RemoteIdType,
       "dlinkSwDhcp6RelayMIB": dlinkSwDhcp6RelayMIB,
       "dDhcp6RelayMIBNotifications": dDhcp6RelayMIBNotifications,
       "dDhcp6RelayMIBObjects": dDhcp6RelayMIBObjects,
       "dDhcp6RelayGeneral": dDhcp6RelayGeneral,
       "dDhcp6RRemoteIdInsertEnabled": dDhcp6RRemoteIdInsertEnabled,
       "dDhcp6RRemoteIdPolicy": dDhcp6RRemoteIdPolicy,
       "dDhcp6RRemoteIdFormat": dDhcp6RRemoteIdFormat,
       "dDhcp6RRemoteIdUdfType": dDhcp6RRemoteIdUdfType,
       "dDhcp6RRemoteIdUdfValue": dDhcp6RRemoteIdUdfValue,
       "dDhcp6RelayIfObjects": dDhcp6RelayIfObjects,
       "dDhcp6RIfRelayDestTable": dDhcp6RIfRelayDestTable,
       "dDhcp6RIfRelayDestEntry": dDhcp6RIfRelayDestEntry,
       "dDhcp6RIfRelayDestIndex": dDhcp6RIfRelayDestIndex,
       "dDhcp6RIfRelayDestDestAddr": dDhcp6RIfRelayDestDestAddr,
       "dDhcp6RIfRelayDestOutIfIndex": dDhcp6RIfRelayDestOutIfIndex,
       "dDhcp6RIfRelayDestRowStatus": dDhcp6RIfRelayDestRowStatus,
       "dDhcp6RelayMIBConformance": dDhcp6RelayMIBConformance,
       "dDhcp6RelayCompliances": dDhcp6RelayCompliances,
       "dDhcp6RelayCompliance": dDhcp6RelayCompliance,
       "dDhcp6RelayGroups": dDhcp6RelayGroups,
       "dDhcp6RBasicGroup": dDhcp6RBasicGroup,
       "dDhcp6RelayOption37Group": dDhcp6RelayOption37Group}
)
