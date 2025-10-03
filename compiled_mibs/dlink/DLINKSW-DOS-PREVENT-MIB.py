# SNMP MIB module (DLINKSW-DOS-PREVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DOS-PREVENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:59 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

dlinkSwDosPrevMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 59)
)
if mibBuilder.loadTexts:
    dlinkSwDosPrevMIB.setRevisions(
        ("2013-05-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DosAttackType(TextualConvention, Integer32):
    status = "current"
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
              24,
              999)
        )
    )
    namedValues = NamedValues(
        *(("landAttack", 1),
          ("blatAttack", 2),
          ("smurfAttack", 3),
          ("tcpNullScan", 4),
          ("tcpXmasScan", 5),
          ("tcpSynFin", 6),
          ("tcpSynSrcPortLess1024", 7),
          ("arpMacSaMismatch", 8),
          ("fraggleAttack", 9),
          ("icmpRedirectAttack", 10),
          ("icmpUnreachableAttack", 11),
          ("ipRouteRecordAttack", 12),
          ("ipSourceRouteAttack", 13),
          ("pingDeathAttack", 14),
          ("tcpFlagSynRst", 15),
          ("tcpOverMacMcbc", 16),
          ("tcpSynWithData", 17),
          ("tcpTinyFragAttack", 18),
          ("tcpUdpPortZero", 19),
          ("tracertAttack", 20),
          ("winNukeAttack", 21),
          ("pingFlood", 22),
          ("synFlood", 23),
          ("teardrop", 24),
          ("all", 999))
    )



# MIB Managed Objects in the order of their OIDs

_DDosPrevMIBNotifications_ObjectIdentity = ObjectIdentity
dDosPrevMIBNotifications = _DDosPrevMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 0)
)
_DDosPrevMIBObjects_ObjectIdentity = ObjectIdentity
dDosPrevMIBObjects = _DDosPrevMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1)
)


class _DDosPrevGlobalNotifsEnabled_Type(TruthValue):
    """Custom type dDosPrevGlobalNotifsEnabled based on TruthValue"""
    defaultValue = 2


_DDosPrevGlobalNotifsEnabled_Type.__name__ = "TruthValue"
_DDosPrevGlobalNotifsEnabled_Object = MibScalar
dDosPrevGlobalNotifsEnabled = _DDosPrevGlobalNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 1),
    _DDosPrevGlobalNotifsEnabled_Type()
)
dDosPrevGlobalNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDosPrevGlobalNotifsEnabled.setStatus("current")
_DDosPrevNotifyInfo_ObjectIdentity = ObjectIdentity
dDosPrevNotifyInfo = _DDosPrevNotifyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 2)
)
_DDosPrevNotiInfoDropFramesCount_Type = Counter64
_DDosPrevNotiInfoDropFramesCount_Object = MibScalar
dDosPrevNotiInfoDropFramesCount = _DDosPrevNotiInfoDropFramesCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 2, 1),
    _DDosPrevNotiInfoDropFramesCount_Type()
)
dDosPrevNotiInfoDropFramesCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dDosPrevNotiInfoDropFramesCount.setStatus("current")
_DDosPrevNotiInfoDropIpAddr_Type = IpAddress
_DDosPrevNotiInfoDropIpAddr_Object = MibScalar
dDosPrevNotiInfoDropIpAddr = _DDosPrevNotiInfoDropIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 2, 2),
    _DDosPrevNotiInfoDropIpAddr_Type()
)
dDosPrevNotiInfoDropIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dDosPrevNotiInfoDropIpAddr.setStatus("current")
_DDosPrevNotiInfoDropPortNumber_Type = Integer32
_DDosPrevNotiInfoDropPortNumber_Object = MibScalar
dDosPrevNotiInfoDropPortNumber = _DDosPrevNotiInfoDropPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 2, 3),
    _DDosPrevNotiInfoDropPortNumber_Type()
)
dDosPrevNotiInfoDropPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dDosPrevNotiInfoDropPortNumber.setStatus("current")
_DDosPrevCtrlTable_Object = MibTable
dDosPrevCtrlTable = _DDosPrevCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 3)
)
if mibBuilder.loadTexts:
    dDosPrevCtrlTable.setStatus("current")
