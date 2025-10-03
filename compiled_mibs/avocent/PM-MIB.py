# SNMP MIB module (PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\avocent\PM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:10 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

pm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17)
)
if mibBuilder.loadTexts:
    pm.setRevisions(
        ("2010-11-24 00:00",
         "2010-09-24 00:00",
         "2010-04-14 00:00",
         "2009-05-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PmProducts_ObjectIdentity = ObjectIdentity
pmProducts = _PmProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1)
)
_Pm1024_ObjectIdentity = ObjectIdentity
pm1024 = _Pm1024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 1)
)
_Pm2003_ObjectIdentity = ObjectIdentity
pm2003 = _Pm2003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 2)
)
_Pm2006_ObjectIdentity = ObjectIdentity
pm2006 = _Pm2006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 3)
)
_Pm2024_ObjectIdentity = ObjectIdentity
pm2024 = _Pm2024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 4)
)
_Pm3003_ObjectIdentity = ObjectIdentity
pm3003 = _Pm3003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 5)
)
_Pm3006_ObjectIdentity = ObjectIdentity
pm3006 = _Pm3006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 6)
)
_Pm3024_ObjectIdentity = ObjectIdentity
pm3024 = _Pm3024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 7)
)
_Pm1010_ObjectIdentity = ObjectIdentity
pm1010 = _Pm1010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 8)
)
_Pm2010_ObjectIdentity = ObjectIdentity
pm2010 = _Pm2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 9)
)
_Pm3010_ObjectIdentity = ObjectIdentity
pm3010 = _Pm3010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 10)
)
_Pm1020_ObjectIdentity = ObjectIdentity
pm1020 = _Pm1020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 11)
)
_Pm2020_ObjectIdentity = ObjectIdentity
pm2020 = _Pm2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 12)
)
_Pm3020_ObjectIdentity = ObjectIdentity
pm3020 = _Pm3020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 1, 13)
)
_PmManagement_ObjectIdentity = ObjectIdentity
pmManagement = _PmManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2)
)
_PmAppliance_ObjectIdentity = ObjectIdentity
pmAppliance = _PmAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 1)
)


class _PmHostName_Type(DisplayString):
    """Custom type pmHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmHostName_Type.__name__ = "DisplayString"
_PmHostName_Object = MibScalar
pmHostName = _PmHostName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 1, 1),
    _PmHostName_Type()
)
pmHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmHostName.setStatus("current")


class _PmProductModel_Type(DisplayString):
    """Custom type pmProductModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_PmProductModel_Type.__name__ = "DisplayString"
_PmProductModel_Object = MibScalar
pmProductModel = _PmProductModel_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 1, 2),
    _PmProductModel_Type()
)
pmProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmProductModel.setStatus("current")


class _PmPartNumber_Type(DisplayString):
    """Custom type pmPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmPartNumber_Type.__name__ = "DisplayString"
_PmPartNumber_Object = MibScalar
pmPartNumber = _PmPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 1, 3),
    _PmPartNumber_Type()
)
pmPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPartNumber.setStatus("current")


class _PmSerialNumber_Type(DisplayString):
    """Custom type pmSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmSerialNumber_Type.__name__ = "DisplayString"
_PmSerialNumber_Object = MibScalar
pmSerialNumber = _PmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 1, 4),
    _PmSerialNumber_Type()
)
pmSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmSerialNumber.setStatus("current")


class _PmEIDNumber_Type(DisplayString):
    """Custom type pmEIDNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmEIDNumber_Type.__name__ = "DisplayString"
_PmEIDNumber_Object = MibScalar
pmEIDNumber = _PmEIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 1, 5),
    _PmEIDNumber_Type()
)
pmEIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEIDNumber.setStatus("current")


class _PmBootcodeVersion_Type(DisplayString):
    """Custom type pmBootcodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmBootcodeVersion_Type.__name__ = "DisplayString"
_PmBootcodeVersion_Object = MibScalar
pmBootcodeVersion = _PmBootcodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 1, 6),
    _PmBootcodeVersion_Type()
)
pmBootcodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmBootcodeVersion.setStatus("current")


class _PmFirmwareVersion_Type(DisplayString):
    """Custom type pmFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmFirmwareVersion_Type.__name__ = "DisplayString"
_PmFirmwareVersion_Object = MibScalar
pmFirmwareVersion = _PmFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 1, 7),
    _PmFirmwareVersion_Type()
)
pmFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFirmwareVersion.setStatus("current")


class _PmReboot_Type(Integer32):
    """Custom type pmReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reboot", 2))
    )


_PmReboot_Type.__name__ = "Integer32"
_PmReboot_Object = MibScalar
pmReboot = _PmReboot_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 1, 9),
    _PmReboot_Type()
)
pmReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmReboot.setStatus("current")
_PmSessions_ObjectIdentity = ObjectIdentity
pmSessions = _PmSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 2)
)
_PmActiveSessionsNumberOfSession_Type = Integer32
_PmActiveSessionsNumberOfSession_Object = MibScalar
pmActiveSessionsNumberOfSession = _PmActiveSessionsNumberOfSession_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 2, 1),
    _PmActiveSessionsNumberOfSession_Type()
)
pmActiveSessionsNumberOfSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmActiveSessionsNumberOfSession.setStatus("current")
_PmActiveSessionsTable_Object = MibTable
pmActiveSessionsTable = _PmActiveSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pmActiveSessionsTable.setStatus("current")
_PmActiveSessionsTableEntry_Object = MibTableRow
pmActiveSessionsTableEntry = _PmActiveSessionsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 2, 2, 1)
)
pmActiveSessionsTableEntry.setIndexNames(
    (0, "PM-MIB", "pmActiveSessionsTableIndex"),
)
if mibBuilder.loadTexts:
    pmActiveSessionsTableEntry.setStatus("current")
_PmActiveSessionsTableIndex_Type = InterfaceIndexOrZero
_PmActiveSessionsTableIndex_Object = MibTableColumn
pmActiveSessionsTableIndex = _PmActiveSessionsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 2, 2, 1, 1),
    _PmActiveSessionsTableIndex_Type()
)
pmActiveSessionsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmActiveSessionsTableIndex.setStatus("current")


class _PmActiveSessionsTableUser_Type(DisplayString):
    """Custom type pmActiveSessionsTableUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmActiveSessionsTableUser_Type.__name__ = "DisplayString"
_PmActiveSessionsTableUser_Object = MibTableColumn
pmActiveSessionsTableUser = _PmActiveSessionsTableUser_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 2, 2, 1, 2),
    _PmActiveSessionsTableUser_Type()
)
pmActiveSessionsTableUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmActiveSessionsTableUser.setStatus("current")


class _PmActiveSessionsTableGroup_Type(DisplayString):
    """Custom type pmActiveSessionsTableGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmActiveSessionsTableGroup_Type.__name__ = "DisplayString"
_PmActiveSessionsTableGroup_Object = MibTableColumn
pmActiveSessionsTableGroup = _PmActiveSessionsTableGroup_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 2, 2, 1, 3),
    _PmActiveSessionsTableGroup_Type()
)
pmActiveSessionsTableGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmActiveSessionsTableGroup.setStatus("current")


class _PmActiveSessionsTableType_Type(DisplayString):
    """Custom type pmActiveSessionsTableType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmActiveSessionsTableType_Type.__name__ = "DisplayString"
_PmActiveSessionsTableType_Object = MibTableColumn
pmActiveSessionsTableType = _PmActiveSessionsTableType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 2, 2, 1, 4),
    _PmActiveSessionsTableType_Type()
)
pmActiveSessionsTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmActiveSessionsTableType.setStatus("current")


class _PmActiveSessionsTableConnection_Type(DisplayString):
    """Custom type pmActiveSessionsTableConnection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmActiveSessionsTableConnection_Type.__name__ = "DisplayString"
_PmActiveSessionsTableConnection_Object = MibTableColumn
pmActiveSessionsTableConnection = _PmActiveSessionsTableConnection_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 2, 2, 1, 5),
    _PmActiveSessionsTableConnection_Type()
)
pmActiveSessionsTableConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmActiveSessionsTableConnection.setStatus("current")


class _PmActiveSessionsTableSessionTime_Type(DisplayString):
    """Custom type pmActiveSessionsTableSessionTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmActiveSessionsTableSessionTime_Type.__name__ = "DisplayString"
_PmActiveSessionsTableSessionTime_Object = MibTableColumn
pmActiveSessionsTableSessionTime = _PmActiveSessionsTableSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 2, 2, 1, 6),
    _PmActiveSessionsTableSessionTime_Type()
)
pmActiveSessionsTableSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmActiveSessionsTableSessionTime.setStatus("current")


class _PmActiveSessionsTableFrom_Type(DisplayString):
    """Custom type pmActiveSessionsTableFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PmActiveSessionsTableFrom_Type.__name__ = "DisplayString"
_PmActiveSessionsTableFrom_Object = MibTableColumn
pmActiveSessionsTableFrom = _PmActiveSessionsTableFrom_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 2, 2, 1, 7),
    _PmActiveSessionsTableFrom_Type()
)
pmActiveSessionsTableFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmActiveSessionsTableFrom.setStatus("current")


class _PmActiveSessionsTableKill_Type(Integer32):
    """Custom type pmActiveSessionsTableKill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("killSession", 2))
    )


_PmActiveSessionsTableKill_Type.__name__ = "Integer32"
_PmActiveSessionsTableKill_Object = MibTableColumn
pmActiveSessionsTableKill = _PmActiveSessionsTableKill_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 2, 2, 1, 8),
    _PmActiveSessionsTableKill_Type()
)
pmActiveSessionsTableKill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmActiveSessionsTableKill.setStatus("current")
_PmPowerMgmt_ObjectIdentity = ObjectIdentity
pmPowerMgmt = _PmPowerMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5)
)
_PmPowerMgmtNumSerialPorts_Type = Integer32
_PmPowerMgmtNumSerialPorts_Object = MibScalar
pmPowerMgmtNumSerialPorts = _PmPowerMgmtNumSerialPorts_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 1),
    _PmPowerMgmtNumSerialPorts_Type()
)
pmPowerMgmtNumSerialPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtNumSerialPorts.setStatus("current")
_PmPowerMgmtSerialTable_Object = MibTable
pmPowerMgmtSerialTable = _PmPowerMgmtSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2)
)
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTable.setStatus("current")
_PmPowerMgmtSerialTableEntry_Object = MibTableRow
pmPowerMgmtSerialTableEntry = _PmPowerMgmtSerialTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1)
)
pmPowerMgmtSerialTableEntry.setIndexNames(
    (0, "PM-MIB", "pmPowerMgmtSerialTableIndex"),
)
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTableEntry.setStatus("current")
_PmPowerMgmtSerialTableIndex_Type = InterfaceIndex
_PmPowerMgmtSerialTableIndex_Object = MibTableColumn
pmPowerMgmtSerialTableIndex = _PmPowerMgmtSerialTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1, 1),
    _PmPowerMgmtSerialTableIndex_Type()
)
pmPowerMgmtSerialTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTableIndex.setStatus("current")
_PmPowerMgmtSerialTablePortNumber_Type = Integer32
_PmPowerMgmtSerialTablePortNumber_Object = MibTableColumn
pmPowerMgmtSerialTablePortNumber = _PmPowerMgmtSerialTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1, 2),
    _PmPowerMgmtSerialTablePortNumber_Type()
)
pmPowerMgmtSerialTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTablePortNumber.setStatus("current")
_PmPowerMgmtSerialTableDeviceName_Type = DisplayString
_PmPowerMgmtSerialTableDeviceName_Object = MibTableColumn
pmPowerMgmtSerialTableDeviceName = _PmPowerMgmtSerialTableDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1, 3),
    _PmPowerMgmtSerialTableDeviceName_Type()
)
pmPowerMgmtSerialTableDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTableDeviceName.setStatus("current")
_PmPowerMgmtSerialTableNumberPDUs_Type = Integer32
_PmPowerMgmtSerialTableNumberPDUs_Object = MibTableColumn
pmPowerMgmtSerialTableNumberPDUs = _PmPowerMgmtSerialTableNumberPDUs_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1, 4),
    _PmPowerMgmtSerialTableNumberPDUs_Type()
)
pmPowerMgmtSerialTableNumberPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTableNumberPDUs.setStatus("current")
_PmPowerMgmtSerialTableBuzzer_Type = Integer32
_PmPowerMgmtSerialTableBuzzer_Object = MibTableColumn
pmPowerMgmtSerialTableBuzzer = _PmPowerMgmtSerialTableBuzzer_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1, 10),
    _PmPowerMgmtSerialTableBuzzer_Type()
)
pmPowerMgmtSerialTableBuzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTableBuzzer.setStatus("current")
_PmPowerMgmtSerialTableSyslog_Type = Integer32
_PmPowerMgmtSerialTableSyslog_Object = MibTableColumn
pmPowerMgmtSerialTableSyslog = _PmPowerMgmtSerialTableSyslog_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1, 11),
    _PmPowerMgmtSerialTableSyslog_Type()
)
pmPowerMgmtSerialTableSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTableSyslog.setStatus("current")
_PmPowerMgmtSerialTableOverCurrent_Type = Integer32
_PmPowerMgmtSerialTableOverCurrent_Object = MibTableColumn
pmPowerMgmtSerialTableOverCurrent = _PmPowerMgmtSerialTableOverCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1, 12),
    _PmPowerMgmtSerialTableOverCurrent_Type()
)
pmPowerMgmtSerialTableOverCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTableOverCurrent.setStatus("current")
_PmPowerMgmtSerialTableCycleInterval_Type = Integer32
_PmPowerMgmtSerialTableCycleInterval_Object = MibTableColumn
pmPowerMgmtSerialTableCycleInterval = _PmPowerMgmtSerialTableCycleInterval_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1, 13),
    _PmPowerMgmtSerialTableCycleInterval_Type()
)
pmPowerMgmtSerialTableCycleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTableCycleInterval.setStatus("current")
_PmPowerMgmtSerialTablePollRate_Type = Integer32
_PmPowerMgmtSerialTablePollRate_Object = MibTableColumn
pmPowerMgmtSerialTablePollRate = _PmPowerMgmtSerialTablePollRate_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1, 14),
    _PmPowerMgmtSerialTablePollRate_Type()
)
pmPowerMgmtSerialTablePollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTablePollRate.setStatus("current")
_PmPowerMgmtSerialTablePassWord_Type = DisplayString
_PmPowerMgmtSerialTablePassWord_Object = MibTableColumn
pmPowerMgmtSerialTablePassWord = _PmPowerMgmtSerialTablePassWord_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1, 15),
    _PmPowerMgmtSerialTablePassWord_Type()
)
pmPowerMgmtSerialTablePassWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTablePassWord.setStatus("current")


class _PmPowerMgmtSerialTableSave_Type(Integer32):
    """Custom type pmPowerMgmtSerialTableSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("save", 2))
    )


_PmPowerMgmtSerialTableSave_Type.__name__ = "Integer32"
_PmPowerMgmtSerialTableSave_Object = MibTableColumn
pmPowerMgmtSerialTableSave = _PmPowerMgmtSerialTableSave_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1, 20),
    _PmPowerMgmtSerialTableSave_Type()
)
pmPowerMgmtSerialTableSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTableSave.setStatus("current")


