# SNMP MIB module (TN-SYS-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-SYS-LOG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:30 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnDevMgmt,) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnDevMgmt")


# MODULE-IDENTITY

tnSyslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogLevelValue(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("emerg", 1),
          ("alert", 2),
          ("crit", 3),
          ("err", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )



class SyslogLevelValueAll(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("emerg", 1),
          ("alert", 2),
          ("crit", 3),
          ("err", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )



# MIB Managed Objects in the order of their OIDs

_TnSyslogMgmtTable_Object = MibTable
tnSyslogMgmtTable = _TnSyslogMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 1)
)
if mibBuilder.loadTexts:
    tnSyslogMgmtTable.setStatus("current")
_TnSyslogMgmtEntry_Object = MibTableRow
tnSyslogMgmtEntry = _TnSyslogMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 1, 1)
)
tnSyslogMgmtEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnSyslogMgmtEntry.setStatus("current")
_TnSyslogServerAddrType_Type = InetAddressType
_TnSyslogServerAddrType_Object = MibTableColumn
tnSyslogServerAddrType = _TnSyslogServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 1, 1, 1),
    _TnSyslogServerAddrType_Type()
)
tnSyslogServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogServerAddrType.setStatus("current")
_TnSyslogServerAddr_Type = InetAddress
_TnSyslogServerAddr_Object = MibTableColumn
tnSyslogServerAddr = _TnSyslogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 1, 1, 2),
    _TnSyslogServerAddr_Type()
)
tnSyslogServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogServerAddr.setStatus("current")


class _TnSyslogServerPort_Type(Integer32):
    """Custom type tnSyslogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSyslogServerPort_Type.__name__ = "Integer32"
_TnSyslogServerPort_Object = MibTableColumn
tnSyslogServerPort = _TnSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 1, 1, 3),
    _TnSyslogServerPort_Type()
)
tnSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogServerPort.setStatus("current")
_TnSyslogLevel_Type = SyslogLevelValue
_TnSyslogLevel_Object = MibTableColumn
tnSyslogLevel = _TnSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 1, 1, 4),
    _TnSyslogLevel_Type()
)
tnSyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogLevel.setStatus("current")


class _TnSyslogMode_Type(Integer32):
    """Custom type tnSyslogMode based on Integer32"""
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
        *(("logLocal", 1),
          ("logRemote", 2),
          ("logLocalAndRemote", 3),
          ("off", 4))
    )


_TnSyslogMode_Type.__name__ = "Integer32"
_TnSyslogMode_Object = MibTableColumn
tnSyslogMode = _TnSyslogMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 1, 1, 5),
    _TnSyslogMode_Type()
)
tnSyslogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogMode.setStatus("current")


class _TnSyslogLocalFileName_Type(DisplayString):
    """Custom type tnSyslogLocalFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TnSyslogLocalFileName_Type.__name__ = "DisplayString"
_TnSyslogLocalFileName_Object = MibTableColumn
tnSyslogLocalFileName = _TnSyslogLocalFileName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 1, 1, 6),
    _TnSyslogLocalFileName_Type()
)
tnSyslogLocalFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogLocalFileName.setStatus("current")


