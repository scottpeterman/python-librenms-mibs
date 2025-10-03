# SNMP MIB module (CIENA-CES-SYSLOG-COLLECTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-SYSLOG-COLLECTOR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:55 2025
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

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesSyslogCollectorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40)
)
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorMIB.setRevisions(
        ("2017-06-07 00:00",
         "2016-07-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogFacility(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("kernel", 0),
          ("user", 1),
          ("mail", 2),
          ("daemon", 3),
          ("auth", 4),
          ("syslog", 5),
          ("lpr", 6),
          ("news", 7),
          ("uucp", 8),
          ("cron", 9),
          ("authPriv", 10),
          ("ftp", 11),
          ("ntp", 12),
          ("security", 13),
          ("console", 14),
          ("clockd2", 15),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("noMap", 24))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesSyslogCollMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesSyslogCollMIBObjects = _CienaCesSyslogCollMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1)
)
_CienaCesSyslogSystem_ObjectIdentity = ObjectIdentity
cienaCesSyslogSystem = _CienaCesSyslogSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 1)
)


class _CienaCesSyslogEnable_Type(CienaGlobalState):
    """Custom type cienaCesSyslogEnable based on CienaGlobalState"""
    defaultValue = 1


_CienaCesSyslogEnable_Type.__name__ = "CienaGlobalState"
_CienaCesSyslogEnable_Object = MibScalar
cienaCesSyslogEnable = _CienaCesSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 1, 1),
    _CienaCesSyslogEnable_Type()
)
cienaCesSyslogEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyslogEnable.setStatus("current")
_CienaCesSyslogColl_ObjectIdentity = ObjectIdentity
cienaCesSyslogColl = _CienaCesSyslogColl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2)
)
_CienaCesSyslogCollectorTable_Object = MibTable
cienaCesSyslogCollectorTable = _CienaCesSyslogCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorTable.setStatus("current")
_CienaCesSyslogCollectorEntry_Object = MibTableRow
cienaCesSyslogCollectorEntry = _CienaCesSyslogCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1, 1)
)
cienaCesSyslogCollectorEntry.setIndexNames(
    (0, "CIENA-CES-SYSLOG-COLLECTOR-MIB", "cienaCesSyslogIndex"),
)
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorEntry.setStatus("current")


class _CienaCesSyslogIndex_Type(Integer32):
    """Custom type cienaCesSyslogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CienaCesSyslogIndex_Type.__name__ = "Integer32"
_CienaCesSyslogIndex_Object = MibTableColumn
cienaCesSyslogIndex = _CienaCesSyslogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1, 1, 1),
    _CienaCesSyslogIndex_Type()
)
cienaCesSyslogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesSyslogIndex.setStatus("current")
_CienaCesSyslogCollectorAddr_Type = DisplayString
_CienaCesSyslogCollectorAddr_Object = MibTableColumn
cienaCesSyslogCollectorAddr = _CienaCesSyslogCollectorAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1, 1, 2),
    _CienaCesSyslogCollectorAddr_Type()
)
cienaCesSyslogCollectorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorAddr.setStatus("current")


class _CienaCesSyslogCollectorUDPPort_Type(Integer32):
    """Custom type cienaCesSyslogCollectorUDPPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesSyslogCollectorUDPPort_Type.__name__ = "Integer32"
_CienaCesSyslogCollectorUDPPort_Object = MibTableColumn
cienaCesSyslogCollectorUDPPort = _CienaCesSyslogCollectorUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1, 1, 3),
    _CienaCesSyslogCollectorUDPPort_Type()
)
cienaCesSyslogCollectorUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorUDPPort.setStatus("current")


class _CienaCesSyslogCollectorFacility_Type(SyslogFacility):
    """Custom type cienaCesSyslogCollectorFacility based on SyslogFacility"""
    defaultValue = 3


_CienaCesSyslogCollectorFacility_Type.__name__ = "SyslogFacility"
_CienaCesSyslogCollectorFacility_Object = MibTableColumn
cienaCesSyslogCollectorFacility = _CienaCesSyslogCollectorFacility_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1, 1, 4),
    _CienaCesSyslogCollectorFacility_Type()
)
cienaCesSyslogCollectorFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorFacility.setStatus("current")


class _CienaCesSyslogCollectorSeverityList_Type(Bits):
    """Custom type cienaCesSyslogCollectorSeverityList based on Bits"""
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("informational", 6),
          ("debug", 7))
    )

_CienaCesSyslogCollectorSeverityList_Type.__name__ = "Bits"
_CienaCesSyslogCollectorSeverityList_Object = MibTableColumn
cienaCesSyslogCollectorSeverityList = _CienaCesSyslogCollectorSeverityList_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1, 1, 5),
    _CienaCesSyslogCollectorSeverityList_Type()
)
cienaCesSyslogCollectorSeverityList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorSeverityList.setStatus("current")
_CienaCesSyslogCollectorUserAdminState_Type = CienaGlobalState
_CienaCesSyslogCollectorUserAdminState_Object = MibTableColumn
cienaCesSyslogCollectorUserAdminState = _CienaCesSyslogCollectorUserAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1, 1, 6),
    _CienaCesSyslogCollectorUserAdminState_Type()
)
cienaCesSyslogCollectorUserAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorUserAdminState.setStatus("current")
_CienaCesSyslogCollectorDhcpAdminState_Type = CienaGlobalState
_CienaCesSyslogCollectorDhcpAdminState_Object = MibTableColumn
cienaCesSyslogCollectorDhcpAdminState = _CienaCesSyslogCollectorDhcpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1, 1, 7),
    _CienaCesSyslogCollectorDhcpAdminState_Type()
)
cienaCesSyslogCollectorDhcpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorDhcpAdminState.setStatus("current")
_CienaCesSyslogCollectorOperState_Type = CienaGlobalState
_CienaCesSyslogCollectorOperState_Object = MibTableColumn
cienaCesSyslogCollectorOperState = _CienaCesSyslogCollectorOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1, 1, 8),
    _CienaCesSyslogCollectorOperState_Type()
)
cienaCesSyslogCollectorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorOperState.setStatus("current")