class _PmPowerMgmtSerialTableRestore_Type(Integer32):
    """Custom type pmPowerMgmtSerialTableRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("restore", 2))
    )


_PmPowerMgmtSerialTableRestore_Type.__name__ = "Integer32"
_PmPowerMgmtSerialTableRestore_Object = MibTableColumn
pmPowerMgmtSerialTableRestore = _PmPowerMgmtSerialTableRestore_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 2, 1, 21),
    _PmPowerMgmtSerialTableRestore_Type()
)
pmPowerMgmtSerialTableRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSerialTableRestore.setStatus("current")
_PmPowerMgmtPDUTable_Object = MibTable
pmPowerMgmtPDUTable = _PmPowerMgmtPDUTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3)
)
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTable.setStatus("current")
_PmPowerMgmtPDUTableEntry_Object = MibTableRow
pmPowerMgmtPDUTableEntry = _PmPowerMgmtPDUTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1)
)
pmPowerMgmtPDUTableEntry.setIndexNames(
    (0, "PM-MIB", "pmPowerMgmtPDUTablePortNumber"),
    (0, "PM-MIB", "pmPowerMgmtPDUTablePduIndex"),
)
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableEntry.setStatus("current")
_PmPowerMgmtPDUTablePortNumber_Type = InterfaceIndex
_PmPowerMgmtPDUTablePortNumber_Object = MibTableColumn
pmPowerMgmtPDUTablePortNumber = _PmPowerMgmtPDUTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 1),
    _PmPowerMgmtPDUTablePortNumber_Type()
)
pmPowerMgmtPDUTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePortNumber.setStatus("current")
_PmPowerMgmtPDUTablePduIndex_Type = InterfaceIndexOrZero
_PmPowerMgmtPDUTablePduIndex_Object = MibTableColumn
pmPowerMgmtPDUTablePduIndex = _PmPowerMgmtPDUTablePduIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 2),
    _PmPowerMgmtPDUTablePduIndex_Type()
)
pmPowerMgmtPDUTablePduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePduIndex.setStatus("current")
_PmPowerMgmtPDUTablePduId_Type = DisplayString
_PmPowerMgmtPDUTablePduId_Object = MibTableColumn
pmPowerMgmtPDUTablePduId = _PmPowerMgmtPDUTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 3),
    _PmPowerMgmtPDUTablePduId_Type()
)
pmPowerMgmtPDUTablePduId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePduId.setStatus("current")
_PmPowerMgmtPDUTablePortName_Type = DisplayString
_PmPowerMgmtPDUTablePortName_Object = MibTableColumn
pmPowerMgmtPDUTablePortName = _PmPowerMgmtPDUTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 4),
    _PmPowerMgmtPDUTablePortName_Type()
)
pmPowerMgmtPDUTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePortName.setStatus("current")
_PmPowerMgmtPDUTableModel_Type = DisplayString
_PmPowerMgmtPDUTableModel_Object = MibTableColumn
pmPowerMgmtPDUTableModel = _PmPowerMgmtPDUTableModel_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 5),
    _PmPowerMgmtPDUTableModel_Type()
)
pmPowerMgmtPDUTableModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableModel.setStatus("current")
_PmPowerMgmtPDUTableVendor_Type = DisplayString
_PmPowerMgmtPDUTableVendor_Object = MibTableColumn
pmPowerMgmtPDUTableVendor = _PmPowerMgmtPDUTableVendor_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 6),
    _PmPowerMgmtPDUTableVendor_Type()
)
pmPowerMgmtPDUTableVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVendor.setStatus("current")
_PmPowerMgmtPDUTableFirmwareVersion_Type = DisplayString
_PmPowerMgmtPDUTableFirmwareVersion_Object = MibTableColumn
pmPowerMgmtPDUTableFirmwareVersion = _PmPowerMgmtPDUTableFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 7),
    _PmPowerMgmtPDUTableFirmwareVersion_Type()
)
pmPowerMgmtPDUTableFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableFirmwareVersion.setStatus("current")
_PmPowerMgmtPDUTableNumberOfOutlets_Type = Integer32
_PmPowerMgmtPDUTableNumberOfOutlets_Object = MibTableColumn
pmPowerMgmtPDUTableNumberOfOutlets = _PmPowerMgmtPDUTableNumberOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 8),
    _PmPowerMgmtPDUTableNumberOfOutlets_Type()
)
pmPowerMgmtPDUTableNumberOfOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableNumberOfOutlets.setStatus("current")
_PmPowerMgmtPDUTableCurrentNOS_Type = Integer32
_PmPowerMgmtPDUTableCurrentNOS_Object = MibTableColumn
pmPowerMgmtPDUTableCurrentNOS = _PmPowerMgmtPDUTableCurrentNOS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 9),
    _PmPowerMgmtPDUTableCurrentNOS_Type()
)
pmPowerMgmtPDUTableCurrentNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrentNOS.setStatus("obsolete")
_PmPowerMgmtPDUTableCurrent1Value_Type = Integer32
_PmPowerMgmtPDUTableCurrent1Value_Object = MibTableColumn
pmPowerMgmtPDUTableCurrent1Value = _PmPowerMgmtPDUTableCurrent1Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 10),
    _PmPowerMgmtPDUTableCurrent1Value_Type()
)
pmPowerMgmtPDUTableCurrent1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrent1Value.setStatus("obsolete")
_PmPowerMgmtPDUTableCurrent1Max_Type = Integer32
_PmPowerMgmtPDUTableCurrent1Max_Object = MibTableColumn
pmPowerMgmtPDUTableCurrent1Max = _PmPowerMgmtPDUTableCurrent1Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 11),
    _PmPowerMgmtPDUTableCurrent1Max_Type()
)
pmPowerMgmtPDUTableCurrent1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrent1Max.setStatus("obsolete")
_PmPowerMgmtPDUTableCurrent2Value_Type = Integer32
_PmPowerMgmtPDUTableCurrent2Value_Object = MibTableColumn
pmPowerMgmtPDUTableCurrent2Value = _PmPowerMgmtPDUTableCurrent2Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 12),
    _PmPowerMgmtPDUTableCurrent2Value_Type()
)
pmPowerMgmtPDUTableCurrent2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrent2Value.setStatus("obsolete")
_PmPowerMgmtPDUTableCurrent2Max_Type = Integer32
_PmPowerMgmtPDUTableCurrent2Max_Object = MibTableColumn
pmPowerMgmtPDUTableCurrent2Max = _PmPowerMgmtPDUTableCurrent2Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 13),
    _PmPowerMgmtPDUTableCurrent2Max_Type()
)
pmPowerMgmtPDUTableCurrent2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrent2Max.setStatus("obsolete")
_PmPowerMgmtPDUTableCurrent3Value_Type = Integer32
_PmPowerMgmtPDUTableCurrent3Value_Object = MibTableColumn
pmPowerMgmtPDUTableCurrent3Value = _PmPowerMgmtPDUTableCurrent3Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 14),
    _PmPowerMgmtPDUTableCurrent3Value_Type()
)
pmPowerMgmtPDUTableCurrent3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrent3Value.setStatus("obsolete")
_PmPowerMgmtPDUTableCurrent3Max_Type = Integer32
_PmPowerMgmtPDUTableCurrent3Max_Object = MibTableColumn
pmPowerMgmtPDUTableCurrent3Max = _PmPowerMgmtPDUTableCurrent3Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 15),
    _PmPowerMgmtPDUTableCurrent3Max_Type()
)
pmPowerMgmtPDUTableCurrent3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrent3Max.setStatus("obsolete")
_PmPowerMgmtPDUTableTemperatureNOS_Type = Integer32
_PmPowerMgmtPDUTableTemperatureNOS_Object = MibTableColumn
pmPowerMgmtPDUTableTemperatureNOS = _PmPowerMgmtPDUTableTemperatureNOS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 16),
    _PmPowerMgmtPDUTableTemperatureNOS_Type()
)
pmPowerMgmtPDUTableTemperatureNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableTemperatureNOS.setStatus("obsolete")
_PmPowerMgmtPDUTableTemperature1Value_Type = Integer32
_PmPowerMgmtPDUTableTemperature1Value_Object = MibTableColumn
pmPowerMgmtPDUTableTemperature1Value = _PmPowerMgmtPDUTableTemperature1Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 17),
    _PmPowerMgmtPDUTableTemperature1Value_Type()
)
pmPowerMgmtPDUTableTemperature1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableTemperature1Value.setStatus("obsolete")
_PmPowerMgmtPDUTableTemperature1Max_Type = Integer32
_PmPowerMgmtPDUTableTemperature1Max_Object = MibTableColumn
pmPowerMgmtPDUTableTemperature1Max = _PmPowerMgmtPDUTableTemperature1Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 18),
    _PmPowerMgmtPDUTableTemperature1Max_Type()
)
pmPowerMgmtPDUTableTemperature1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableTemperature1Max.setStatus("obsolete")
_PmPowerMgmtPDUTableTemperature2Value_Type = Integer32
_PmPowerMgmtPDUTableTemperature2Value_Object = MibTableColumn
pmPowerMgmtPDUTableTemperature2Value = _PmPowerMgmtPDUTableTemperature2Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 19),
    _PmPowerMgmtPDUTableTemperature2Value_Type()
)
pmPowerMgmtPDUTableTemperature2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableTemperature2Value.setStatus("obsolete")
_PmPowerMgmtPDUTableTemperature2Max_Type = Integer32
_PmPowerMgmtPDUTableTemperature2Max_Object = MibTableColumn
pmPowerMgmtPDUTableTemperature2Max = _PmPowerMgmtPDUTableTemperature2Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 20),
    _PmPowerMgmtPDUTableTemperature2Max_Type()
)
pmPowerMgmtPDUTableTemperature2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableTemperature2Max.setStatus("obsolete")
_PmPowerMgmtPDUTableTemperature3Value_Type = Integer32
_PmPowerMgmtPDUTableTemperature3Value_Object = MibTableColumn
pmPowerMgmtPDUTableTemperature3Value = _PmPowerMgmtPDUTableTemperature3Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 21),
    _PmPowerMgmtPDUTableTemperature3Value_Type()
)
pmPowerMgmtPDUTableTemperature3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableTemperature3Value.setStatus("obsolete")
_PmPowerMgmtPDUTableTemperature3Max_Type = Integer32
_PmPowerMgmtPDUTableTemperature3Max_Object = MibTableColumn
pmPowerMgmtPDUTableTemperature3Max = _PmPowerMgmtPDUTableTemperature3Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 22),
    _PmPowerMgmtPDUTableTemperature3Max_Type()
)
pmPowerMgmtPDUTableTemperature3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableTemperature3Max.setStatus("obsolete")
_PmPowerMgmtPDUTableHumidityNOS_Type = Integer32
_PmPowerMgmtPDUTableHumidityNOS_Object = MibTableColumn
pmPowerMgmtPDUTableHumidityNOS = _PmPowerMgmtPDUTableHumidityNOS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 23),
    _PmPowerMgmtPDUTableHumidityNOS_Type()
)
pmPowerMgmtPDUTableHumidityNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableHumidityNOS.setStatus("obsolete")
_PmPowerMgmtPDUTableHumidity1Value_Type = Integer32
_PmPowerMgmtPDUTableHumidity1Value_Object = MibTableColumn
pmPowerMgmtPDUTableHumidity1Value = _PmPowerMgmtPDUTableHumidity1Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 24),
    _PmPowerMgmtPDUTableHumidity1Value_Type()
)
pmPowerMgmtPDUTableHumidity1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableHumidity1Value.setStatus("obsolete")
_PmPowerMgmtPDUTableHumidity1Max_Type = Integer32
_PmPowerMgmtPDUTableHumidity1Max_Object = MibTableColumn
pmPowerMgmtPDUTableHumidity1Max = _PmPowerMgmtPDUTableHumidity1Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 25),
    _PmPowerMgmtPDUTableHumidity1Max_Type()
)
pmPowerMgmtPDUTableHumidity1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableHumidity1Max.setStatus("obsolete")
_PmPowerMgmtPDUTableHumidity2Value_Type = Integer32
_PmPowerMgmtPDUTableHumidity2Value_Object = MibTableColumn
pmPowerMgmtPDUTableHumidity2Value = _PmPowerMgmtPDUTableHumidity2Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 26),
    _PmPowerMgmtPDUTableHumidity2Value_Type()
)
pmPowerMgmtPDUTableHumidity2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableHumidity2Value.setStatus("obsolete")
_PmPowerMgmtPDUTableHumidity2Max_Type = Integer32
_PmPowerMgmtPDUTableHumidity2Max_Object = MibTableColumn
pmPowerMgmtPDUTableHumidity2Max = _PmPowerMgmtPDUTableHumidity2Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 27),
    _PmPowerMgmtPDUTableHumidity2Max_Type()
)
pmPowerMgmtPDUTableHumidity2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableHumidity2Max.setStatus("obsolete")
_PmPowerMgmtPDUTableHumidity3Value_Type = Integer32
_PmPowerMgmtPDUTableHumidity3Value_Object = MibTableColumn
pmPowerMgmtPDUTableHumidity3Value = _PmPowerMgmtPDUTableHumidity3Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 28),
    _PmPowerMgmtPDUTableHumidity3Value_Type()
)
pmPowerMgmtPDUTableHumidity3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableHumidity3Value.setStatus("obsolete")
_PmPowerMgmtPDUTableHumidity3Max_Type = Integer32
_PmPowerMgmtPDUTableHumidity3Max_Object = MibTableColumn
pmPowerMgmtPDUTableHumidity3Max = _PmPowerMgmtPDUTableHumidity3Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 29),
    _PmPowerMgmtPDUTableHumidity3Max_Type()
)
pmPowerMgmtPDUTableHumidity3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableHumidity3Max.setStatus("obsolete")
_PmPowerMgmtPDUTableVoltageNOS_Type = Integer32
_PmPowerMgmtPDUTableVoltageNOS_Object = MibTableColumn
pmPowerMgmtPDUTableVoltageNOS = _PmPowerMgmtPDUTableVoltageNOS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 30),
    _PmPowerMgmtPDUTableVoltageNOS_Type()
)
pmPowerMgmtPDUTableVoltageNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltageNOS.setStatus("obsolete")
_PmPowerMgmtPDUTableVoltage1Value_Type = Integer32
_PmPowerMgmtPDUTableVoltage1Value_Object = MibTableColumn
pmPowerMgmtPDUTableVoltage1Value = _PmPowerMgmtPDUTableVoltage1Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 31),
    _PmPowerMgmtPDUTableVoltage1Value_Type()
)
pmPowerMgmtPDUTableVoltage1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltage1Value.setStatus("obsolete")
_PmPowerMgmtPDUTableVoltage1Max_Type = Integer32
_PmPowerMgmtPDUTableVoltage1Max_Object = MibTableColumn
pmPowerMgmtPDUTableVoltage1Max = _PmPowerMgmtPDUTableVoltage1Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 32),
    _PmPowerMgmtPDUTableVoltage1Max_Type()
)
pmPowerMgmtPDUTableVoltage1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltage1Max.setStatus("obsolete")
_PmPowerMgmtPDUTableVoltage2Value_Type = Integer32
_PmPowerMgmtPDUTableVoltage2Value_Object = MibTableColumn
pmPowerMgmtPDUTableVoltage2Value = _PmPowerMgmtPDUTableVoltage2Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 33),
    _PmPowerMgmtPDUTableVoltage2Value_Type()
)
pmPowerMgmtPDUTableVoltage2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltage2Value.setStatus("obsolete")
_PmPowerMgmtPDUTableVoltage2Max_Type = Integer32
_PmPowerMgmtPDUTableVoltage2Max_Object = MibTableColumn
pmPowerMgmtPDUTableVoltage2Max = _PmPowerMgmtPDUTableVoltage2Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 34),
    _PmPowerMgmtPDUTableVoltage2Max_Type()
)
pmPowerMgmtPDUTableVoltage2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltage2Max.setStatus("obsolete")
_PmPowerMgmtPDUTableVoltage3Value_Type = Integer32
_PmPowerMgmtPDUTableVoltage3Value_Object = MibTableColumn
pmPowerMgmtPDUTableVoltage3Value = _PmPowerMgmtPDUTableVoltage3Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 35),
    _PmPowerMgmtPDUTableVoltage3Value_Type()
)
pmPowerMgmtPDUTableVoltage3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltage3Value.setStatus("obsolete")
_PmPowerMgmtPDUTableVoltage3Max_Type = Integer32
_PmPowerMgmtPDUTableVoltage3Max_Object = MibTableColumn
pmPowerMgmtPDUTableVoltage3Max = _PmPowerMgmtPDUTableVoltage3Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 36),
    _PmPowerMgmtPDUTableVoltage3Max_Type()
)
pmPowerMgmtPDUTableVoltage3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltage3Max.setStatus("obsolete")
_PmPowerMgmtPDUTableNumberOfPhases_Type = Integer32
_PmPowerMgmtPDUTableNumberOfPhases_Object = MibTableColumn
pmPowerMgmtPDUTableNumberOfPhases = _PmPowerMgmtPDUTableNumberOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 37),
    _PmPowerMgmtPDUTableNumberOfPhases_Type()
)
pmPowerMgmtPDUTableNumberOfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableNumberOfPhases.setStatus("current")
_PmPowerMgmtPDUTableNumberOfBanks_Type = Integer32
_PmPowerMgmtPDUTableNumberOfBanks_Object = MibTableColumn
pmPowerMgmtPDUTableNumberOfBanks = _PmPowerMgmtPDUTableNumberOfBanks_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 38),
    _PmPowerMgmtPDUTableNumberOfBanks_Type()
)
pmPowerMgmtPDUTableNumberOfBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableNumberOfBanks.setStatus("current")
_PmPowerMgmtPDUTableNumberOfSensors_Type = Integer32
_PmPowerMgmtPDUTableNumberOfSensors_Object = MibTableColumn
pmPowerMgmtPDUTableNumberOfSensors = _PmPowerMgmtPDUTableNumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 40),
    _PmPowerMgmtPDUTableNumberOfSensors_Type()
)
pmPowerMgmtPDUTableNumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableNumberOfSensors.setStatus("current")


class _PmPowerMgmtPDUTableFactoryDefault_Type(Integer32):
    """Custom type pmPowerMgmtPDUTableFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtPDUTableFactoryDefault_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTableFactoryDefault_Object = MibTableColumn
pmPowerMgmtPDUTableFactoryDefault = _PmPowerMgmtPDUTableFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 41),
    _PmPowerMgmtPDUTableFactoryDefault_Type()
)
pmPowerMgmtPDUTableFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableFactoryDefault.setStatus("current")
_PmPowerMgmtPDUTableColdStartDelay_Type = Integer32
_PmPowerMgmtPDUTableColdStartDelay_Object = MibTableColumn
pmPowerMgmtPDUTableColdStartDelay = _PmPowerMgmtPDUTableColdStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 42),
    _PmPowerMgmtPDUTableColdStartDelay_Type()
)
pmPowerMgmtPDUTableColdStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableColdStartDelay.setStatus("current")


class _PmPowerMgmtPDUTableReboot_Type(Integer32):
    """Custom type pmPowerMgmtPDUTableReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reboot", 2))
    )


_PmPowerMgmtPDUTableReboot_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTableReboot_Object = MibTableColumn
pmPowerMgmtPDUTableReboot = _PmPowerMgmtPDUTableReboot_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 43),
    _PmPowerMgmtPDUTableReboot_Type()
)
pmPowerMgmtPDUTableReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableReboot.setStatus("current")
_PmPowerMgmtPDUTableMaxCurrent_Type = Integer32
_PmPowerMgmtPDUTableMaxCurrent_Object = MibTableColumn
pmPowerMgmtPDUTableMaxCurrent = _PmPowerMgmtPDUTableMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 44),
    _PmPowerMgmtPDUTableMaxCurrent_Type()
)
pmPowerMgmtPDUTableMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableMaxCurrent.setStatus("current")


class _PmPowerMgmtPDUTableAlarm_Type(Integer32):
    """Custom type pmPowerMgmtPDUTableAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("blow-fuse", 2),
          ("hw-ocp", 3),
          ("high-critical", 4),
          ("high-warning", 5),
          ("low-warning", 6),
          ("low-critical", 7))
    )


_PmPowerMgmtPDUTableAlarm_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTableAlarm_Object = MibTableColumn
pmPowerMgmtPDUTableAlarm = _PmPowerMgmtPDUTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 45),
    _PmPowerMgmtPDUTableAlarm_Type()
)
pmPowerMgmtPDUTableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableAlarm.setStatus("current")
_PmPowerMgmtPDUTableCurrentValue_Type = Integer32
_PmPowerMgmtPDUTableCurrentValue_Object = MibTableColumn
pmPowerMgmtPDUTableCurrentValue = _PmPowerMgmtPDUTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 50),
    _PmPowerMgmtPDUTableCurrentValue_Type()
)
pmPowerMgmtPDUTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrentValue.setStatus("current")
_PmPowerMgmtPDUTableCurrentMax_Type = Integer32
_PmPowerMgmtPDUTableCurrentMax_Object = MibTableColumn
pmPowerMgmtPDUTableCurrentMax = _PmPowerMgmtPDUTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 51),
    _PmPowerMgmtPDUTableCurrentMax_Type()
)
pmPowerMgmtPDUTableCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrentMax.setStatus("current")
_PmPowerMgmtPDUTableCurrentMin_Type = Integer32
_PmPowerMgmtPDUTableCurrentMin_Object = MibTableColumn
pmPowerMgmtPDUTableCurrentMin = _PmPowerMgmtPDUTableCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 52),
    _PmPowerMgmtPDUTableCurrentMin_Type()
)
pmPowerMgmtPDUTableCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrentMin.setStatus("current")
_PmPowerMgmtPDUTableCurrentAvg_Type = Integer32
_PmPowerMgmtPDUTableCurrentAvg_Object = MibTableColumn
pmPowerMgmtPDUTableCurrentAvg = _PmPowerMgmtPDUTableCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 53),
    _PmPowerMgmtPDUTableCurrentAvg_Type()
)
pmPowerMgmtPDUTableCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrentAvg.setStatus("current")