class _TnSyslogServerEnable_Type(Integer32):
    """Custom type tnSyslogServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnSyslogServerEnable_Type.__name__ = "Integer32"
_TnSyslogServerEnable_Object = MibTableColumn
tnSyslogServerEnable = _TnSyslogServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 1, 1, 7),
    _TnSyslogServerEnable_Type()
)
tnSyslogServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogServerEnable.setStatus("current")
_TnSyslogMessageTable_Object = MibTable
tnSyslogMessageTable = _TnSyslogMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 2)
)
if mibBuilder.loadTexts:
    tnSyslogMessageTable.setStatus("current")
_TnSyslogMessageEntry_Object = MibTableRow
tnSyslogMessageEntry = _TnSyslogMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 2, 1)
)
tnSyslogMessageEntry.setIndexNames(
    (0, "TN-SYS-LOG-MIB", "tnSyslogMessageId"),
)
if mibBuilder.loadTexts:
    tnSyslogMessageEntry.setStatus("current")
_TnSyslogMessageId_Type = Integer32
_TnSyslogMessageId_Object = MibTableColumn
tnSyslogMessageId = _TnSyslogMessageId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 2, 1, 1),
    _TnSyslogMessageId_Type()
)
tnSyslogMessageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyslogMessageId.setStatus("current")
_TnSyslogMessageTime_Type = DisplayString
_TnSyslogMessageTime_Object = MibTableColumn
tnSyslogMessageTime = _TnSyslogMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 2, 1, 2),
    _TnSyslogMessageTime_Type()
)
tnSyslogMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyslogMessageTime.setStatus("current")
_TnSyslogMessageLevel_Type = SyslogLevelValue
_TnSyslogMessageLevel_Object = MibTableColumn
tnSyslogMessageLevel = _TnSyslogMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 2, 1, 3),
    _TnSyslogMessageLevel_Type()
)
tnSyslogMessageLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyslogMessageLevel.setStatus("current")
_TnSyslogMessage_Type = DisplayString
_TnSyslogMessage_Object = MibTableColumn
tnSyslogMessage = _TnSyslogMessage_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 2, 1, 4),
    _TnSyslogMessage_Type()
)
tnSyslogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyslogMessage.setStatus("current")
_TnSyslogExtTable_Object = MibTable
tnSyslogExtTable = _TnSyslogExtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 3)
)
if mibBuilder.loadTexts:
    tnSyslogExtTable.setStatus("current")
_TnSyslogExtEntry_Object = MibTableRow
tnSyslogExtEntry = _TnSyslogExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 3, 1)
)
tnSyslogExtEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnSyslogExtEntry.setStatus("current")
_TnSyslogQueryLevel_Type = SyslogLevelValueAll
_TnSyslogQueryLevel_Object = MibTableColumn
tnSyslogQueryLevel = _TnSyslogQueryLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 3, 1, 1),
    _TnSyslogQueryLevel_Type()
)
tnSyslogQueryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogQueryLevel.setStatus("current")
_TnSyslogClearLevel_Type = SyslogLevelValueAll
_TnSyslogClearLevel_Object = MibTableColumn
tnSyslogClearLevel = _TnSyslogClearLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 3, 1, 2),
    _TnSyslogClearLevel_Type()
)
tnSyslogClearLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogClearLevel.setStatus("current")
_TnSyslogClear_Type = TruthValue
_TnSyslogClear_Object = MibTableColumn
tnSyslogClear = _TnSyslogClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 18, 3, 1, 3),
    _TnSyslogClear_Type()
)
tnSyslogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SYS-LOG-MIB",
    **{"SyslogLevelValue": SyslogLevelValue,
       "SyslogLevelValueAll": SyslogLevelValueAll,
       "tnSyslogMIB": tnSyslogMIB,
       "tnSyslogMgmtTable": tnSyslogMgmtTable,
       "tnSyslogMgmtEntry": tnSyslogMgmtEntry,
       "tnSyslogServerAddrType": tnSyslogServerAddrType,
       "tnSyslogServerAddr": tnSyslogServerAddr,
       "tnSyslogServerPort": tnSyslogServerPort,
       "tnSyslogLevel": tnSyslogLevel,
       "tnSyslogMode": tnSyslogMode,
       "tnSyslogLocalFileName": tnSyslogLocalFileName,
       "tnSyslogServerEnable": tnSyslogServerEnable,
       "tnSyslogMessageTable": tnSyslogMessageTable,
       "tnSyslogMessageEntry": tnSyslogMessageEntry,
       "tnSyslogMessageId": tnSyslogMessageId,
       "tnSyslogMessageTime": tnSyslogMessageTime,
       "tnSyslogMessageLevel": tnSyslogMessageLevel,
       "tnSyslogMessage": tnSyslogMessage,
       "tnSyslogExtTable": tnSyslogExtTable,
       "tnSyslogExtEntry": tnSyslogExtEntry,
       "tnSyslogQueryLevel": tnSyslogQueryLevel,
       "tnSyslogClearLevel": tnSyslogClearLevel,
       "tnSyslogClear": tnSyslogClear}
)
