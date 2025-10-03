# SNMP MIB module (LAMBDATRAIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\deltanet\LAMBDATRAIL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:23 2025
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
 iso,
 private) = mibBuilder.importSymbols(
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
    "iso",
    "private")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Deltanet_ObjectIdentity = ObjectIdentity
deltanet = _Deltanet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616)
)
_SnmpAgent_ObjectIdentity = ObjectIdentity
snmpAgent = _SnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 1)
)
_AgentSw_ObjectIdentity = ObjectIdentity
agentSw = _AgentSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 1, 1)
)
_AgentSoftwareMajorVer_Type = Integer32
_AgentSoftwareMajorVer_Object = MibScalar
agentSoftwareMajorVer = _AgentSoftwareMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 1, 1),
    _AgentSoftwareMajorVer_Type()
)
agentSoftwareMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSoftwareMajorVer.setStatus("mandatory")
_AgentSoftwareMinorVer_Type = Integer32
_AgentSoftwareMinorVer_Object = MibScalar
agentSoftwareMinorVer = _AgentSoftwareMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 1, 2),
    _AgentSoftwareMinorVer_Type()
)
agentSoftwareMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSoftwareMinorVer.setStatus("mandatory")


class _AgentOutBandBaudRate_Type(Integer32):
    """Custom type agentOutBandBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9600,
              19200,
              38400,
              57600,
              115200)
        )
    )
    namedValues = NamedValues(
        *(("b9600", 9600),
          ("b19200", 19200),
          ("b38400", 38400),
          ("b57600", 57600),
          ("b115200", 115200))
    )


_AgentOutBandBaudRate_Type.__name__ = "Integer32"
_AgentOutBandBaudRate_Object = MibScalar
agentOutBandBaudRate = _AgentOutBandBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 2),
    _AgentOutBandBaudRate_Type()
)
agentOutBandBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutBandBaudRate.setStatus("mandatory")
_AgentConsoleIdleTimeouts_Type = Integer32
_AgentConsoleIdleTimeouts_Object = MibScalar
agentConsoleIdleTimeouts = _AgentConsoleIdleTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 3),
    _AgentConsoleIdleTimeouts_Type()
)
agentConsoleIdleTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConsoleIdleTimeouts.setStatus("mandatory")


class _AgentPrompt_Type(DisplayString):
    """Custom type agentPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AgentPrompt_Type.__name__ = "DisplayString"
_AgentPrompt_Object = MibScalar
agentPrompt = _AgentPrompt_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 4),
    _AgentPrompt_Type()
)
agentPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPrompt.setStatus("mandatory")


class _AgentBootMethod_Type(Integer32):
    """Custom type agentBootMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("dhcp", 2))
    )


_AgentBootMethod_Type.__name__ = "Integer32"
_AgentBootMethod_Object = MibScalar
agentBootMethod = _AgentBootMethod_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 5),
    _AgentBootMethod_Type()
)
agentBootMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootMethod.setStatus("mandatory")
_AgentIpAddr_Type = IpAddress
_AgentIpAddr_Object = MibScalar
agentIpAddr = _AgentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 6),
    _AgentIpAddr_Type()
)
agentIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpAddr.setStatus("mandatory")
_AgentIpNetMask_Type = IpAddress
_AgentIpNetMask_Object = MibScalar
agentIpNetMask = _AgentIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 7),
    _AgentIpNetMask_Type()
)
agentIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpNetMask.setStatus("mandatory")
_AgentDefaultGateway_Type = IpAddress
_AgentDefaultGateway_Object = MibScalar
agentDefaultGateway = _AgentDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 8),
    _AgentDefaultGateway_Type()
)
agentDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDefaultGateway.setStatus("mandatory")
_AgentPrimaryDnsServer_Type = IpAddress
_AgentPrimaryDnsServer_Object = MibScalar
agentPrimaryDnsServer = _AgentPrimaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 9),
    _AgentPrimaryDnsServer_Type()
)
agentPrimaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPrimaryDnsServer.setStatus("mandatory")
_AgentSecondaryDnsServer_Type = IpAddress
_AgentSecondaryDnsServer_Object = MibScalar
agentSecondaryDnsServer = _AgentSecondaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 10),
    _AgentSecondaryDnsServer_Type()
)
agentSecondaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSecondaryDnsServer.setStatus("mandatory")


class _AgentSnmpServer_Type(Integer32):
    """Custom type agentSnmpServer based on Integer32"""
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


_AgentSnmpServer_Type.__name__ = "Integer32"
_AgentSnmpServer_Object = MibScalar
agentSnmpServer = _AgentSnmpServer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 11),
    _AgentSnmpServer_Type()
)
agentSnmpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpServer.setStatus("mandatory")


class _AgentHttpServer_Type(Integer32):
    """Custom type agentHttpServer based on Integer32"""
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


_AgentHttpServer_Type.__name__ = "Integer32"
_AgentHttpServer_Object = MibScalar
agentHttpServer = _AgentHttpServer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 12),
    _AgentHttpServer_Type()
)
agentHttpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentHttpServer.setStatus("mandatory")
_AgentTelnet_ObjectIdentity = ObjectIdentity
agentTelnet = _AgentTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 1, 13)
)


class _AgentTelnetServer_Type(Integer32):
    """Custom type agentTelnetServer based on Integer32"""
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


_AgentTelnetServer_Type.__name__ = "Integer32"
_AgentTelnetServer_Object = MibScalar
agentTelnetServer = _AgentTelnetServer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 13, 1),
    _AgentTelnetServer_Type()
)
agentTelnetServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetServer.setStatus("mandatory")
_AgentTelnetIdleTimeouts_Type = Integer32
_AgentTelnetIdleTimeouts_Object = MibScalar
agentTelnetIdleTimeouts = _AgentTelnetIdleTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 13, 2),
    _AgentTelnetIdleTimeouts_Type()
)
agentTelnetIdleTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetIdleTimeouts.setStatus("mandatory")


class _AgentTelnetMaxSessions_Type(Integer32):
    """Custom type agentTelnetMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AgentTelnetMaxSessions_Type.__name__ = "Integer32"