class _PmPowerMgmtPDUTableCurrentReset_Type(Integer32):
    """Custom type pmPowerMgmtPDUTableCurrentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtPDUTableCurrentReset_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTableCurrentReset_Object = MibTableColumn
pmPowerMgmtPDUTableCurrentReset = _PmPowerMgmtPDUTableCurrentReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 54),
    _PmPowerMgmtPDUTableCurrentReset_Type()
)
pmPowerMgmtPDUTableCurrentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrentReset.setStatus("current")
_PmPowerMgmtPDUTablePowerValue_Type = Integer32
_PmPowerMgmtPDUTablePowerValue_Object = MibTableColumn
pmPowerMgmtPDUTablePowerValue = _PmPowerMgmtPDUTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 60),
    _PmPowerMgmtPDUTablePowerValue_Type()
)
pmPowerMgmtPDUTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerValue.setStatus("current")
_PmPowerMgmtPDUTablePowerMax_Type = Integer32
_PmPowerMgmtPDUTablePowerMax_Object = MibTableColumn
pmPowerMgmtPDUTablePowerMax = _PmPowerMgmtPDUTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 61),
    _PmPowerMgmtPDUTablePowerMax_Type()
)
pmPowerMgmtPDUTablePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerMax.setStatus("current")
_PmPowerMgmtPDUTablePowerMin_Type = Integer32
_PmPowerMgmtPDUTablePowerMin_Object = MibTableColumn
pmPowerMgmtPDUTablePowerMin = _PmPowerMgmtPDUTablePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 62),
    _PmPowerMgmtPDUTablePowerMin_Type()
)
pmPowerMgmtPDUTablePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerMin.setStatus("current")
_PmPowerMgmtPDUTablePowerAvg_Type = Integer32
_PmPowerMgmtPDUTablePowerAvg_Object = MibTableColumn
pmPowerMgmtPDUTablePowerAvg = _PmPowerMgmtPDUTablePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 63),
    _PmPowerMgmtPDUTablePowerAvg_Type()
)
pmPowerMgmtPDUTablePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerAvg.setStatus("current")


class _PmPowerMgmtPDUTablePowerReset_Type(Integer32):
    """Custom type pmPowerMgmtPDUTablePowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtPDUTablePowerReset_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTablePowerReset_Object = MibTableColumn
pmPowerMgmtPDUTablePowerReset = _PmPowerMgmtPDUTablePowerReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 64),
    _PmPowerMgmtPDUTablePowerReset_Type()
)
pmPowerMgmtPDUTablePowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerReset.setStatus("current")


class _PmPowerMgmtPDUTablePowerType_Type(Integer32):
    """Custom type pmPowerMgmtPDUTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("measured", 2))
    )


_PmPowerMgmtPDUTablePowerType_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTablePowerType_Object = MibTableColumn
pmPowerMgmtPDUTablePowerType = _PmPowerMgmtPDUTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 65),
    _PmPowerMgmtPDUTablePowerType_Type()
)
pmPowerMgmtPDUTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerType.setStatus("current")
_PmPowerMgmtPDUTableVoltageValue_Type = Integer32
_PmPowerMgmtPDUTableVoltageValue_Object = MibTableColumn
pmPowerMgmtPDUTableVoltageValue = _PmPowerMgmtPDUTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 70),
    _PmPowerMgmtPDUTableVoltageValue_Type()
)
pmPowerMgmtPDUTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltageValue.setStatus("current")
_PmPowerMgmtPDUTableVoltageMax_Type = Integer32
_PmPowerMgmtPDUTableVoltageMax_Object = MibTableColumn
pmPowerMgmtPDUTableVoltageMax = _PmPowerMgmtPDUTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 71),
    _PmPowerMgmtPDUTableVoltageMax_Type()
)
pmPowerMgmtPDUTableVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltageMax.setStatus("current")
_PmPowerMgmtPDUTableVoltageMin_Type = Integer32
_PmPowerMgmtPDUTableVoltageMin_Object = MibTableColumn
pmPowerMgmtPDUTableVoltageMin = _PmPowerMgmtPDUTableVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 72),
    _PmPowerMgmtPDUTableVoltageMin_Type()
)
pmPowerMgmtPDUTableVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltageMin.setStatus("current")
_PmPowerMgmtPDUTableVoltageAvg_Type = Integer32
_PmPowerMgmtPDUTableVoltageAvg_Object = MibTableColumn
pmPowerMgmtPDUTableVoltageAvg = _PmPowerMgmtPDUTableVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 73),
    _PmPowerMgmtPDUTableVoltageAvg_Type()
)
pmPowerMgmtPDUTableVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltageAvg.setStatus("current")


class _PmPowerMgmtPDUTableVoltageReset_Type(Integer32):
    """Custom type pmPowerMgmtPDUTableVoltageReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtPDUTableVoltageReset_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTableVoltageReset_Object = MibTableColumn
pmPowerMgmtPDUTableVoltageReset = _PmPowerMgmtPDUTableVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 74),
    _PmPowerMgmtPDUTableVoltageReset_Type()
)
pmPowerMgmtPDUTableVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltageReset.setStatus("current")


class _PmPowerMgmtPDUTableVoltageType_Type(Integer32):
    """Custom type pmPowerMgmtPDUTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("measured", 2))
    )


_PmPowerMgmtPDUTableVoltageType_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTableVoltageType_Object = MibTableColumn
pmPowerMgmtPDUTableVoltageType = _PmPowerMgmtPDUTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 75),
    _PmPowerMgmtPDUTableVoltageType_Type()
)
pmPowerMgmtPDUTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableVoltageType.setStatus("current")
_PmPowerMgmtPDUTablePowerFactorValue_Type = Integer32
_PmPowerMgmtPDUTablePowerFactorValue_Object = MibTableColumn
pmPowerMgmtPDUTablePowerFactorValue = _PmPowerMgmtPDUTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 80),
    _PmPowerMgmtPDUTablePowerFactorValue_Type()
)
pmPowerMgmtPDUTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerFactorValue.setStatus("current")
_PmPowerMgmtPDUTablePowerFactorMax_Type = Integer32
_PmPowerMgmtPDUTablePowerFactorMax_Object = MibTableColumn
pmPowerMgmtPDUTablePowerFactorMax = _PmPowerMgmtPDUTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 81),
    _PmPowerMgmtPDUTablePowerFactorMax_Type()
)
pmPowerMgmtPDUTablePowerFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerFactorMax.setStatus("current")
_PmPowerMgmtPDUTablePowerFactorMin_Type = Integer32
_PmPowerMgmtPDUTablePowerFactorMin_Object = MibTableColumn
pmPowerMgmtPDUTablePowerFactorMin = _PmPowerMgmtPDUTablePowerFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 82),
    _PmPowerMgmtPDUTablePowerFactorMin_Type()
)
pmPowerMgmtPDUTablePowerFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerFactorMin.setStatus("current")
_PmPowerMgmtPDUTablePowerFactorAvg_Type = Integer32
_PmPowerMgmtPDUTablePowerFactorAvg_Object = MibTableColumn
pmPowerMgmtPDUTablePowerFactorAvg = _PmPowerMgmtPDUTablePowerFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 83),
    _PmPowerMgmtPDUTablePowerFactorAvg_Type()
)
pmPowerMgmtPDUTablePowerFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerFactorAvg.setStatus("current")


class _PmPowerMgmtPDUTablePowerFactorReset_Type(Integer32):
    """Custom type pmPowerMgmtPDUTablePowerFactorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtPDUTablePowerFactorReset_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTablePowerFactorReset_Object = MibTableColumn
pmPowerMgmtPDUTablePowerFactorReset = _PmPowerMgmtPDUTablePowerFactorReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 84),
    _PmPowerMgmtPDUTablePowerFactorReset_Type()
)
pmPowerMgmtPDUTablePowerFactorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerFactorReset.setStatus("current")


class _PmPowerMgmtPDUTablePowerFactorType_Type(Integer32):
    """Custom type pmPowerMgmtPDUTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("measured", 2))
    )


_PmPowerMgmtPDUTablePowerFactorType_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTablePowerFactorType_Object = MibTableColumn
pmPowerMgmtPDUTablePowerFactorType = _PmPowerMgmtPDUTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 85),
    _PmPowerMgmtPDUTablePowerFactorType_Type()
)
pmPowerMgmtPDUTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerFactorType.setStatus("current")


class _PmPowerMgmtPDUTablePowerControl_Type(Integer32):
    """Custom type pmPowerMgmtPDUTablePowerControl based on Integer32"""
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
        *(("noAction", 1),
          ("powerOn", 2),
          ("powerOff", 3),
          ("powerCycle", 4))
    )


_PmPowerMgmtPDUTablePowerControl_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTablePowerControl_Object = MibTableColumn
pmPowerMgmtPDUTablePowerControl = _PmPowerMgmtPDUTablePowerControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 90),
    _PmPowerMgmtPDUTablePowerControl_Type()
)
pmPowerMgmtPDUTablePowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTablePowerControl.setStatus("current")


class _PmPowerMgmtPDUTableResetOCP_Type(Integer32):
    """Custom type pmPowerMgmtPDUTableResetOCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtPDUTableResetOCP_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTableResetOCP_Object = MibTableColumn
pmPowerMgmtPDUTableResetOCP = _PmPowerMgmtPDUTableResetOCP_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 91),
    _PmPowerMgmtPDUTableResetOCP_Type()
)
pmPowerMgmtPDUTableResetOCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableResetOCP.setStatus("current")
_PmPowerMgmtPDUTableCurrentHighCritical_Type = Integer32
_PmPowerMgmtPDUTableCurrentHighCritical_Object = MibTableColumn
pmPowerMgmtPDUTableCurrentHighCritical = _PmPowerMgmtPDUTableCurrentHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 100),
    _PmPowerMgmtPDUTableCurrentHighCritical_Type()
)
pmPowerMgmtPDUTableCurrentHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrentHighCritical.setStatus("current")
_PmPowerMgmtPDUTableCurrentHighWarning_Type = Integer32
_PmPowerMgmtPDUTableCurrentHighWarning_Object = MibTableColumn
pmPowerMgmtPDUTableCurrentHighWarning = _PmPowerMgmtPDUTableCurrentHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 101),
    _PmPowerMgmtPDUTableCurrentHighWarning_Type()
)
pmPowerMgmtPDUTableCurrentHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrentHighWarning.setStatus("current")
_PmPowerMgmtPDUTableCurrentLowWarning_Type = Integer32
_PmPowerMgmtPDUTableCurrentLowWarning_Object = MibTableColumn
pmPowerMgmtPDUTableCurrentLowWarning = _PmPowerMgmtPDUTableCurrentLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 102),
    _PmPowerMgmtPDUTableCurrentLowWarning_Type()
)
pmPowerMgmtPDUTableCurrentLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrentLowWarning.setStatus("current")
_PmPowerMgmtPDUTableCurrentLowCritical_Type = Integer32
_PmPowerMgmtPDUTableCurrentLowCritical_Object = MibTableColumn
pmPowerMgmtPDUTableCurrentLowCritical = _PmPowerMgmtPDUTableCurrentLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 103),
    _PmPowerMgmtPDUTableCurrentLowCritical_Type()
)
pmPowerMgmtPDUTableCurrentLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableCurrentLowCritical.setStatus("current")
_PmPowerMgmtPDUTableEnergyValue_Type = Integer32
_PmPowerMgmtPDUTableEnergyValue_Object = MibTableColumn
pmPowerMgmtPDUTableEnergyValue = _PmPowerMgmtPDUTableEnergyValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 105),
    _PmPowerMgmtPDUTableEnergyValue_Type()
)
pmPowerMgmtPDUTableEnergyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableEnergyValue.setStatus("current")
_PmPowerMgmtPDUTableEnergyStartTime_Type = DisplayString
_PmPowerMgmtPDUTableEnergyStartTime_Object = MibTableColumn
pmPowerMgmtPDUTableEnergyStartTime = _PmPowerMgmtPDUTableEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 106),
    _PmPowerMgmtPDUTableEnergyStartTime_Type()
)
pmPowerMgmtPDUTableEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableEnergyStartTime.setStatus("current")


class _PmPowerMgmtPDUTableEnergyReset_Type(Integer32):
    """Custom type pmPowerMgmtPDUTableEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtPDUTableEnergyReset_Type.__name__ = "Integer32"
_PmPowerMgmtPDUTableEnergyReset_Object = MibTableColumn
pmPowerMgmtPDUTableEnergyReset = _PmPowerMgmtPDUTableEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 3, 1, 107),
    _PmPowerMgmtPDUTableEnergyReset_Type()
)
pmPowerMgmtPDUTableEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPDUTableEnergyReset.setStatus("current")
_PmPowerMgmtTotalNumberOfOutlets_Type = Integer32
_PmPowerMgmtTotalNumberOfOutlets_Object = MibScalar
pmPowerMgmtTotalNumberOfOutlets = _PmPowerMgmtTotalNumberOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 4),
    _PmPowerMgmtTotalNumberOfOutlets_Type()
)
pmPowerMgmtTotalNumberOfOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtTotalNumberOfOutlets.setStatus("current")
_PmPowerMgmtOutletsTable_Object = MibTable
pmPowerMgmtOutletsTable = _PmPowerMgmtOutletsTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5)
)
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTable.setStatus("current")
_PmPowerMgmtOutletsTableEntry_Object = MibTableRow
pmPowerMgmtOutletsTableEntry = _PmPowerMgmtOutletsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1)
)
pmPowerMgmtOutletsTableEntry.setIndexNames(
    (0, "PM-MIB", "pmPowerMgmtOutletsTablePortNumber"),
    (0, "PM-MIB", "pmPowerMgmtOutletsTablePduNumber"),
    (0, "PM-MIB", "pmPowerMgmtOutletsTableNumber"),
)
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableEntry.setStatus("current")
_PmPowerMgmtOutletsTablePortNumber_Type = InterfaceIndex
_PmPowerMgmtOutletsTablePortNumber_Object = MibTableColumn
pmPowerMgmtOutletsTablePortNumber = _PmPowerMgmtOutletsTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 1),
    _PmPowerMgmtOutletsTablePortNumber_Type()
)
pmPowerMgmtOutletsTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePortNumber.setStatus("current")
_PmPowerMgmtOutletsTablePduNumber_Type = InterfaceIndex
_PmPowerMgmtOutletsTablePduNumber_Object = MibTableColumn
pmPowerMgmtOutletsTablePduNumber = _PmPowerMgmtOutletsTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 2),
    _PmPowerMgmtOutletsTablePduNumber_Type()
)
pmPowerMgmtOutletsTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePduNumber.setStatus("current")
_PmPowerMgmtOutletsTableNumber_Type = InterfaceIndex
_PmPowerMgmtOutletsTableNumber_Object = MibTableColumn
pmPowerMgmtOutletsTableNumber = _PmPowerMgmtOutletsTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 3),
    _PmPowerMgmtOutletsTableNumber_Type()
)
pmPowerMgmtOutletsTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableNumber.setStatus("current")
_PmPowerMgmtOutletsTableName_Type = DisplayString
_PmPowerMgmtOutletsTableName_Object = MibTableColumn
pmPowerMgmtOutletsTableName = _PmPowerMgmtOutletsTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 4),
    _PmPowerMgmtOutletsTableName_Type()
)
pmPowerMgmtOutletsTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableName.setStatus("current")


class _PmPowerMgmtOutletsTableStatus_Type(Integer32):
    """Custom type pmPowerMgmtOutletsTableStatus based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("offLocked", 3),
          ("onLocked", 4),
          ("offCycle", 5),
          ("onPendingOff", 6),
          ("offPendingOn", 7),
          ("onPendingCycle", 8),
          ("notSet", 9),
          ("onFixed", 10),
          ("offShutdown", 11),
          ("tripped", 12))
    )


_PmPowerMgmtOutletsTableStatus_Type.__name__ = "Integer32"
_PmPowerMgmtOutletsTableStatus_Object = MibTableColumn
pmPowerMgmtOutletsTableStatus = _PmPowerMgmtOutletsTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 5),
    _PmPowerMgmtOutletsTableStatus_Type()
)
pmPowerMgmtOutletsTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableStatus.setStatus("current")


class _PmPowerMgmtOutletsTablePowerControl_Type(Integer32):
    """Custom type pmPowerMgmtOutletsTablePowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("powerOn", 2),
          ("powerOff", 3),
          ("powerCycle", 4),
          ("powerLock", 5),
          ("powerUnlock", 6))
    )


_PmPowerMgmtOutletsTablePowerControl_Type.__name__ = "Integer32"
_PmPowerMgmtOutletsTablePowerControl_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerControl = _PmPowerMgmtOutletsTablePowerControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 6),
    _PmPowerMgmtOutletsTablePowerControl_Type()
)
pmPowerMgmtOutletsTablePowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerControl.setStatus("current")
_PmPowerMgmtOutletsTablePortName_Type = DisplayString
_PmPowerMgmtOutletsTablePortName_Object = MibTableColumn
pmPowerMgmtOutletsTablePortName = _PmPowerMgmtOutletsTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 7),
    _PmPowerMgmtOutletsTablePortName_Type()
)
pmPowerMgmtOutletsTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePortName.setStatus("current")
_PmPowerMgmtOutletsTablePduId_Type = DisplayString
_PmPowerMgmtOutletsTablePduId_Object = MibTableColumn
pmPowerMgmtOutletsTablePduId = _PmPowerMgmtOutletsTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 8),
    _PmPowerMgmtOutletsTablePduId_Type()
)
pmPowerMgmtOutletsTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePduId.setStatus("current")
_PmPowerMgmtOutletsTablePostOnDelay_Type = Integer32
_PmPowerMgmtOutletsTablePostOnDelay_Object = MibTableColumn
pmPowerMgmtOutletsTablePostOnDelay = _PmPowerMgmtOutletsTablePostOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 9),
    _PmPowerMgmtOutletsTablePostOnDelay_Type()
)
pmPowerMgmtOutletsTablePostOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePostOnDelay.setStatus("current")
_PmPowerMgmtOutletsTablePostOffDelay_Type = Integer32
_PmPowerMgmtOutletsTablePostOffDelay_Object = MibTableColumn
pmPowerMgmtOutletsTablePostOffDelay = _PmPowerMgmtOutletsTablePostOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 10),
    _PmPowerMgmtOutletsTablePostOffDelay_Type()
)
pmPowerMgmtOutletsTablePostOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePostOffDelay.setStatus("current")


class _PmPowerMgmtOutletsTableAlarm_Type(Integer32):
    """Custom type pmPowerMgmtOutletsTableAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("blow-fuse", 2),
          ("hw-ocp", 3),
          ("high-critical", 4),
          ("high-warning", 5),
          ("low-warning", 6),
          ("low-critical", 7))
    )


_PmPowerMgmtOutletsTableAlarm_Type.__name__ = "Integer32"
_PmPowerMgmtOutletsTableAlarm_Object = MibTableColumn
pmPowerMgmtOutletsTableAlarm = _PmPowerMgmtOutletsTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 45),
    _PmPowerMgmtOutletsTableAlarm_Type()
)
pmPowerMgmtOutletsTableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableAlarm.setStatus("current")
_PmPowerMgmtOutletsTableCurrentValue_Type = Integer32
_PmPowerMgmtOutletsTableCurrentValue_Object = MibTableColumn
pmPowerMgmtOutletsTableCurrentValue = _PmPowerMgmtOutletsTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 50),
    _PmPowerMgmtOutletsTableCurrentValue_Type()
)
pmPowerMgmtOutletsTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableCurrentValue.setStatus("current")
_PmPowerMgmtOutletsTableCurrentMax_Type = Integer32
_PmPowerMgmtOutletsTableCurrentMax_Object = MibTableColumn
pmPowerMgmtOutletsTableCurrentMax = _PmPowerMgmtOutletsTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 51),
    _PmPowerMgmtOutletsTableCurrentMax_Type()
)
pmPowerMgmtOutletsTableCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableCurrentMax.setStatus("current")
_PmPowerMgmtOutletsTableCurrentMin_Type = Integer32
_PmPowerMgmtOutletsTableCurrentMin_Object = MibTableColumn
pmPowerMgmtOutletsTableCurrentMin = _PmPowerMgmtOutletsTableCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 52),
    _PmPowerMgmtOutletsTableCurrentMin_Type()
)
pmPowerMgmtOutletsTableCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableCurrentMin.setStatus("current")
_PmPowerMgmtOutletsTableCurrentAvg_Type = Integer32
_PmPowerMgmtOutletsTableCurrentAvg_Object = MibTableColumn
pmPowerMgmtOutletsTableCurrentAvg = _PmPowerMgmtOutletsTableCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 53),
    _PmPowerMgmtOutletsTableCurrentAvg_Type()
)
pmPowerMgmtOutletsTableCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableCurrentAvg.setStatus("current")


