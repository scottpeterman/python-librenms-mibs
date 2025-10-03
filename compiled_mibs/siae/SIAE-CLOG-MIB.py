# SNMP MIB module (SIAE-CLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-CLOG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:47 2025
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

(alarmTrap,) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "alarmTrap")

(equipIpSnmpAgentAddress,) = mibBuilder.importSymbols(
    "SIAE-EQUIP-MIB",
    "equipIpSnmpAgentAddress")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

(accessControlLoginIpAddress,) = mibBuilder.importSymbols(
    "SIAE-USER-MIB",
    "accessControlLoginIpAddress")

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

commandLog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40)
)
if mibBuilder.loadTexts:
    commandLog.setRevisions(
        ("2015-03-23 00:00",
         "2014-06-23 00:00",
         "2014-02-03 00:00",
         "2013-12-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CommandLogMibVersion_Type = Integer32
_CommandLogMibVersion_Object = MibScalar
commandLogMibVersion = _CommandLogMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40, 1),
    _CommandLogMibVersion_Type()
)
commandLogMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandLogMibVersion.setStatus("current")


class _CommandLogActionRequest_Type(Integer32):
    """Custom type commandLogActionRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("delete", 1),
          ("read", 2))
    )


_CommandLogActionRequest_Type.__name__ = "Integer32"
_CommandLogActionRequest_Object = MibScalar
commandLogActionRequest = _CommandLogActionRequest_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40, 2),
    _CommandLogActionRequest_Type()
)
commandLogActionRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandLogActionRequest.setStatus("current")


class _CommandLogFtpFile_Type(DisplayString):
    """Custom type commandLogFtpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommandLogFtpFile_Type.__name__ = "DisplayString"
_CommandLogFtpFile_Object = MibScalar
commandLogFtpFile = _CommandLogFtpFile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40, 3),
    _CommandLogFtpFile_Type()
)
commandLogFtpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandLogFtpFile.setStatus("current")


class _CommandLogMgmtInterfaceFilter_Type(Bits):
    """Custom type commandLogMgmtInterfaceFilter based on Bits"""
    namedValues = NamedValues(
        *(("cli", 0),
          ("web", 1),
          ("snmp", 2),
          ("remoteCli", 3))
    )

_CommandLogMgmtInterfaceFilter_Type.__name__ = "Bits"
_CommandLogMgmtInterfaceFilter_Object = MibScalar
commandLogMgmtInterfaceFilter = _CommandLogMgmtInterfaceFilter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40, 4),
    _CommandLogMgmtInterfaceFilter_Type()
)
commandLogMgmtInterfaceFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandLogMgmtInterfaceFilter.setStatus("current")
_CommandLogStartTimeFilter_Type = Unsigned32
_CommandLogStartTimeFilter_Object = MibScalar
commandLogStartTimeFilter = _CommandLogStartTimeFilter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40, 5),
    _CommandLogStartTimeFilter_Type()
)
commandLogStartTimeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandLogStartTimeFilter.setStatus("current")
_CommandLogEndTimeFilter_Type = Unsigned32
_CommandLogEndTimeFilter_Object = MibScalar
commandLogEndTimeFilter = _CommandLogEndTimeFilter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40, 6),
    _CommandLogEndTimeFilter_Type()
)
commandLogEndTimeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandLogEndTimeFilter.setStatus("current")


class _CommandLogUserNameFilter_Type(DisplayString):
    """Custom type commandLogUserNameFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CommandLogUserNameFilter_Type.__name__ = "DisplayString"
_CommandLogUserNameFilter_Object = MibScalar
commandLogUserNameFilter = _CommandLogUserNameFilter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40, 7),
    _CommandLogUserNameFilter_Type()
)
commandLogUserNameFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandLogUserNameFilter.setStatus("current")


class _CommandLogSourceAddressFilter_Type(DisplayString):
    """Custom type commandLogSourceAddressFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CommandLogSourceAddressFilter_Type.__name__ = "DisplayString"
_CommandLogSourceAddressFilter_Object = MibScalar
commandLogSourceAddressFilter = _CommandLogSourceAddressFilter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40, 8),
    _CommandLogSourceAddressFilter_Type()
)
commandLogSourceAddressFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandLogSourceAddressFilter.setStatus("current")


class _CommandLogFtpStatus_Type(Integer32):
    """Custom type commandLogFtpStatus based on Integer32"""
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
        *(("transferring", 1),
          ("completed", 2),
          ("interrupted", 3),
          ("empty", 4))
    )


_CommandLogFtpStatus_Type.__name__ = "Integer32"
_CommandLogFtpStatus_Object = MibScalar
commandLogFtpStatus = _CommandLogFtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40, 9),
    _CommandLogFtpStatus_Type()
)
commandLogFtpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandLogFtpStatus.setStatus("current")


class _CommandLogFtpStatusTrapNotification_Type(Integer32):
    """Custom type commandLogFtpStatusTrapNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 1),
          ("trapEnable", 2),
          ("trapEnableWithACK", 3))
    )


_CommandLogFtpStatusTrapNotification_Type.__name__ = "Integer32"
_CommandLogFtpStatusTrapNotification_Object = MibScalar
commandLogFtpStatusTrapNotification = _CommandLogFtpStatusTrapNotification_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40, 10),
    _CommandLogFtpStatusTrapNotification_Type()
)
commandLogFtpStatusTrapNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandLogFtpStatusTrapNotification.setStatus("current")
_CommandLogLastCommandTime_Type = Unsigned32
_CommandLogLastCommandTime_Object = MibScalar
commandLogLastCommandTime = _CommandLogLastCommandTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40, 11),
    _CommandLogLastCommandTime_Type()
)
commandLogLastCommandTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandLogLastCommandTime.setStatus("current")


class _CommandLogLastCommandUser_Type(DisplayString):
    """Custom type commandLogLastCommandUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CommandLogLastCommandUser_Type.__name__ = "DisplayString"
_CommandLogLastCommandUser_Object = MibScalar
commandLogLastCommandUser = _CommandLogLastCommandUser_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 40, 12),
    _CommandLogLastCommandUser_Type()
)
commandLogLastCommandUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandLogLastCommandUser.setStatus("current")

# Managed Objects groups


# Notification objects

commandLogFtpStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 4001)
)
commandLogFtpStatusTrap.setObjects(
      *(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-CLOG-MIB", "commandLogFtpStatus"),
        ("SIAE-USER-MIB", "accessControlLoginIpAddress"))
)
if mibBuilder.loadTexts:
    commandLogFtpStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-CLOG-MIB",
    **{"commandLogFtpStatusTrap": commandLogFtpStatusTrap,
       "commandLog": commandLog,
       "commandLogMibVersion": commandLogMibVersion,
       "commandLogActionRequest": commandLogActionRequest,
       "commandLogFtpFile": commandLogFtpFile,
       "commandLogMgmtInterfaceFilter": commandLogMgmtInterfaceFilter,
       "commandLogStartTimeFilter": commandLogStartTimeFilter,
       "commandLogEndTimeFilter": commandLogEndTimeFilter,
       "commandLogUserNameFilter": commandLogUserNameFilter,
       "commandLogSourceAddressFilter": commandLogSourceAddressFilter,
       "commandLogFtpStatus": commandLogFtpStatus,
       "commandLogFtpStatusTrapNotification": commandLogFtpStatusTrapNotification,
       "commandLogLastCommandTime": commandLogLastCommandTime,
       "commandLogLastCommandUser": commandLogLastCommandUser}
)