_AgentTelnetMaxSessions_Object = MibScalar
agentTelnetMaxSessions = _AgentTelnetMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 13, 3),
    _AgentTelnetMaxSessions_Type()
)
agentTelnetMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetMaxSessions.setStatus("mandatory")


class _AgentFtpServer_Type(Integer32):
    """Custom type agentFtpServer based on Integer32"""
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


_AgentFtpServer_Type.__name__ = "Integer32"
_AgentFtpServer_Object = MibScalar
agentFtpServer = _AgentFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 14),
    _AgentFtpServer_Type()
)
agentFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFtpServer.setStatus("mandatory")


class _AgentTftpServer_Type(Integer32):
    """Custom type agentTftpServer based on Integer32"""
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


_AgentTftpServer_Type.__name__ = "Integer32"
_AgentTftpServer_Object = MibScalar
agentTftpServer = _AgentTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 15),
    _AgentTftpServer_Type()
)
agentTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTftpServer.setStatus("mandatory")


class _AgentSendTrap_Type(Integer32):
    """Custom type agentSendTrap based on Integer32"""
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


_AgentSendTrap_Type.__name__ = "Integer32"
_AgentSendTrap_Object = MibScalar
agentSendTrap = _AgentSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 16),
    _AgentSendTrap_Type()
)
agentSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSendTrap.setStatus("mandatory")
_AgentTrapTargetTable_Object = MibTable
agentTrapTargetTable = _AgentTrapTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 17)
)
if mibBuilder.loadTexts:
    agentTrapTargetTable.setStatus("mandatory")
_AgentTrapTargetEntry_Object = MibTableRow
agentTrapTargetEntry = _AgentTrapTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 17, 1)
)
agentTrapTargetEntry.setIndexNames(
    (0, "LAMBDATRAIL-MIB", "agentTrapIndex"),
)
if mibBuilder.loadTexts:
    agentTrapTargetEntry.setStatus("mandatory")
_AgentTrapIndex_Type = Integer32
_AgentTrapIndex_Object = MibTableColumn
agentTrapIndex = _AgentTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 17, 1, 1),
    _AgentTrapIndex_Type()
)
agentTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapIndex.setStatus("mandatory")
_AgentTrapTargetIpAddr_Type = IpAddress
_AgentTrapTargetIpAddr_Object = MibTableColumn
agentTrapTargetIpAddr = _AgentTrapTargetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 17, 1, 2),
    _AgentTrapTargetIpAddr_Type()
)
agentTrapTargetIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapTargetIpAddr.setStatus("mandatory")


class _AgentTrapTargetComm_Type(DisplayString):
    """Custom type agentTrapTargetComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgentTrapTargetComm_Type.__name__ = "DisplayString"
_AgentTrapTargetComm_Object = MibTableColumn
agentTrapTargetComm = _AgentTrapTargetComm_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 17, 1, 3),
    _AgentTrapTargetComm_Type()
)
agentTrapTargetComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapTargetComm.setStatus("mandatory")
_AgentEmailAlert_ObjectIdentity = ObjectIdentity
agentEmailAlert = _AgentEmailAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 1, 18)
)


class _AgentSendEmailAlert_Type(Integer32):
    """Custom type agentSendEmailAlert based on Integer32"""
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


_AgentSendEmailAlert_Type.__name__ = "Integer32"
_AgentSendEmailAlert_Object = MibScalar
agentSendEmailAlert = _AgentSendEmailAlert_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 18, 1),
    _AgentSendEmailAlert_Type()
)
agentSendEmailAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSendEmailAlert.setStatus("mandatory")
_AgentEmailServerIpAddr_Type = IpAddress
_AgentEmailServerIpAddr_Object = MibScalar
agentEmailServerIpAddr = _AgentEmailServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 18, 2),
    _AgentEmailServerIpAddr_Type()
)
agentEmailServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentEmailServerIpAddr.setStatus("mandatory")
_AgentRecipientTable_Object = MibTable
agentRecipientTable = _AgentRecipientTable_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 18, 3)
)
if mibBuilder.loadTexts:
    agentRecipientTable.setStatus("mandatory")
_AgentRecipientEntry_Object = MibTableRow
agentRecipientEntry = _AgentRecipientEntry_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 18, 3, 1)
)
agentRecipientEntry.setIndexNames(
    (0, "LAMBDATRAIL-MIB", "agentRecipientIndex"),
)
if mibBuilder.loadTexts:
    agentRecipientEntry.setStatus("mandatory")
_AgentRecipientIndex_Type = Integer32
_AgentRecipientIndex_Object = MibTableColumn
agentRecipientIndex = _AgentRecipientIndex_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 18, 3, 1, 1),
    _AgentRecipientIndex_Type()
)
agentRecipientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRecipientIndex.setStatus("mandatory")


class _AgentRecipientEmailAddress_Type(DisplayString):
    """Custom type agentRecipientEmailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AgentRecipientEmailAddress_Type.__name__ = "DisplayString"
_AgentRecipientEmailAddress_Object = MibTableColumn
agentRecipientEmailAddress = _AgentRecipientEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 18, 3, 1, 2),
    _AgentRecipientEmailAddress_Type()
)
agentRecipientEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRecipientEmailAddress.setStatus("mandatory")
_AgentSyslog_ObjectIdentity = ObjectIdentity
agentSyslog = _AgentSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 1, 19)
)