class _PmPowerMgmtOutletsTableCurrentReset_Type(Integer32):
    """Custom type pmPowerMgmtOutletsTableCurrentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtOutletsTableCurrentReset_Type.__name__ = "Integer32"
_PmPowerMgmtOutletsTableCurrentReset_Object = MibTableColumn
pmPowerMgmtOutletsTableCurrentReset = _PmPowerMgmtOutletsTableCurrentReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 54),
    _PmPowerMgmtOutletsTableCurrentReset_Type()
)
pmPowerMgmtOutletsTableCurrentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableCurrentReset.setStatus("current")
_PmPowerMgmtOutletsTablePowerValue_Type = Integer32
_PmPowerMgmtOutletsTablePowerValue_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerValue = _PmPowerMgmtOutletsTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 60),
    _PmPowerMgmtOutletsTablePowerValue_Type()
)
pmPowerMgmtOutletsTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerValue.setStatus("current")
_PmPowerMgmtOutletsTablePowerMax_Type = Integer32
_PmPowerMgmtOutletsTablePowerMax_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerMax = _PmPowerMgmtOutletsTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 61),
    _PmPowerMgmtOutletsTablePowerMax_Type()
)
pmPowerMgmtOutletsTablePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerMax.setStatus("current")
_PmPowerMgmtOutletsTablePowerMin_Type = Integer32
_PmPowerMgmtOutletsTablePowerMin_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerMin = _PmPowerMgmtOutletsTablePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 62),
    _PmPowerMgmtOutletsTablePowerMin_Type()
)
pmPowerMgmtOutletsTablePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerMin.setStatus("current")
_PmPowerMgmtOutletsTablePowerAvg_Type = Integer32
_PmPowerMgmtOutletsTablePowerAvg_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerAvg = _PmPowerMgmtOutletsTablePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 63),
    _PmPowerMgmtOutletsTablePowerAvg_Type()
)
pmPowerMgmtOutletsTablePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerAvg.setStatus("current")


class _PmPowerMgmtOutletsTablePowerReset_Type(Integer32):
    """Custom type pmPowerMgmtOutletsTablePowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtOutletsTablePowerReset_Type.__name__ = "Integer32"
_PmPowerMgmtOutletsTablePowerReset_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerReset = _PmPowerMgmtOutletsTablePowerReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 64),
    _PmPowerMgmtOutletsTablePowerReset_Type()
)
pmPowerMgmtOutletsTablePowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerReset.setStatus("current")


class _PmPowerMgmtOutletsTablePowerType_Type(Integer32):
    """Custom type pmPowerMgmtOutletsTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("measured", 2))
    )


_PmPowerMgmtOutletsTablePowerType_Type.__name__ = "Integer32"
_PmPowerMgmtOutletsTablePowerType_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerType = _PmPowerMgmtOutletsTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 65),
    _PmPowerMgmtOutletsTablePowerType_Type()
)
pmPowerMgmtOutletsTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerType.setStatus("current")
_PmPowerMgmtOutletsTableVoltageValue_Type = Integer32
_PmPowerMgmtOutletsTableVoltageValue_Object = MibTableColumn
pmPowerMgmtOutletsTableVoltageValue = _PmPowerMgmtOutletsTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 70),
    _PmPowerMgmtOutletsTableVoltageValue_Type()
)
pmPowerMgmtOutletsTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableVoltageValue.setStatus("current")
_PmPowerMgmtOutletsTableVoltageMax_Type = Integer32
_PmPowerMgmtOutletsTableVoltageMax_Object = MibTableColumn
pmPowerMgmtOutletsTableVoltageMax = _PmPowerMgmtOutletsTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 71),
    _PmPowerMgmtOutletsTableVoltageMax_Type()
)
pmPowerMgmtOutletsTableVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableVoltageMax.setStatus("current")
_PmPowerMgmtOutletsTableVoltageMin_Type = Integer32
_PmPowerMgmtOutletsTableVoltageMin_Object = MibTableColumn
pmPowerMgmtOutletsTableVoltageMin = _PmPowerMgmtOutletsTableVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 72),
    _PmPowerMgmtOutletsTableVoltageMin_Type()
)
pmPowerMgmtOutletsTableVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableVoltageMin.setStatus("current")
_PmPowerMgmtOutletsTableVoltageAvg_Type = Integer32
_PmPowerMgmtOutletsTableVoltageAvg_Object = MibTableColumn
pmPowerMgmtOutletsTableVoltageAvg = _PmPowerMgmtOutletsTableVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 73),
    _PmPowerMgmtOutletsTableVoltageAvg_Type()
)
pmPowerMgmtOutletsTableVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableVoltageAvg.setStatus("current")


class _PmPowerMgmtOutletsTableVoltageReset_Type(Integer32):
    """Custom type pmPowerMgmtOutletsTableVoltageReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtOutletsTableVoltageReset_Type.__name__ = "Integer32"
_PmPowerMgmtOutletsTableVoltageReset_Object = MibTableColumn
pmPowerMgmtOutletsTableVoltageReset = _PmPowerMgmtOutletsTableVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 74),
    _PmPowerMgmtOutletsTableVoltageReset_Type()
)
pmPowerMgmtOutletsTableVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableVoltageReset.setStatus("current")


class _PmPowerMgmtOutletsTableVoltageType_Type(Integer32):
    """Custom type pmPowerMgmtOutletsTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("measured", 2))
    )


_PmPowerMgmtOutletsTableVoltageType_Type.__name__ = "Integer32"
_PmPowerMgmtOutletsTableVoltageType_Object = MibTableColumn
pmPowerMgmtOutletsTableVoltageType = _PmPowerMgmtOutletsTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 75),
    _PmPowerMgmtOutletsTableVoltageType_Type()
)
pmPowerMgmtOutletsTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableVoltageType.setStatus("current")
_PmPowerMgmtOutletsTablePowerFactorValue_Type = Integer32
_PmPowerMgmtOutletsTablePowerFactorValue_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerFactorValue = _PmPowerMgmtOutletsTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 80),
    _PmPowerMgmtOutletsTablePowerFactorValue_Type()
)
pmPowerMgmtOutletsTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerFactorValue.setStatus("current")
_PmPowerMgmtOutletsTablePowerFactorMax_Type = Integer32
_PmPowerMgmtOutletsTablePowerFactorMax_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerFactorMax = _PmPowerMgmtOutletsTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 81),
    _PmPowerMgmtOutletsTablePowerFactorMax_Type()
)
pmPowerMgmtOutletsTablePowerFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerFactorMax.setStatus("current")
_PmPowerMgmtOutletsTablePowerFactorMin_Type = Integer32
_PmPowerMgmtOutletsTablePowerFactorMin_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerFactorMin = _PmPowerMgmtOutletsTablePowerFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 82),
    _PmPowerMgmtOutletsTablePowerFactorMin_Type()
)
pmPowerMgmtOutletsTablePowerFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerFactorMin.setStatus("current")
_PmPowerMgmtOutletsTablePowerFactorAvg_Type = Integer32
_PmPowerMgmtOutletsTablePowerFactorAvg_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerFactorAvg = _PmPowerMgmtOutletsTablePowerFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 83),
    _PmPowerMgmtOutletsTablePowerFactorAvg_Type()
)
pmPowerMgmtOutletsTablePowerFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerFactorAvg.setStatus("current")


class _PmPowerMgmtOutletsTablePowerFactorReset_Type(Integer32):
    """Custom type pmPowerMgmtOutletsTablePowerFactorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtOutletsTablePowerFactorReset_Type.__name__ = "Integer32"
_PmPowerMgmtOutletsTablePowerFactorReset_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerFactorReset = _PmPowerMgmtOutletsTablePowerFactorReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 84),
    _PmPowerMgmtOutletsTablePowerFactorReset_Type()
)
pmPowerMgmtOutletsTablePowerFactorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerFactorReset.setStatus("current")


class _PmPowerMgmtOutletsTablePowerFactorType_Type(Integer32):
    """Custom type pmPowerMgmtOutletsTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("measured", 2))
    )


_PmPowerMgmtOutletsTablePowerFactorType_Type.__name__ = "Integer32"
_PmPowerMgmtOutletsTablePowerFactorType_Object = MibTableColumn
pmPowerMgmtOutletsTablePowerFactorType = _PmPowerMgmtOutletsTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 85),
    _PmPowerMgmtOutletsTablePowerFactorType_Type()
)
pmPowerMgmtOutletsTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTablePowerFactorType.setStatus("current")
_PmPowerMgmtOutletsTableCurrentHighCritical_Type = Integer32
_PmPowerMgmtOutletsTableCurrentHighCritical_Object = MibTableColumn
pmPowerMgmtOutletsTableCurrentHighCritical = _PmPowerMgmtOutletsTableCurrentHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 100),
    _PmPowerMgmtOutletsTableCurrentHighCritical_Type()
)
pmPowerMgmtOutletsTableCurrentHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableCurrentHighCritical.setStatus("current")
_PmPowerMgmtOutletsTableCurrentHighWarning_Type = Integer32
_PmPowerMgmtOutletsTableCurrentHighWarning_Object = MibTableColumn
pmPowerMgmtOutletsTableCurrentHighWarning = _PmPowerMgmtOutletsTableCurrentHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 101),
    _PmPowerMgmtOutletsTableCurrentHighWarning_Type()
)
pmPowerMgmtOutletsTableCurrentHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableCurrentHighWarning.setStatus("current")
_PmPowerMgmtOutletsTableCurrentLowWarning_Type = Integer32
_PmPowerMgmtOutletsTableCurrentLowWarning_Object = MibTableColumn
pmPowerMgmtOutletsTableCurrentLowWarning = _PmPowerMgmtOutletsTableCurrentLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 102),
    _PmPowerMgmtOutletsTableCurrentLowWarning_Type()
)
pmPowerMgmtOutletsTableCurrentLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableCurrentLowWarning.setStatus("current")
_PmPowerMgmtOutletsTableCurrentLowCritical_Type = Integer32
_PmPowerMgmtOutletsTableCurrentLowCritical_Object = MibTableColumn
pmPowerMgmtOutletsTableCurrentLowCritical = _PmPowerMgmtOutletsTableCurrentLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 103),
    _PmPowerMgmtOutletsTableCurrentLowCritical_Type()
)
pmPowerMgmtOutletsTableCurrentLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableCurrentLowCritical.setStatus("current")
_PmPowerMgmtOutletsTableEnergyValue_Type = Integer32
_PmPowerMgmtOutletsTableEnergyValue_Object = MibTableColumn
pmPowerMgmtOutletsTableEnergyValue = _PmPowerMgmtOutletsTableEnergyValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 105),
    _PmPowerMgmtOutletsTableEnergyValue_Type()
)
pmPowerMgmtOutletsTableEnergyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableEnergyValue.setStatus("current")
_PmPowerMgmtOutletsTableEnergyStartTime_Type = DisplayString
_PmPowerMgmtOutletsTableEnergyStartTime_Object = MibTableColumn
pmPowerMgmtOutletsTableEnergyStartTime = _PmPowerMgmtOutletsTableEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 106),
    _PmPowerMgmtOutletsTableEnergyStartTime_Type()
)
pmPowerMgmtOutletsTableEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableEnergyStartTime.setStatus("current")


class _PmPowerMgmtOutletsTableEnergyReset_Type(Integer32):
    """Custom type pmPowerMgmtOutletsTableEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtOutletsTableEnergyReset_Type.__name__ = "Integer32"
_PmPowerMgmtOutletsTableEnergyReset_Object = MibTableColumn
pmPowerMgmtOutletsTableEnergyReset = _PmPowerMgmtOutletsTableEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 5, 1, 107),
    _PmPowerMgmtOutletsTableEnergyReset_Type()
)
pmPowerMgmtOutletsTableEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtOutletsTableEnergyReset.setStatus("current")
_PmPowerMgmtNumberOfOutletGroup_Type = Integer32
_PmPowerMgmtNumberOfOutletGroup_Object = MibScalar
pmPowerMgmtNumberOfOutletGroup = _PmPowerMgmtNumberOfOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 6),
    _PmPowerMgmtNumberOfOutletGroup_Type()
)
pmPowerMgmtNumberOfOutletGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtNumberOfOutletGroup.setStatus("current")
_PmPowerMgmtGroupTable_Object = MibTable
pmPowerMgmtGroupTable = _PmPowerMgmtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 7)
)
if mibBuilder.loadTexts:
    pmPowerMgmtGroupTable.setStatus("current")
_PmPowerMgmtGroupTableEntry_Object = MibTableRow
pmPowerMgmtGroupTableEntry = _PmPowerMgmtGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 7, 1)
)
pmPowerMgmtGroupTableEntry.setIndexNames(
    (0, "PM-MIB", "pmPowerMgmtGroupTableIndex"),
)
if mibBuilder.loadTexts:
    pmPowerMgmtGroupTableEntry.setStatus("current")
_PmPowerMgmtGroupTableIndex_Type = InterfaceIndexOrZero
_PmPowerMgmtGroupTableIndex_Object = MibTableColumn
pmPowerMgmtGroupTableIndex = _PmPowerMgmtGroupTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 7, 1, 1),
    _PmPowerMgmtGroupTableIndex_Type()
)
pmPowerMgmtGroupTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtGroupTableIndex.setStatus("current")
_PmPowerMgmtGroupTableName_Type = DisplayString
_PmPowerMgmtGroupTableName_Object = MibTableColumn
pmPowerMgmtGroupTableName = _PmPowerMgmtGroupTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 7, 1, 2),
    _PmPowerMgmtGroupTableName_Type()
)
pmPowerMgmtGroupTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtGroupTableName.setStatus("current")


class _PmPowerMgmtGroupTableStatus_Type(Integer32):
    """Custom type pmPowerMgmtGroupTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_PmPowerMgmtGroupTableStatus_Type.__name__ = "Integer32"
_PmPowerMgmtGroupTableStatus_Object = MibTableColumn
pmPowerMgmtGroupTableStatus = _PmPowerMgmtGroupTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 7, 1, 3),
    _PmPowerMgmtGroupTableStatus_Type()
)
pmPowerMgmtGroupTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtGroupTableStatus.setStatus("current")


class _PmPowerMgmtGroupTablePowerControl_Type(Integer32):
    """Custom type pmPowerMgmtGroupTablePowerControl based on Integer32"""
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
        *(("noAction", 1),
          ("powerOn", 2),
          ("powerOff", 3),
          ("powerCycle", 4))
    )


_PmPowerMgmtGroupTablePowerControl_Type.__name__ = "Integer32"
_PmPowerMgmtGroupTablePowerControl_Object = MibTableColumn
pmPowerMgmtGroupTablePowerControl = _PmPowerMgmtGroupTablePowerControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 7, 1, 4),
    _PmPowerMgmtGroupTablePowerControl_Type()
)
pmPowerMgmtGroupTablePowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtGroupTablePowerControl.setStatus("current")
_PmPowerMgmtTotalNumberOfPhases_Type = Integer32
_PmPowerMgmtTotalNumberOfPhases_Object = MibScalar
pmPowerMgmtTotalNumberOfPhases = _PmPowerMgmtTotalNumberOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 8),
    _PmPowerMgmtTotalNumberOfPhases_Type()
)
pmPowerMgmtTotalNumberOfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtTotalNumberOfPhases.setStatus("current")
_PmPowerMgmtPhasesTable_Object = MibTable
pmPowerMgmtPhasesTable = _PmPowerMgmtPhasesTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9)
)
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTable.setStatus("current")
_PmPowerMgmtPhasesTableEntry_Object = MibTableRow
pmPowerMgmtPhasesTableEntry = _PmPowerMgmtPhasesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1)
)
pmPowerMgmtPhasesTableEntry.setIndexNames(
    (0, "PM-MIB", "pmPowerMgmtPhasesTablePortNumber"),
    (0, "PM-MIB", "pmPowerMgmtPhasesTablePduNumber"),
    (0, "PM-MIB", "pmPowerMgmtPhasesTableNumber"),
)
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableEntry.setStatus("current")
_PmPowerMgmtPhasesTablePortNumber_Type = InterfaceIndex
_PmPowerMgmtPhasesTablePortNumber_Object = MibTableColumn
pmPowerMgmtPhasesTablePortNumber = _PmPowerMgmtPhasesTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 1),
    _PmPowerMgmtPhasesTablePortNumber_Type()
)
pmPowerMgmtPhasesTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePortNumber.setStatus("current")
_PmPowerMgmtPhasesTablePduNumber_Type = InterfaceIndex
_PmPowerMgmtPhasesTablePduNumber_Object = MibTableColumn
pmPowerMgmtPhasesTablePduNumber = _PmPowerMgmtPhasesTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 2),
    _PmPowerMgmtPhasesTablePduNumber_Type()
)
pmPowerMgmtPhasesTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePduNumber.setStatus("current")
_PmPowerMgmtPhasesTableNumber_Type = InterfaceIndex
_PmPowerMgmtPhasesTableNumber_Object = MibTableColumn
pmPowerMgmtPhasesTableNumber = _PmPowerMgmtPhasesTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 3),
    _PmPowerMgmtPhasesTableNumber_Type()
)
pmPowerMgmtPhasesTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableNumber.setStatus("current")
_PmPowerMgmtPhasesTableName_Type = DisplayString
_PmPowerMgmtPhasesTableName_Object = MibTableColumn
pmPowerMgmtPhasesTableName = _PmPowerMgmtPhasesTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 4),
    _PmPowerMgmtPhasesTableName_Type()
)
pmPowerMgmtPhasesTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableName.setStatus("current")
_PmPowerMgmtPhasesTablePortName_Type = DisplayString
_PmPowerMgmtPhasesTablePortName_Object = MibTableColumn
pmPowerMgmtPhasesTablePortName = _PmPowerMgmtPhasesTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 5),
    _PmPowerMgmtPhasesTablePortName_Type()
)
pmPowerMgmtPhasesTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePortName.setStatus("current")
_PmPowerMgmtPhasesTablePduId_Type = DisplayString
_PmPowerMgmtPhasesTablePduId_Object = MibTableColumn
pmPowerMgmtPhasesTablePduId = _PmPowerMgmtPhasesTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 6),
    _PmPowerMgmtPhasesTablePduId_Type()
)
pmPowerMgmtPhasesTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePduId.setStatus("current")


class _PmPowerMgmtPhasesTableAlarm_Type(Integer32):
    """Custom type pmPowerMgmtPhasesTableAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("blow-fuse", 2),
          ("hw-ocp", 3),
          ("high-critical", 4),
          ("high-warning", 5),
          ("low-warning", 6),
          ("low-critical", 7))
    )