_DDosPrevCtrlEntry_Object = MibTableRow
dDosPrevCtrlEntry = _DDosPrevCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 3, 1)
)
dDosPrevCtrlEntry.setIndexNames(
    (0, "DLINKSW-DOS-PREVENT-MIB", "dDoSPrevCtrlAttackType"),
)
if mibBuilder.loadTexts:
    dDosPrevCtrlEntry.setStatus("current")
_DDoSPrevCtrlAttackType_Type = DosAttackType
_DDoSPrevCtrlAttackType_Object = MibTableColumn
dDoSPrevCtrlAttackType = _DDoSPrevCtrlAttackType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 3, 1, 1),
    _DDoSPrevCtrlAttackType_Type()
)
dDoSPrevCtrlAttackType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDoSPrevCtrlAttackType.setStatus("current")


class _DDoSPrevCtrlEnabled_Type(TruthValue):
    """Custom type dDoSPrevCtrlEnabled based on TruthValue"""
    defaultValue = 2


_DDoSPrevCtrlEnabled_Type.__name__ = "TruthValue"
_DDoSPrevCtrlEnabled_Object = MibTableColumn
dDoSPrevCtrlEnabled = _DDoSPrevCtrlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 3, 1, 2),
    _DDoSPrevCtrlEnabled_Type()
)
dDoSPrevCtrlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDoSPrevCtrlEnabled.setStatus("current")


class _DDoSPrevCtrlActionType_Type(Integer32):
    """Custom type dDoSPrevCtrlActionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("redirect", 2))
    )


_DDoSPrevCtrlActionType_Type.__name__ = "Integer32"
_DDoSPrevCtrlActionType_Object = MibTableColumn
dDoSPrevCtrlActionType = _DDoSPrevCtrlActionType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 3, 1, 3),
    _DDoSPrevCtrlActionType_Type()
)
dDoSPrevCtrlActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDoSPrevCtrlActionType.setStatus("current")


class _DDoSPrevCtrlRedirectPort_Type(InterfaceIndexOrZero):
    """Custom type dDoSPrevCtrlRedirectPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_DDoSPrevCtrlRedirectPort_Type.__name__ = "InterfaceIndexOrZero"
_DDoSPrevCtrlRedirectPort_Object = MibTableColumn
dDoSPrevCtrlRedirectPort = _DDoSPrevCtrlRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 3, 1, 4),
    _DDoSPrevCtrlRedirectPort_Type()
)
dDoSPrevCtrlRedirectPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDoSPrevCtrlRedirectPort.setStatus("current")


class _DDoSPrevCtrlRedirectPriority_Type(Integer32):
    """Custom type dDoSPrevCtrlRedirectPriority based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DDoSPrevCtrlRedirectPriority_Type.__name__ = "Integer32"
_DDoSPrevCtrlRedirectPriority_Object = MibTableColumn
dDoSPrevCtrlRedirectPriority = _DDoSPrevCtrlRedirectPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 3, 1, 5),
    _DDoSPrevCtrlRedirectPriority_Type()
)
dDoSPrevCtrlRedirectPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDoSPrevCtrlRedirectPriority.setStatus("current")


class _DDoSPrevCtrlRedirectRateLimit_Type(Unsigned32):
    """Custom type dDoSPrevCtrlRedirectRateLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_DDoSPrevCtrlRedirectRateLimit_Type.__name__ = "Unsigned32"
_DDoSPrevCtrlRedirectRateLimit_Object = MibTableColumn
dDoSPrevCtrlRedirectRateLimit = _DDoSPrevCtrlRedirectRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 3, 1, 6),
    _DDoSPrevCtrlRedirectRateLimit_Type()
)
dDoSPrevCtrlRedirectRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDoSPrevCtrlRedirectRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    dDoSPrevCtrlRedirectRateLimit.setUnits("kbps")
_DDoSPrevCounterTable_Object = MibTable
dDoSPrevCounterTable = _DDoSPrevCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 4)
)
if mibBuilder.loadTexts:
    dDoSPrevCounterTable.setStatus("current")