class _AgentSyslogOnOff_Type(Integer32):
    """Custom type agentSyslogOnOff based on Integer32"""
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


_AgentSyslogOnOff_Type.__name__ = "Integer32"
_AgentSyslogOnOff_Object = MibScalar
agentSyslogOnOff = _AgentSyslogOnOff_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 19, 1),
    _AgentSyslogOnOff_Type()
)
agentSyslogOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSyslogOnOff.setStatus("mandatory")


class _AgentSaveLogsToFlash_Type(Integer32):
    """Custom type agentSaveLogsToFlash based on Integer32"""
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


_AgentSaveLogsToFlash_Type.__name__ = "Integer32"
_AgentSaveLogsToFlash_Object = MibScalar
agentSaveLogsToFlash = _AgentSaveLogsToFlash_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 19, 2),
    _AgentSaveLogsToFlash_Type()
)
agentSaveLogsToFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSaveLogsToFlash.setStatus("mandatory")


class _AgentClearAllLogs_Type(Integer32):
    """Custom type agentClearAllLogs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("access", 2))
    )


_AgentClearAllLogs_Type.__name__ = "Integer32"
_AgentClearAllLogs_Object = MibScalar
agentClearAllLogs = _AgentClearAllLogs_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 19, 3),
    _AgentClearAllLogs_Type()
)
agentClearAllLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearAllLogs.setStatus("mandatory")
_AgentSyslogServerTable_Object = MibTable
agentSyslogServerTable = _AgentSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 19, 4)
)
if mibBuilder.loadTexts:
    agentSyslogServerTable.setStatus("mandatory")
_AgentSyslogServerEntry_Object = MibTableRow
agentSyslogServerEntry = _AgentSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 19, 4, 1)
)
agentSyslogServerEntry.setIndexNames(
    (0, "LAMBDATRAIL-MIB", "agentSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    agentSyslogServerEntry.setStatus("mandatory")
_AgentSyslogServerIndex_Type = Integer32
_AgentSyslogServerIndex_Object = MibTableColumn
agentSyslogServerIndex = _AgentSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 19, 4, 1, 1),
    _AgentSyslogServerIndex_Type()
)
agentSyslogServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSyslogServerIndex.setStatus("mandatory")
_AgentSyslogServerIpAddr_Type = IpAddress
_AgentSyslogServerIpAddr_Object = MibTableColumn
agentSyslogServerIpAddr = _AgentSyslogServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 19, 4, 1, 2),
    _AgentSyslogServerIpAddr_Type()
)
agentSyslogServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSyslogServerIpAddr.setStatus("mandatory")
_AgentSecureIp_ObjectIdentity = ObjectIdentity
agentSecureIp = _AgentSecureIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 1, 20)
)


class _AgentSecureIpOnOff_Type(Integer32):
    """Custom type agentSecureIpOnOff based on Integer32"""
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


_AgentSecureIpOnOff_Type.__name__ = "Integer32"
_AgentSecureIpOnOff_Object = MibScalar
agentSecureIpOnOff = _AgentSecureIpOnOff_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 20, 1),
    _AgentSecureIpOnOff_Type()
)
agentSecureIpOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSecureIpOnOff.setStatus("mandatory")
_AgentSecureIpTable_Object = MibTable
agentSecureIpTable = _AgentSecureIpTable_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 20, 2)
)
if mibBuilder.loadTexts:
    agentSecureIpTable.setStatus("mandatory")
_AgentSecureIpEntry_Object = MibTableRow
agentSecureIpEntry = _AgentSecureIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 20, 2, 1)
)
agentSecureIpEntry.setIndexNames(
    (0, "LAMBDATRAIL-MIB", "agentSecureIpIndex"),
)
if mibBuilder.loadTexts:
    agentSecureIpEntry.setStatus("mandatory")
_AgentSecureIpIndex_Type = Integer32
_AgentSecureIpIndex_Object = MibTableColumn
agentSecureIpIndex = _AgentSecureIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 20, 2, 1, 1),
    _AgentSecureIpIndex_Type()
)
agentSecureIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSecureIpIndex.setStatus("mandatory")
_AgentSecureIpAddr_Type = IpAddress
_AgentSecureIpAddr_Object = MibTableColumn
agentSecureIpAddr = _AgentSecureIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 20, 2, 1, 2),
    _AgentSecureIpAddr_Type()
)
agentSecureIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSecureIpAddr.setStatus("mandatory")
_AgentTime_ObjectIdentity = ObjectIdentity
agentTime = _AgentTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21)
)


class _AgentNtpClientOnOff_Type(Integer32):
    """Custom type agentNtpClientOnOff based on Integer32"""
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


_AgentNtpClientOnOff_Type.__name__ = "Integer32"
_AgentNtpClientOnOff_Object = MibScalar
agentNtpClientOnOff = _AgentNtpClientOnOff_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 1),
    _AgentNtpClientOnOff_Type()
)
agentNtpClientOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpClientOnOff.setStatus("mandatory")
_AgentNtpServerIpAddr_Type = IpAddress
_AgentNtpServerIpAddr_Object = MibScalar
agentNtpServerIpAddr = _AgentNtpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 2),
    _AgentNtpServerIpAddr_Type()
)
agentNtpServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpServerIpAddr.setStatus("mandatory")


class _AgentNtpUpdateInterval_Type(Integer32):
    """Custom type agentNtpUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_AgentNtpUpdateInterval_Type.__name__ = "Integer32"
_AgentNtpUpdateInterval_Object = MibScalar
agentNtpUpdateInterval = _AgentNtpUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 3),
    _AgentNtpUpdateInterval_Type()
)
agentNtpUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpUpdateInterval.setStatus("mandatory")