_PmPowerMgmtPhasesTableAlarm_Type.__name__ = "Integer32"
_PmPowerMgmtPhasesTableAlarm_Object = MibTableColumn
pmPowerMgmtPhasesTableAlarm = _PmPowerMgmtPhasesTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 45),
    _PmPowerMgmtPhasesTableAlarm_Type()
)
pmPowerMgmtPhasesTableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableAlarm.setStatus("current")
_PmPowerMgmtPhasesTableCurrentValue_Type = Integer32
_PmPowerMgmtPhasesTableCurrentValue_Object = MibTableColumn
pmPowerMgmtPhasesTableCurrentValue = _PmPowerMgmtPhasesTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 50),
    _PmPowerMgmtPhasesTableCurrentValue_Type()
)
pmPowerMgmtPhasesTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableCurrentValue.setStatus("current")
_PmPowerMgmtPhasesTableCurrentMax_Type = Integer32
_PmPowerMgmtPhasesTableCurrentMax_Object = MibTableColumn
pmPowerMgmtPhasesTableCurrentMax = _PmPowerMgmtPhasesTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 51),
    _PmPowerMgmtPhasesTableCurrentMax_Type()
)
pmPowerMgmtPhasesTableCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableCurrentMax.setStatus("current")
_PmPowerMgmtPhasesTableCurrentMin_Type = Integer32
_PmPowerMgmtPhasesTableCurrentMin_Object = MibTableColumn
pmPowerMgmtPhasesTableCurrentMin = _PmPowerMgmtPhasesTableCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 52),
    _PmPowerMgmtPhasesTableCurrentMin_Type()
)
pmPowerMgmtPhasesTableCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableCurrentMin.setStatus("current")
_PmPowerMgmtPhasesTableCurrentAvg_Type = Integer32
_PmPowerMgmtPhasesTableCurrentAvg_Object = MibTableColumn
pmPowerMgmtPhasesTableCurrentAvg = _PmPowerMgmtPhasesTableCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 53),
    _PmPowerMgmtPhasesTableCurrentAvg_Type()
)
pmPowerMgmtPhasesTableCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableCurrentAvg.setStatus("current")


class _PmPowerMgmtPhasesTableCurrentReset_Type(Integer32):
    """Custom type pmPowerMgmtPhasesTableCurrentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtPhasesTableCurrentReset_Type.__name__ = "Integer32"
_PmPowerMgmtPhasesTableCurrentReset_Object = MibTableColumn
pmPowerMgmtPhasesTableCurrentReset = _PmPowerMgmtPhasesTableCurrentReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 54),
    _PmPowerMgmtPhasesTableCurrentReset_Type()
)
pmPowerMgmtPhasesTableCurrentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableCurrentReset.setStatus("current")
_PmPowerMgmtPhasesTablePowerValue_Type = Integer32
_PmPowerMgmtPhasesTablePowerValue_Object = MibTableColumn
pmPowerMgmtPhasesTablePowerValue = _PmPowerMgmtPhasesTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 60),
    _PmPowerMgmtPhasesTablePowerValue_Type()
)
pmPowerMgmtPhasesTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePowerValue.setStatus("current")
_PmPowerMgmtPhasesTablePowerMax_Type = Integer32
_PmPowerMgmtPhasesTablePowerMax_Object = MibTableColumn
pmPowerMgmtPhasesTablePowerMax = _PmPowerMgmtPhasesTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 61),
    _PmPowerMgmtPhasesTablePowerMax_Type()
)
pmPowerMgmtPhasesTablePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePowerMax.setStatus("current")
_PmPowerMgmtPhasesTablePowerMin_Type = Integer32
_PmPowerMgmtPhasesTablePowerMin_Object = MibTableColumn
pmPowerMgmtPhasesTablePowerMin = _PmPowerMgmtPhasesTablePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 62),
    _PmPowerMgmtPhasesTablePowerMin_Type()
)
pmPowerMgmtPhasesTablePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePowerMin.setStatus("current")
_PmPowerMgmtPhasesTablePowerAvg_Type = Integer32
_PmPowerMgmtPhasesTablePowerAvg_Object = MibTableColumn
pmPowerMgmtPhasesTablePowerAvg = _PmPowerMgmtPhasesTablePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 63),
    _PmPowerMgmtPhasesTablePowerAvg_Type()
)
pmPowerMgmtPhasesTablePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePowerAvg.setStatus("current")


class _PmPowerMgmtPhasesTablePowerReset_Type(Integer32):
    """Custom type pmPowerMgmtPhasesTablePowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtPhasesTablePowerReset_Type.__name__ = "Integer32"
_PmPowerMgmtPhasesTablePowerReset_Object = MibTableColumn
pmPowerMgmtPhasesTablePowerReset = _PmPowerMgmtPhasesTablePowerReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 64),
    _PmPowerMgmtPhasesTablePowerReset_Type()
)
pmPowerMgmtPhasesTablePowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePowerReset.setStatus("current")


class _PmPowerMgmtPhasesTablePowerType_Type(Integer32):
    """Custom type pmPowerMgmtPhasesTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("measured", 2))
    )


_PmPowerMgmtPhasesTablePowerType_Type.__name__ = "Integer32"
_PmPowerMgmtPhasesTablePowerType_Object = MibTableColumn
pmPowerMgmtPhasesTablePowerType = _PmPowerMgmtPhasesTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 65),
    _PmPowerMgmtPhasesTablePowerType_Type()
)
pmPowerMgmtPhasesTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePowerType.setStatus("current")
_PmPowerMgmtPhasesTableVoltageValue_Type = Integer32
_PmPowerMgmtPhasesTableVoltageValue_Object = MibTableColumn
pmPowerMgmtPhasesTableVoltageValue = _PmPowerMgmtPhasesTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 70),
    _PmPowerMgmtPhasesTableVoltageValue_Type()
)
pmPowerMgmtPhasesTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableVoltageValue.setStatus("current")
_PmPowerMgmtPhasesTableVoltageMax_Type = Integer32
_PmPowerMgmtPhasesTableVoltageMax_Object = MibTableColumn
pmPowerMgmtPhasesTableVoltageMax = _PmPowerMgmtPhasesTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 71),
    _PmPowerMgmtPhasesTableVoltageMax_Type()
)
pmPowerMgmtPhasesTableVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableVoltageMax.setStatus("current")
_PmPowerMgmtPhasesTableVoltageMin_Type = Integer32
_PmPowerMgmtPhasesTableVoltageMin_Object = MibTableColumn
pmPowerMgmtPhasesTableVoltageMin = _PmPowerMgmtPhasesTableVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 72),
    _PmPowerMgmtPhasesTableVoltageMin_Type()
)
pmPowerMgmtPhasesTableVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableVoltageMin.setStatus("current")
_PmPowerMgmtPhasesTableVoltageAvg_Type = Integer32
_PmPowerMgmtPhasesTableVoltageAvg_Object = MibTableColumn
pmPowerMgmtPhasesTableVoltageAvg = _PmPowerMgmtPhasesTableVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 73),
    _PmPowerMgmtPhasesTableVoltageAvg_Type()
)
pmPowerMgmtPhasesTableVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableVoltageAvg.setStatus("current")


class _PmPowerMgmtPhasesTableVoltageReset_Type(Integer32):
    """Custom type pmPowerMgmtPhasesTableVoltageReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtPhasesTableVoltageReset_Type.__name__ = "Integer32"
_PmPowerMgmtPhasesTableVoltageReset_Object = MibTableColumn
pmPowerMgmtPhasesTableVoltageReset = _PmPowerMgmtPhasesTableVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 74),
    _PmPowerMgmtPhasesTableVoltageReset_Type()
)
pmPowerMgmtPhasesTableVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableVoltageReset.setStatus("current")


class _PmPowerMgmtPhasesTableVoltageType_Type(Integer32):
    """Custom type pmPowerMgmtPhasesTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("measured", 2))
    )


_PmPowerMgmtPhasesTableVoltageType_Type.__name__ = "Integer32"
_PmPowerMgmtPhasesTableVoltageType_Object = MibTableColumn
pmPowerMgmtPhasesTableVoltageType = _PmPowerMgmtPhasesTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 75),
    _PmPowerMgmtPhasesTableVoltageType_Type()
)
pmPowerMgmtPhasesTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableVoltageType.setStatus("current")
_PmPowerMgmtPhasesTablePowerFactorValue_Type = Integer32
_PmPowerMgmtPhasesTablePowerFactorValue_Object = MibTableColumn
pmPowerMgmtPhasesTablePowerFactorValue = _PmPowerMgmtPhasesTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 80),
    _PmPowerMgmtPhasesTablePowerFactorValue_Type()
)
pmPowerMgmtPhasesTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePowerFactorValue.setStatus("current")
_PmPowerMgmtPhasesTablePowerFactorMax_Type = Integer32
_PmPowerMgmtPhasesTablePowerFactorMax_Object = MibTableColumn
pmPowerMgmtPhasesTablePowerFactorMax = _PmPowerMgmtPhasesTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 81),
    _PmPowerMgmtPhasesTablePowerFactorMax_Type()
)
pmPowerMgmtPhasesTablePowerFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePowerFactorMax.setStatus("current")
_PmPowerMgmtPhasesTablePowerFactorMin_Type = Integer32
_PmPowerMgmtPhasesTablePowerFactorMin_Object = MibTableColumn
pmPowerMgmtPhasesTablePowerFactorMin = _PmPowerMgmtPhasesTablePowerFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 82),
    _PmPowerMgmtPhasesTablePowerFactorMin_Type()
)
pmPowerMgmtPhasesTablePowerFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePowerFactorMin.setStatus("current")
_PmPowerMgmtPhasesTablePowerFactorAvg_Type = Integer32
_PmPowerMgmtPhasesTablePowerFactorAvg_Object = MibTableColumn
pmPowerMgmtPhasesTablePowerFactorAvg = _PmPowerMgmtPhasesTablePowerFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 83),
    _PmPowerMgmtPhasesTablePowerFactorAvg_Type()
)
pmPowerMgmtPhasesTablePowerFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePowerFactorAvg.setStatus("current")


class _PmPowerMgmtPhasesTablePowerFactorReset_Type(Integer32):
    """Custom type pmPowerMgmtPhasesTablePowerFactorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtPhasesTablePowerFactorReset_Type.__name__ = "Integer32"
_PmPowerMgmtPhasesTablePowerFactorReset_Object = MibTableColumn
pmPowerMgmtPhasesTablePowerFactorReset = _PmPowerMgmtPhasesTablePowerFactorReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 84),
    _PmPowerMgmtPhasesTablePowerFactorReset_Type()
)
pmPowerMgmtPhasesTablePowerFactorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePowerFactorReset.setStatus("current")


class _PmPowerMgmtPhasesTablePowerFactorType_Type(Integer32):
    """Custom type pmPowerMgmtPhasesTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("measured", 2))
    )


_PmPowerMgmtPhasesTablePowerFactorType_Type.__name__ = "Integer32"
_PmPowerMgmtPhasesTablePowerFactorType_Object = MibTableColumn
pmPowerMgmtPhasesTablePowerFactorType = _PmPowerMgmtPhasesTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 85),
    _PmPowerMgmtPhasesTablePowerFactorType_Type()
)
pmPowerMgmtPhasesTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTablePowerFactorType.setStatus("current")
_PmPowerMgmtPhasesTableCurrentHighCritical_Type = Integer32
_PmPowerMgmtPhasesTableCurrentHighCritical_Object = MibTableColumn
pmPowerMgmtPhasesTableCurrentHighCritical = _PmPowerMgmtPhasesTableCurrentHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 100),
    _PmPowerMgmtPhasesTableCurrentHighCritical_Type()
)
pmPowerMgmtPhasesTableCurrentHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableCurrentHighCritical.setStatus("current")
_PmPowerMgmtPhasesTableCurrentHighWarning_Type = Integer32
_PmPowerMgmtPhasesTableCurrentHighWarning_Object = MibTableColumn
pmPowerMgmtPhasesTableCurrentHighWarning = _PmPowerMgmtPhasesTableCurrentHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 101),
    _PmPowerMgmtPhasesTableCurrentHighWarning_Type()
)
pmPowerMgmtPhasesTableCurrentHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableCurrentHighWarning.setStatus("current")
_PmPowerMgmtPhasesTableCurrentLowWarning_Type = Integer32
_PmPowerMgmtPhasesTableCurrentLowWarning_Object = MibTableColumn
pmPowerMgmtPhasesTableCurrentLowWarning = _PmPowerMgmtPhasesTableCurrentLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 102),
    _PmPowerMgmtPhasesTableCurrentLowWarning_Type()
)
pmPowerMgmtPhasesTableCurrentLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableCurrentLowWarning.setStatus("current")
_PmPowerMgmtPhasesTableCurrentLowCritical_Type = Integer32
_PmPowerMgmtPhasesTableCurrentLowCritical_Object = MibTableColumn
pmPowerMgmtPhasesTableCurrentLowCritical = _PmPowerMgmtPhasesTableCurrentLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 9, 1, 103),
    _PmPowerMgmtPhasesTableCurrentLowCritical_Type()
)
pmPowerMgmtPhasesTableCurrentLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtPhasesTableCurrentLowCritical.setStatus("current")
_PmPowerMgmtTotalNumberOfBanks_Type = Integer32
_PmPowerMgmtTotalNumberOfBanks_Object = MibScalar
pmPowerMgmtTotalNumberOfBanks = _PmPowerMgmtTotalNumberOfBanks_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 10),
    _PmPowerMgmtTotalNumberOfBanks_Type()
)
pmPowerMgmtTotalNumberOfBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtTotalNumberOfBanks.setStatus("current")
_PmPowerMgmtBanksTable_Object = MibTable
pmPowerMgmtBanksTable = _PmPowerMgmtBanksTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11)
)
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTable.setStatus("current")
_PmPowerMgmtBanksTableEntry_Object = MibTableRow
pmPowerMgmtBanksTableEntry = _PmPowerMgmtBanksTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1)
)
pmPowerMgmtBanksTableEntry.setIndexNames(
    (0, "PM-MIB", "pmPowerMgmtBanksTablePortNumber"),
    (0, "PM-MIB", "pmPowerMgmtBanksTablePduNumber"),
    (0, "PM-MIB", "pmPowerMgmtBanksTableNumber"),
)
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableEntry.setStatus("current")
_PmPowerMgmtBanksTablePortNumber_Type = InterfaceIndex
_PmPowerMgmtBanksTablePortNumber_Object = MibTableColumn
pmPowerMgmtBanksTablePortNumber = _PmPowerMgmtBanksTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 1),
    _PmPowerMgmtBanksTablePortNumber_Type()
)
pmPowerMgmtBanksTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePortNumber.setStatus("current")
_PmPowerMgmtBanksTablePduNumber_Type = InterfaceIndex
_PmPowerMgmtBanksTablePduNumber_Object = MibTableColumn
pmPowerMgmtBanksTablePduNumber = _PmPowerMgmtBanksTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 2),
    _PmPowerMgmtBanksTablePduNumber_Type()
)
pmPowerMgmtBanksTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePduNumber.setStatus("current")
_PmPowerMgmtBanksTableNumber_Type = InterfaceIndex
_PmPowerMgmtBanksTableNumber_Object = MibTableColumn
pmPowerMgmtBanksTableNumber = _PmPowerMgmtBanksTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 3),
    _PmPowerMgmtBanksTableNumber_Type()
)
pmPowerMgmtBanksTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableNumber.setStatus("current")
_PmPowerMgmtBanksTableName_Type = DisplayString
_PmPowerMgmtBanksTableName_Object = MibTableColumn
pmPowerMgmtBanksTableName = _PmPowerMgmtBanksTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 4),
    _PmPowerMgmtBanksTableName_Type()
)
pmPowerMgmtBanksTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableName.setStatus("current")
_PmPowerMgmtBanksTablePortName_Type = DisplayString
_PmPowerMgmtBanksTablePortName_Object = MibTableColumn
pmPowerMgmtBanksTablePortName = _PmPowerMgmtBanksTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 5),
    _PmPowerMgmtBanksTablePortName_Type()
)
pmPowerMgmtBanksTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePortName.setStatus("current")
_PmPowerMgmtBanksTablePduId_Type = DisplayString
_PmPowerMgmtBanksTablePduId_Object = MibTableColumn
pmPowerMgmtBanksTablePduId = _PmPowerMgmtBanksTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 6),
    _PmPowerMgmtBanksTablePduId_Type()
)
pmPowerMgmtBanksTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePduId.setStatus("current")


class _PmPowerMgmtBanksTableAlarm_Type(Integer32):
    """Custom type pmPowerMgmtBanksTableAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("blow-fuse", 2),
          ("hw-ocp", 3),
          ("high-critical", 4),
          ("high-warning", 5),
          ("low-warning", 6),
          ("low-critical", 7))
    )


_PmPowerMgmtBanksTableAlarm_Type.__name__ = "Integer32"
_PmPowerMgmtBanksTableAlarm_Object = MibTableColumn
pmPowerMgmtBanksTableAlarm = _PmPowerMgmtBanksTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 45),
    _PmPowerMgmtBanksTableAlarm_Type()
)
pmPowerMgmtBanksTableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableAlarm.setStatus("current")
_PmPowerMgmtBanksTableCurrentValue_Type = Integer32
_PmPowerMgmtBanksTableCurrentValue_Object = MibTableColumn
pmPowerMgmtBanksTableCurrentValue = _PmPowerMgmtBanksTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 50),
    _PmPowerMgmtBanksTableCurrentValue_Type()
)
pmPowerMgmtBanksTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableCurrentValue.setStatus("current")
_PmPowerMgmtBanksTableCurrentMax_Type = Integer32
_PmPowerMgmtBanksTableCurrentMax_Object = MibTableColumn
pmPowerMgmtBanksTableCurrentMax = _PmPowerMgmtBanksTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 51),
    _PmPowerMgmtBanksTableCurrentMax_Type()
)
pmPowerMgmtBanksTableCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableCurrentMax.setStatus("current")
_PmPowerMgmtBanksTableCurrentMin_Type = Integer32
_PmPowerMgmtBanksTableCurrentMin_Object = MibTableColumn
pmPowerMgmtBanksTableCurrentMin = _PmPowerMgmtBanksTableCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 52),
    _PmPowerMgmtBanksTableCurrentMin_Type()
)
pmPowerMgmtBanksTableCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableCurrentMin.setStatus("current")
_PmPowerMgmtBanksTableCurrentAvg_Type = Integer32
_PmPowerMgmtBanksTableCurrentAvg_Object = MibTableColumn
pmPowerMgmtBanksTableCurrentAvg = _PmPowerMgmtBanksTableCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 53),
    _PmPowerMgmtBanksTableCurrentAvg_Type()
)
pmPowerMgmtBanksTableCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableCurrentAvg.setStatus("current")