_DDoSPrevCounterEntry_Object = MibTableRow
dDoSPrevCounterEntry = _DDoSPrevCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 4, 1)
)
dDoSPrevCounterEntry.setIndexNames(
    (0, "DLINKSW-DOS-PREVENT-MIB", "dDoSPrevCounterAttackType"),
)
if mibBuilder.loadTexts:
    dDoSPrevCounterEntry.setStatus("current")
_DDoSPrevCounterAttackType_Type = DosAttackType
_DDoSPrevCounterAttackType_Object = MibTableColumn
dDoSPrevCounterAttackType = _DDoSPrevCounterAttackType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 4, 1, 1),
    _DDoSPrevCounterAttackType_Type()
)
dDoSPrevCounterAttackType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDoSPrevCounterAttackType.setStatus("current")
_DDoSPrevCounterFrameCount_Type = Counter64
_DDoSPrevCounterFrameCount_Object = MibTableColumn
dDoSPrevCounterFrameCount = _DDoSPrevCounterFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 4, 1, 2),
    _DDoSPrevCounterFrameCount_Type()
)
dDoSPrevCounterFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDoSPrevCounterFrameCount.setStatus("current")


class _DDoSPrevCounterClearCounter_Type(Integer32):
    """Custom type dDoSPrevCounterClearCounter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DDoSPrevCounterClearCounter_Type.__name__ = "Integer32"
_DDoSPrevCounterClearCounter_Object = MibTableColumn
dDoSPrevCounterClearCounter = _DDoSPrevCounterClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 1, 4, 1, 3),
    _DDoSPrevCounterClearCounter_Type()
)
dDoSPrevCounterClearCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDoSPrevCounterClearCounter.setStatus("current")
_DDosPrevMIBConformance_ObjectIdentity = ObjectIdentity
dDosPrevMIBConformance = _DDosPrevMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 2)
)
_DDosPrevMIBCompliances_ObjectIdentity = ObjectIdentity
dDosPrevMIBCompliances = _DDosPrevMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 2, 1)
)
_DDosPrevMIBGroups_ObjectIdentity = ObjectIdentity
dDosPrevMIBGroups = _DDosPrevMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 2, 2)
)

# Managed Objects groups

dDosPrevBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 2, 2, 1)
)
dDosPrevBasicGroup.setObjects(
      *(("DLINKSW-DOS-PREVENT-MIB", "dDoSPrevCtrlEnabled"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDoSPrevCounterFrameCount"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDoSPrevCounterClearCounter"))
)
if mibBuilder.loadTexts:
    dDosPrevBasicGroup.setStatus("current")

dDosPrevActionRedirectCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 2, 2, 2)
)
dDosPrevActionRedirectCtrlGroup.setObjects(
      *(("DLINKSW-DOS-PREVENT-MIB", "dDoSPrevCtrlActionType"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDoSPrevCtrlRedirectPort"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDoSPrevCtrlRedirectPriority"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDoSPrevCtrlRedirectRateLimit"))
)
if mibBuilder.loadTexts:
    dDosPrevActionRedirectCtrlGroup.setStatus("current")

dDosPrevNotifyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 2, 2, 3)
)
dDosPrevNotifyObjectGroup.setObjects(
      *(("DLINKSW-DOS-PREVENT-MIB", "dDosPrevGlobalNotifsEnabled"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDosPrevNotiInfoDropFramesCount"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDosPrevNotiInfoDropIpAddr"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDosPrevNotiInfoDropPortNumber"))
)
if mibBuilder.loadTexts:
    dDosPrevNotifyObjectGroup.setStatus("current")


# Notification objects

dDosPreveAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 0, 1)
)
dDosPreveAttackDetected.setObjects(
    ("DLINKSW-DOS-PREVENT-MIB", "dDosPrevNotiInfoDropFramesCount")
)
if mibBuilder.loadTexts:
    dDosPreveAttackDetected.setStatus(
        "current"
    )

dDosPreveAttackDetectedPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 0, 2)
)
dDosPreveAttackDetectedPacket.setObjects(
      *(("DLINKSW-DOS-PREVENT-MIB", "dDoSPrevCtrlAttackType"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDosPrevNotiInfoDropIpAddr"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDosPrevNotiInfoDropPortNumber"))
)
if mibBuilder.loadTexts:
    dDosPreveAttackDetectedPacket.setStatus(
        "current"
    )


# Notifications groups

dDosPrevNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 2, 2, 4)
)
dDosPrevNotificationsGroup.setObjects(
      *(("DLINKSW-DOS-PREVENT-MIB", "dDosPreveAttackDetected"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDosPreveAttackDetectedPacket"))
)
if mibBuilder.loadTexts:
    dDosPrevNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dDosPrevMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 59, 2, 1, 1)
)
dDosPrevMIBCompliance.setObjects(
      *(("DLINKSW-DOS-PREVENT-MIB", "dDosPrevBasicGroup"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDosPrevNotifyObjectGroup"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDosPrevNotificationsGroup"),
        ("DLINKSW-DOS-PREVENT-MIB", "dDosPrevActionRedirectCtrlGroup"))
)
if mibBuilder.loadTexts:
    dDosPrevMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DOS-PREVENT-MIB",
    **{"DosAttackType": DosAttackType,
       "dlinkSwDosPrevMIB": dlinkSwDosPrevMIB,
       "dDosPrevMIBNotifications": dDosPrevMIBNotifications,
       "dDosPreveAttackDetected": dDosPreveAttackDetected,
       "dDosPreveAttackDetectedPacket": dDosPreveAttackDetectedPacket,
       "dDosPrevMIBObjects": dDosPrevMIBObjects,
       "dDosPrevGlobalNotifsEnabled": dDosPrevGlobalNotifsEnabled,
       "dDosPrevNotifyInfo": dDosPrevNotifyInfo,
       "dDosPrevNotiInfoDropFramesCount": dDosPrevNotiInfoDropFramesCount,
       "dDosPrevNotiInfoDropIpAddr": dDosPrevNotiInfoDropIpAddr,
       "dDosPrevNotiInfoDropPortNumber": dDosPrevNotiInfoDropPortNumber,
       "dDosPrevCtrlTable": dDosPrevCtrlTable,
       "dDosPrevCtrlEntry": dDosPrevCtrlEntry,
       "dDoSPrevCtrlAttackType": dDoSPrevCtrlAttackType,
       "dDoSPrevCtrlEnabled": dDoSPrevCtrlEnabled,
       "dDoSPrevCtrlActionType": dDoSPrevCtrlActionType,
       "dDoSPrevCtrlRedirectPort": dDoSPrevCtrlRedirectPort,
       "dDoSPrevCtrlRedirectPriority": dDoSPrevCtrlRedirectPriority,
       "dDoSPrevCtrlRedirectRateLimit": dDoSPrevCtrlRedirectRateLimit,
       "dDoSPrevCounterTable": dDoSPrevCounterTable,
       "dDoSPrevCounterEntry": dDoSPrevCounterEntry,
       "dDoSPrevCounterAttackType": dDoSPrevCounterAttackType,
       "dDoSPrevCounterFrameCount": dDoSPrevCounterFrameCount,
       "dDoSPrevCounterClearCounter": dDoSPrevCounterClearCounter,
       "dDosPrevMIBConformance": dDosPrevMIBConformance,
       "dDosPrevMIBCompliances": dDosPrevMIBCompliances,
       "dDosPrevMIBCompliance": dDosPrevMIBCompliance,
       "dDosPrevMIBGroups": dDosPrevMIBGroups,
       "dDosPrevBasicGroup": dDosPrevBasicGroup,
       "dDosPrevActionRedirectCtrlGroup": dDosPrevActionRedirectCtrlGroup,
       "dDosPrevNotifyObjectGroup": dDosPrevNotifyObjectGroup,
       "dDosPrevNotificationsGroup": dDosPrevNotificationsGroup}
)