class _AgentTimeZoneName_Type(DisplayString):
    """Custom type agentTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AgentTimeZoneName_Type.__name__ = "DisplayString"
_AgentTimeZoneName_Object = MibScalar
agentTimeZoneName = _AgentTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 4),
    _AgentTimeZoneName_Type()
)
agentTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTimeZoneName.setStatus("mandatory")


class _AgentTimeZoneHoursOffsetWithGMT_Type(Integer32):
    """Custom type agentTimeZoneHoursOffsetWithGMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 23),
    )


_AgentTimeZoneHoursOffsetWithGMT_Type.__name__ = "Integer32"
_AgentTimeZoneHoursOffsetWithGMT_Object = MibScalar
agentTimeZoneHoursOffsetWithGMT = _AgentTimeZoneHoursOffsetWithGMT_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 5),
    _AgentTimeZoneHoursOffsetWithGMT_Type()
)
agentTimeZoneHoursOffsetWithGMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTimeZoneHoursOffsetWithGMT.setStatus("mandatory")


class _AgentTimeZoneMinutesOffsetWithGMT_Type(Integer32):
    """Custom type agentTimeZoneMinutesOffsetWithGMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AgentTimeZoneMinutesOffsetWithGMT_Type.__name__ = "Integer32"
_AgentTimeZoneMinutesOffsetWithGMT_Object = MibScalar
agentTimeZoneMinutesOffsetWithGMT = _AgentTimeZoneMinutesOffsetWithGMT_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 6),
    _AgentTimeZoneMinutesOffsetWithGMT_Type()
)
agentTimeZoneMinutesOffsetWithGMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTimeZoneMinutesOffsetWithGMT.setStatus("mandatory")


class _AgentSummerTime_Type(Integer32):
    """Custom type agentSummerTime based on Integer32"""
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
        *(("summer", 1),
          ("Sun", 2),
          ("lastSun", 3),
          ("manual", 4))
    )


_AgentSummerTime_Type.__name__ = "Integer32"
_AgentSummerTime_Object = MibScalar
agentSummerTime = _AgentSummerTime_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 7),
    _AgentSummerTime_Type()
)
agentSummerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSummerTime.setStatus("mandatory")


class _AgentSummerTimeBeginMonth_Type(Integer32):
    """Custom type agentSummerTimeBeginMonth based on Integer32"""
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
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_AgentSummerTimeBeginMonth_Type.__name__ = "Integer32"
_AgentSummerTimeBeginMonth_Object = MibScalar
agentSummerTimeBeginMonth = _AgentSummerTimeBeginMonth_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 8),
    _AgentSummerTimeBeginMonth_Type()
)
agentSummerTimeBeginMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSummerTimeBeginMonth.setStatus("mandatory")


class _AgentSummerTimeBeginNth_Type(Integer32):
    """Custom type agentSummerTimeBeginNth based on Integer32"""
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
        *(("first", 1),
          ("second", 2),
          ("third", 3),
          ("fourth", 4),
          ("last", 5))
    )


_AgentSummerTimeBeginNth_Type.__name__ = "Integer32"
_AgentSummerTimeBeginNth_Object = MibScalar
agentSummerTimeBeginNth = _AgentSummerTimeBeginNth_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 9),
    _AgentSummerTimeBeginNth_Type()
)
agentSummerTimeBeginNth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSummerTimeBeginNth.setStatus("mandatory")


class _AgentSummerTimeBeginWeekday_Type(Integer32):
    """Custom type agentSummerTimeBeginWeekday based on Integer32"""
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
        *(("sun", 1),
          ("mon", 2),
          ("tue", 3),
          ("wed", 4),
          ("thu", 5),
          ("fri", 6),
          ("sat", 7))
    )


_AgentSummerTimeBeginWeekday_Type.__name__ = "Integer32"
_AgentSummerTimeBeginWeekday_Object = MibScalar
agentSummerTimeBeginWeekday = _AgentSummerTimeBeginWeekday_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 10),
    _AgentSummerTimeBeginWeekday_Type()
)
agentSummerTimeBeginWeekday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSummerTimeBeginWeekday.setStatus("mandatory")


class _AgentSummerTimeBeginHour_Type(Integer32):
    """Custom type agentSummerTimeBeginHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AgentSummerTimeBeginHour_Type.__name__ = "Integer32"
_AgentSummerTimeBeginHour_Object = MibScalar
agentSummerTimeBeginHour = _AgentSummerTimeBeginHour_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 11),
    _AgentSummerTimeBeginHour_Type()
)
agentSummerTimeBeginHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSummerTimeBeginHour.setStatus("mandatory")


class _AgentSummerTimeBeginMinute_Type(Integer32):
    """Custom type agentSummerTimeBeginMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AgentSummerTimeBeginMinute_Type.__name__ = "Integer32"
_AgentSummerTimeBeginMinute_Object = MibScalar
agentSummerTimeBeginMinute = _AgentSummerTimeBeginMinute_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 12),
    _AgentSummerTimeBeginMinute_Type()
)
agentSummerTimeBeginMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSummerTimeBeginMinute.setStatus("mandatory")


class _AgentSummerTimeEndMonth_Type(Integer32):
    """Custom type agentSummerTimeEndMonth based on Integer32"""
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
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_AgentSummerTimeEndMonth_Type.__name__ = "Integer32"
_AgentSummerTimeEndMonth_Object = MibScalar
agentSummerTimeEndMonth = _AgentSummerTimeEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 13),
    _AgentSummerTimeEndMonth_Type()
)
agentSummerTimeEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSummerTimeEndMonth.setStatus("mandatory")


class _AgentSummerTimeEndNth_Type(Integer32):
    """Custom type agentSummerTimeEndNth based on Integer32"""
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
        *(("first", 1),
          ("second", 2),
          ("third", 3),
          ("fourth", 4),
          ("last", 5))
    )


_AgentSummerTimeEndNth_Type.__name__ = "Integer32"
_AgentSummerTimeEndNth_Object = MibScalar
agentSummerTimeEndNth = _AgentSummerTimeEndNth_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 14),
    _AgentSummerTimeEndNth_Type()
)
agentSummerTimeEndNth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSummerTimeEndNth.setStatus("mandatory")


class _AgentSummerTimeEndWeekday_Type(Integer32):
    """Custom type agentSummerTimeEndWeekday based on Integer32"""
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
        *(("sun", 1),
          ("mon", 2),
          ("tue", 3),
          ("wed", 4),
          ("thu", 5),
          ("fri", 6),
          ("sat", 7))
    )


_AgentSummerTimeEndWeekday_Type.__name__ = "Integer32"
_AgentSummerTimeEndWeekday_Object = MibScalar
agentSummerTimeEndWeekday = _AgentSummerTimeEndWeekday_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 15),
    _AgentSummerTimeEndWeekday_Type()
)
agentSummerTimeEndWeekday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSummerTimeEndWeekday.setStatus("mandatory")


class _AgentSummerTimeEndHour_Type(Integer32):
    """Custom type agentSummerTimeEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AgentSummerTimeEndHour_Type.__name__ = "Integer32"