class _PmPowerMgmtBanksTableCurrentReset_Type(Integer32):
    """Custom type pmPowerMgmtBanksTableCurrentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtBanksTableCurrentReset_Type.__name__ = "Integer32"
_PmPowerMgmtBanksTableCurrentReset_Object = MibTableColumn
pmPowerMgmtBanksTableCurrentReset = _PmPowerMgmtBanksTableCurrentReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 54),
    _PmPowerMgmtBanksTableCurrentReset_Type()
)
pmPowerMgmtBanksTableCurrentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableCurrentReset.setStatus("current")
_PmPowerMgmtBanksTablePowerValue_Type = Integer32
_PmPowerMgmtBanksTablePowerValue_Object = MibTableColumn
pmPowerMgmtBanksTablePowerValue = _PmPowerMgmtBanksTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 60),
    _PmPowerMgmtBanksTablePowerValue_Type()
)
pmPowerMgmtBanksTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePowerValue.setStatus("current")
_PmPowerMgmtBanksTablePowerMax_Type = Integer32
_PmPowerMgmtBanksTablePowerMax_Object = MibTableColumn
pmPowerMgmtBanksTablePowerMax = _PmPowerMgmtBanksTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 61),
    _PmPowerMgmtBanksTablePowerMax_Type()
)
pmPowerMgmtBanksTablePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePowerMax.setStatus("current")
_PmPowerMgmtBanksTablePowerMin_Type = Integer32
_PmPowerMgmtBanksTablePowerMin_Object = MibTableColumn
pmPowerMgmtBanksTablePowerMin = _PmPowerMgmtBanksTablePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 62),
    _PmPowerMgmtBanksTablePowerMin_Type()
)
pmPowerMgmtBanksTablePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePowerMin.setStatus("current")
_PmPowerMgmtBanksTablePowerAvg_Type = Integer32
_PmPowerMgmtBanksTablePowerAvg_Object = MibTableColumn
pmPowerMgmtBanksTablePowerAvg = _PmPowerMgmtBanksTablePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 63),
    _PmPowerMgmtBanksTablePowerAvg_Type()
)
pmPowerMgmtBanksTablePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePowerAvg.setStatus("current")


class _PmPowerMgmtBanksTablePowerReset_Type(Integer32):
    """Custom type pmPowerMgmtBanksTablePowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtBanksTablePowerReset_Type.__name__ = "Integer32"
_PmPowerMgmtBanksTablePowerReset_Object = MibTableColumn
pmPowerMgmtBanksTablePowerReset = _PmPowerMgmtBanksTablePowerReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 64),
    _PmPowerMgmtBanksTablePowerReset_Type()
)
pmPowerMgmtBanksTablePowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePowerReset.setStatus("current")


class _PmPowerMgmtBanksTablePowerType_Type(Integer32):
    """Custom type pmPowerMgmtBanksTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("measured", 2))
    )


_PmPowerMgmtBanksTablePowerType_Type.__name__ = "Integer32"
_PmPowerMgmtBanksTablePowerType_Object = MibTableColumn
pmPowerMgmtBanksTablePowerType = _PmPowerMgmtBanksTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 65),
    _PmPowerMgmtBanksTablePowerType_Type()
)
pmPowerMgmtBanksTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePowerType.setStatus("current")
_PmPowerMgmtBanksTableVoltageValue_Type = Integer32
_PmPowerMgmtBanksTableVoltageValue_Object = MibTableColumn
pmPowerMgmtBanksTableVoltageValue = _PmPowerMgmtBanksTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 70),
    _PmPowerMgmtBanksTableVoltageValue_Type()
)
pmPowerMgmtBanksTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableVoltageValue.setStatus("current")
_PmPowerMgmtBanksTableVoltageMax_Type = Integer32
_PmPowerMgmtBanksTableVoltageMax_Object = MibTableColumn
pmPowerMgmtBanksTableVoltageMax = _PmPowerMgmtBanksTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 71),
    _PmPowerMgmtBanksTableVoltageMax_Type()
)
pmPowerMgmtBanksTableVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableVoltageMax.setStatus("current")
_PmPowerMgmtBanksTableVoltageMin_Type = Integer32
_PmPowerMgmtBanksTableVoltageMin_Object = MibTableColumn
pmPowerMgmtBanksTableVoltageMin = _PmPowerMgmtBanksTableVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 72),
    _PmPowerMgmtBanksTableVoltageMin_Type()
)
pmPowerMgmtBanksTableVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableVoltageMin.setStatus("current")
_PmPowerMgmtBanksTableVoltageAvg_Type = Integer32
_PmPowerMgmtBanksTableVoltageAvg_Object = MibTableColumn
pmPowerMgmtBanksTableVoltageAvg = _PmPowerMgmtBanksTableVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 73),
    _PmPowerMgmtBanksTableVoltageAvg_Type()
)
pmPowerMgmtBanksTableVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableVoltageAvg.setStatus("current")


class _PmPowerMgmtBanksTableVoltageReset_Type(Integer32):
    """Custom type pmPowerMgmtBanksTableVoltageReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtBanksTableVoltageReset_Type.__name__ = "Integer32"
_PmPowerMgmtBanksTableVoltageReset_Object = MibTableColumn
pmPowerMgmtBanksTableVoltageReset = _PmPowerMgmtBanksTableVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 74),
    _PmPowerMgmtBanksTableVoltageReset_Type()
)
pmPowerMgmtBanksTableVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableVoltageReset.setStatus("current")


class _PmPowerMgmtBanksTableVoltageType_Type(Integer32):
    """Custom type pmPowerMgmtBanksTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("measured", 2))
    )


_PmPowerMgmtBanksTableVoltageType_Type.__name__ = "Integer32"
_PmPowerMgmtBanksTableVoltageType_Object = MibTableColumn
pmPowerMgmtBanksTableVoltageType = _PmPowerMgmtBanksTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 75),
    _PmPowerMgmtBanksTableVoltageType_Type()
)
pmPowerMgmtBanksTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableVoltageType.setStatus("current")
_PmPowerMgmtBanksTablePowerFactorValue_Type = Integer32
_PmPowerMgmtBanksTablePowerFactorValue_Object = MibTableColumn
pmPowerMgmtBanksTablePowerFactorValue = _PmPowerMgmtBanksTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 80),
    _PmPowerMgmtBanksTablePowerFactorValue_Type()
)
pmPowerMgmtBanksTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePowerFactorValue.setStatus("current")
_PmPowerMgmtBanksTablePowerFactorMax_Type = Integer32
_PmPowerMgmtBanksTablePowerFactorMax_Object = MibTableColumn
pmPowerMgmtBanksTablePowerFactorMax = _PmPowerMgmtBanksTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 81),
    _PmPowerMgmtBanksTablePowerFactorMax_Type()
)
pmPowerMgmtBanksTablePowerFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePowerFactorMax.setStatus("current")
_PmPowerMgmtBanksTablePowerFactorMin_Type = Integer32
_PmPowerMgmtBanksTablePowerFactorMin_Object = MibTableColumn
pmPowerMgmtBanksTablePowerFactorMin = _PmPowerMgmtBanksTablePowerFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 82),
    _PmPowerMgmtBanksTablePowerFactorMin_Type()
)
pmPowerMgmtBanksTablePowerFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePowerFactorMin.setStatus("current")
_PmPowerMgmtBanksTablePowerFactorAvg_Type = Integer32
_PmPowerMgmtBanksTablePowerFactorAvg_Object = MibTableColumn
pmPowerMgmtBanksTablePowerFactorAvg = _PmPowerMgmtBanksTablePowerFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 83),
    _PmPowerMgmtBanksTablePowerFactorAvg_Type()
)
pmPowerMgmtBanksTablePowerFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePowerFactorAvg.setStatus("current")


class _PmPowerMgmtBanksTablePowerFactorReset_Type(Integer32):
    """Custom type pmPowerMgmtBanksTablePowerFactorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtBanksTablePowerFactorReset_Type.__name__ = "Integer32"
_PmPowerMgmtBanksTablePowerFactorReset_Object = MibTableColumn
pmPowerMgmtBanksTablePowerFactorReset = _PmPowerMgmtBanksTablePowerFactorReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 84),
    _PmPowerMgmtBanksTablePowerFactorReset_Type()
)
pmPowerMgmtBanksTablePowerFactorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePowerFactorReset.setStatus("current")


class _PmPowerMgmtBanksTablePowerFactorType_Type(Integer32):
    """Custom type pmPowerMgmtBanksTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none-sensor", 0),
          ("estimated", 1),
          ("measured", 2))
    )


_PmPowerMgmtBanksTablePowerFactorType_Type.__name__ = "Integer32"
_PmPowerMgmtBanksTablePowerFactorType_Object = MibTableColumn
pmPowerMgmtBanksTablePowerFactorType = _PmPowerMgmtBanksTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 85),
    _PmPowerMgmtBanksTablePowerFactorType_Type()
)
pmPowerMgmtBanksTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTablePowerFactorType.setStatus("current")
_PmPowerMgmtBanksTableCurrentHighCritical_Type = Integer32
_PmPowerMgmtBanksTableCurrentHighCritical_Object = MibTableColumn
pmPowerMgmtBanksTableCurrentHighCritical = _PmPowerMgmtBanksTableCurrentHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 100),
    _PmPowerMgmtBanksTableCurrentHighCritical_Type()
)
pmPowerMgmtBanksTableCurrentHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableCurrentHighCritical.setStatus("current")
_PmPowerMgmtBanksTableCurrentHighWarning_Type = Integer32
_PmPowerMgmtBanksTableCurrentHighWarning_Object = MibTableColumn
pmPowerMgmtBanksTableCurrentHighWarning = _PmPowerMgmtBanksTableCurrentHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 101),
    _PmPowerMgmtBanksTableCurrentHighWarning_Type()
)
pmPowerMgmtBanksTableCurrentHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableCurrentHighWarning.setStatus("current")
_PmPowerMgmtBanksTableCurrentLowWarning_Type = Integer32
_PmPowerMgmtBanksTableCurrentLowWarning_Object = MibTableColumn
pmPowerMgmtBanksTableCurrentLowWarning = _PmPowerMgmtBanksTableCurrentLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 102),
    _PmPowerMgmtBanksTableCurrentLowWarning_Type()
)
pmPowerMgmtBanksTableCurrentLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableCurrentLowWarning.setStatus("current")
_PmPowerMgmtBanksTableCurrentLowCritical_Type = Integer32
_PmPowerMgmtBanksTableCurrentLowCritical_Object = MibTableColumn
pmPowerMgmtBanksTableCurrentLowCritical = _PmPowerMgmtBanksTableCurrentLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 103),
    _PmPowerMgmtBanksTableCurrentLowCritical_Type()
)
pmPowerMgmtBanksTableCurrentLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableCurrentLowCritical.setStatus("current")
_PmPowerMgmtBanksTableEnergyValue_Type = Integer32
_PmPowerMgmtBanksTableEnergyValue_Object = MibTableColumn
pmPowerMgmtBanksTableEnergyValue = _PmPowerMgmtBanksTableEnergyValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 105),
    _PmPowerMgmtBanksTableEnergyValue_Type()
)
pmPowerMgmtBanksTableEnergyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableEnergyValue.setStatus("current")
_PmPowerMgmtBanksTableEnergyStartTime_Type = DisplayString
_PmPowerMgmtBanksTableEnergyStartTime_Object = MibTableColumn
pmPowerMgmtBanksTableEnergyStartTime = _PmPowerMgmtBanksTableEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 106),
    _PmPowerMgmtBanksTableEnergyStartTime_Type()
)
pmPowerMgmtBanksTableEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableEnergyStartTime.setStatus("current")


class _PmPowerMgmtBanksTableEnergyReset_Type(Integer32):
    """Custom type pmPowerMgmtBanksTableEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtBanksTableEnergyReset_Type.__name__ = "Integer32"
_PmPowerMgmtBanksTableEnergyReset_Object = MibTableColumn
pmPowerMgmtBanksTableEnergyReset = _PmPowerMgmtBanksTableEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 11, 1, 107),
    _PmPowerMgmtBanksTableEnergyReset_Type()
)
pmPowerMgmtBanksTableEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtBanksTableEnergyReset.setStatus("current")
_PmPowerMgmtTotalNumberOfSensors_Type = Integer32
_PmPowerMgmtTotalNumberOfSensors_Object = MibScalar
pmPowerMgmtTotalNumberOfSensors = _PmPowerMgmtTotalNumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 12),
    _PmPowerMgmtTotalNumberOfSensors_Type()
)
pmPowerMgmtTotalNumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtTotalNumberOfSensors.setStatus("current")
_PmPowerMgmtSensorsTable_Object = MibTable
pmPowerMgmtSensorsTable = _PmPowerMgmtSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13)
)
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTable.setStatus("current")
_PmPowerMgmtSensorsTableEntry_Object = MibTableRow
pmPowerMgmtSensorsTableEntry = _PmPowerMgmtSensorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1)
)
pmPowerMgmtSensorsTableEntry.setIndexNames(
    (0, "PM-MIB", "pmPowerMgmtSensorsTablePortNumber"),
    (0, "PM-MIB", "pmPowerMgmtSensorsTablePduNumber"),
    (0, "PM-MIB", "pmPowerMgmtSensorsTableNumber"),
)
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableEntry.setStatus("current")
_PmPowerMgmtSensorsTablePortNumber_Type = InterfaceIndex
_PmPowerMgmtSensorsTablePortNumber_Object = MibTableColumn
pmPowerMgmtSensorsTablePortNumber = _PmPowerMgmtSensorsTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 1),
    _PmPowerMgmtSensorsTablePortNumber_Type()
)
pmPowerMgmtSensorsTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTablePortNumber.setStatus("current")
_PmPowerMgmtSensorsTablePduNumber_Type = InterfaceIndex
_PmPowerMgmtSensorsTablePduNumber_Object = MibTableColumn
pmPowerMgmtSensorsTablePduNumber = _PmPowerMgmtSensorsTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 2),
    _PmPowerMgmtSensorsTablePduNumber_Type()
)
pmPowerMgmtSensorsTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTablePduNumber.setStatus("current")
_PmPowerMgmtSensorsTableNumber_Type = InterfaceIndex
_PmPowerMgmtSensorsTableNumber_Object = MibTableColumn
pmPowerMgmtSensorsTableNumber = _PmPowerMgmtSensorsTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 3),
    _PmPowerMgmtSensorsTableNumber_Type()
)
pmPowerMgmtSensorsTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableNumber.setStatus("current")
_PmPowerMgmtSensorsTableName_Type = DisplayString
_PmPowerMgmtSensorsTableName_Object = MibTableColumn
pmPowerMgmtSensorsTableName = _PmPowerMgmtSensorsTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 4),
    _PmPowerMgmtSensorsTableName_Type()
)
pmPowerMgmtSensorsTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableName.setStatus("current")
_PmPowerMgmtSensorsTablePortName_Type = DisplayString
_PmPowerMgmtSensorsTablePortName_Object = MibTableColumn
pmPowerMgmtSensorsTablePortName = _PmPowerMgmtSensorsTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 5),
    _PmPowerMgmtSensorsTablePortName_Type()
)
pmPowerMgmtSensorsTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTablePortName.setStatus("current")
_PmPowerMgmtSensorsTablePduId_Type = DisplayString
_PmPowerMgmtSensorsTablePduId_Object = MibTableColumn
pmPowerMgmtSensorsTablePduId = _PmPowerMgmtSensorsTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 6),
    _PmPowerMgmtSensorsTablePduId_Type()
)
pmPowerMgmtSensorsTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTablePduId.setStatus("current")


class _PmPowerMgmtSensorsTableType_Type(Integer32):
    """Custom type pmPowerMgmtSensorsTableType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("temp-internal", 1),
          ("temperature", 2),
          ("humidity", 3),
          ("air-flow", 4),
          ("smoke", 5),
          ("dry-concact", 6),
          ("water-level", 7),
          ("motion", 8),
          ("unplugged", 9),
          ("unknown", 10))
    )


_PmPowerMgmtSensorsTableType_Type.__name__ = "Integer32"
_PmPowerMgmtSensorsTableType_Object = MibTableColumn
pmPowerMgmtSensorsTableType = _PmPowerMgmtSensorsTableType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 7),
    _PmPowerMgmtSensorsTableType_Type()
)
pmPowerMgmtSensorsTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableType.setStatus("current")


class _PmPowerMgmtSensorsTableStatus_Type(Integer32):
    """Custom type pmPowerMgmtSensorsTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("triggered", 2),
          ("not-applicable", 3),
          ("opened", 4),
          ("closed", 5))
    )


_PmPowerMgmtSensorsTableStatus_Type.__name__ = "Integer32"
_PmPowerMgmtSensorsTableStatus_Object = MibTableColumn
pmPowerMgmtSensorsTableStatus = _PmPowerMgmtSensorsTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 8),
    _PmPowerMgmtSensorsTableStatus_Type()
)
pmPowerMgmtSensorsTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableStatus.setStatus("current")
_PmPowerMgmtSensorsTableValue_Type = DisplayString
_PmPowerMgmtSensorsTableValue_Object = MibTableColumn
pmPowerMgmtSensorsTableValue = _PmPowerMgmtSensorsTableValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 20),
    _PmPowerMgmtSensorsTableValue_Type()
)
pmPowerMgmtSensorsTableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableValue.setStatus("current")
_PmPowerMgmtSensorsTableValueMax_Type = DisplayString
_PmPowerMgmtSensorsTableValueMax_Object = MibTableColumn
pmPowerMgmtSensorsTableValueMax = _PmPowerMgmtSensorsTableValueMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 21),
    _PmPowerMgmtSensorsTableValueMax_Type()
)
pmPowerMgmtSensorsTableValueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableValueMax.setStatus("current")
_PmPowerMgmtSensorsTableValueMin_Type = DisplayString
_PmPowerMgmtSensorsTableValueMin_Object = MibTableColumn
pmPowerMgmtSensorsTableValueMin = _PmPowerMgmtSensorsTableValueMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 22),
    _PmPowerMgmtSensorsTableValueMin_Type()
)
pmPowerMgmtSensorsTableValueMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableValueMin.setStatus("current")
_PmPowerMgmtSensorsTableValueAvg_Type = DisplayString
_PmPowerMgmtSensorsTableValueAvg_Object = MibTableColumn
pmPowerMgmtSensorsTableValueAvg = _PmPowerMgmtSensorsTableValueAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 23),
    _PmPowerMgmtSensorsTableValueAvg_Type()
)
pmPowerMgmtSensorsTableValueAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableValueAvg.setStatus("current")
_PmPowerMgmtSensorsTableValueInt_Type = Integer32
_PmPowerMgmtSensorsTableValueInt_Object = MibTableColumn
pmPowerMgmtSensorsTableValueInt = _PmPowerMgmtSensorsTableValueInt_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 25),
    _PmPowerMgmtSensorsTableValueInt_Type()
)
pmPowerMgmtSensorsTableValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableValueInt.setStatus("current")
_PmPowerMgmtSensorsTableValueMaxInt_Type = Integer32
_PmPowerMgmtSensorsTableValueMaxInt_Object = MibTableColumn
pmPowerMgmtSensorsTableValueMaxInt = _PmPowerMgmtSensorsTableValueMaxInt_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 26),
    _PmPowerMgmtSensorsTableValueMaxInt_Type()
)
pmPowerMgmtSensorsTableValueMaxInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableValueMaxInt.setStatus("current")
_PmPowerMgmtSensorsTableValueMinInt_Type = Integer32
_PmPowerMgmtSensorsTableValueMinInt_Object = MibTableColumn
pmPowerMgmtSensorsTableValueMinInt = _PmPowerMgmtSensorsTableValueMinInt_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 27),
    _PmPowerMgmtSensorsTableValueMinInt_Type()
)
pmPowerMgmtSensorsTableValueMinInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableValueMinInt.setStatus("current")
_PmPowerMgmtSensorsTableValueAvgInt_Type = Integer32
_PmPowerMgmtSensorsTableValueAvgInt_Object = MibTableColumn
pmPowerMgmtSensorsTableValueAvgInt = _PmPowerMgmtSensorsTableValueAvgInt_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 28),
    _PmPowerMgmtSensorsTableValueAvgInt_Type()
)
pmPowerMgmtSensorsTableValueAvgInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableValueAvgInt.setStatus("current")


