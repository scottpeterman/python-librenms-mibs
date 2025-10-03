# SNMP MIB module (STORMSHIELD-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-ALARM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:57 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(snsNotifications,
 stormshieldMIB) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "snsNotifications",
    "stormshieldMIB")


# MODULE-IDENTITY

snsAlarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5)
)
if mibBuilder.loadTexts:
    snsAlarm.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsATable_Object = MibTable
snsATable = _SnsATable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0)
)
if mibBuilder.loadTexts:
    snsATable.setStatus("current")
_SnsAEntry_Object = MibTableRow
snsAEntry = _SnsAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1)
)
snsAEntry.setIndexNames(
    (0, "STORMSHIELD-ALARM-MIB", "snsAIndex"),
)
if mibBuilder.loadTexts:
    snsAEntry.setStatus("current")


class _SnsAIndex_Type(Integer32):
    """Custom type snsAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnsAIndex_Type.__name__ = "Integer32"
_SnsAIndex_Object = MibTableColumn
snsAIndex = _SnsAIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 0),
    _SnsAIndex_Type()
)
snsAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snsAIndex.setStatus("current")
_SnsATime_Type = OctetString
_SnsATime_Object = MibTableColumn
snsATime = _SnsATime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 1),
    _SnsATime_Type()
)
snsATime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsATime.setStatus("current")
_SnsASif_Type = OctetString
_SnsASif_Object = MibTableColumn
snsASif = _SnsASif_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 2),
    _SnsASif_Type()
)
snsASif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASif.setStatus("current")
_SnsADif_Type = OctetString
_SnsADif_Object = MibTableColumn
snsADif = _SnsADif_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 3),
    _SnsADif_Type()
)
snsADif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsADif.setStatus("current")
_SnsAProto_Type = OctetString
_SnsAProto_Object = MibTableColumn
snsAProto = _SnsAProto_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 4),
    _SnsAProto_Type()
)
snsAProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAProto.setStatus("current")
_SnsASaddr_Type = OctetString
_SnsASaddr_Object = MibTableColumn
snsASaddr = _SnsASaddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 5),
    _SnsASaddr_Type()
)
snsASaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASaddr.setStatus("current")
_SnsADaddr_Type = OctetString
_SnsADaddr_Object = MibTableColumn
snsADaddr = _SnsADaddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 6),
    _SnsADaddr_Type()
)
snsADaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsADaddr.setStatus("current")
_SnsASport_Type = Integer32
_SnsASport_Object = MibTableColumn
snsASport = _SnsASport_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 7),
    _SnsASport_Type()
)
snsASport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASport.setStatus("current")
_SnsADport_Type = Integer32
_SnsADport_Object = MibTableColumn
snsADport = _SnsADport_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 8),
    _SnsADport_Type()
)
snsADport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsADport.setStatus("current")
_SnsASname_Type = OctetString
_SnsASname_Object = MibTableColumn
snsASname = _SnsASname_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 9),
    _SnsASname_Type()
)
snsASname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsASname.setStatus("current")
_SnsADname_Type = OctetString
_SnsADname_Object = MibTableColumn
snsADname = _SnsADname_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 10),
    _SnsADname_Type()
)
snsADname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsADname.setStatus("current")
_SnsAMessage_Type = SnmpAdminString
_SnsAMessage_Object = MibTableColumn
snsAMessage = _SnsAMessage_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 11),
    _SnsAMessage_Type()
)
snsAMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAMessage.setStatus("current")
_SnsAicmpTable_Object = MibTable
snsAicmpTable = _SnsAicmpTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1)
)
if mibBuilder.loadTexts:
    snsAicmpTable.setStatus("current")
_SnsAicmpEntry_Object = MibTableRow
snsAicmpEntry = _SnsAicmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1)
)
snsAicmpEntry.setIndexNames(
    (0, "STORMSHIELD-ALARM-MIB", "snsAicmpIndex"),
)
if mibBuilder.loadTexts:
    snsAicmpEntry.setStatus("current")


class _SnsAicmpIndex_Type(Integer32):
    """Custom type snsAicmpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnsAicmpIndex_Type.__name__ = "Integer32"