_AgentSummerTimeEndHour_Object = MibScalar
agentSummerTimeEndHour = _AgentSummerTimeEndHour_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 16),
    _AgentSummerTimeEndHour_Type()
)
agentSummerTimeEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSummerTimeEndHour.setStatus("mandatory")


class _AgentSummerTimeEndMinute_Type(Integer32):
    """Custom type agentSummerTimeEndMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AgentSummerTimeEndMinute_Type.__name__ = "Integer32"
_AgentSummerTimeEndMinute_Object = MibScalar
agentSummerTimeEndMinute = _AgentSummerTimeEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 21, 17),
    _AgentSummerTimeEndMinute_Type()
)
agentSummerTimeEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSummerTimeEndMinute.setStatus("mandatory")


class _AgentSaveRunningCfg_Type(Integer32):
    """Custom type agentSaveRunningCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("saveConfiguration", 2))
    )


_AgentSaveRunningCfg_Type.__name__ = "Integer32"
_AgentSaveRunningCfg_Object = MibScalar
agentSaveRunningCfg = _AgentSaveRunningCfg_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 22),
    _AgentSaveRunningCfg_Type()
)
agentSaveRunningCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSaveRunningCfg.setStatus("mandatory")
_AgentDefault_ObjectIdentity = ObjectIdentity
agentDefault = _AgentDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 1, 23)
)


class _AgentKeepCurrentIP_Type(Integer32):
    """Custom type agentKeepCurrentIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("keepCurrentIP", 2))
    )


_AgentKeepCurrentIP_Type.__name__ = "Integer32"
_AgentKeepCurrentIP_Object = MibScalar
agentKeepCurrentIP = _AgentKeepCurrentIP_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 23, 1),
    _AgentKeepCurrentIP_Type()
)
agentKeepCurrentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentKeepCurrentIP.setStatus("mandatory")


class _AgentKeepCurrentSNMP_Type(Integer32):
    """Custom type agentKeepCurrentSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("keepCurrentSNMP", 2))
    )


_AgentKeepCurrentSNMP_Type.__name__ = "Integer32"
_AgentKeepCurrentSNMP_Object = MibScalar
agentKeepCurrentSNMP = _AgentKeepCurrentSNMP_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 23, 2),
    _AgentKeepCurrentSNMP_Type()
)
agentKeepCurrentSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentKeepCurrentSNMP.setStatus("mandatory")


class _AgentKeepCurrentPort_Type(Integer32):
    """Custom type agentKeepCurrentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("keepCurrentPort", 2))
    )


_AgentKeepCurrentPort_Type.__name__ = "Integer32"
_AgentKeepCurrentPort_Object = MibScalar
agentKeepCurrentPort = _AgentKeepCurrentPort_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 23, 3),
    _AgentKeepCurrentPort_Type()
)
agentKeepCurrentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentKeepCurrentPort.setStatus("mandatory")


class _AgentKeepCurrentUser_Type(Integer32):
    """Custom type agentKeepCurrentUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("keepCurrentUser", 2))
    )


_AgentKeepCurrentUser_Type.__name__ = "Integer32"
_AgentKeepCurrentUser_Object = MibScalar
agentKeepCurrentUser = _AgentKeepCurrentUser_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 23, 4),
    _AgentKeepCurrentUser_Type()
)
agentKeepCurrentUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentKeepCurrentUser.setStatus("mandatory")


class _AgentFactoryDefault_Type(Integer32):
    """Custom type agentFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("factoryDefault", 2))
    )


_AgentFactoryDefault_Type.__name__ = "Integer32"
_AgentFactoryDefault_Object = MibScalar
agentFactoryDefault = _AgentFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 23, 5),
    _AgentFactoryDefault_Type()
)
agentFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFactoryDefault.setStatus("mandatory")


class _AgentReloadSystem_Type(Integer32):
    """Custom type agentReloadSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("reloadSystem", 2))
    )


_AgentReloadSystem_Type.__name__ = "Integer32"
_AgentReloadSystem_Object = MibScalar
agentReloadSystem = _AgentReloadSystem_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 24),
    _AgentReloadSystem_Type()
)
agentReloadSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentReloadSystem.setStatus("mandatory")
_AgentTftpUpgrade_ObjectIdentity = ObjectIdentity
agentTftpUpgrade = _AgentTftpUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 1, 25)
)
_AgentTftpServerIpAddr_Type = IpAddress
_AgentTftpServerIpAddr_Object = MibScalar
agentTftpServerIpAddr = _AgentTftpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 25, 1),
    _AgentTftpServerIpAddr_Type()
)
agentTftpServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTftpServerIpAddr.setStatus("mandatory")


