# SNMP MIB module (Axos-Trap-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\Axos-Trap-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:48 2025
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

(axosAlarmAdditionalInfo,
 axosAlarmAddress,
 axosAlarmCategory,
 axosAlarmIndex,
 axosAlarmInstanceId,
 axosAlarmName,
 axosAlarmServiceAffecting,
 axosAlarmSeverity,
 axosAlarmText,
 axosAlarmTime,
 axosAlarmTimeStamp,
 axosAlarmType,
 axosEventAdditionalInfo1,
 axosEventAdditionalInfo2,
 axosEventAdditionalInfo3,
 axosEventAdditionalInfo4,
 axosEventAdditionalInfo5,
 axosEventAdditionalInfo6,
 axosEventAdditionalInfo7) = mibBuilder.importSymbols(
    "AXOS-ALARM-MIB",
    "axosAlarmAdditionalInfo",
    "axosAlarmAddress",
    "axosAlarmCategory",
    "axosAlarmIndex",
    "axosAlarmInstanceId",
    "axosAlarmName",
    "axosAlarmServiceAffecting",
    "axosAlarmSeverity",
    "axosAlarmText",
    "axosAlarmTime",
    "axosAlarmTimeStamp",
    "axosAlarmType",
    "axosEventAdditionalInfo1",
    "axosEventAdditionalInfo2",
    "axosEventAdditionalInfo3",
    "axosEventAdditionalInfo4",
    "axosEventAdditionalInfo5",
    "axosEventAdditionalInfo6",
    "axosEventAdditionalInfo7")

(axosModules,) = mibBuilder.importSymbols(
    "CALIX-PRODUCT-MIB",
    "axosModules")

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

axosTrapModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    axosTrapModule.setRevisions(
        ("2016-04-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxosTrap_ObjectIdentity = ObjectIdentity
axosTrap = _AxosTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 1, 1)
)
_AxosNotificationObjects_ObjectIdentity = ObjectIdentity
axosNotificationObjects = _AxosNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 1, 1, 1)
)
_AxosTrapSequenceNo_Type = Integer32
_AxosTrapSequenceNo_Object = MibScalar
axosTrapSequenceNo = _AxosTrapSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 1, 1, 1, 1),
    _AxosTrapSequenceNo_Type()
)
axosTrapSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosTrapSequenceNo.setStatus("current")
_AxosNotifications_ObjectIdentity = ObjectIdentity
axosNotifications = _AxosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 1, 1, 2)
)

# Managed Objects groups


# Notification objects

axosTrapAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 1, 1, 2, 1)
)
axosTrapAlarmRaised.setObjects(
      *(("Axos-Trap-MIB", "axosTrapSequenceNo"),
        ("AXOS-ALARM-MIB", "axosAlarmIndex"),
        ("AXOS-ALARM-MIB", "axosAlarmName"),
        ("AXOS-ALARM-MIB", "axosAlarmType"),
        ("AXOS-ALARM-MIB", "axosAlarmCategory"),
        ("AXOS-ALARM-MIB", "axosAlarmInstanceId"),
        ("AXOS-ALARM-MIB", "axosAlarmSeverity"),
        ("AXOS-ALARM-MIB", "axosAlarmServiceAffecting"),
        ("AXOS-ALARM-MIB", "axosAlarmAddress"),
        ("AXOS-ALARM-MIB", "axosAlarmText"),
        ("AXOS-ALARM-MIB", "axosAlarmTimeStamp"),
        ("AXOS-ALARM-MIB", "axosAlarmTime"),
        ("AXOS-ALARM-MIB", "axosAlarmAdditionalInfo"))
)
if mibBuilder.loadTexts:
    axosTrapAlarmRaised.setStatus(
        "current"
    )

axosTrapAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 1, 1, 2, 2)
)
axosTrapAlarmCleared.setObjects(
      *(("Axos-Trap-MIB", "axosTrapSequenceNo"),
        ("AXOS-ALARM-MIB", "axosAlarmIndex"),
        ("AXOS-ALARM-MIB", "axosAlarmName"),
        ("AXOS-ALARM-MIB", "axosAlarmType"),
        ("AXOS-ALARM-MIB", "axosAlarmCategory"),
        ("AXOS-ALARM-MIB", "axosAlarmInstanceId"),
        ("AXOS-ALARM-MIB", "axosAlarmSeverity"),
        ("AXOS-ALARM-MIB", "axosAlarmServiceAffecting"),
        ("AXOS-ALARM-MIB", "axosAlarmAddress"),
        ("AXOS-ALARM-MIB", "axosAlarmText"),
        ("AXOS-ALARM-MIB", "axosAlarmTimeStamp"),
        ("AXOS-ALARM-MIB", "axosAlarmTime"),
        ("AXOS-ALARM-MIB", "axosAlarmAdditionalInfo"))
)
if mibBuilder.loadTexts:
    axosTrapAlarmCleared.setStatus(
        "current"
    )

axosTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 1, 1, 2, 3)
)
axosTrapEvent.setObjects(
      *(("Axos-Trap-MIB", "axosTrapSequenceNo"),
        ("AXOS-ALARM-MIB", "axosAlarmIndex"),
        ("AXOS-ALARM-MIB", "axosAlarmName"),
        ("AXOS-ALARM-MIB", "axosAlarmType"),
        ("AXOS-ALARM-MIB", "axosAlarmCategory"),
        ("AXOS-ALARM-MIB", "axosAlarmAddress"),
        ("AXOS-ALARM-MIB", "axosAlarmText"),
        ("AXOS-ALARM-MIB", "axosAlarmTimeStamp"),
        ("AXOS-ALARM-MIB", "axosAlarmTime"),
        ("AXOS-ALARM-MIB", "axosEventAdditionalInfo1"),
        ("AXOS-ALARM-MIB", "axosEventAdditionalInfo2"),
        ("AXOS-ALARM-MIB", "axosEventAdditionalInfo3"),
        ("AXOS-ALARM-MIB", "axosEventAdditionalInfo4"),
        ("AXOS-ALARM-MIB", "axosEventAdditionalInfo5"),
        ("AXOS-ALARM-MIB", "axosEventAdditionalInfo6"),
        ("AXOS-ALARM-MIB", "axosEventAdditionalInfo7"))
)
if mibBuilder.loadTexts:
    axosTrapEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Axos-Trap-MIB",
    **{"axosTrapModule": axosTrapModule,
       "axosTrap": axosTrap,
       "axosNotificationObjects": axosNotificationObjects,
       "axosTrapSequenceNo": axosTrapSequenceNo,
       "axosNotifications": axosNotifications,
       "axosTrapAlarmRaised": axosTrapAlarmRaised,
       "axosTrapAlarmCleared": axosTrapAlarmCleared,
       "axosTrapEvent": axosTrapEvent}
)