_SnsAicmpIndex_Object = MibTableColumn
snsAicmpIndex = _SnsAicmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 0),
    _SnsAicmpIndex_Type()
)
snsAicmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snsAicmpIndex.setStatus("current")
_SnsAicmpTime_Type = OctetString
_SnsAicmpTime_Object = MibTableColumn
snsAicmpTime = _SnsAicmpTime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 1),
    _SnsAicmpTime_Type()
)
snsAicmpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAicmpTime.setStatus("current")
_SnsAicmpSif_Type = OctetString
_SnsAicmpSif_Object = MibTableColumn
snsAicmpSif = _SnsAicmpSif_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 2),
    _SnsAicmpSif_Type()
)
snsAicmpSif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAicmpSif.setStatus("current")
_SnsAicmpDif_Type = OctetString
_SnsAicmpDif_Object = MibTableColumn
snsAicmpDif = _SnsAicmpDif_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 3),
    _SnsAicmpDif_Type()
)
snsAicmpDif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAicmpDif.setStatus("current")
_SnsAicmpSaddr_Type = OctetString
_SnsAicmpSaddr_Object = MibTableColumn
snsAicmpSaddr = _SnsAicmpSaddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 4),
    _SnsAicmpSaddr_Type()
)
snsAicmpSaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAicmpSaddr.setStatus("current")
_SnsAicmpDaddr_Type = OctetString
_SnsAicmpDaddr_Object = MibTableColumn
snsAicmpDaddr = _SnsAicmpDaddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 5),
    _SnsAicmpDaddr_Type()
)
snsAicmpDaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAicmpDaddr.setStatus("current")
_SnsAicmpType_Type = Integer32
_SnsAicmpType_Object = MibTableColumn
snsAicmpType = _SnsAicmpType_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 6),
    _SnsAicmpType_Type()
)
snsAicmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAicmpType.setStatus("current")
_SnsAicmpCode_Type = Integer32
_SnsAicmpCode_Object = MibTableColumn
snsAicmpCode = _SnsAicmpCode_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 7),
    _SnsAicmpCode_Type()
)
snsAicmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAicmpCode.setStatus("current")
_SnsAicmpSname_Type = OctetString
_SnsAicmpSname_Object = MibTableColumn
snsAicmpSname = _SnsAicmpSname_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 8),
    _SnsAicmpSname_Type()
)
snsAicmpSname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAicmpSname.setStatus("current")
_SnsAicmpDname_Type = OctetString
_SnsAicmpDname_Object = MibTableColumn
snsAicmpDname = _SnsAicmpDname_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 9),
    _SnsAicmpDname_Type()
)
snsAicmpDname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAicmpDname.setStatus("current")
_SnsAicmpMessage_Type = SnmpAdminString
_SnsAicmpMessage_Object = MibTableColumn
snsAicmpMessage = _SnsAicmpMessage_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 10),
    _SnsAicmpMessage_Type()
)
snsAicmpMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAicmpMessage.setStatus("current")

# Managed Objects groups


# Notification objects

snsNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11256, 1, 6, 1)
)
snsNotification.setObjects(
      *(("STORMSHIELD-ALARM-MIB", "snsATime"),
        ("STORMSHIELD-ALARM-MIB", "snsASif"),
        ("STORMSHIELD-ALARM-MIB", "snsASaddr"),
        ("STORMSHIELD-ALARM-MIB", "snsADaddr"),
        ("STORMSHIELD-ALARM-MIB", "snsAMessage"))
)
if mibBuilder.loadTexts:
    snsNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-ALARM-MIB",
    **{"snsAlarm": snsAlarm,
       "snsATable": snsATable,
       "snsAEntry": snsAEntry,
       "snsAIndex": snsAIndex,
       "snsATime": snsATime,
       "snsASif": snsASif,
       "snsADif": snsADif,
       "snsAProto": snsAProto,
       "snsASaddr": snsASaddr,
       "snsADaddr": snsADaddr,
       "snsASport": snsASport,
       "snsADport": snsADport,
       "snsASname": snsASname,
       "snsADname": snsADname,
       "snsAMessage": snsAMessage,
       "snsAicmpTable": snsAicmpTable,
       "snsAicmpEntry": snsAicmpEntry,
       "snsAicmpIndex": snsAicmpIndex,
       "snsAicmpTime": snsAicmpTime,
       "snsAicmpSif": snsAicmpSif,
       "snsAicmpDif": snsAicmpDif,
       "snsAicmpSaddr": snsAicmpSaddr,
       "snsAicmpDaddr": snsAicmpDaddr,
       "snsAicmpType": snsAicmpType,
       "snsAicmpCode": snsAicmpCode,
       "snsAicmpSname": snsAicmpSname,
       "snsAicmpDname": snsAicmpDname,
       "snsAicmpMessage": snsAicmpMessage,
       "snsNotification": snsNotification}
)