class _AgentUpgradeFileName_Type(DisplayString):
    """Custom type agentUpgradeFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AgentUpgradeFileName_Type.__name__ = "DisplayString"
_AgentUpgradeFileName_Object = MibScalar
agentUpgradeFileName = _AgentUpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 25, 2),
    _AgentUpgradeFileName_Type()
)
agentUpgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUpgradeFileName.setStatus("mandatory")


class _AgentUpgradeState_Type(Integer32):
    """Custom type agentUpgradeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2),
          ("inProgress", 3))
    )


_AgentUpgradeState_Type.__name__ = "Integer32"
_AgentUpgradeState_Object = MibScalar
agentUpgradeState = _AgentUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 35616, 1, 25, 3),
    _AgentUpgradeState_Type()
)
agentUpgradeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUpgradeState.setStatus("mandatory")
_ProductType_ObjectIdentity = ObjectIdentity
productType = _ProductType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 2)
)
_Cwdm_ObjectIdentity = ObjectIdentity
cwdm = _Cwdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1)
)
_Lambdatrail_ObjectIdentity = ObjectIdentity
lambdatrail = _Lambdatrail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1)
)
_SystemTemperature_Type = Integer32
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 1),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("mandatory")


class _SystemPower1_Type(Integer32):
    """Custom type systemPower1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notplugged", 1),
          ("off", 2),
          ("on", 3))
    )


_SystemPower1_Type.__name__ = "Integer32"
_SystemPower1_Object = MibScalar
systemPower1 = _SystemPower1_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 2),
    _SystemPower1_Type()
)
systemPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPower1.setStatus("mandatory")


class _SystemPower2_Type(Integer32):
    """Custom type systemPower2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notplugged", 1),
          ("off", 2),
          ("on", 3))
    )


_SystemPower2_Type.__name__ = "Integer32"
_SystemPower2_Object = MibScalar
systemPower2 = _SystemPower2_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 3),
    _SystemPower2_Type()
)
systemPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPower2.setStatus("mandatory")


class _SystemFan1_Type(Integer32):
    """Custom type systemFan1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("off", 2),
          ("on", 3))
    )


_SystemFan1_Type.__name__ = "Integer32"
_SystemFan1_Object = MibScalar
systemFan1 = _SystemFan1_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 4),
    _SystemFan1_Type()
)
systemFan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFan1.setStatus("mandatory")


class _SystemFan1Selection_Type(Integer32):
    """Custom type systemFan1Selection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOff", 1),
          ("alwaysOn", 2),
          ("byTemperature", 3))
    )


_SystemFan1Selection_Type.__name__ = "Integer32"
_SystemFan1Selection_Object = MibScalar
systemFan1Selection = _SystemFan1Selection_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 5),
    _SystemFan1Selection_Type()
)
systemFan1Selection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFan1Selection.setStatus("mandatory")
_SystemFan1OnTemperature_Type = Integer32
_SystemFan1OnTemperature_Object = MibScalar
systemFan1OnTemperature = _SystemFan1OnTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 6),
    _SystemFan1OnTemperature_Type()
)
systemFan1OnTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFan1OnTemperature.setStatus("mandatory")
_SystemFan1OffTemperature_Type = Integer32
_SystemFan1OffTemperature_Object = MibScalar
systemFan1OffTemperature = _SystemFan1OffTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 7),
    _SystemFan1OffTemperature_Type()
)
systemFan1OffTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFan1OffTemperature.setStatus("mandatory")


class _SystemFan2_Type(Integer32):
    """Custom type systemFan2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("off", 2),
          ("on", 3))
    )


_SystemFan2_Type.__name__ = "Integer32"
_SystemFan2_Object = MibScalar
systemFan2 = _SystemFan2_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 8),
    _SystemFan2_Type()
)
systemFan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFan2.setStatus("mandatory")


class _SystemFan2Selection_Type(Integer32):
    """Custom type systemFan2Selection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOff", 1),
          ("alwaysOn", 2),
          ("byTemperature", 3))
    )


_SystemFan2Selection_Type.__name__ = "Integer32"
_SystemFan2Selection_Object = MibScalar
systemFan2Selection = _SystemFan2Selection_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 9),
    _SystemFan2Selection_Type()
)
systemFan2Selection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFan2Selection.setStatus("mandatory")
_SystemFan2OnTemperature_Type = Integer32
_SystemFan2OnTemperature_Object = MibScalar
systemFan2OnTemperature = _SystemFan2OnTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 10),
    _SystemFan2OnTemperature_Type()
)
systemFan2OnTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFan2OnTemperature.setStatus("mandatory")
_SystemFan2OffTemperature_Type = Integer32
_SystemFan2OffTemperature_Object = MibScalar
systemFan2OffTemperature = _SystemFan2OffTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 11),
    _SystemFan2OffTemperature_Type()
)
systemFan2OffTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFan2OffTemperature.setStatus("mandatory")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1)
)
portEntry.setIndexNames(
    (0, "LAMBDATRAIL-MIB", "portId"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortId_Type = Integer32
_PortId_Object = MibTableColumn
portId = _PortId_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 1),
    _PortId_Type()
)
portId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portId.setStatus("mandatory")


class _PortLicensed_Type(Integer32):
    """Custom type portLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortLicensed_Type.__name__ = "Integer32"
_PortLicensed_Object = MibTableColumn
portLicensed = _PortLicensed_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 2),
    _PortLicensed_Type()
)
portLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLicensed.setStatus("mandatory")


class _PortEnabled_Type(Integer32):
    """Custom type portEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PortEnabled_Type.__name__ = "Integer32"
_PortEnabled_Object = MibTableColumn
portEnabled = _PortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 3),
    _PortEnabled_Type()
)
portEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnabled.setStatus("mandatory")