class _CienaCesSyslogCollectorCustomPrefix_Type(DisplayString):
    """Custom type cienaCesSyslogCollectorCustomPrefix based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CienaCesSyslogCollectorCustomPrefix_Type.__name__ = "DisplayString"
_CienaCesSyslogCollectorCustomPrefix_Object = MibTableColumn
cienaCesSyslogCollectorCustomPrefix = _CienaCesSyslogCollectorCustomPrefix_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1, 1, 9),
    _CienaCesSyslogCollectorCustomPrefix_Type()
)
cienaCesSyslogCollectorCustomPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorCustomPrefix.setStatus("current")
_CienaCesSyslogCollectorResolvedInetAddrType_Type = InetAddressType
_CienaCesSyslogCollectorResolvedInetAddrType_Object = MibTableColumn
cienaCesSyslogCollectorResolvedInetAddrType = _CienaCesSyslogCollectorResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1, 1, 10),
    _CienaCesSyslogCollectorResolvedInetAddrType_Type()
)
cienaCesSyslogCollectorResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorResolvedInetAddrType.setStatus("current")
_CienaCesSyslogCollectorResolvedInetAddress_Type = InetAddress
_CienaCesSyslogCollectorResolvedInetAddress_Object = MibTableColumn
cienaCesSyslogCollectorResolvedInetAddress = _CienaCesSyslogCollectorResolvedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 1, 2, 1, 1, 11),
    _CienaCesSyslogCollectorResolvedInetAddress_Type()
)
cienaCesSyslogCollectorResolvedInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyslogCollectorResolvedInetAddress.setStatus("current")
_CienaCesSyslogCollMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesSyslogCollMIBConformance = _CienaCesSyslogCollMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 3)
)
_CienaCesSyslogCollMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesSyslogCollMIBCompliances = _CienaCesSyslogCollMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 3, 1)
)
_CienaCesSyslogCollMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesSyslogCollMIBGroups = _CienaCesSyslogCollMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 40, 3, 2)
)
_CienaCesSyslogCollMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesSyslogCollMIBNotificationPrefix = _CienaCesSyslogCollMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 41)
)
_CienaCesSyslogCollMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesSyslogCollMIBNotifications = _CienaCesSyslogCollMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 41, 0)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-SYSLOG-COLLECTOR-MIB",
    **{"SyslogFacility": SyslogFacility,
       "cienaCesSyslogCollectorMIB": cienaCesSyslogCollectorMIB,
       "cienaCesSyslogCollMIBObjects": cienaCesSyslogCollMIBObjects,
       "cienaCesSyslogSystem": cienaCesSyslogSystem,
       "cienaCesSyslogEnable": cienaCesSyslogEnable,
       "cienaCesSyslogColl": cienaCesSyslogColl,
       "cienaCesSyslogCollectorTable": cienaCesSyslogCollectorTable,
       "cienaCesSyslogCollectorEntry": cienaCesSyslogCollectorEntry,
       "cienaCesSyslogIndex": cienaCesSyslogIndex,
       "cienaCesSyslogCollectorAddr": cienaCesSyslogCollectorAddr,
       "cienaCesSyslogCollectorUDPPort": cienaCesSyslogCollectorUDPPort,
       "cienaCesSyslogCollectorFacility": cienaCesSyslogCollectorFacility,
       "cienaCesSyslogCollectorSeverityList": cienaCesSyslogCollectorSeverityList,
       "cienaCesSyslogCollectorUserAdminState": cienaCesSyslogCollectorUserAdminState,
       "cienaCesSyslogCollectorDhcpAdminState": cienaCesSyslogCollectorDhcpAdminState,
       "cienaCesSyslogCollectorOperState": cienaCesSyslogCollectorOperState,
       "cienaCesSyslogCollectorCustomPrefix": cienaCesSyslogCollectorCustomPrefix,
       "cienaCesSyslogCollectorResolvedInetAddrType": cienaCesSyslogCollectorResolvedInetAddrType,
       "cienaCesSyslogCollectorResolvedInetAddress": cienaCesSyslogCollectorResolvedInetAddress,
       "cienaCesSyslogCollMIBConformance": cienaCesSyslogCollMIBConformance,
       "cienaCesSyslogCollMIBCompliances": cienaCesSyslogCollMIBCompliances,
       "cienaCesSyslogCollMIBGroups": cienaCesSyslogCollMIBGroups,
       "cienaCesSyslogCollMIBNotificationPrefix": cienaCesSyslogCollMIBNotificationPrefix,
       "cienaCesSyslogCollMIBNotifications": cienaCesSyslogCollMIBNotifications}
)