class _PmPowerMgmtSensorsTableValueReset_Type(Integer32):
    """Custom type pmPowerMgmtSensorsTableValueReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_PmPowerMgmtSensorsTableValueReset_Type.__name__ = "Integer32"
_PmPowerMgmtSensorsTableValueReset_Object = MibTableColumn
pmPowerMgmtSensorsTableValueReset = _PmPowerMgmtSensorsTableValueReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 30),
    _PmPowerMgmtSensorsTableValueReset_Type()
)
pmPowerMgmtSensorsTableValueReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableValueReset.setStatus("current")
_PmPowerMgmtSensorsTableHighCritical_Type = Integer32
_PmPowerMgmtSensorsTableHighCritical_Object = MibTableColumn
pmPowerMgmtSensorsTableHighCritical = _PmPowerMgmtSensorsTableHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 40),
    _PmPowerMgmtSensorsTableHighCritical_Type()
)
pmPowerMgmtSensorsTableHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableHighCritical.setStatus("current")
_PmPowerMgmtSensorsTableHighWarning_Type = Integer32
_PmPowerMgmtSensorsTableHighWarning_Object = MibTableColumn
pmPowerMgmtSensorsTableHighWarning = _PmPowerMgmtSensorsTableHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 41),
    _PmPowerMgmtSensorsTableHighWarning_Type()
)
pmPowerMgmtSensorsTableHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableHighWarning.setStatus("current")
_PmPowerMgmtSensorsTableLowWarning_Type = Integer32
_PmPowerMgmtSensorsTableLowWarning_Object = MibTableColumn
pmPowerMgmtSensorsTableLowWarning = _PmPowerMgmtSensorsTableLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 42),
    _PmPowerMgmtSensorsTableLowWarning_Type()
)
pmPowerMgmtSensorsTableLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableLowWarning.setStatus("current")
_PmPowerMgmtSensorsTableLowCritical_Type = Integer32
_PmPowerMgmtSensorsTableLowCritical_Object = MibTableColumn
pmPowerMgmtSensorsTableLowCritical = _PmPowerMgmtSensorsTableLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 43),
    _PmPowerMgmtSensorsTableLowCritical_Type()
)
pmPowerMgmtSensorsTableLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableLowCritical.setStatus("current")


class _PmPowerMgmtSensorsTableUnit_Type(Integer32):
    """Custom type pmPowerMgmtSensorsTableUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("fahrenheit", 2),
          ("celsius", 3),
          ("percent", 4),
          ("afu", 5))
    )