class _PortAPSD_Type(Integer32):
    """Custom type portAPSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PortAPSD_Type.__name__ = "Integer32"
_PortAPSD_Object = MibTableColumn
portAPSD = _PortAPSD_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 4),
    _PortAPSD_Type()
)
portAPSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAPSD.setStatus("mandatory")


class _PortLinePlugged_Type(Integer32):
    """Custom type portLinePlugged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPlugged", 1),
          ("plugged", 2),
          ("notAvailable", 3))
    )


_PortLinePlugged_Type.__name__ = "Integer32"
_PortLinePlugged_Object = MibTableColumn
portLinePlugged = _PortLinePlugged_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 5),
    _PortLinePlugged_Type()
)
portLinePlugged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinePlugged.setStatus("mandatory")


class _PortLineLink_Type(Integer32):
    """Custom type portLineLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("notAvailable", 3))
    )


_PortLineLink_Type.__name__ = "Integer32"
_PortLineLink_Object = MibTableColumn
portLineLink = _PortLineLink_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 6),
    _PortLineLink_Type()
)
portLineLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLineLink.setStatus("mandatory")
_PortLineWavelength_Type = Integer32
_PortLineWavelength_Object = MibTableColumn
portLineWavelength = _PortLineWavelength_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 7),
    _PortLineWavelength_Type()
)
portLineWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLineWavelength.setStatus("mandatory")
_PortLineTxPower_Type = Integer32
_PortLineTxPower_Object = MibTableColumn
portLineTxPower = _PortLineTxPower_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 8),
    _PortLineTxPower_Type()
)
portLineTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLineTxPower.setStatus("mandatory")
_PortLineRxPower_Type = Integer32
_PortLineRxPower_Object = MibTableColumn
portLineRxPower = _PortLineRxPower_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 9),
    _PortLineRxPower_Type()
)
portLineRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLineRxPower.setStatus("mandatory")
_PortLineLaserTemp_Type = Integer32
_PortLineLaserTemp_Object = MibTableColumn
portLineLaserTemp = _PortLineLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 10),
    _PortLineLaserTemp_Type()
)
portLineLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLineLaserTemp.setStatus("mandatory")
_PortLineLaserBias_Type = Integer32
_PortLineLaserBias_Object = MibTableColumn
portLineLaserBias = _PortLineLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 11),
    _PortLineLaserBias_Type()
)
portLineLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLineLaserBias.setStatus("mandatory")


class _PortClientPlugged_Type(Integer32):
    """Custom type portClientPlugged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPlugged", 1),
          ("plugged", 2),
          ("notAvailable", 3))
    )


_PortClientPlugged_Type.__name__ = "Integer32"
_PortClientPlugged_Object = MibTableColumn
portClientPlugged = _PortClientPlugged_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 12),
    _PortClientPlugged_Type()
)
portClientPlugged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClientPlugged.setStatus("mandatory")


class _PortClientLink_Type(Integer32):
    """Custom type portClientLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("notAvailable", 3))
    )


_PortClientLink_Type.__name__ = "Integer32"
_PortClientLink_Object = MibTableColumn
portClientLink = _PortClientLink_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 13),
    _PortClientLink_Type()
)
portClientLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClientLink.setStatus("mandatory")
_PortClientWavelength_Type = Integer32
_PortClientWavelength_Object = MibTableColumn
portClientWavelength = _PortClientWavelength_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 14),
    _PortClientWavelength_Type()
)
portClientWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClientWavelength.setStatus("mandatory")
_PortClientTxPower_Type = Integer32
_PortClientTxPower_Object = MibTableColumn
portClientTxPower = _PortClientTxPower_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 15),
    _PortClientTxPower_Type()
)
portClientTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClientTxPower.setStatus("mandatory")
_PortClientRxPower_Type = Integer32
_PortClientRxPower_Object = MibTableColumn
portClientRxPower = _PortClientRxPower_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 16),
    _PortClientRxPower_Type()
)
portClientRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClientRxPower.setStatus("mandatory")
_PortClientLaserTemp_Type = Integer32
_PortClientLaserTemp_Object = MibTableColumn
portClientLaserTemp = _PortClientLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 17),
    _PortClientLaserTemp_Type()
)
portClientLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClientLaserTemp.setStatus("mandatory")
_PortClientLaserBias_Type = Integer32
_PortClientLaserBias_Object = MibTableColumn
portClientLaserBias = _PortClientLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 18),
    _PortClientLaserBias_Type()
)
portClientLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClientLaserBias.setStatus("mandatory")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 12, 1, 19),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("mandatory")
_UsablePorts_Type = Integer32
_UsablePorts_Object = MibScalar
usablePorts = _UsablePorts_Object(
    (1, 3, 6, 1, 4, 1, 35616, 2, 1, 1, 13),
    _UsablePorts_Type()
)
usablePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usablePorts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LAMBDATRAIL-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "deltanet": deltanet,
       "snmpAgent": snmpAgent,
       "agentSw": agentSw,
       "agentSoftwareMajorVer": agentSoftwareMajorVer,
       "agentSoftwareMinorVer": agentSoftwareMinorVer,
       "agentOutBandBaudRate": agentOutBandBaudRate,
       "agentConsoleIdleTimeouts": agentConsoleIdleTimeouts,
       "agentPrompt": agentPrompt,
       "agentBootMethod": agentBootMethod,
       "agentIpAddr": agentIpAddr,
       "agentIpNetMask": agentIpNetMask,
       "agentDefaultGateway": agentDefaultGateway,
       "agentPrimaryDnsServer": agentPrimaryDnsServer,
       "agentSecondaryDnsServer": agentSecondaryDnsServer,
       "agentSnmpServer": agentSnmpServer,
       "agentHttpServer": agentHttpServer,
       "agentTelnet": agentTelnet,
       "agentTelnetServer": agentTelnetServer,
       "agentTelnetIdleTimeouts": agentTelnetIdleTimeouts,
       "agentTelnetMaxSessions": agentTelnetMaxSessions,
       "agentFtpServer": agentFtpServer,
       "agentTftpServer": agentTftpServer,
       "agentSendTrap": agentSendTrap,
       "agentTrapTargetTable": agentTrapTargetTable,
       "agentTrapTargetEntry": agentTrapTargetEntry,
       "agentTrapIndex": agentTrapIndex,
       "agentTrapTargetIpAddr": agentTrapTargetIpAddr,
       "agentTrapTargetComm": agentTrapTargetComm,
       "agentEmailAlert": agentEmailAlert,
       "agentSendEmailAlert": agentSendEmailAlert,
       "agentEmailServerIpAddr": agentEmailServerIpAddr,
       "agentRecipientTable": agentRecipientTable,
       "agentRecipientEntry": agentRecipientEntry,
       "agentRecipientIndex": agentRecipientIndex,
       "agentRecipientEmailAddress": agentRecipientEmailAddress,
       "agentSyslog": agentSyslog,
       "agentSyslogOnOff": agentSyslogOnOff,
       "agentSaveLogsToFlash": agentSaveLogsToFlash,
       "agentClearAllLogs": agentClearAllLogs,
       "agentSyslogServerTable": agentSyslogServerTable,
       "agentSyslogServerEntry": agentSyslogServerEntry,
       "agentSyslogServerIndex": agentSyslogServerIndex,
       "agentSyslogServerIpAddr": agentSyslogServerIpAddr,
       "agentSecureIp": agentSecureIp,
       "agentSecureIpOnOff": agentSecureIpOnOff,
       "agentSecureIpTable": agentSecureIpTable,
       "agentSecureIpEntry": agentSecureIpEntry,
       "agentSecureIpIndex": agentSecureIpIndex,
       "agentSecureIpAddr": agentSecureIpAddr,
       "agentTime": agentTime,
       "agentNtpClientOnOff": agentNtpClientOnOff,
       "agentNtpServerIpAddr": agentNtpServerIpAddr,
       "agentNtpUpdateInterval": agentNtpUpdateInterval,
       "agentTimeZoneName": agentTimeZoneName,
       "agentTimeZoneHoursOffsetWithGMT": agentTimeZoneHoursOffsetWithGMT,
       "agentTimeZoneMinutesOffsetWithGMT": agentTimeZoneMinutesOffsetWithGMT,
       "agentSummerTime": agentSummerTime,
       "agentSummerTimeBeginMonth": agentSummerTimeBeginMonth,
       "agentSummerTimeBeginNth": agentSummerTimeBeginNth,
       "agentSummerTimeBeginWeekday": agentSummerTimeBeginWeekday,
       "agentSummerTimeBeginHour": agentSummerTimeBeginHour,
       "agentSummerTimeBeginMinute": agentSummerTimeBeginMinute,
       "agentSummerTimeEndMonth": agentSummerTimeEndMonth,
       "agentSummerTimeEndNth": agentSummerTimeEndNth,
       "agentSummerTimeEndWeekday": agentSummerTimeEndWeekday,
       "agentSummerTimeEndHour": agentSummerTimeEndHour,
       "agentSummerTimeEndMinute": agentSummerTimeEndMinute,
       "agentSaveRunningCfg": agentSaveRunningCfg,
       "agentDefault": agentDefault,
       "agentKeepCurrentIP": agentKeepCurrentIP,
       "agentKeepCurrentSNMP": agentKeepCurrentSNMP,
       "agentKeepCurrentPort": agentKeepCurrentPort,
       "agentKeepCurrentUser": agentKeepCurrentUser,
       "agentFactoryDefault": agentFactoryDefault,
       "agentReloadSystem": agentReloadSystem,
       "agentTftpUpgrade": agentTftpUpgrade,
       "agentTftpServerIpAddr": agentTftpServerIpAddr,
       "agentUpgradeFileName": agentUpgradeFileName,
       "agentUpgradeState": agentUpgradeState,
       "productType": productType,
       "cwdm": cwdm,
       "lambdatrail": lambdatrail,
       "systemTemperature": systemTemperature,
       "systemPower1": systemPower1,
       "systemPower2": systemPower2,
       "systemFan1": systemFan1,
       "systemFan1Selection": systemFan1Selection,
       "systemFan1OnTemperature": systemFan1OnTemperature,
       "systemFan1OffTemperature": systemFan1OffTemperature,
       "systemFan2": systemFan2,
       "systemFan2Selection": systemFan2Selection,
       "systemFan2OnTemperature": systemFan2OnTemperature,
       "systemFan2OffTemperature": systemFan2OffTemperature,
       "portTable": portTable,
       "portEntry": portEntry,
       "portId": portId,
       "portLicensed": portLicensed,
       "portEnabled": portEnabled,
       "portAPSD": portAPSD,
       "portLinePlugged": portLinePlugged,
       "portLineLink": portLineLink,
       "portLineWavelength": portLineWavelength,
       "portLineTxPower": portLineTxPower,
       "portLineRxPower": portLineRxPower,
       "portLineLaserTemp": portLineLaserTemp,
       "portLineLaserBias": portLineLaserBias,
       "portClientPlugged": portClientPlugged,
       "portClientLink": portClientLink,
       "portClientWavelength": portClientWavelength,
       "portClientTxPower": portClientTxPower,
       "portClientRxPower": portClientRxPower,
       "portClientLaserTemp": portClientLaserTemp,
       "portClientLaserBias": portClientLaserBias,
       "portName": portName,
       "usablePorts": usablePorts}
)