_PmPowerMgmtSensorsTableUnit_Type.__name__ = "Integer32"
_PmPowerMgmtSensorsTableUnit_Object = MibTableColumn
pmPowerMgmtSensorsTableUnit = _PmPowerMgmtSensorsTableUnit_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 45),
    _PmPowerMgmtSensorsTableUnit_Type()
)
pmPowerMgmtSensorsTableUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableUnit.setStatus("current")
_PmPowerMgmtSensorsTableHighCriticalC_Type = Integer32
_PmPowerMgmtSensorsTableHighCriticalC_Object = MibTableColumn
pmPowerMgmtSensorsTableHighCriticalC = _PmPowerMgmtSensorsTableHighCriticalC_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 50),
    _PmPowerMgmtSensorsTableHighCriticalC_Type()
)
pmPowerMgmtSensorsTableHighCriticalC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableHighCriticalC.setStatus("current")
_PmPowerMgmtSensorsTableHighWarningC_Type = Integer32
_PmPowerMgmtSensorsTableHighWarningC_Object = MibTableColumn
pmPowerMgmtSensorsTableHighWarningC = _PmPowerMgmtSensorsTableHighWarningC_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 51),
    _PmPowerMgmtSensorsTableHighWarningC_Type()
)
pmPowerMgmtSensorsTableHighWarningC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableHighWarningC.setStatus("current")
_PmPowerMgmtSensorsTableLowWarningC_Type = Integer32
_PmPowerMgmtSensorsTableLowWarningC_Object = MibTableColumn
pmPowerMgmtSensorsTableLowWarningC = _PmPowerMgmtSensorsTableLowWarningC_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 52),
    _PmPowerMgmtSensorsTableLowWarningC_Type()
)
pmPowerMgmtSensorsTableLowWarningC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableLowWarningC.setStatus("current")
_PmPowerMgmtSensorsTableLowCriticalC_Type = Integer32
_PmPowerMgmtSensorsTableLowCriticalC_Object = MibTableColumn
pmPowerMgmtSensorsTableLowCriticalC = _PmPowerMgmtSensorsTableLowCriticalC_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 53),
    _PmPowerMgmtSensorsTableLowCriticalC_Type()
)
pmPowerMgmtSensorsTableLowCriticalC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableLowCriticalC.setStatus("current")
_PmPowerMgmtSensorsTableHighCriticalF_Type = Integer32
_PmPowerMgmtSensorsTableHighCriticalF_Object = MibTableColumn
pmPowerMgmtSensorsTableHighCriticalF = _PmPowerMgmtSensorsTableHighCriticalF_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 60),
    _PmPowerMgmtSensorsTableHighCriticalF_Type()
)
pmPowerMgmtSensorsTableHighCriticalF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableHighCriticalF.setStatus("current")
_PmPowerMgmtSensorsTableHighWarningF_Type = Integer32
_PmPowerMgmtSensorsTableHighWarningF_Object = MibTableColumn
pmPowerMgmtSensorsTableHighWarningF = _PmPowerMgmtSensorsTableHighWarningF_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 61),
    _PmPowerMgmtSensorsTableHighWarningF_Type()
)
pmPowerMgmtSensorsTableHighWarningF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableHighWarningF.setStatus("current")
_PmPowerMgmtSensorsTableLowWarningF_Type = Integer32
_PmPowerMgmtSensorsTableLowWarningF_Object = MibTableColumn
pmPowerMgmtSensorsTableLowWarningF = _PmPowerMgmtSensorsTableLowWarningF_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 62),
    _PmPowerMgmtSensorsTableLowWarningF_Type()
)
pmPowerMgmtSensorsTableLowWarningF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableLowWarningF.setStatus("current")
_PmPowerMgmtSensorsTableLowCriticalF_Type = Integer32
_PmPowerMgmtSensorsTableLowCriticalF_Object = MibTableColumn
pmPowerMgmtSensorsTableLowCriticalF = _PmPowerMgmtSensorsTableLowCriticalF_Object(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 5, 13, 1, 63),
    _PmPowerMgmtSensorsTableLowCriticalF_Type()
)
pmPowerMgmtSensorsTableLowCriticalF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPowerMgmtSensorsTableLowCriticalF.setStatus("current")
_PmTrapObject_ObjectIdentity = ObjectIdentity
pmTrapObject = _PmTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 17, 2, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PM-MIB",
    **{"pm": pm,
       "pmProducts": pmProducts,
       "pm1024": pm1024,
       "pm2003": pm2003,
       "pm2006": pm2006,
       "pm2024": pm2024,
       "pm3003": pm3003,
       "pm3006": pm3006,
       "pm3024": pm3024,
       "pm1010": pm1010,
       "pm2010": pm2010,
       "pm3010": pm3010,
       "pm1020": pm1020,
       "pm2020": pm2020,
       "pm3020": pm3020,
       "pmManagement": pmManagement,
       "pmAppliance": pmAppliance,
       "pmHostName": pmHostName,
       "pmProductModel": pmProductModel,
       "pmPartNumber": pmPartNumber,
       "pmSerialNumber": pmSerialNumber,
       "pmEIDNumber": pmEIDNumber,
       "pmBootcodeVersion": pmBootcodeVersion,
       "pmFirmwareVersion": pmFirmwareVersion,
       "pmReboot": pmReboot,
       "pmSessions": pmSessions,
       "pmActiveSessionsNumberOfSession": pmActiveSessionsNumberOfSession,
       "pmActiveSessionsTable": pmActiveSessionsTable,
       "pmActiveSessionsTableEntry": pmActiveSessionsTableEntry,
       "pmActiveSessionsTableIndex": pmActiveSessionsTableIndex,
       "pmActiveSessionsTableUser": pmActiveSessionsTableUser,
       "pmActiveSessionsTableGroup": pmActiveSessionsTableGroup,
       "pmActiveSessionsTableType": pmActiveSessionsTableType,
       "pmActiveSessionsTableConnection": pmActiveSessionsTableConnection,
       "pmActiveSessionsTableSessionTime": pmActiveSessionsTableSessionTime,
       "pmActiveSessionsTableFrom": pmActiveSessionsTableFrom,
       "pmActiveSessionsTableKill": pmActiveSessionsTableKill,
       "pmPowerMgmt": pmPowerMgmt,
       "pmPowerMgmtNumSerialPorts": pmPowerMgmtNumSerialPorts,
       "pmPowerMgmtSerialTable": pmPowerMgmtSerialTable,
       "pmPowerMgmtSerialTableEntry": pmPowerMgmtSerialTableEntry,
       "pmPowerMgmtSerialTableIndex": pmPowerMgmtSerialTableIndex,
       "pmPowerMgmtSerialTablePortNumber": pmPowerMgmtSerialTablePortNumber,
       "pmPowerMgmtSerialTableDeviceName": pmPowerMgmtSerialTableDeviceName,
       "pmPowerMgmtSerialTableNumberPDUs": pmPowerMgmtSerialTableNumberPDUs,
       "pmPowerMgmtSerialTableBuzzer": pmPowerMgmtSerialTableBuzzer,
       "pmPowerMgmtSerialTableSyslog": pmPowerMgmtSerialTableSyslog,
       "pmPowerMgmtSerialTableOverCurrent": pmPowerMgmtSerialTableOverCurrent,
       "pmPowerMgmtSerialTableCycleInterval": pmPowerMgmtSerialTableCycleInterval,
       "pmPowerMgmtSerialTablePollRate": pmPowerMgmtSerialTablePollRate,
       "pmPowerMgmtSerialTablePassWord": pmPowerMgmtSerialTablePassWord,
       "pmPowerMgmtSerialTableSave": pmPowerMgmtSerialTableSave,
       "pmPowerMgmtSerialTableRestore": pmPowerMgmtSerialTableRestore,
       "pmPowerMgmtPDUTable": pmPowerMgmtPDUTable,
       "pmPowerMgmtPDUTableEntry": pmPowerMgmtPDUTableEntry,
       "pmPowerMgmtPDUTablePortNumber": pmPowerMgmtPDUTablePortNumber,
       "pmPowerMgmtPDUTablePduIndex": pmPowerMgmtPDUTablePduIndex,
       "pmPowerMgmtPDUTablePduId": pmPowerMgmtPDUTablePduId,
       "pmPowerMgmtPDUTablePortName": pmPowerMgmtPDUTablePortName,
       "pmPowerMgmtPDUTableModel": pmPowerMgmtPDUTableModel,
       "pmPowerMgmtPDUTableVendor": pmPowerMgmtPDUTableVendor,
       "pmPowerMgmtPDUTableFirmwareVersion": pmPowerMgmtPDUTableFirmwareVersion,
       "pmPowerMgmtPDUTableNumberOfOutlets": pmPowerMgmtPDUTableNumberOfOutlets,
       "pmPowerMgmtPDUTableCurrentNOS": pmPowerMgmtPDUTableCurrentNOS,
       "pmPowerMgmtPDUTableCurrent1Value": pmPowerMgmtPDUTableCurrent1Value,
       "pmPowerMgmtPDUTableCurrent1Max": pmPowerMgmtPDUTableCurrent1Max,
       "pmPowerMgmtPDUTableCurrent2Value": pmPowerMgmtPDUTableCurrent2Value,
       "pmPowerMgmtPDUTableCurrent2Max": pmPowerMgmtPDUTableCurrent2Max,
       "pmPowerMgmtPDUTableCurrent3Value": pmPowerMgmtPDUTableCurrent3Value,
       "pmPowerMgmtPDUTableCurrent3Max": pmPowerMgmtPDUTableCurrent3Max,
       "pmPowerMgmtPDUTableTemperatureNOS": pmPowerMgmtPDUTableTemperatureNOS,
       "pmPowerMgmtPDUTableTemperature1Value": pmPowerMgmtPDUTableTemperature1Value,
       "pmPowerMgmtPDUTableTemperature1Max": pmPowerMgmtPDUTableTemperature1Max,
       "pmPowerMgmtPDUTableTemperature2Value": pmPowerMgmtPDUTableTemperature2Value,
       "pmPowerMgmtPDUTableTemperature2Max": pmPowerMgmtPDUTableTemperature2Max,
       "pmPowerMgmtPDUTableTemperature3Value": pmPowerMgmtPDUTableTemperature3Value,
       "pmPowerMgmtPDUTableTemperature3Max": pmPowerMgmtPDUTableTemperature3Max,
       "pmPowerMgmtPDUTableHumidityNOS": pmPowerMgmtPDUTableHumidityNOS,
       "pmPowerMgmtPDUTableHumidity1Value": pmPowerMgmtPDUTableHumidity1Value,
       "pmPowerMgmtPDUTableHumidity1Max": pmPowerMgmtPDUTableHumidity1Max,
       "pmPowerMgmtPDUTableHumidity2Value": pmPowerMgmtPDUTableHumidity2Value,
       "pmPowerMgmtPDUTableHumidity2Max": pmPowerMgmtPDUTableHumidity2Max,
       "pmPowerMgmtPDUTableHumidity3Value": pmPowerMgmtPDUTableHumidity3Value,
       "pmPowerMgmtPDUTableHumidity3Max": pmPowerMgmtPDUTableHumidity3Max,
       "pmPowerMgmtPDUTableVoltageNOS": pmPowerMgmtPDUTableVoltageNOS,
       "pmPowerMgmtPDUTableVoltage1Value": pmPowerMgmtPDUTableVoltage1Value,
       "pmPowerMgmtPDUTableVoltage1Max": pmPowerMgmtPDUTableVoltage1Max,
       "pmPowerMgmtPDUTableVoltage2Value": pmPowerMgmtPDUTableVoltage2Value,
       "pmPowerMgmtPDUTableVoltage2Max": pmPowerMgmtPDUTableVoltage2Max,
       "pmPowerMgmtPDUTableVoltage3Value": pmPowerMgmtPDUTableVoltage3Value,
       "pmPowerMgmtPDUTableVoltage3Max": pmPowerMgmtPDUTableVoltage3Max,
       "pmPowerMgmtPDUTableNumberOfPhases": pmPowerMgmtPDUTableNumberOfPhases,
       "pmPowerMgmtPDUTableNumberOfBanks": pmPowerMgmtPDUTableNumberOfBanks,
       "pmPowerMgmtPDUTableNumberOfSensors": pmPowerMgmtPDUTableNumberOfSensors,
       "pmPowerMgmtPDUTableFactoryDefault": pmPowerMgmtPDUTableFactoryDefault,
       "pmPowerMgmtPDUTableColdStartDelay": pmPowerMgmtPDUTableColdStartDelay,
       "pmPowerMgmtPDUTableReboot": pmPowerMgmtPDUTableReboot,
       "pmPowerMgmtPDUTableMaxCurrent": pmPowerMgmtPDUTableMaxCurrent,
       "pmPowerMgmtPDUTableAlarm": pmPowerMgmtPDUTableAlarm,
       "pmPowerMgmtPDUTableCurrentValue": pmPowerMgmtPDUTableCurrentValue,
       "pmPowerMgmtPDUTableCurrentMax": pmPowerMgmtPDUTableCurrentMax,
       "pmPowerMgmtPDUTableCurrentMin": pmPowerMgmtPDUTableCurrentMin,
       "pmPowerMgmtPDUTableCurrentAvg": pmPowerMgmtPDUTableCurrentAvg,
       "pmPowerMgmtPDUTableCurrentReset": pmPowerMgmtPDUTableCurrentReset,
       "pmPowerMgmtPDUTablePowerValue": pmPowerMgmtPDUTablePowerValue,
       "pmPowerMgmtPDUTablePowerMax": pmPowerMgmtPDUTablePowerMax,
       "pmPowerMgmtPDUTablePowerMin": pmPowerMgmtPDUTablePowerMin,
       "pmPowerMgmtPDUTablePowerAvg": pmPowerMgmtPDUTablePowerAvg,
       "pmPowerMgmtPDUTablePowerReset": pmPowerMgmtPDUTablePowerReset,
       "pmPowerMgmtPDUTablePowerType": pmPowerMgmtPDUTablePowerType,
       "pmPowerMgmtPDUTableVoltageValue": pmPowerMgmtPDUTableVoltageValue,
       "pmPowerMgmtPDUTableVoltageMax": pmPowerMgmtPDUTableVoltageMax,
       "pmPowerMgmtPDUTableVoltageMin": pmPowerMgmtPDUTableVoltageMin,
       "pmPowerMgmtPDUTableVoltageAvg": pmPowerMgmtPDUTableVoltageAvg,
       "pmPowerMgmtPDUTableVoltageReset": pmPowerMgmtPDUTableVoltageReset,
       "pmPowerMgmtPDUTableVoltageType": pmPowerMgmtPDUTableVoltageType,
       "pmPowerMgmtPDUTablePowerFactorValue": pmPowerMgmtPDUTablePowerFactorValue,
       "pmPowerMgmtPDUTablePowerFactorMax": pmPowerMgmtPDUTablePowerFactorMax,
       "pmPowerMgmtPDUTablePowerFactorMin": pmPowerMgmtPDUTablePowerFactorMin,
       "pmPowerMgmtPDUTablePowerFactorAvg": pmPowerMgmtPDUTablePowerFactorAvg,
       "pmPowerMgmtPDUTablePowerFactorReset": pmPowerMgmtPDUTablePowerFactorReset,
       "pmPowerMgmtPDUTablePowerFactorType": pmPowerMgmtPDUTablePowerFactorType,
       "pmPowerMgmtPDUTablePowerControl": pmPowerMgmtPDUTablePowerControl,
       "pmPowerMgmtPDUTableResetOCP": pmPowerMgmtPDUTableResetOCP,
       "pmPowerMgmtPDUTableCurrentHighCritical": pmPowerMgmtPDUTableCurrentHighCritical,
       "pmPowerMgmtPDUTableCurrentHighWarning": pmPowerMgmtPDUTableCurrentHighWarning,
       "pmPowerMgmtPDUTableCurrentLowWarning": pmPowerMgmtPDUTableCurrentLowWarning,
       "pmPowerMgmtPDUTableCurrentLowCritical": pmPowerMgmtPDUTableCurrentLowCritical,
       "pmPowerMgmtPDUTableEnergyValue": pmPowerMgmtPDUTableEnergyValue,
       "pmPowerMgmtPDUTableEnergyStartTime": pmPowerMgmtPDUTableEnergyStartTime,
       "pmPowerMgmtPDUTableEnergyReset": pmPowerMgmtPDUTableEnergyReset,
       "pmPowerMgmtTotalNumberOfOutlets": pmPowerMgmtTotalNumberOfOutlets,
       "pmPowerMgmtOutletsTable": pmPowerMgmtOutletsTable,
       "pmPowerMgmtOutletsTableEntry": pmPowerMgmtOutletsTableEntry,
       "pmPowerMgmtOutletsTablePortNumber": pmPowerMgmtOutletsTablePortNumber,
       "pmPowerMgmtOutletsTablePduNumber": pmPowerMgmtOutletsTablePduNumber,
       "pmPowerMgmtOutletsTableNumber": pmPowerMgmtOutletsTableNumber,
       "pmPowerMgmtOutletsTableName": pmPowerMgmtOutletsTableName,
       "pmPowerMgmtOutletsTableStatus": pmPowerMgmtOutletsTableStatus,
       "pmPowerMgmtOutletsTablePowerControl": pmPowerMgmtOutletsTablePowerControl,
       "pmPowerMgmtOutletsTablePortName": pmPowerMgmtOutletsTablePortName,
       "pmPowerMgmtOutletsTablePduId": pmPowerMgmtOutletsTablePduId,
       "pmPowerMgmtOutletsTablePostOnDelay": pmPowerMgmtOutletsTablePostOnDelay,
       "pmPowerMgmtOutletsTablePostOffDelay": pmPowerMgmtOutletsTablePostOffDelay,
       "pmPowerMgmtOutletsTableAlarm": pmPowerMgmtOutletsTableAlarm,
       "pmPowerMgmtOutletsTableCurrentValue": pmPowerMgmtOutletsTableCurrentValue,
       "pmPowerMgmtOutletsTableCurrentMax": pmPowerMgmtOutletsTableCurrentMax,
       "pmPowerMgmtOutletsTableCurrentMin": pmPowerMgmtOutletsTableCurrentMin,
       "pmPowerMgmtOutletsTableCurrentAvg": pmPowerMgmtOutletsTableCurrentAvg,
       "pmPowerMgmtOutletsTableCurrentReset": pmPowerMgmtOutletsTableCurrentReset,
       "pmPowerMgmtOutletsTablePowerValue": pmPowerMgmtOutletsTablePowerValue,
       "pmPowerMgmtOutletsTablePowerMax": pmPowerMgmtOutletsTablePowerMax,
       "pmPowerMgmtOutletsTablePowerMin": pmPowerMgmtOutletsTablePowerMin,
       "pmPowerMgmtOutletsTablePowerAvg": pmPowerMgmtOutletsTablePowerAvg,
       "pmPowerMgmtOutletsTablePowerReset": pmPowerMgmtOutletsTablePowerReset,
       "pmPowerMgmtOutletsTablePowerType": pmPowerMgmtOutletsTablePowerType,
       "pmPowerMgmtOutletsTableVoltageValue": pmPowerMgmtOutletsTableVoltageValue,
       "pmPowerMgmtOutletsTableVoltageMax": pmPowerMgmtOutletsTableVoltageMax,
       "pmPowerMgmtOutletsTableVoltageMin": pmPowerMgmtOutletsTableVoltageMin,
       "pmPowerMgmtOutletsTableVoltageAvg": pmPowerMgmtOutletsTableVoltageAvg,
       "pmPowerMgmtOutletsTableVoltageReset": pmPowerMgmtOutletsTableVoltageReset,
       "pmPowerMgmtOutletsTableVoltageType": pmPowerMgmtOutletsTableVoltageType,
       "pmPowerMgmtOutletsTablePowerFactorValue": pmPowerMgmtOutletsTablePowerFactorValue,
       "pmPowerMgmtOutletsTablePowerFactorMax": pmPowerMgmtOutletsTablePowerFactorMax,
       "pmPowerMgmtOutletsTablePowerFactorMin": pmPowerMgmtOutletsTablePowerFactorMin,
       "pmPowerMgmtOutletsTablePowerFactorAvg": pmPowerMgmtOutletsTablePowerFactorAvg,
       "pmPowerMgmtOutletsTablePowerFactorReset": pmPowerMgmtOutletsTablePowerFactorReset,
       "pmPowerMgmtOutletsTablePowerFactorType": pmPowerMgmtOutletsTablePowerFactorType,
       "pmPowerMgmtOutletsTableCurrentHighCritical": pmPowerMgmtOutletsTableCurrentHighCritical,
       "pmPowerMgmtOutletsTableCurrentHighWarning": pmPowerMgmtOutletsTableCurrentHighWarning,
       "pmPowerMgmtOutletsTableCurrentLowWarning": pmPowerMgmtOutletsTableCurrentLowWarning,
       "pmPowerMgmtOutletsTableCurrentLowCritical": pmPowerMgmtOutletsTableCurrentLowCritical,
       "pmPowerMgmtOutletsTableEnergyValue": pmPowerMgmtOutletsTableEnergyValue,
       "pmPowerMgmtOutletsTableEnergyStartTime": pmPowerMgmtOutletsTableEnergyStartTime,
       "pmPowerMgmtOutletsTableEnergyReset": pmPowerMgmtOutletsTableEnergyReset,
       "pmPowerMgmtNumberOfOutletGroup": pmPowerMgmtNumberOfOutletGroup,
       "pmPowerMgmtGroupTable": pmPowerMgmtGroupTable,
       "pmPowerMgmtGroupTableEntry": pmPowerMgmtGroupTableEntry,
       "pmPowerMgmtGroupTableIndex": pmPowerMgmtGroupTableIndex,
       "pmPowerMgmtGroupTableName": pmPowerMgmtGroupTableName,
       "pmPowerMgmtGroupTableStatus": pmPowerMgmtGroupTableStatus,
       "pmPowerMgmtGroupTablePowerControl": pmPowerMgmtGroupTablePowerControl,
       "pmPowerMgmtTotalNumberOfPhases": pmPowerMgmtTotalNumberOfPhases,
       "pmPowerMgmtPhasesTable": pmPowerMgmtPhasesTable,
       "pmPowerMgmtPhasesTableEntry": pmPowerMgmtPhasesTableEntry,
       "pmPowerMgmtPhasesTablePortNumber": pmPowerMgmtPhasesTablePortNumber,
       "pmPowerMgmtPhasesTablePduNumber": pmPowerMgmtPhasesTablePduNumber,
       "pmPowerMgmtPhasesTableNumber": pmPowerMgmtPhasesTableNumber,
       "pmPowerMgmtPhasesTableName": pmPowerMgmtPhasesTableName,
       "pmPowerMgmtPhasesTablePortName": pmPowerMgmtPhasesTablePortName,
       "pmPowerMgmtPhasesTablePduId": pmPowerMgmtPhasesTablePduId,
       "pmPowerMgmtPhasesTableAlarm": pmPowerMgmtPhasesTableAlarm,
       "pmPowerMgmtPhasesTableCurrentValue": pmPowerMgmtPhasesTableCurrentValue,
       "pmPowerMgmtPhasesTableCurrentMax": pmPowerMgmtPhasesTableCurrentMax,
       "pmPowerMgmtPhasesTableCurrentMin": pmPowerMgmtPhasesTableCurrentMin,
       "pmPowerMgmtPhasesTableCurrentAvg": pmPowerMgmtPhasesTableCurrentAvg,
       "pmPowerMgmtPhasesTableCurrentReset": pmPowerMgmtPhasesTableCurrentReset,
       "pmPowerMgmtPhasesTablePowerValue": pmPowerMgmtPhasesTablePowerValue,
       "pmPowerMgmtPhasesTablePowerMax": pmPowerMgmtPhasesTablePowerMax,
       "pmPowerMgmtPhasesTablePowerMin": pmPowerMgmtPhasesTablePowerMin,
       "pmPowerMgmtPhasesTablePowerAvg": pmPowerMgmtPhasesTablePowerAvg,
       "pmPowerMgmtPhasesTablePowerReset": pmPowerMgmtPhasesTablePowerReset,
       "pmPowerMgmtPhasesTablePowerType": pmPowerMgmtPhasesTablePowerType,
       "pmPowerMgmtPhasesTableVoltageValue": pmPowerMgmtPhasesTableVoltageValue,
       "pmPowerMgmtPhasesTableVoltageMax": pmPowerMgmtPhasesTableVoltageMax,
       "pmPowerMgmtPhasesTableVoltageMin": pmPowerMgmtPhasesTableVoltageMin,
       "pmPowerMgmtPhasesTableVoltageAvg": pmPowerMgmtPhasesTableVoltageAvg,
       "pmPowerMgmtPhasesTableVoltageReset": pmPowerMgmtPhasesTableVoltageReset,
       "pmPowerMgmtPhasesTableVoltageType": pmPowerMgmtPhasesTableVoltageType,
       "pmPowerMgmtPhasesTablePowerFactorValue": pmPowerMgmtPhasesTablePowerFactorValue,
       "pmPowerMgmtPhasesTablePowerFactorMax": pmPowerMgmtPhasesTablePowerFactorMax,
       "pmPowerMgmtPhasesTablePowerFactorMin": pmPowerMgmtPhasesTablePowerFactorMin,
       "pmPowerMgmtPhasesTablePowerFactorAvg": pmPowerMgmtPhasesTablePowerFactorAvg,
       "pmPowerMgmtPhasesTablePowerFactorReset": pmPowerMgmtPhasesTablePowerFactorReset,
       "pmPowerMgmtPhasesTablePowerFactorType": pmPowerMgmtPhasesTablePowerFactorType,
       "pmPowerMgmtPhasesTableCurrentHighCritical": pmPowerMgmtPhasesTableCurrentHighCritical,
       "pmPowerMgmtPhasesTableCurrentHighWarning": pmPowerMgmtPhasesTableCurrentHighWarning,
       "pmPowerMgmtPhasesTableCurrentLowWarning": pmPowerMgmtPhasesTableCurrentLowWarning,
       "pmPowerMgmtPhasesTableCurrentLowCritical": pmPowerMgmtPhasesTableCurrentLowCritical,
       "pmPowerMgmtTotalNumberOfBanks": pmPowerMgmtTotalNumberOfBanks,
       "pmPowerMgmtBanksTable": pmPowerMgmtBanksTable,
       "pmPowerMgmtBanksTableEntry": pmPowerMgmtBanksTableEntry,
       "pmPowerMgmtBanksTablePortNumber": pmPowerMgmtBanksTablePortNumber,
       "pmPowerMgmtBanksTablePduNumber": pmPowerMgmtBanksTablePduNumber,
       "pmPowerMgmtBanksTableNumber": pmPowerMgmtBanksTableNumber,
       "pmPowerMgmtBanksTableName": pmPowerMgmtBanksTableName,
       "pmPowerMgmtBanksTablePortName": pmPowerMgmtBanksTablePortName,
       "pmPowerMgmtBanksTablePduId": pmPowerMgmtBanksTablePduId,
       "pmPowerMgmtBanksTableAlarm": pmPowerMgmtBanksTableAlarm,
       "pmPowerMgmtBanksTableCurrentValue": pmPowerMgmtBanksTableCurrentValue,
       "pmPowerMgmtBanksTableCurrentMax": pmPowerMgmtBanksTableCurrentMax,
       "pmPowerMgmtBanksTableCurrentMin": pmPowerMgmtBanksTableCurrentMin,
       "pmPowerMgmtBanksTableCurrentAvg": pmPowerMgmtBanksTableCurrentAvg,
       "pmPowerMgmtBanksTableCurrentReset": pmPowerMgmtBanksTableCurrentReset,
       "pmPowerMgmtBanksTablePowerValue": pmPowerMgmtBanksTablePowerValue,
       "pmPowerMgmtBanksTablePowerMax": pmPowerMgmtBanksTablePowerMax,
       "pmPowerMgmtBanksTablePowerMin": pmPowerMgmtBanksTablePowerMin,
       "pmPowerMgmtBanksTablePowerAvg": pmPowerMgmtBanksTablePowerAvg,
       "pmPowerMgmtBanksTablePowerReset": pmPowerMgmtBanksTablePowerReset,
       "pmPowerMgmtBanksTablePowerType": pmPowerMgmtBanksTablePowerType,
       "pmPowerMgmtBanksTableVoltageValue": pmPowerMgmtBanksTableVoltageValue,
       "pmPowerMgmtBanksTableVoltageMax": pmPowerMgmtBanksTableVoltageMax,
       "pmPowerMgmtBanksTableVoltageMin": pmPowerMgmtBanksTableVoltageMin,
       "pmPowerMgmtBanksTableVoltageAvg": pmPowerMgmtBanksTableVoltageAvg,
       "pmPowerMgmtBanksTableVoltageReset": pmPowerMgmtBanksTableVoltageReset,
       "pmPowerMgmtBanksTableVoltageType": pmPowerMgmtBanksTableVoltageType,
       "pmPowerMgmtBanksTablePowerFactorValue": pmPowerMgmtBanksTablePowerFactorValue,
       "pmPowerMgmtBanksTablePowerFactorMax": pmPowerMgmtBanksTablePowerFactorMax,
       "pmPowerMgmtBanksTablePowerFactorMin": pmPowerMgmtBanksTablePowerFactorMin,
       "pmPowerMgmtBanksTablePowerFactorAvg": pmPowerMgmtBanksTablePowerFactorAvg,
       "pmPowerMgmtBanksTablePowerFactorReset": pmPowerMgmtBanksTablePowerFactorReset,
       "pmPowerMgmtBanksTablePowerFactorType": pmPowerMgmtBanksTablePowerFactorType,
       "pmPowerMgmtBanksTableCurrentHighCritical": pmPowerMgmtBanksTableCurrentHighCritical,
       "pmPowerMgmtBanksTableCurrentHighWarning": pmPowerMgmtBanksTableCurrentHighWarning,
       "pmPowerMgmtBanksTableCurrentLowWarning": pmPowerMgmtBanksTableCurrentLowWarning,
       "pmPowerMgmtBanksTableCurrentLowCritical": pmPowerMgmtBanksTableCurrentLowCritical,
       "pmPowerMgmtBanksTableEnergyValue": pmPowerMgmtBanksTableEnergyValue,
       "pmPowerMgmtBanksTableEnergyStartTime": pmPowerMgmtBanksTableEnergyStartTime,
       "pmPowerMgmtBanksTableEnergyReset": pmPowerMgmtBanksTableEnergyReset,
       "pmPowerMgmtTotalNumberOfSensors": pmPowerMgmtTotalNumberOfSensors,
       "pmPowerMgmtSensorsTable": pmPowerMgmtSensorsTable,
       "pmPowerMgmtSensorsTableEntry": pmPowerMgmtSensorsTableEntry,
       "pmPowerMgmtSensorsTablePortNumber": pmPowerMgmtSensorsTablePortNumber,
       "pmPowerMgmtSensorsTablePduNumber": pmPowerMgmtSensorsTablePduNumber,
       "pmPowerMgmtSensorsTableNumber": pmPowerMgmtSensorsTableNumber,
       "pmPowerMgmtSensorsTableName": pmPowerMgmtSensorsTableName,
       "pmPowerMgmtSensorsTablePortName": pmPowerMgmtSensorsTablePortName,
       "pmPowerMgmtSensorsTablePduId": pmPowerMgmtSensorsTablePduId,
       "pmPowerMgmtSensorsTableType": pmPowerMgmtSensorsTableType,
       "pmPowerMgmtSensorsTableStatus": pmPowerMgmtSensorsTableStatus,
       "pmPowerMgmtSensorsTableValue": pmPowerMgmtSensorsTableValue,
       "pmPowerMgmtSensorsTableValueMax": pmPowerMgmtSensorsTableValueMax,
       "pmPowerMgmtSensorsTableValueMin": pmPowerMgmtSensorsTableValueMin,
       "pmPowerMgmtSensorsTableValueAvg": pmPowerMgmtSensorsTableValueAvg,
       "pmPowerMgmtSensorsTableValueInt": pmPowerMgmtSensorsTableValueInt,
       "pmPowerMgmtSensorsTableValueMaxInt": pmPowerMgmtSensorsTableValueMaxInt,
       "pmPowerMgmtSensorsTableValueMinInt": pmPowerMgmtSensorsTableValueMinInt,
       "pmPowerMgmtSensorsTableValueAvgInt": pmPowerMgmtSensorsTableValueAvgInt,
       "pmPowerMgmtSensorsTableValueReset": pmPowerMgmtSensorsTableValueReset,
       "pmPowerMgmtSensorsTableHighCritical": pmPowerMgmtSensorsTableHighCritical,
       "pmPowerMgmtSensorsTableHighWarning": pmPowerMgmtSensorsTableHighWarning,
       "pmPowerMgmtSensorsTableLowWarning": pmPowerMgmtSensorsTableLowWarning,
       "pmPowerMgmtSensorsTableLowCritical": pmPowerMgmtSensorsTableLowCritical,
       "pmPowerMgmtSensorsTableUnit": pmPowerMgmtSensorsTableUnit,
       "pmPowerMgmtSensorsTableHighCriticalC": pmPowerMgmtSensorsTableHighCriticalC,
       "pmPowerMgmtSensorsTableHighWarningC": pmPowerMgmtSensorsTableHighWarningC,
       "pmPowerMgmtSensorsTableLowWarningC": pmPowerMgmtSensorsTableLowWarningC,
       "pmPowerMgmtSensorsTableLowCriticalC": pmPowerMgmtSensorsTableLowCriticalC,
       "pmPowerMgmtSensorsTableHighCriticalF": pmPowerMgmtSensorsTableHighCriticalF,
       "pmPowerMgmtSensorsTableHighWarningF": pmPowerMgmtSensorsTableHighWarningF,
       "pmPowerMgmtSensorsTableLowWarningF": pmPowerMgmtSensorsTableLowWarningF,
       "pmPowerMgmtSensorsTableLowCriticalF": pmPowerMgmtSensorsTableLowCriticalF,
       "pmTrapObject": pmTrapObject}
)
