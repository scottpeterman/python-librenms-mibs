# SNMP MIB module (SLE-VOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-VOIP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:07 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleVoip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25)
)


# Types definitions



class OwnerString(OctetString):
    """Custom type OwnerString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class EnableDisableState(Integer32):
    """Custom type EnableDisableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleVoipBase_ObjectIdentity = ObjectIdentity
sleVoipBase = _SleVoipBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1)
)
_SleVoipBaseInfo_ObjectIdentity = ObjectIdentity
sleVoipBaseInfo = _SleVoipBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 1)
)
_SleVoipInterface_Type = OctetString
_SleVoipInterface_Object = MibScalar
sleVoipInterface = _SleVoipInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 1, 1),
    _SleVoipInterface_Type()
)
sleVoipInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipInterface.setStatus("current")


class _SleVoipProtocol_Type(Integer32):
    """Custom type sleVoipProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sip", 1),
          ("mgcp", 3))
    )


_SleVoipProtocol_Type.__name__ = "Integer32"
_SleVoipProtocol_Object = MibScalar
sleVoipProtocol = _SleVoipProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 1, 2),
    _SleVoipProtocol_Type()
)
sleVoipProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipProtocol.setStatus("current")


class _SleVoipRtcp_Type(Integer32):
    """Custom type sleVoipRtcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("voipRtcpDisable", 0),
          ("voipRtcpEnable", 1))
    )


_SleVoipRtcp_Type.__name__ = "Integer32"
_SleVoipRtcp_Object = MibScalar
sleVoipRtcp = _SleVoipRtcp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 1, 3),
    _SleVoipRtcp_Type()
)
sleVoipRtcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipRtcp.setStatus("current")


class _SleVoipFaxmode_Type(Integer32):
    """Custom type sleVoipFaxmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("voipFaxmodeT30", 0),
          ("voipFaxmodeT38", 1))
    )


_SleVoipFaxmode_Type.__name__ = "Integer32"
_SleVoipFaxmode_Object = MibScalar
sleVoipFaxmode = _SleVoipFaxmode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 1, 4),
    _SleVoipFaxmode_Type()
)
sleVoipFaxmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipFaxmode.setStatus("current")
_SleVoipBaseControl_ObjectIdentity = ObjectIdentity
sleVoipBaseControl = _SleVoipBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 2)
)


class _SleVoipBaseControlRequest_Type(Integer32):
    """Custom type sleVoipBaseControlRequest based on Integer32"""
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
        *(("setVoipInterface", 1),
          ("setVoipProtocol", 2),
          ("voipRestartStackOnly", 3),
          ("voipRestartAll", 4),
          ("setVoipRtcp", 5),
          ("setVoipFaxmode", 6))
    )


_SleVoipBaseControlRequest_Type.__name__ = "Integer32"
_SleVoipBaseControlRequest_Object = MibScalar
sleVoipBaseControlRequest = _SleVoipBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 2, 1),
    _SleVoipBaseControlRequest_Type()
)
sleVoipBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipBaseControlRequest.setStatus("current")
_SleVoipBaseControlStatus_Type = SleControlStatusType
_SleVoipBaseControlStatus_Object = MibScalar
sleVoipBaseControlStatus = _SleVoipBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 2, 2),
    _SleVoipBaseControlStatus_Type()
)
sleVoipBaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipBaseControlStatus.setStatus("current")
_SleVoipBaseControlTimer_Type = Gauge32
_SleVoipBaseControlTimer_Object = MibScalar
sleVoipBaseControlTimer = _SleVoipBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 2, 3),
    _SleVoipBaseControlTimer_Type()
)
sleVoipBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipBaseControlTimer.setStatus("current")
_SleVoipBaseControlTimeStamp_Type = TimeTicks
_SleVoipBaseControlTimeStamp_Object = MibScalar
sleVoipBaseControlTimeStamp = _SleVoipBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 2, 4),
    _SleVoipBaseControlTimeStamp_Type()
)
sleVoipBaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipBaseControlTimeStamp.setStatus("current")
_SleVoipBaseControlReqResult_Type = SleControlRequestResultType
_SleVoipBaseControlReqResult_Object = MibScalar
sleVoipBaseControlReqResult = _SleVoipBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 2, 5),
    _SleVoipBaseControlReqResult_Type()
)
sleVoipBaseControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipBaseControlReqResult.setStatus("current")
_SleVoipBaseControlInterface_Type = OctetString
_SleVoipBaseControlInterface_Object = MibScalar
sleVoipBaseControlInterface = _SleVoipBaseControlInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 2, 6),
    _SleVoipBaseControlInterface_Type()
)
sleVoipBaseControlInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipBaseControlInterface.setStatus("current")


class _SleVoipBaseControlProtocol_Type(Integer32):
    """Custom type sleVoipBaseControlProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sip", 1),
          ("mgcp", 3))
    )


_SleVoipBaseControlProtocol_Type.__name__ = "Integer32"
_SleVoipBaseControlProtocol_Object = MibScalar
sleVoipBaseControlProtocol = _SleVoipBaseControlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 2, 7),
    _SleVoipBaseControlProtocol_Type()
)
sleVoipBaseControlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipBaseControlProtocol.setStatus("current")


class _SleVoipBaseControlRtcp_Type(Integer32):
    """Custom type sleVoipBaseControlRtcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("voipRtcpDisable", 0),
          ("voipRtcpEnable", 1))
    )


_SleVoipBaseControlRtcp_Type.__name__ = "Integer32"
_SleVoipBaseControlRtcp_Object = MibScalar
sleVoipBaseControlRtcp = _SleVoipBaseControlRtcp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 2, 8),
    _SleVoipBaseControlRtcp_Type()
)
sleVoipBaseControlRtcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipBaseControlRtcp.setStatus("current")


class _SleVoipBaseControlFaxmode_Type(Integer32):
    """Custom type sleVoipBaseControlFaxmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("voipFaxmodeT30", 0),
          ("voipFaxmodeT38", 1))
    )


_SleVoipBaseControlFaxmode_Type.__name__ = "Integer32"
_SleVoipBaseControlFaxmode_Object = MibScalar
sleVoipBaseControlFaxmode = _SleVoipBaseControlFaxmode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 2, 9),
    _SleVoipBaseControlFaxmode_Type()
)
sleVoipBaseControlFaxmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipBaseControlFaxmode.setStatus("current")
_SleVoipBaseNotification_ObjectIdentity = ObjectIdentity
sleVoipBaseNotification = _SleVoipBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 3)
)
_SleVoipVoice_ObjectIdentity = ObjectIdentity
sleVoipVoice = _SleVoipVoice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2)
)
_SleVoipVoiceTable_Object = MibTable
sleVoipVoiceTable = _SleVoipVoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 1)
)
if mibBuilder.loadTexts:
    sleVoipVoiceTable.setStatus("current")
_SleVoipVoiceEntry_Object = MibTableRow
sleVoipVoiceEntry = _SleVoipVoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 1, 1)
)
sleVoipVoiceEntry.setIndexNames(
    (0, "SLE-VOIP-MIB", "sleVoipVoiceIndex"),
)
if mibBuilder.loadTexts:
    sleVoipVoiceEntry.setStatus("current")


class _SleVoipVoiceIndex_Type(Integer32):
    """Custom type sleVoipVoiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipVoiceIndex_Type.__name__ = "Integer32"
_SleVoipVoiceIndex_Object = MibTableColumn
sleVoipVoiceIndex = _SleVoipVoiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 1, 1, 1),
    _SleVoipVoiceIndex_Type()
)
sleVoipVoiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipVoiceIndex.setStatus("current")


class _SleVoipVoiceEncoding_Type(Integer32):
    """Custom type sleVoipVoiceEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("a", 0),
          ("m", 1))
    )


_SleVoipVoiceEncoding_Type.__name__ = "Integer32"
_SleVoipVoiceEncoding_Object = MibTableColumn
sleVoipVoiceEncoding = _SleVoipVoiceEncoding_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 1, 1, 2),
    _SleVoipVoiceEncoding_Type()
)
sleVoipVoiceEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipVoiceEncoding.setStatus("current")


class _SleVoipVoiceUserEncoding_Type(Integer32):
    """Custom type sleVoipVoiceUserEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("a", 0),
          ("m", 1))
    )


_SleVoipVoiceUserEncoding_Type.__name__ = "Integer32"
_SleVoipVoiceUserEncoding_Object = MibTableColumn
sleVoipVoiceUserEncoding = _SleVoipVoiceUserEncoding_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 1, 1, 3),
    _SleVoipVoiceUserEncoding_Type()
)
sleVoipVoiceUserEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipVoiceUserEncoding.setStatus("current")


class _SleVoipVoiceComfortNoise_Type(Integer32):
    """Custom type sleVoipVoiceComfortNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_SleVoipVoiceComfortNoise_Type.__name__ = "Integer32"
_SleVoipVoiceComfortNoise_Object = MibTableColumn
sleVoipVoiceComfortNoise = _SleVoipVoiceComfortNoise_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 1, 1, 4),
    _SleVoipVoiceComfortNoise_Type()
)
sleVoipVoiceComfortNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipVoiceComfortNoise.setStatus("current")


class _SleVoipVoiceEchoCancel_Type(Integer32):
    """Custom type sleVoipVoiceEchoCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleVoipVoiceEchoCancel_Type.__name__ = "Integer32"
_SleVoipVoiceEchoCancel_Object = MibTableColumn
sleVoipVoiceEchoCancel = _SleVoipVoiceEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 1, 1, 5),
    _SleVoipVoiceEchoCancel_Type()
)
sleVoipVoiceEchoCancel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipVoiceEchoCancel.setStatus("current")


class _SleVoipVoicePacketLoss_Type(Integer32):
    """Custom type sleVoipVoicePacketLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleVoipVoicePacketLoss_Type.__name__ = "Integer32"
_SleVoipVoicePacketLoss_Object = MibTableColumn
sleVoipVoicePacketLoss = _SleVoipVoicePacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 1, 1, 6),
    _SleVoipVoicePacketLoss_Type()
)
sleVoipVoicePacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipVoicePacketLoss.setStatus("current")


class _SleVoipVoiceVad_Type(Integer32):
    """Custom type sleVoipVoiceVad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleVoipVoiceVad_Type.__name__ = "Integer32"
_SleVoipVoiceVad_Object = MibTableColumn
sleVoipVoiceVad = _SleVoipVoiceVad_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 1, 1, 7),
    _SleVoipVoiceVad_Type()
)
sleVoipVoiceVad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipVoiceVad.setStatus("current")


class _SleVoipVoiceDSCP_Type(Unsigned32):
    """Custom type sleVoipVoiceDSCP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleVoipVoiceDSCP_Type.__name__ = "Unsigned32"
_SleVoipVoiceDSCP_Object = MibTableColumn
sleVoipVoiceDSCP = _SleVoipVoiceDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 1, 1, 8),
    _SleVoipVoiceDSCP_Type()
)
sleVoipVoiceDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipVoiceDSCP.setStatus("current")


class _SleVoipVoiceJitter_Type(Unsigned32):
    """Custom type sleVoipVoiceJitter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_SleVoipVoiceJitter_Type.__name__ = "Unsigned32"
_SleVoipVoiceJitter_Object = MibTableColumn
sleVoipVoiceJitter = _SleVoipVoiceJitter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 1, 1, 9),
    _SleVoipVoiceJitter_Type()
)
sleVoipVoiceJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipVoiceJitter.setStatus("current")
_SleVoipVoiceControl_ObjectIdentity = ObjectIdentity
sleVoipVoiceControl = _SleVoipVoiceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2)
)


class _SleVoipVoiceControlRequest_Type(Integer32):
    """Custom type sleVoipVoiceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableVoiceVoip", 1),
          ("disableVoiceVoip", 2))
    )


_SleVoipVoiceControlRequest_Type.__name__ = "Integer32"
_SleVoipVoiceControlRequest_Object = MibScalar
sleVoipVoiceControlRequest = _SleVoipVoiceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 1),
    _SleVoipVoiceControlRequest_Type()
)
sleVoipVoiceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipVoiceControlRequest.setStatus("current")
_SleVoipVoiceControlStatus_Type = SleControlStatusType
_SleVoipVoiceControlStatus_Object = MibScalar
sleVoipVoiceControlStatus = _SleVoipVoiceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 2),
    _SleVoipVoiceControlStatus_Type()
)
sleVoipVoiceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipVoiceControlStatus.setStatus("current")
_SleVoipVoiceControlTimer_Type = Gauge32
_SleVoipVoiceControlTimer_Object = MibScalar
sleVoipVoiceControlTimer = _SleVoipVoiceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 3),
    _SleVoipVoiceControlTimer_Type()
)
sleVoipVoiceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipVoiceControlTimer.setStatus("current")
_SleVoipVoiceControlTimeStamp_Type = TimeTicks
_SleVoipVoiceControlTimeStamp_Object = MibScalar
sleVoipVoiceControlTimeStamp = _SleVoipVoiceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 4),
    _SleVoipVoiceControlTimeStamp_Type()
)
sleVoipVoiceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipVoiceControlTimeStamp.setStatus("current")
_SleVoipVoiceControlReqResult_Type = SleControlRequestResultType
_SleVoipVoiceControlReqResult_Object = MibScalar
sleVoipVoiceControlReqResult = _SleVoipVoiceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 5),
    _SleVoipVoiceControlReqResult_Type()
)
sleVoipVoiceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipVoiceControlReqResult.setStatus("current")


class _SleVoipVoiceControlIndex_Type(Integer32):
    """Custom type sleVoipVoiceControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipVoiceControlIndex_Type.__name__ = "Integer32"
_SleVoipVoiceControlIndex_Object = MibScalar
sleVoipVoiceControlIndex = _SleVoipVoiceControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 6),
    _SleVoipVoiceControlIndex_Type()
)
sleVoipVoiceControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipVoiceControlIndex.setStatus("current")


class _SleVoipVoiceControlEncoding_Type(Integer32):
    """Custom type sleVoipVoiceControlEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 0),
          ("mulaw", 1))
    )


_SleVoipVoiceControlEncoding_Type.__name__ = "Integer32"
_SleVoipVoiceControlEncoding_Object = MibScalar
sleVoipVoiceControlEncoding = _SleVoipVoiceControlEncoding_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 7),
    _SleVoipVoiceControlEncoding_Type()
)
sleVoipVoiceControlEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipVoiceControlEncoding.setStatus("current")


class _SleVoipVoiceControlUserEncoding_Type(Integer32):
    """Custom type sleVoipVoiceControlUserEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 0),
          ("mulaw", 1))
    )


_SleVoipVoiceControlUserEncoding_Type.__name__ = "Integer32"
_SleVoipVoiceControlUserEncoding_Object = MibScalar
sleVoipVoiceControlUserEncoding = _SleVoipVoiceControlUserEncoding_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 8),
    _SleVoipVoiceControlUserEncoding_Type()
)
sleVoipVoiceControlUserEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipVoiceControlUserEncoding.setStatus("current")


class _SleVoipVoiceControlComfortNoise_Type(Integer32):
    """Custom type sleVoipVoiceControlComfortNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_SleVoipVoiceControlComfortNoise_Type.__name__ = "Integer32"
_SleVoipVoiceControlComfortNoise_Object = MibScalar
sleVoipVoiceControlComfortNoise = _SleVoipVoiceControlComfortNoise_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 9),
    _SleVoipVoiceControlComfortNoise_Type()
)
sleVoipVoiceControlComfortNoise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipVoiceControlComfortNoise.setStatus("current")


class _SleVoipVoiceControlEchoCancel_Type(Integer32):
    """Custom type sleVoipVoiceControlEchoCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleVoipVoiceControlEchoCancel_Type.__name__ = "Integer32"
_SleVoipVoiceControlEchoCancel_Object = MibScalar
sleVoipVoiceControlEchoCancel = _SleVoipVoiceControlEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 10),
    _SleVoipVoiceControlEchoCancel_Type()
)
sleVoipVoiceControlEchoCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipVoiceControlEchoCancel.setStatus("current")


class _SleVoipVoiceControlPacketLoss_Type(Integer32):
    """Custom type sleVoipVoiceControlPacketLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleVoipVoiceControlPacketLoss_Type.__name__ = "Integer32"
_SleVoipVoiceControlPacketLoss_Object = MibScalar
sleVoipVoiceControlPacketLoss = _SleVoipVoiceControlPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 11),
    _SleVoipVoiceControlPacketLoss_Type()
)
sleVoipVoiceControlPacketLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipVoiceControlPacketLoss.setStatus("current")


class _SleVoipVoiceControlVad_Type(Integer32):
    """Custom type sleVoipVoiceControlVad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleVoipVoiceControlVad_Type.__name__ = "Integer32"
_SleVoipVoiceControlVad_Object = MibScalar
sleVoipVoiceControlVad = _SleVoipVoiceControlVad_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 12),
    _SleVoipVoiceControlVad_Type()
)
sleVoipVoiceControlVad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipVoiceControlVad.setStatus("current")


class _SleVoipVoiceControlDSCP_Type(Unsigned32):
    """Custom type sleVoipVoiceControlDSCP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleVoipVoiceControlDSCP_Type.__name__ = "Unsigned32"
_SleVoipVoiceControlDSCP_Object = MibScalar
sleVoipVoiceControlDSCP = _SleVoipVoiceControlDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 13),
    _SleVoipVoiceControlDSCP_Type()
)
sleVoipVoiceControlDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipVoiceControlDSCP.setStatus("current")


class _SleVoipVoiceControlJitter_Type(Unsigned32):
    """Custom type sleVoipVoiceControlJitter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_SleVoipVoiceControlJitter_Type.__name__ = "Unsigned32"
_SleVoipVoiceControlJitter_Object = MibScalar
sleVoipVoiceControlJitter = _SleVoipVoiceControlJitter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 2, 14),
    _SleVoipVoiceControlJitter_Type()
)
sleVoipVoiceControlJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipVoiceControlJitter.setStatus("current")
_SleVoiceNotification_ObjectIdentity = ObjectIdentity
sleVoiceNotification = _SleVoiceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 3)
)
_SleVoipSipUser_ObjectIdentity = ObjectIdentity
sleVoipSipUser = _SleVoipSipUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3)
)
_SleVoipSipUserTable_Object = MibTable
sleVoipSipUserTable = _SleVoipSipUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 1)
)
if mibBuilder.loadTexts:
    sleVoipSipUserTable.setStatus("current")
_SleVoipSipUserEntry_Object = MibTableRow
sleVoipSipUserEntry = _SleVoipSipUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 1, 1)
)
sleVoipSipUserEntry.setIndexNames(
    (0, "SLE-VOIP-MIB", "sleVoipSipUserIndex"),
)
if mibBuilder.loadTexts:
    sleVoipSipUserEntry.setStatus("current")


class _SleVoipSipUserIndex_Type(Unsigned32):
    """Custom type sleVoipSipUserIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipSipUserIndex_Type.__name__ = "Unsigned32"
_SleVoipSipUserIndex_Object = MibTableColumn
sleVoipSipUserIndex = _SleVoipSipUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 1, 1, 1),
    _SleVoipSipUserIndex_Type()
)
sleVoipSipUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipUserIndex.setStatus("current")


class _SleVoipSipUserAgent_Type(Integer32):
    """Custom type sleVoipSipUserAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipSipUserAgent_Type.__name__ = "Integer32"
_SleVoipSipUserAgent_Object = MibTableColumn
sleVoipSipUserAgent = _SleVoipSipUserAgent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 1, 1, 2),
    _SleVoipSipUserAgent_Type()
)
sleVoipSipUserAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipUserAgent.setStatus("current")
_SleVoipSipUserAOR_Type = OctetString
_SleVoipSipUserAOR_Object = MibTableColumn
sleVoipSipUserAOR = _SleVoipSipUserAOR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 1, 1, 3),
    _SleVoipSipUserAOR_Type()
)
sleVoipSipUserAOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipUserAOR.setStatus("current")
_SleVoipSipUserDisplayName_Type = OctetString
_SleVoipSipUserDisplayName_Object = MibTableColumn
sleVoipSipUserDisplayName = _SleVoipSipUserDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 1, 1, 4),
    _SleVoipSipUserDisplayName_Type()
)
sleVoipSipUserDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipUserDisplayName.setStatus("current")
_SleVoipSipUserUserName_Type = OctetString
_SleVoipSipUserUserName_Object = MibTableColumn
sleVoipSipUserUserName = _SleVoipSipUserUserName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 1, 1, 5),
    _SleVoipSipUserUserName_Type()
)
sleVoipSipUserUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipUserUserName.setStatus("current")
_SleVoipSipUserPassword_Type = OctetString
_SleVoipSipUserPassword_Object = MibTableColumn
sleVoipSipUserPassword = _SleVoipSipUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 1, 1, 6),
    _SleVoipSipUserPassword_Type()
)
sleVoipSipUserPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipUserPassword.setStatus("current")
_SleVoipSipUserControl_ObjectIdentity = ObjectIdentity
sleVoipSipUserControl = _SleVoipSipUserControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 2)
)


class _SleVoipSipUserControlRequest_Type(Integer32):
    """Custom type sleVoipSipUserControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableVoipSipUser", 1),
          ("disableVoipSipUser", 2))
    )


_SleVoipSipUserControlRequest_Type.__name__ = "Integer32"
_SleVoipSipUserControlRequest_Object = MibScalar
sleVoipSipUserControlRequest = _SleVoipSipUserControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 2, 1),
    _SleVoipSipUserControlRequest_Type()
)
sleVoipSipUserControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipUserControlRequest.setStatus("current")
_SleVoipSipUserControlStatus_Type = SleControlStatusType
_SleVoipSipUserControlStatus_Object = MibScalar
sleVoipSipUserControlStatus = _SleVoipSipUserControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 2, 2),
    _SleVoipSipUserControlStatus_Type()
)
sleVoipSipUserControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipUserControlStatus.setStatus("current")
_SleVoipSipUserControlTimer_Type = Gauge32
_SleVoipSipUserControlTimer_Object = MibScalar
sleVoipSipUserControlTimer = _SleVoipSipUserControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 2, 3),
    _SleVoipSipUserControlTimer_Type()
)
sleVoipSipUserControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipUserControlTimer.setStatus("current")
_SleVoipSipUserControlTimeStamp_Type = TimeTicks
_SleVoipSipUserControlTimeStamp_Object = MibScalar
sleVoipSipUserControlTimeStamp = _SleVoipSipUserControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 2, 4),
    _SleVoipSipUserControlTimeStamp_Type()
)
sleVoipSipUserControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipUserControlTimeStamp.setStatus("current")
_SleVoipSipUserControlReqResult_Type = SleControlRequestResultType
_SleVoipSipUserControlReqResult_Object = MibScalar
sleVoipSipUserControlReqResult = _SleVoipSipUserControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 2, 5),
    _SleVoipSipUserControlReqResult_Type()
)
sleVoipSipUserControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipUserControlReqResult.setStatus("current")


class _SleVoipSipUserControlIndex_Type(Unsigned32):
    """Custom type sleVoipSipUserControlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipSipUserControlIndex_Type.__name__ = "Unsigned32"
_SleVoipSipUserControlIndex_Object = MibScalar
sleVoipSipUserControlIndex = _SleVoipSipUserControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 2, 6),
    _SleVoipSipUserControlIndex_Type()
)
sleVoipSipUserControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipUserControlIndex.setStatus("current")


class _SleVoipSipUserControlAgent_Type(Integer32):
    """Custom type sleVoipSipUserControlAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipSipUserControlAgent_Type.__name__ = "Integer32"
_SleVoipSipUserControlAgent_Object = MibScalar
sleVoipSipUserControlAgent = _SleVoipSipUserControlAgent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 2, 7),
    _SleVoipSipUserControlAgent_Type()
)
sleVoipSipUserControlAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipUserControlAgent.setStatus("current")
_SleVoipSipUserControlAOR_Type = OctetString
_SleVoipSipUserControlAOR_Object = MibScalar
sleVoipSipUserControlAOR = _SleVoipSipUserControlAOR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 2, 8),
    _SleVoipSipUserControlAOR_Type()
)
sleVoipSipUserControlAOR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipUserControlAOR.setStatus("current")
_SleVoipSipUserControlDisplayName_Type = OctetString
_SleVoipSipUserControlDisplayName_Object = MibScalar
sleVoipSipUserControlDisplayName = _SleVoipSipUserControlDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 2, 9),
    _SleVoipSipUserControlDisplayName_Type()
)
sleVoipSipUserControlDisplayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipUserControlDisplayName.setStatus("current")
_SleVoipSipUserControlUserName_Type = OctetString
_SleVoipSipUserControlUserName_Object = MibScalar
sleVoipSipUserControlUserName = _SleVoipSipUserControlUserName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 2, 10),
    _SleVoipSipUserControlUserName_Type()
)
sleVoipSipUserControlUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipUserControlUserName.setStatus("current")
_SleVoipSipUserControlPassword_Type = OctetString
_SleVoipSipUserControlPassword_Object = MibScalar
sleVoipSipUserControlPassword = _SleVoipSipUserControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 2, 11),
    _SleVoipSipUserControlPassword_Type()
)
sleVoipSipUserControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipUserControlPassword.setStatus("current")
_SleVoipSipUserNotification_ObjectIdentity = ObjectIdentity
sleVoipSipUserNotification = _SleVoipSipUserNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 3)
)
_SleVoipSipAgent_ObjectIdentity = ObjectIdentity
sleVoipSipAgent = _SleVoipSipAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4)
)
_SleVoipSipAgentTable_Object = MibTable
sleVoipSipAgentTable = _SleVoipSipAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 1)
)
if mibBuilder.loadTexts:
    sleVoipSipAgentTable.setStatus("current")
_SleVoipSipAgentEntry_Object = MibTableRow
sleVoipSipAgentEntry = _SleVoipSipAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 1, 1)
)
sleVoipSipAgentEntry.setIndexNames(
    (0, "SLE-VOIP-MIB", "sleVoipSipAgentIndex"),
)
if mibBuilder.loadTexts:
    sleVoipSipAgentEntry.setStatus("current")


class _SleVoipSipAgentIndex_Type(Integer32):
    """Custom type sleVoipSipAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipSipAgentIndex_Type.__name__ = "Integer32"
_SleVoipSipAgentIndex_Object = MibTableColumn
sleVoipSipAgentIndex = _SleVoipSipAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 1, 1, 1),
    _SleVoipSipAgentIndex_Type()
)
sleVoipSipAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentIndex.setStatus("current")


class _SleVoipSipAgentServer_Type(OctetString):
    """Custom type sleVoipSipAgentServer based on OctetString"""
    defaultValue = OctetString("")


_SleVoipSipAgentServer_Type.__name__ = "OctetString"
_SleVoipSipAgentServer_Object = MibTableColumn
sleVoipSipAgentServer = _SleVoipSipAgentServer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 1, 1, 2),
    _SleVoipSipAgentServer_Type()
)
sleVoipSipAgentServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentServer.setStatus("current")


class _SleVoipSipAgentPort_Type(Integer32):
    """Custom type sleVoipSipAgentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleVoipSipAgentPort_Type.__name__ = "Integer32"
_SleVoipSipAgentPort_Object = MibTableColumn
sleVoipSipAgentPort = _SleVoipSipAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 1, 1, 3),
    _SleVoipSipAgentPort_Type()
)
sleVoipSipAgentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentPort.setStatus("current")


class _SleVoipSipAgentTypeOfService_Type(Integer32):
    """Custom type sleVoipSipAgentTypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleVoipSipAgentTypeOfService_Type.__name__ = "Integer32"
_SleVoipSipAgentTypeOfService_Object = MibTableColumn
sleVoipSipAgentTypeOfService = _SleVoipSipAgentTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 1, 1, 4),
    _SleVoipSipAgentTypeOfService_Type()
)
sleVoipSipAgentTypeOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentTypeOfService.setStatus("current")


class _SleVoipSipAgentTransport_Type(Integer32):
    """Custom type sleVoipSipAgentTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_SleVoipSipAgentTransport_Type.__name__ = "Integer32"
_SleVoipSipAgentTransport_Object = MibTableColumn
sleVoipSipAgentTransport = _SleVoipSipAgentTransport_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 1, 1, 5),
    _SleVoipSipAgentTransport_Type()
)
sleVoipSipAgentTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentTransport.setStatus("current")
_SleVoipSipAgentRegistrar_Type = OctetString
_SleVoipSipAgentRegistrar_Object = MibTableColumn
sleVoipSipAgentRegistrar = _SleVoipSipAgentRegistrar_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 1, 1, 6),
    _SleVoipSipAgentRegistrar_Type()
)
sleVoipSipAgentRegistrar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentRegistrar.setStatus("current")
_SleVoipSipAgentPrimary_Type = OctetString
_SleVoipSipAgentPrimary_Object = MibTableColumn
sleVoipSipAgentPrimary = _SleVoipSipAgentPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 1, 1, 7),
    _SleVoipSipAgentPrimary_Type()
)
sleVoipSipAgentPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentPrimary.setStatus("current")
_SleVoipSipAgentSecondary_Type = OctetString
_SleVoipSipAgentSecondary_Object = MibTableColumn
sleVoipSipAgentSecondary = _SleVoipSipAgentSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 1, 1, 8),
    _SleVoipSipAgentSecondary_Type()
)
sleVoipSipAgentSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentSecondary.setStatus("current")
_SleVoipSipAgentProfileName_Type = OctetString
_SleVoipSipAgentProfileName_Object = MibTableColumn
sleVoipSipAgentProfileName = _SleVoipSipAgentProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 1, 1, 9),
    _SleVoipSipAgentProfileName_Type()
)
sleVoipSipAgentProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentProfileName.setStatus("current")


class _SleVoipSipAgentExpireTimer_Type(Integer32):
    """Custom type sleVoipSipAgentExpireTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 360),
    )


_SleVoipSipAgentExpireTimer_Type.__name__ = "Integer32"
_SleVoipSipAgentExpireTimer_Object = MibTableColumn
sleVoipSipAgentExpireTimer = _SleVoipSipAgentExpireTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 1, 1, 10),
    _SleVoipSipAgentExpireTimer_Type()
)
sleVoipSipAgentExpireTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentExpireTimer.setStatus("current")
_SleVoipSipAgentControl_ObjectIdentity = ObjectIdentity
sleVoipSipAgentControl = _SleVoipSipAgentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2)
)


class _SleVoipSipAgentControlRequest_Type(Integer32):
    """Custom type sleVoipSipAgentControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableSipAgent", 1),
          ("disableSipAgent", 2))
    )


_SleVoipSipAgentControlRequest_Type.__name__ = "Integer32"
_SleVoipSipAgentControlRequest_Object = MibScalar
sleVoipSipAgentControlRequest = _SleVoipSipAgentControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 1),
    _SleVoipSipAgentControlRequest_Type()
)
sleVoipSipAgentControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlRequest.setStatus("current")
_SleVoipSipAgentControlStatus_Type = SleControlStatusType
_SleVoipSipAgentControlStatus_Object = MibScalar
sleVoipSipAgentControlStatus = _SleVoipSipAgentControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 2),
    _SleVoipSipAgentControlStatus_Type()
)
sleVoipSipAgentControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlStatus.setStatus("current")
_SleVoipSipAgentControlTimer_Type = Gauge32
_SleVoipSipAgentControlTimer_Object = MibScalar
sleVoipSipAgentControlTimer = _SleVoipSipAgentControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 3),
    _SleVoipSipAgentControlTimer_Type()
)
sleVoipSipAgentControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlTimer.setStatus("current")
_SleVoipSipAgentControlTimeStamp_Type = TimeTicks
_SleVoipSipAgentControlTimeStamp_Object = MibScalar
sleVoipSipAgentControlTimeStamp = _SleVoipSipAgentControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 4),
    _SleVoipSipAgentControlTimeStamp_Type()
)
sleVoipSipAgentControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlTimeStamp.setStatus("current")
_SleVoipSipAgentControlReqResult_Type = SleControlRequestResultType
_SleVoipSipAgentControlReqResult_Object = MibScalar
sleVoipSipAgentControlReqResult = _SleVoipSipAgentControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 5),
    _SleVoipSipAgentControlReqResult_Type()
)
sleVoipSipAgentControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlReqResult.setStatus("current")


class _SleVoipSipAgentControlIndex_Type(Integer32):
    """Custom type sleVoipSipAgentControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipSipAgentControlIndex_Type.__name__ = "Integer32"
_SleVoipSipAgentControlIndex_Object = MibScalar
sleVoipSipAgentControlIndex = _SleVoipSipAgentControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 6),
    _SleVoipSipAgentControlIndex_Type()
)
sleVoipSipAgentControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlIndex.setStatus("current")
_SleVoipSipAgentControlServer_Type = OctetString
_SleVoipSipAgentControlServer_Object = MibScalar
sleVoipSipAgentControlServer = _SleVoipSipAgentControlServer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 7),
    _SleVoipSipAgentControlServer_Type()
)
sleVoipSipAgentControlServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlServer.setStatus("current")
_SleVoipSipAgentControlPort_Type = Integer32
_SleVoipSipAgentControlPort_Object = MibScalar
sleVoipSipAgentControlPort = _SleVoipSipAgentControlPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 8),
    _SleVoipSipAgentControlPort_Type()
)
sleVoipSipAgentControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlPort.setStatus("current")


class _SleVoipSipAgentControlTypeOfService_Type(Integer32):
    """Custom type sleVoipSipAgentControlTypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleVoipSipAgentControlTypeOfService_Type.__name__ = "Integer32"
_SleVoipSipAgentControlTypeOfService_Object = MibScalar
sleVoipSipAgentControlTypeOfService = _SleVoipSipAgentControlTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 9),
    _SleVoipSipAgentControlTypeOfService_Type()
)
sleVoipSipAgentControlTypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlTypeOfService.setStatus("current")


class _SleVoipSipAgentControlTransport_Type(Integer32):
    """Custom type sleVoipSipAgentControlTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_SleVoipSipAgentControlTransport_Type.__name__ = "Integer32"
_SleVoipSipAgentControlTransport_Object = MibScalar
sleVoipSipAgentControlTransport = _SleVoipSipAgentControlTransport_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 10),
    _SleVoipSipAgentControlTransport_Type()
)
sleVoipSipAgentControlTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlTransport.setStatus("current")
_SleVoipSipAgentControlRegistrar_Type = OctetString
_SleVoipSipAgentControlRegistrar_Object = MibScalar
sleVoipSipAgentControlRegistrar = _SleVoipSipAgentControlRegistrar_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 11),
    _SleVoipSipAgentControlRegistrar_Type()
)
sleVoipSipAgentControlRegistrar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlRegistrar.setStatus("current")
_SleVoipSipAgentControlPrimary_Type = OctetString
_SleVoipSipAgentControlPrimary_Object = MibScalar
sleVoipSipAgentControlPrimary = _SleVoipSipAgentControlPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 12),
    _SleVoipSipAgentControlPrimary_Type()
)
sleVoipSipAgentControlPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlPrimary.setStatus("current")
_SleVoipSipAgentControlSecondary_Type = OctetString
_SleVoipSipAgentControlSecondary_Object = MibScalar
sleVoipSipAgentControlSecondary = _SleVoipSipAgentControlSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 13),
    _SleVoipSipAgentControlSecondary_Type()
)
sleVoipSipAgentControlSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlSecondary.setStatus("current")
_SleVoipSipAgentControlProfileName_Type = OctetString
_SleVoipSipAgentControlProfileName_Object = MibScalar
sleVoipSipAgentControlProfileName = _SleVoipSipAgentControlProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 14),
    _SleVoipSipAgentControlProfileName_Type()
)
sleVoipSipAgentControlProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlProfileName.setStatus("current")


class _SleVoipSipAgentControlExpireTimer_Type(Integer32):
    """Custom type sleVoipSipAgentControlExpireTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 360),
    )


_SleVoipSipAgentControlExpireTimer_Type.__name__ = "Integer32"
_SleVoipSipAgentControlExpireTimer_Object = MibScalar
sleVoipSipAgentControlExpireTimer = _SleVoipSipAgentControlExpireTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 2, 15),
    _SleVoipSipAgentControlExpireTimer_Type()
)
sleVoipSipAgentControlExpireTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipSipAgentControlExpireTimer.setStatus("current")
_SleVoipSipAgentNotification_ObjectIdentity = ObjectIdentity
sleVoipSipAgentNotification = _SleVoipSipAgentNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 3)
)
_SleVoipMgcpEndpoint_ObjectIdentity = ObjectIdentity
sleVoipMgcpEndpoint = _SleVoipMgcpEndpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5)
)
_SleVoipMgcpEndpointTable_Object = MibTable
sleVoipMgcpEndpointTable = _SleVoipMgcpEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 1)
)
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointTable.setStatus("current")
_SleVoipMgcpEndpointEntry_Object = MibTableRow
sleVoipMgcpEndpointEntry = _SleVoipMgcpEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 1, 1)
)
sleVoipMgcpEndpointEntry.setIndexNames(
    (0, "SLE-VOIP-MIB", "sleVoipMgcpEndpointIndex"),
)
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointEntry.setStatus("current")


class _SleVoipMgcpEndpointIndex_Type(Unsigned32):
    """Custom type sleVoipMgcpEndpointIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipMgcpEndpointIndex_Type.__name__ = "Unsigned32"
_SleVoipMgcpEndpointIndex_Object = MibTableColumn
sleVoipMgcpEndpointIndex = _SleVoipMgcpEndpointIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 1, 1, 1),
    _SleVoipMgcpEndpointIndex_Type()
)
sleVoipMgcpEndpointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointIndex.setStatus("current")


class _SleVoipMgcpEndpointAgent_Type(Integer32):
    """Custom type sleVoipMgcpEndpointAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipMgcpEndpointAgent_Type.__name__ = "Integer32"
_SleVoipMgcpEndpointAgent_Object = MibTableColumn
sleVoipMgcpEndpointAgent = _SleVoipMgcpEndpointAgent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 1, 1, 2),
    _SleVoipMgcpEndpointAgent_Type()
)
sleVoipMgcpEndpointAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointAgent.setStatus("current")
_SleVoipMgcpEndpointName_Type = OctetString
_SleVoipMgcpEndpointName_Object = MibTableColumn
sleVoipMgcpEndpointName = _SleVoipMgcpEndpointName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 1, 1, 3),
    _SleVoipMgcpEndpointName_Type()
)
sleVoipMgcpEndpointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointName.setStatus("current")
_SleVoipMgcpEndpointControl_ObjectIdentity = ObjectIdentity
sleVoipMgcpEndpointControl = _SleVoipMgcpEndpointControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 2)
)


class _SleVoipMgcpEndpointControlRequest_Type(Integer32):
    """Custom type sleVoipMgcpEndpointControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableMgcpEndpoint", 1),
          ("disableMgcpEndpoint", 2))
    )


_SleVoipMgcpEndpointControlRequest_Type.__name__ = "Integer32"
_SleVoipMgcpEndpointControlRequest_Object = MibScalar
sleVoipMgcpEndpointControlRequest = _SleVoipMgcpEndpointControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 2, 1),
    _SleVoipMgcpEndpointControlRequest_Type()
)
sleVoipMgcpEndpointControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointControlRequest.setStatus("current")
_SleVoipMgcpEndpointControlStatus_Type = SleControlStatusType
_SleVoipMgcpEndpointControlStatus_Object = MibScalar
sleVoipMgcpEndpointControlStatus = _SleVoipMgcpEndpointControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 2, 2),
    _SleVoipMgcpEndpointControlStatus_Type()
)
sleVoipMgcpEndpointControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointControlStatus.setStatus("current")
_SleVoipMgcpEndpointControlTimer_Type = Gauge32
_SleVoipMgcpEndpointControlTimer_Object = MibScalar
sleVoipMgcpEndpointControlTimer = _SleVoipMgcpEndpointControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 2, 3),
    _SleVoipMgcpEndpointControlTimer_Type()
)
sleVoipMgcpEndpointControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointControlTimer.setStatus("current")
_SleVoipMgcpEndpointControlTimeStamp_Type = TimeTicks
_SleVoipMgcpEndpointControlTimeStamp_Object = MibScalar
sleVoipMgcpEndpointControlTimeStamp = _SleVoipMgcpEndpointControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 2, 4),
    _SleVoipMgcpEndpointControlTimeStamp_Type()
)
sleVoipMgcpEndpointControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointControlTimeStamp.setStatus("current")
_SleVoipMgcpEndpointControlReqResult_Type = SleControlRequestResultType
_SleVoipMgcpEndpointControlReqResult_Object = MibScalar
sleVoipMgcpEndpointControlReqResult = _SleVoipMgcpEndpointControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 2, 5),
    _SleVoipMgcpEndpointControlReqResult_Type()
)
sleVoipMgcpEndpointControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointControlReqResult.setStatus("current")


class _SleVoipMgcpEndpointControlIndex_Type(Unsigned32):
    """Custom type sleVoipMgcpEndpointControlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipMgcpEndpointControlIndex_Type.__name__ = "Unsigned32"
_SleVoipMgcpEndpointControlIndex_Object = MibScalar
sleVoipMgcpEndpointControlIndex = _SleVoipMgcpEndpointControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 2, 6),
    _SleVoipMgcpEndpointControlIndex_Type()
)
sleVoipMgcpEndpointControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointControlIndex.setStatus("current")


class _SleVoipMgcpEndpointControlAgent_Type(Integer32):
    """Custom type sleVoipMgcpEndpointControlAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipMgcpEndpointControlAgent_Type.__name__ = "Integer32"
_SleVoipMgcpEndpointControlAgent_Object = MibScalar
sleVoipMgcpEndpointControlAgent = _SleVoipMgcpEndpointControlAgent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 2, 7),
    _SleVoipMgcpEndpointControlAgent_Type()
)
sleVoipMgcpEndpointControlAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointControlAgent.setStatus("current")
_SleVoipMgcpEndpointControlName_Type = OctetString
_SleVoipMgcpEndpointControlName_Object = MibScalar
sleVoipMgcpEndpointControlName = _SleVoipMgcpEndpointControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 2, 8),
    _SleVoipMgcpEndpointControlName_Type()
)
sleVoipMgcpEndpointControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointControlName.setStatus("current")
_SleVoipMgcpEndpointNotification_ObjectIdentity = ObjectIdentity
sleVoipMgcpEndpointNotification = _SleVoipMgcpEndpointNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 3)
)
_SleVoipMgcpAgent_ObjectIdentity = ObjectIdentity
sleVoipMgcpAgent = _SleVoipMgcpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6)
)
_SleVoipMgcpAgentTable_Object = MibTable
sleVoipMgcpAgentTable = _SleVoipMgcpAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 1)
)
if mibBuilder.loadTexts:
    sleVoipMgcpAgentTable.setStatus("current")
_SleVoipMgcpAgentEntry_Object = MibTableRow
sleVoipMgcpAgentEntry = _SleVoipMgcpAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 1, 1)
)
sleVoipMgcpAgentEntry.setIndexNames(
    (0, "SLE-VOIP-MIB", "sleVoipMgcpAgentIndex"),
)
if mibBuilder.loadTexts:
    sleVoipMgcpAgentEntry.setStatus("current")


class _SleVoipMgcpAgentIndex_Type(Integer32):
    """Custom type sleVoipMgcpAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipMgcpAgentIndex_Type.__name__ = "Integer32"
_SleVoipMgcpAgentIndex_Object = MibTableColumn
sleVoipMgcpAgentIndex = _SleVoipMgcpAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 1, 1, 1),
    _SleVoipMgcpAgentIndex_Type()
)
sleVoipMgcpAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentIndex.setStatus("current")
_SleVoipMgcpCallAgent_Type = IpAddress
_SleVoipMgcpCallAgent_Object = MibTableColumn
sleVoipMgcpCallAgent = _SleVoipMgcpCallAgent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 1, 1, 2),
    _SleVoipMgcpCallAgent_Type()
)
sleVoipMgcpCallAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpCallAgent.setStatus("current")


class _SleVoipMgcpCallAgentPort_Type(Integer32):
    """Custom type sleVoipMgcpCallAgentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleVoipMgcpCallAgentPort_Type.__name__ = "Integer32"
_SleVoipMgcpCallAgentPort_Object = MibTableColumn
sleVoipMgcpCallAgentPort = _SleVoipMgcpCallAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 1, 1, 3),
    _SleVoipMgcpCallAgentPort_Type()
)
sleVoipMgcpCallAgentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpCallAgentPort.setStatus("current")


class _SleVoipMgcpAgentPort_Type(Integer32):
    """Custom type sleVoipMgcpAgentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleVoipMgcpAgentPort_Type.__name__ = "Integer32"
_SleVoipMgcpAgentPort_Object = MibTableColumn
sleVoipMgcpAgentPort = _SleVoipMgcpAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 1, 1, 4),
    _SleVoipMgcpAgentPort_Type()
)
sleVoipMgcpAgentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentPort.setStatus("current")


class _SleVoipMgcpAgentTOS_Type(Integer32):
    """Custom type sleVoipMgcpAgentTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleVoipMgcpAgentTOS_Type.__name__ = "Integer32"
_SleVoipMgcpAgentTOS_Object = MibTableColumn
sleVoipMgcpAgentTOS = _SleVoipMgcpAgentTOS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 1, 1, 5),
    _SleVoipMgcpAgentTOS_Type()
)
sleVoipMgcpAgentTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentTOS.setStatus("current")


class _SleVoipMgcpAgentVendor_Type(Integer32):
    """Custom type sleVoipMgcpAgentVendor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dssw", 1),
          ("mssw", 2),
          ("g6sw", 3),
          ("cssw", 4))
    )


_SleVoipMgcpAgentVendor_Type.__name__ = "Integer32"
_SleVoipMgcpAgentVendor_Object = MibTableColumn
sleVoipMgcpAgentVendor = _SleVoipMgcpAgentVendor_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 1, 1, 6),
    _SleVoipMgcpAgentVendor_Type()
)
sleVoipMgcpAgentVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentVendor.setStatus("current")
_SleVoipMgcpAgentDNS_Type = OctetString
_SleVoipMgcpAgentDNS_Object = MibTableColumn
sleVoipMgcpAgentDNS = _SleVoipMgcpAgentDNS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 1, 1, 7),
    _SleVoipMgcpAgentDNS_Type()
)
sleVoipMgcpAgentDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentDNS.setStatus("current")
_SleVoipMgcpAgentProfileName_Type = OctetString
_SleVoipMgcpAgentProfileName_Object = MibTableColumn
sleVoipMgcpAgentProfileName = _SleVoipMgcpAgentProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 1, 1, 8),
    _SleVoipMgcpAgentProfileName_Type()
)
sleVoipMgcpAgentProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentProfileName.setStatus("current")
_SleVoipMgcpAgentControl_ObjectIdentity = ObjectIdentity
sleVoipMgcpAgentControl = _SleVoipMgcpAgentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2)
)


class _SleVoipMgcpAgentControlRequest_Type(Integer32):
    """Custom type sleVoipMgcpAgentControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableVoipMgcpAgent", 1),
          ("disableVoipMgcpAgent", 2))
    )


_SleVoipMgcpAgentControlRequest_Type.__name__ = "Integer32"
_SleVoipMgcpAgentControlRequest_Object = MibScalar
sleVoipMgcpAgentControlRequest = _SleVoipMgcpAgentControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 1),
    _SleVoipMgcpAgentControlRequest_Type()
)
sleVoipMgcpAgentControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlRequest.setStatus("current")
_SleVoipMgcpAgentControlStatus_Type = SleControlStatusType
_SleVoipMgcpAgentControlStatus_Object = MibScalar
sleVoipMgcpAgentControlStatus = _SleVoipMgcpAgentControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 2),
    _SleVoipMgcpAgentControlStatus_Type()
)
sleVoipMgcpAgentControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlStatus.setStatus("current")
_SleVoipMgcpAgentControlTimer_Type = Gauge32
_SleVoipMgcpAgentControlTimer_Object = MibScalar
sleVoipMgcpAgentControlTimer = _SleVoipMgcpAgentControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 3),
    _SleVoipMgcpAgentControlTimer_Type()
)
sleVoipMgcpAgentControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlTimer.setStatus("current")
_SleVoipMgcpAgentControlTimeStamp_Type = TimeTicks
_SleVoipMgcpAgentControlTimeStamp_Object = MibScalar
sleVoipMgcpAgentControlTimeStamp = _SleVoipMgcpAgentControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 4),
    _SleVoipMgcpAgentControlTimeStamp_Type()
)
sleVoipMgcpAgentControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlTimeStamp.setStatus("current")
_SleVoipMgcpAgentControlReqResult_Type = SleControlRequestResultType
_SleVoipMgcpAgentControlReqResult_Object = MibScalar
sleVoipMgcpAgentControlReqResult = _SleVoipMgcpAgentControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 5),
    _SleVoipMgcpAgentControlReqResult_Type()
)
sleVoipMgcpAgentControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlReqResult.setStatus("current")


class _SleVoipMgcpAgentControlIndex_Type(Integer32):
    """Custom type sleVoipMgcpAgentControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipMgcpAgentControlIndex_Type.__name__ = "Integer32"
_SleVoipMgcpAgentControlIndex_Object = MibScalar
sleVoipMgcpAgentControlIndex = _SleVoipMgcpAgentControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 6),
    _SleVoipMgcpAgentControlIndex_Type()
)
sleVoipMgcpAgentControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlIndex.setStatus("current")
_SleVoipMgcpAgentControlCallAgent_Type = OctetString
_SleVoipMgcpAgentControlCallAgent_Object = MibScalar
sleVoipMgcpAgentControlCallAgent = _SleVoipMgcpAgentControlCallAgent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 7),
    _SleVoipMgcpAgentControlCallAgent_Type()
)
sleVoipMgcpAgentControlCallAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlCallAgent.setStatus("current")


class _SleVoipMgcpAgentControlCallAgentPort_Type(Integer32):
    """Custom type sleVoipMgcpAgentControlCallAgentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleVoipMgcpAgentControlCallAgentPort_Type.__name__ = "Integer32"
_SleVoipMgcpAgentControlCallAgentPort_Object = MibScalar
sleVoipMgcpAgentControlCallAgentPort = _SleVoipMgcpAgentControlCallAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 8),
    _SleVoipMgcpAgentControlCallAgentPort_Type()
)
sleVoipMgcpAgentControlCallAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlCallAgentPort.setStatus("current")


class _SleVoipMgcpAgentControlPort_Type(Integer32):
    """Custom type sleVoipMgcpAgentControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleVoipMgcpAgentControlPort_Type.__name__ = "Integer32"
_SleVoipMgcpAgentControlPort_Object = MibScalar
sleVoipMgcpAgentControlPort = _SleVoipMgcpAgentControlPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 9),
    _SleVoipMgcpAgentControlPort_Type()
)
sleVoipMgcpAgentControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlPort.setStatus("current")


class _SleVoipMgcpAgentControlTOS_Type(Integer32):
    """Custom type sleVoipMgcpAgentControlTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleVoipMgcpAgentControlTOS_Type.__name__ = "Integer32"
_SleVoipMgcpAgentControlTOS_Object = MibScalar
sleVoipMgcpAgentControlTOS = _SleVoipMgcpAgentControlTOS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 10),
    _SleVoipMgcpAgentControlTOS_Type()
)
sleVoipMgcpAgentControlTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlTOS.setStatus("current")


class _SleVoipMgcpAgentControlVendor_Type(Integer32):
    """Custom type sleVoipMgcpAgentControlVendor based on Integer32"""
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
        *(("dssw", 1),
          ("mssw", 2),
          ("g6sw", 3),
          ("cssw", 4))
    )


_SleVoipMgcpAgentControlVendor_Type.__name__ = "Integer32"
_SleVoipMgcpAgentControlVendor_Object = MibScalar
sleVoipMgcpAgentControlVendor = _SleVoipMgcpAgentControlVendor_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 11),
    _SleVoipMgcpAgentControlVendor_Type()
)
sleVoipMgcpAgentControlVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlVendor.setStatus("current")
_SleVoipMgcpAgentControlDNS_Type = OctetString
_SleVoipMgcpAgentControlDNS_Object = MibScalar
sleVoipMgcpAgentControlDNS = _SleVoipMgcpAgentControlDNS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 12),
    _SleVoipMgcpAgentControlDNS_Type()
)
sleVoipMgcpAgentControlDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlDNS.setStatus("current")
_SleVoipMgcpAgentControlProfileName_Type = OctetString
_SleVoipMgcpAgentControlProfileName_Object = MibScalar
sleVoipMgcpAgentControlProfileName = _SleVoipMgcpAgentControlProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 2, 13),
    _SleVoipMgcpAgentControlProfileName_Type()
)
sleVoipMgcpAgentControlProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMgcpAgentControlProfileName.setStatus("current")
_SleVoipMgcpAgentNotification_ObjectIdentity = ObjectIdentity
sleVoipMgcpAgentNotification = _SleVoipMgcpAgentNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 3)
)
_SleVoipPots_ObjectIdentity = ObjectIdentity
sleVoipPots = _SleVoipPots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 7)
)
_SleVoipPotsStatusTable_Object = MibTable
sleVoipPotsStatusTable = _SleVoipPotsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 7, 1)
)
if mibBuilder.loadTexts:
    sleVoipPotsStatusTable.setStatus("current")
_SleVoipPotsStatusEntry_Object = MibTableRow
sleVoipPotsStatusEntry = _SleVoipPotsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 7, 1, 1)
)
sleVoipPotsStatusEntry.setIndexNames(
    (0, "SLE-VOIP-MIB", "sleVoipSipAgentIndex"),
)
if mibBuilder.loadTexts:
    sleVoipPotsStatusEntry.setStatus("current")


class _SleVoipPotsStatusIndex_Type(Unsigned32):
    """Custom type sleVoipPotsStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipPotsStatusIndex_Type.__name__ = "Unsigned32"
_SleVoipPotsStatusIndex_Object = MibTableColumn
sleVoipPotsStatusIndex = _SleVoipPotsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 7, 1, 1, 1),
    _SleVoipPotsStatusIndex_Type()
)
sleVoipPotsStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipPotsStatusIndex.setStatus("current")


class _SleVoipPotsStatus_Type(Integer32):
    """Custom type sleVoipPotsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("twoway", 1),
          ("threeway", 2),
          ("fax", 3))
    )


_SleVoipPotsStatus_Type.__name__ = "Integer32"
_SleVoipPotsStatus_Object = MibTableColumn
sleVoipPotsStatus = _SleVoipPotsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 7, 1, 1, 2),
    _SleVoipPotsStatus_Type()
)
sleVoipPotsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipPotsStatus.setStatus("current")


class _SleVoipPotsStatusHookState_Type(Integer32):
    """Custom type sleVoipPotsStatusHookState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_SleVoipPotsStatusHookState_Type.__name__ = "Integer32"
_SleVoipPotsStatusHookState_Object = MibTableColumn
sleVoipPotsStatusHookState = _SleVoipPotsStatusHookState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 7, 1, 1, 3),
    _SleVoipPotsStatusHookState_Type()
)
sleVoipPotsStatusHookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipPotsStatusHookState.setStatus("current")


class _SleVoipPotsStatusRegisterState_Type(Integer32):
    """Custom type sleVoipPotsStatusRegisterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("out", 0),
          ("in", 1))
    )


_SleVoipPotsStatusRegisterState_Type.__name__ = "Integer32"
_SleVoipPotsStatusRegisterState_Object = MibTableColumn
sleVoipPotsStatusRegisterState = _SleVoipPotsStatusRegisterState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 7, 1, 1, 4),
    _SleVoipPotsStatusRegisterState_Type()
)
sleVoipPotsStatusRegisterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipPotsStatusRegisterState.setStatus("current")
_SleVoipMediaProfile_ObjectIdentity = ObjectIdentity
sleVoipMediaProfile = _SleVoipMediaProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8)
)
_SleVoipMediaProfileTable_Object = MibTable
sleVoipMediaProfileTable = _SleVoipMediaProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 1)
)
if mibBuilder.loadTexts:
    sleVoipMediaProfileTable.setStatus("current")
_SleVoipMediaProfileEntry_Object = MibTableRow
sleVoipMediaProfileEntry = _SleVoipMediaProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 1, 1)
)
sleVoipMediaProfileEntry.setIndexNames(
    (0, "SLE-VOIP-MIB", "sleVoipMediaProfileIndex"),
)
if mibBuilder.loadTexts:
    sleVoipMediaProfileEntry.setStatus("current")


class _SleVoipMediaProfileIndex_Type(Integer32):
    """Custom type sleVoipMediaProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipMediaProfileIndex_Type.__name__ = "Integer32"
_SleVoipMediaProfileIndex_Object = MibTableColumn
sleVoipMediaProfileIndex = _SleVoipMediaProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 1, 1, 1),
    _SleVoipMediaProfileIndex_Type()
)
sleVoipMediaProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMediaProfileIndex.setStatus("current")


class _SleVoipMediaProfileCodecSelection_Type(Integer32):
    """Custom type sleVoipMediaProfileCodecSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              8,
              18)
        )
    )
    namedValues = NamedValues(
        *(("pcmu", 0),
          ("g723", 4),
          ("pcma", 8),
          ("g729", 18))
    )


_SleVoipMediaProfileCodecSelection_Type.__name__ = "Integer32"
_SleVoipMediaProfileCodecSelection_Object = MibTableColumn
sleVoipMediaProfileCodecSelection = _SleVoipMediaProfileCodecSelection_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 1, 1, 2),
    _SleVoipMediaProfileCodecSelection_Type()
)
sleVoipMediaProfileCodecSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMediaProfileCodecSelection.setStatus("current")


class _SleVoipMediaProfilePacketPeriod_Type(Integer32):
    """Custom type sleVoipMediaProfilePacketPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_SleVoipMediaProfilePacketPeriod_Type.__name__ = "Integer32"
_SleVoipMediaProfilePacketPeriod_Object = MibTableColumn
sleVoipMediaProfilePacketPeriod = _SleVoipMediaProfilePacketPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 1, 1, 3),
    _SleVoipMediaProfilePacketPeriod_Type()
)
sleVoipMediaProfilePacketPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMediaProfilePacketPeriod.setStatus("current")


class _SleVoipMediaProfileSilenceSuppression_Type(Integer32):
    """Custom type sleVoipMediaProfileSilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleVoipMediaProfileSilenceSuppression_Type.__name__ = "Integer32"
_SleVoipMediaProfileSilenceSuppression_Object = MibTableColumn
sleVoipMediaProfileSilenceSuppression = _SleVoipMediaProfileSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 1, 1, 4),
    _SleVoipMediaProfileSilenceSuppression_Type()
)
sleVoipMediaProfileSilenceSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMediaProfileSilenceSuppression.setStatus("current")
_SleVoipMediaProfileControl_ObjectIdentity = ObjectIdentity
sleVoipMediaProfileControl = _SleVoipMediaProfileControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 2)
)


class _SleVoipMediaProfileControlRequest_Type(Integer32):
    """Custom type sleVoipMediaProfileControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableVoipMediaProfile", 1),
          ("disableVoipMediaProfile", 2))
    )


_SleVoipMediaProfileControlRequest_Type.__name__ = "Integer32"
_SleVoipMediaProfileControlRequest_Object = MibScalar
sleVoipMediaProfileControlRequest = _SleVoipMediaProfileControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 2, 1),
    _SleVoipMediaProfileControlRequest_Type()
)
sleVoipMediaProfileControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMediaProfileControlRequest.setStatus("current")
_SleVoipMediaProfileControlStatus_Type = SleControlStatusType
_SleVoipMediaProfileControlStatus_Object = MibScalar
sleVoipMediaProfileControlStatus = _SleVoipMediaProfileControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 2, 2),
    _SleVoipMediaProfileControlStatus_Type()
)
sleVoipMediaProfileControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMediaProfileControlStatus.setStatus("current")
_SleVoipMediaProfileControlTimer_Type = Gauge32
_SleVoipMediaProfileControlTimer_Object = MibScalar
sleVoipMediaProfileControlTimer = _SleVoipMediaProfileControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 2, 3),
    _SleVoipMediaProfileControlTimer_Type()
)
sleVoipMediaProfileControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMediaProfileControlTimer.setStatus("current")
_SleVoipMediaProfileControlTimeStamp_Type = TimeTicks
_SleVoipMediaProfileControlTimeStamp_Object = MibScalar
sleVoipMediaProfileControlTimeStamp = _SleVoipMediaProfileControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 2, 4),
    _SleVoipMediaProfileControlTimeStamp_Type()
)
sleVoipMediaProfileControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMediaProfileControlTimeStamp.setStatus("current")
_SleVoipMediaProfileControlReqResult_Type = SleControlRequestResultType
_SleVoipMediaProfileControlReqResult_Object = MibScalar
sleVoipMediaProfileControlReqResult = _SleVoipMediaProfileControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 2, 5),
    _SleVoipMediaProfileControlReqResult_Type()
)
sleVoipMediaProfileControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipMediaProfileControlReqResult.setStatus("current")


class _SleVoipMediaProfileControlIndex_Type(Integer32):
    """Custom type sleVoipMediaProfileControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipMediaProfileControlIndex_Type.__name__ = "Integer32"
_SleVoipMediaProfileControlIndex_Object = MibScalar
sleVoipMediaProfileControlIndex = _SleVoipMediaProfileControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 2, 6),
    _SleVoipMediaProfileControlIndex_Type()
)
sleVoipMediaProfileControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMediaProfileControlIndex.setStatus("current")


class _SleVoipMediaProfileControlCodecSelection_Type(Integer32):
    """Custom type sleVoipMediaProfileControlCodecSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              8,
              18)
        )
    )
    namedValues = NamedValues(
        *(("pcmu", 0),
          ("g723", 4),
          ("pcma", 8),
          ("g729", 18))
    )


_SleVoipMediaProfileControlCodecSelection_Type.__name__ = "Integer32"
_SleVoipMediaProfileControlCodecSelection_Object = MibScalar
sleVoipMediaProfileControlCodecSelection = _SleVoipMediaProfileControlCodecSelection_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 2, 7),
    _SleVoipMediaProfileControlCodecSelection_Type()
)
sleVoipMediaProfileControlCodecSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMediaProfileControlCodecSelection.setStatus("current")


class _SleVoipMediaProfileControlPacketPeriod_Type(Integer32):
    """Custom type sleVoipMediaProfileControlPacketPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_SleVoipMediaProfileControlPacketPeriod_Type.__name__ = "Integer32"
_SleVoipMediaProfileControlPacketPeriod_Object = MibScalar
sleVoipMediaProfileControlPacketPeriod = _SleVoipMediaProfileControlPacketPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 2, 8),
    _SleVoipMediaProfileControlPacketPeriod_Type()
)
sleVoipMediaProfileControlPacketPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMediaProfileControlPacketPeriod.setStatus("current")


class _SleVoipMediaProfileControlSilenceSuppression_Type(Integer32):
    """Custom type sleVoipMediaProfileControlSilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleVoipMediaProfileControlSilenceSuppression_Type.__name__ = "Integer32"
_SleVoipMediaProfileControlSilenceSuppression_Object = MibScalar
sleVoipMediaProfileControlSilenceSuppression = _SleVoipMediaProfileControlSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 2, 9),
    _SleVoipMediaProfileControlSilenceSuppression_Type()
)
sleVoipMediaProfileControlSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipMediaProfileControlSilenceSuppression.setStatus("current")
_SleVoipMediaProfileNotification_ObjectIdentity = ObjectIdentity
sleVoipMediaProfileNotification = _SleVoipMediaProfileNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 3)
)
_SleVoipRtpProfile_ObjectIdentity = ObjectIdentity
sleVoipRtpProfile = _SleVoipRtpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9)
)
_SleVoipRtpProfileInfo_ObjectIdentity = ObjectIdentity
sleVoipRtpProfileInfo = _SleVoipRtpProfileInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 1)
)


class _SleVoipRtpProfilePortMin_Type(Integer32):
    """Custom type sleVoipRtpProfilePortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 60000),
    )


_SleVoipRtpProfilePortMin_Type.__name__ = "Integer32"
_SleVoipRtpProfilePortMin_Object = MibScalar
sleVoipRtpProfilePortMin = _SleVoipRtpProfilePortMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 1, 1),
    _SleVoipRtpProfilePortMin_Type()
)
sleVoipRtpProfilePortMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipRtpProfilePortMin.setStatus("current")


class _SleVoipRtpProfileDscpMark_Type(Integer32):
    """Custom type sleVoipRtpProfileDscpMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleVoipRtpProfileDscpMark_Type.__name__ = "Integer32"
_SleVoipRtpProfileDscpMark_Object = MibScalar
sleVoipRtpProfileDscpMark = _SleVoipRtpProfileDscpMark_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 1, 2),
    _SleVoipRtpProfileDscpMark_Type()
)
sleVoipRtpProfileDscpMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipRtpProfileDscpMark.setStatus("current")


class _SleVoipRtpProfileOob_Type(Integer32):
    """Custom type sleVoipRtpProfileOob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleVoipRtpProfileOob_Type.__name__ = "Integer32"
_SleVoipRtpProfileOob_Object = MibScalar
sleVoipRtpProfileOob = _SleVoipRtpProfileOob_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 1, 3),
    _SleVoipRtpProfileOob_Type()
)
sleVoipRtpProfileOob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipRtpProfileOob.setStatus("current")


class _SleVoipRtpProfileDtmfEvent_Type(Integer32):
    """Custom type sleVoipRtpProfileDtmfEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleVoipRtpProfileDtmfEvent_Type.__name__ = "Integer32"
_SleVoipRtpProfileDtmfEvent_Object = MibScalar
sleVoipRtpProfileDtmfEvent = _SleVoipRtpProfileDtmfEvent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 1, 4),
    _SleVoipRtpProfileDtmfEvent_Type()
)
sleVoipRtpProfileDtmfEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipRtpProfileDtmfEvent.setStatus("current")
_SleVoipRtpProfileControl_ObjectIdentity = ObjectIdentity
sleVoipRtpProfileControl = _SleVoipRtpProfileControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 2)
)


class _SleVoipRtpProfileControlRequest_Type(Integer32):
    """Custom type sleVoipRtpProfileControlRequest based on Integer32"""
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
        *(("setVoipRtpPortMin", 1),
          ("setVoipRtpDscp", 2),
          ("setVoipRtpOob", 3),
          ("setVoipRtpDtmf", 4))
    )


_SleVoipRtpProfileControlRequest_Type.__name__ = "Integer32"
_SleVoipRtpProfileControlRequest_Object = MibScalar
sleVoipRtpProfileControlRequest = _SleVoipRtpProfileControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 2, 1),
    _SleVoipRtpProfileControlRequest_Type()
)
sleVoipRtpProfileControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipRtpProfileControlRequest.setStatus("current")
_SleVoipRtpProfileControlStatus_Type = SleControlStatusType
_SleVoipRtpProfileControlStatus_Object = MibScalar
sleVoipRtpProfileControlStatus = _SleVoipRtpProfileControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 2, 2),
    _SleVoipRtpProfileControlStatus_Type()
)
sleVoipRtpProfileControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipRtpProfileControlStatus.setStatus("current")
_SleVoipRtpProfileControlTimer_Type = Gauge32
_SleVoipRtpProfileControlTimer_Object = MibScalar
sleVoipRtpProfileControlTimer = _SleVoipRtpProfileControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 2, 3),
    _SleVoipRtpProfileControlTimer_Type()
)
sleVoipRtpProfileControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipRtpProfileControlTimer.setStatus("current")
_SleVoipRtpProfileControlTimeStamp_Type = TimeTicks
_SleVoipRtpProfileControlTimeStamp_Object = MibScalar
sleVoipRtpProfileControlTimeStamp = _SleVoipRtpProfileControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 2, 4),
    _SleVoipRtpProfileControlTimeStamp_Type()
)
sleVoipRtpProfileControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipRtpProfileControlTimeStamp.setStatus("current")
_SleVoipRtpProfileControlReqResult_Type = SleControlRequestResultType
_SleVoipRtpProfileControlReqResult_Object = MibScalar
sleVoipRtpProfileControlReqResult = _SleVoipRtpProfileControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 2, 5),
    _SleVoipRtpProfileControlReqResult_Type()
)
sleVoipRtpProfileControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipRtpProfileControlReqResult.setStatus("current")


class _SleVoipRtpProfileControlPortMin_Type(Integer32):
    """Custom type sleVoipRtpProfileControlPortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 60000),
    )


_SleVoipRtpProfileControlPortMin_Type.__name__ = "Integer32"
_SleVoipRtpProfileControlPortMin_Object = MibScalar
sleVoipRtpProfileControlPortMin = _SleVoipRtpProfileControlPortMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 2, 6),
    _SleVoipRtpProfileControlPortMin_Type()
)
sleVoipRtpProfileControlPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipRtpProfileControlPortMin.setStatus("current")


class _SleVoipRtpProfileControlDscpMark_Type(Integer32):
    """Custom type sleVoipRtpProfileControlDscpMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SleVoipRtpProfileControlDscpMark_Type.__name__ = "Integer32"
_SleVoipRtpProfileControlDscpMark_Object = MibScalar
sleVoipRtpProfileControlDscpMark = _SleVoipRtpProfileControlDscpMark_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 2, 7),
    _SleVoipRtpProfileControlDscpMark_Type()
)
sleVoipRtpProfileControlDscpMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipRtpProfileControlDscpMark.setStatus("current")


class _SleVoipRtpProfileControlOob_Type(Integer32):
    """Custom type sleVoipRtpProfileControlOob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleVoipRtpProfileControlOob_Type.__name__ = "Integer32"
_SleVoipRtpProfileControlOob_Object = MibScalar
sleVoipRtpProfileControlOob = _SleVoipRtpProfileControlOob_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 2, 8),
    _SleVoipRtpProfileControlOob_Type()
)
sleVoipRtpProfileControlOob.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipRtpProfileControlOob.setStatus("current")


class _SleVoipRtpProfileControlDtmfEvent_Type(Integer32):
    """Custom type sleVoipRtpProfileControlDtmfEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SleVoipRtpProfileControlDtmfEvent_Type.__name__ = "Integer32"
_SleVoipRtpProfileControlDtmfEvent_Object = MibScalar
sleVoipRtpProfileControlDtmfEvent = _SleVoipRtpProfileControlDtmfEvent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 2, 9),
    _SleVoipRtpProfileControlDtmfEvent_Type()
)
sleVoipRtpProfileControlDtmfEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipRtpProfileControlDtmfEvent.setStatus("current")
_SleVoipRtpProfileNotification_ObjectIdentity = ObjectIdentity
sleVoipRtpProfileNotification = _SleVoipRtpProfileNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 3)
)
_SleVoipTimer_ObjectIdentity = ObjectIdentity
sleVoipTimer = _SleVoipTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10)
)
_SleVoipTimerTable_Object = MibTable
sleVoipTimerTable = _SleVoipTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 1)
)
if mibBuilder.loadTexts:
    sleVoipTimerTable.setStatus("current")
_SleVoipTimerEntry_Object = MibTableRow
sleVoipTimerEntry = _SleVoipTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 1, 1)
)
sleVoipTimerEntry.setIndexNames(
    (0, "SLE-VOIP-MIB", "sleVoipTimerIndex"),
)
if mibBuilder.loadTexts:
    sleVoipTimerEntry.setStatus("current")


class _SleVoipTimerIndex_Type(Integer32):
    """Custom type sleVoipTimerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipTimerIndex_Type.__name__ = "Integer32"
_SleVoipTimerIndex_Object = MibTableColumn
sleVoipTimerIndex = _SleVoipTimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 1, 1, 1),
    _SleVoipTimerIndex_Type()
)
sleVoipTimerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipTimerIndex.setStatus("current")


class _SleVoipTimerCriticalTimeout_Type(Integer32):
    """Custom type sleVoipTimerCriticalTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_SleVoipTimerCriticalTimeout_Type.__name__ = "Integer32"
_SleVoipTimerCriticalTimeout_Object = MibTableColumn
sleVoipTimerCriticalTimeout = _SleVoipTimerCriticalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 1, 1, 2),
    _SleVoipTimerCriticalTimeout_Type()
)
sleVoipTimerCriticalTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipTimerCriticalTimeout.setStatus("current")


class _SleVoipTimerFirstDigit_Type(Integer32):
    """Custom type sleVoipTimerFirstDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 30000),
    )


_SleVoipTimerFirstDigit_Type.__name__ = "Integer32"
_SleVoipTimerFirstDigit_Object = MibTableColumn
sleVoipTimerFirstDigit = _SleVoipTimerFirstDigit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 1, 1, 3),
    _SleVoipTimerFirstDigit_Type()
)
sleVoipTimerFirstDigit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipTimerFirstDigit.setStatus("current")


class _SleVoipTimerIntraDigit_Type(Integer32):
    """Custom type sleVoipTimerIntraDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 15000),
    )


_SleVoipTimerIntraDigit_Type.__name__ = "Integer32"
_SleVoipTimerIntraDigit_Object = MibTableColumn
sleVoipTimerIntraDigit = _SleVoipTimerIntraDigit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 1, 1, 4),
    _SleVoipTimerIntraDigit_Type()
)
sleVoipTimerIntraDigit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipTimerIntraDigit.setStatus("current")
_SleVoipTimerControl_ObjectIdentity = ObjectIdentity
sleVoipTimerControl = _SleVoipTimerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 2)
)


class _SleVoipTimerControlRequest_Type(Integer32):
    """Custom type sleVoipTimerControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableVoipTimer", 1),
          ("disableVoipTimer", 2))
    )


_SleVoipTimerControlRequest_Type.__name__ = "Integer32"
_SleVoipTimerControlRequest_Object = MibScalar
sleVoipTimerControlRequest = _SleVoipTimerControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 2, 1),
    _SleVoipTimerControlRequest_Type()
)
sleVoipTimerControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipTimerControlRequest.setStatus("current")
_SleVoipTimerControlStatus_Type = SleControlStatusType
_SleVoipTimerControlStatus_Object = MibScalar
sleVoipTimerControlStatus = _SleVoipTimerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 2, 2),
    _SleVoipTimerControlStatus_Type()
)
sleVoipTimerControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipTimerControlStatus.setStatus("current")
_SleVoipTimerControlTimer_Type = Gauge32
_SleVoipTimerControlTimer_Object = MibScalar
sleVoipTimerControlTimer = _SleVoipTimerControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 2, 3),
    _SleVoipTimerControlTimer_Type()
)
sleVoipTimerControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipTimerControlTimer.setStatus("current")
_SleVoipTimerControlTimeStamp_Type = TimeTicks
_SleVoipTimerControlTimeStamp_Object = MibScalar
sleVoipTimerControlTimeStamp = _SleVoipTimerControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 2, 4),
    _SleVoipTimerControlTimeStamp_Type()
)
sleVoipTimerControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipTimerControlTimeStamp.setStatus("current")
_SleVoipTimerControlReqResult_Type = SleControlRequestResultType
_SleVoipTimerControlReqResult_Object = MibScalar
sleVoipTimerControlReqResult = _SleVoipTimerControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 2, 5),
    _SleVoipTimerControlReqResult_Type()
)
sleVoipTimerControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipTimerControlReqResult.setStatus("current")


class _SleVoipTimerControlIndex_Type(Integer32):
    """Custom type sleVoipTimerControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipTimerControlIndex_Type.__name__ = "Integer32"
_SleVoipTimerControlIndex_Object = MibScalar
sleVoipTimerControlIndex = _SleVoipTimerControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 2, 6),
    _SleVoipTimerControlIndex_Type()
)
sleVoipTimerControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipTimerControlIndex.setStatus("current")


class _SleVoipTimerControlCriticalTimeout_Type(Integer32):
    """Custom type sleVoipTimerControlCriticalTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_SleVoipTimerControlCriticalTimeout_Type.__name__ = "Integer32"
_SleVoipTimerControlCriticalTimeout_Object = MibScalar
sleVoipTimerControlCriticalTimeout = _SleVoipTimerControlCriticalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 2, 7),
    _SleVoipTimerControlCriticalTimeout_Type()
)
sleVoipTimerControlCriticalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipTimerControlCriticalTimeout.setStatus("current")


class _SleVoipTimerControlFirstDigit_Type(Integer32):
    """Custom type sleVoipTimerControlFirstDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 30000),
    )


_SleVoipTimerControlFirstDigit_Type.__name__ = "Integer32"
_SleVoipTimerControlFirstDigit_Object = MibScalar
sleVoipTimerControlFirstDigit = _SleVoipTimerControlFirstDigit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 2, 8),
    _SleVoipTimerControlFirstDigit_Type()
)
sleVoipTimerControlFirstDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipTimerControlFirstDigit.setStatus("current")


class _SleVoipTimerControlIntraDigit_Type(Integer32):
    """Custom type sleVoipTimerControlIntraDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 15000),
    )


_SleVoipTimerControlIntraDigit_Type.__name__ = "Integer32"
_SleVoipTimerControlIntraDigit_Object = MibScalar
sleVoipTimerControlIntraDigit = _SleVoipTimerControlIntraDigit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 2, 9),
    _SleVoipTimerControlIntraDigit_Type()
)
sleVoipTimerControlIntraDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipTimerControlIntraDigit.setStatus("current")
_SleVoipTimerNotification_ObjectIdentity = ObjectIdentity
sleVoipTimerNotification = _SleVoipTimerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 3)
)
_SleVoipDialPlan_ObjectIdentity = ObjectIdentity
sleVoipDialPlan = _SleVoipDialPlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11)
)
_SleVoipDialPlanTable_Object = MibTable
sleVoipDialPlanTable = _SleVoipDialPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 1)
)
if mibBuilder.loadTexts:
    sleVoipDialPlanTable.setStatus("current")
_SleVoipDialPlanEntry_Object = MibTableRow
sleVoipDialPlanEntry = _SleVoipDialPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 1, 1)
)
sleVoipDialPlanEntry.setIndexNames(
    (0, "SLE-VOIP-MIB", "sleVoipDialPlanIndex"),
)
if mibBuilder.loadTexts:
    sleVoipDialPlanEntry.setStatus("current")


class _SleVoipDialPlanPotStatusIndex_Type(Integer32):
    """Custom type sleVoipDialPlanPotStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipDialPlanPotStatusIndex_Type.__name__ = "Integer32"
_SleVoipDialPlanPotStatusIndex_Object = MibTableColumn
sleVoipDialPlanPotStatusIndex = _SleVoipDialPlanPotStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 1, 1, 1),
    _SleVoipDialPlanPotStatusIndex_Type()
)
sleVoipDialPlanPotStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipDialPlanPotStatusIndex.setStatus("current")


class _SleVoipDialPlanIndex_Type(Integer32):
    """Custom type sleVoipDialPlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SleVoipDialPlanIndex_Type.__name__ = "Integer32"
_SleVoipDialPlanIndex_Object = MibTableColumn
sleVoipDialPlanIndex = _SleVoipDialPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 1, 1, 2),
    _SleVoipDialPlanIndex_Type()
)
sleVoipDialPlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipDialPlanIndex.setStatus("current")
_SleVoipDialPlanDigitMap_Type = OctetString
_SleVoipDialPlanDigitMap_Object = MibTableColumn
sleVoipDialPlanDigitMap = _SleVoipDialPlanDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 1, 1, 3),
    _SleVoipDialPlanDigitMap_Type()
)
sleVoipDialPlanDigitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipDialPlanDigitMap.setStatus("current")
_SleVoipDialPlanControl_ObjectIdentity = ObjectIdentity
sleVoipDialPlanControl = _SleVoipDialPlanControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 2)
)


class _SleVoipDialPlanControlRequest_Type(Integer32):
    """Custom type sleVoipDialPlanControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableVoipDialPlan", 1),
          ("disableVoipDialPlan", 2))
    )


_SleVoipDialPlanControlRequest_Type.__name__ = "Integer32"
_SleVoipDialPlanControlRequest_Object = MibScalar
sleVoipDialPlanControlRequest = _SleVoipDialPlanControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 2, 1),
    _SleVoipDialPlanControlRequest_Type()
)
sleVoipDialPlanControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipDialPlanControlRequest.setStatus("current")
_SleVoipDialPlanControlStatus_Type = SleControlStatusType
_SleVoipDialPlanControlStatus_Object = MibScalar
sleVoipDialPlanControlStatus = _SleVoipDialPlanControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 2, 2),
    _SleVoipDialPlanControlStatus_Type()
)
sleVoipDialPlanControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipDialPlanControlStatus.setStatus("current")
_SleVoipDialPlanControlTimer_Type = Gauge32
_SleVoipDialPlanControlTimer_Object = MibScalar
sleVoipDialPlanControlTimer = _SleVoipDialPlanControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 2, 3),
    _SleVoipDialPlanControlTimer_Type()
)
sleVoipDialPlanControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipDialPlanControlTimer.setStatus("current")
_SleVoipDialPlanControlTimeStamp_Type = TimeTicks
_SleVoipDialPlanControlTimeStamp_Object = MibScalar
sleVoipDialPlanControlTimeStamp = _SleVoipDialPlanControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 2, 4),
    _SleVoipDialPlanControlTimeStamp_Type()
)
sleVoipDialPlanControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipDialPlanControlTimeStamp.setStatus("current")
_SleVoipDialPlanControlReqResult_Type = SleControlRequestResultType
_SleVoipDialPlanControlReqResult_Object = MibScalar
sleVoipDialPlanControlReqResult = _SleVoipDialPlanControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 2, 5),
    _SleVoipDialPlanControlReqResult_Type()
)
sleVoipDialPlanControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipDialPlanControlReqResult.setStatus("current")


class _SleVoipDialPlanControlPotStatusIndex_Type(Integer32):
    """Custom type sleVoipDialPlanControlPotStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipDialPlanControlPotStatusIndex_Type.__name__ = "Integer32"
_SleVoipDialPlanControlPotStatusIndex_Object = MibScalar
sleVoipDialPlanControlPotStatusIndex = _SleVoipDialPlanControlPotStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 2, 6),
    _SleVoipDialPlanControlPotStatusIndex_Type()
)
sleVoipDialPlanControlPotStatusIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipDialPlanControlPotStatusIndex.setStatus("current")


class _SleVoipDialPlanControlIndex_Type(Integer32):
    """Custom type sleVoipDialPlanControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SleVoipDialPlanControlIndex_Type.__name__ = "Integer32"
_SleVoipDialPlanControlIndex_Object = MibScalar
sleVoipDialPlanControlIndex = _SleVoipDialPlanControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 2, 7),
    _SleVoipDialPlanControlIndex_Type()
)
sleVoipDialPlanControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipDialPlanControlIndex.setStatus("current")
_SleVoipDialPlanControlDigitMap_Type = OctetString
_SleVoipDialPlanControlDigitMap_Object = MibScalar
sleVoipDialPlanControlDigitMap = _SleVoipDialPlanControlDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 2, 8),
    _SleVoipDialPlanControlDigitMap_Type()
)
sleVoipDialPlanControlDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleVoipDialPlanControlDigitMap.setStatus("current")
_SleVoipDialPlanNotification_ObjectIdentity = ObjectIdentity
sleVoipDialPlanNotification = _SleVoipDialPlanNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 3)
)
_SleVoipStatistics_ObjectIdentity = ObjectIdentity
sleVoipStatistics = _SleVoipStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12)
)
_SleVoipStatisticsTable_Object = MibTable
sleVoipStatisticsTable = _SleVoipStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1)
)
if mibBuilder.loadTexts:
    sleVoipStatisticsTable.setStatus("current")
_SleVoipStatisticsEntry_Object = MibTableRow
sleVoipStatisticsEntry = _SleVoipStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1)
)
sleVoipStatisticsEntry.setIndexNames(
    (0, "SLE-VOIP-MIB", "sleVoipStatisticsIndex"),
)
if mibBuilder.loadTexts:
    sleVoipStatisticsEntry.setStatus("current")


class _SleVoipStatisticsIndex_Type(Integer32):
    """Custom type sleVoipStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SleVoipStatisticsIndex_Type.__name__ = "Integer32"
_SleVoipStatisticsIndex_Object = MibTableColumn
sleVoipStatisticsIndex = _SleVoipStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 1),
    _SleVoipStatisticsIndex_Type()
)
sleVoipStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsIndex.setStatus("current")
_SleVoipStatisticsFormat_Type = Unsigned32
_SleVoipStatisticsFormat_Object = MibTableColumn
sleVoipStatisticsFormat = _SleVoipStatisticsFormat_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 2),
    _SleVoipStatisticsFormat_Type()
)
sleVoipStatisticsFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsFormat.setStatus("current")
_SleVoipStatisticsCallTimer_Type = Unsigned32
_SleVoipStatisticsCallTimer_Object = MibTableColumn
sleVoipStatisticsCallTimer = _SleVoipStatisticsCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 3),
    _SleVoipStatisticsCallTimer_Type()
)
sleVoipStatisticsCallTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsCallTimer.setStatus("current")
_SleVoipStatisticsCurrentPlayoutDelay_Type = Unsigned32
_SleVoipStatisticsCurrentPlayoutDelay_Object = MibTableColumn
sleVoipStatisticsCurrentPlayoutDelay = _SleVoipStatisticsCurrentPlayoutDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 4),
    _SleVoipStatisticsCurrentPlayoutDelay_Type()
)
sleVoipStatisticsCurrentPlayoutDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsCurrentPlayoutDelay.setStatus("current")
_SleVoipStatisticsMinPlayoutDelay_Type = Unsigned32
_SleVoipStatisticsMinPlayoutDelay_Object = MibTableColumn
sleVoipStatisticsMinPlayoutDelay = _SleVoipStatisticsMinPlayoutDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 5),
    _SleVoipStatisticsMinPlayoutDelay_Type()
)
sleVoipStatisticsMinPlayoutDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsMinPlayoutDelay.setStatus("current")
_SleVoipStatisticsMaxPlayoutDelay_Type = Unsigned32
_SleVoipStatisticsMaxPlayoutDelay_Object = MibTableColumn
sleVoipStatisticsMaxPlayoutDelay = _SleVoipStatisticsMaxPlayoutDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 6),
    _SleVoipStatisticsMaxPlayoutDelay_Type()
)
sleVoipStatisticsMaxPlayoutDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsMaxPlayoutDelay.setStatus("current")
_SleVoipStatisticsClockOffset_Type = Unsigned32
_SleVoipStatisticsClockOffset_Object = MibTableColumn
sleVoipStatisticsClockOffset = _SleVoipStatisticsClockOffset_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 7),
    _SleVoipStatisticsClockOffset_Type()
)
sleVoipStatisticsClockOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsClockOffset.setStatus("current")
_SleVoipStatisticsPeakJitter_Type = Unsigned32
_SleVoipStatisticsPeakJitter_Object = MibTableColumn
sleVoipStatisticsPeakJitter = _SleVoipStatisticsPeakJitter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 8),
    _SleVoipStatisticsPeakJitter_Type()
)
sleVoipStatisticsPeakJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsPeakJitter.setStatus("current")
_SleVoipStatisticsInterpolativeConcealment_Type = Unsigned32
_SleVoipStatisticsInterpolativeConcealment_Object = MibTableColumn
sleVoipStatisticsInterpolativeConcealment = _SleVoipStatisticsInterpolativeConcealment_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 9),
    _SleVoipStatisticsInterpolativeConcealment_Type()
)
sleVoipStatisticsInterpolativeConcealment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsInterpolativeConcealment.setStatus("current")
_SleVoipStatisticsSilenceConcealment_Type = Unsigned32
_SleVoipStatisticsSilenceConcealment_Object = MibTableColumn
sleVoipStatisticsSilenceConcealment = _SleVoipStatisticsSilenceConcealment_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 10),
    _SleVoipStatisticsSilenceConcealment_Type()
)
sleVoipStatisticsSilenceConcealment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsSilenceConcealment.setStatus("current")
_SleVoipStatisticsOverflowDiscard_Type = Unsigned32
_SleVoipStatisticsOverflowDiscard_Object = MibTableColumn
sleVoipStatisticsOverflowDiscard = _SleVoipStatisticsOverflowDiscard_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 11),
    _SleVoipStatisticsOverflowDiscard_Type()
)
sleVoipStatisticsOverflowDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsOverflowDiscard.setStatus("current")
_SleVoipStatisticsEndpointDetectionErrors_Type = Unsigned32
_SleVoipStatisticsEndpointDetectionErrors_Object = MibTableColumn
sleVoipStatisticsEndpointDetectionErrors = _SleVoipStatisticsEndpointDetectionErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 12),
    _SleVoipStatisticsEndpointDetectionErrors_Type()
)
sleVoipStatisticsEndpointDetectionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsEndpointDetectionErrors.setStatus("current")
_SleVoipStatisticsTxVoicePackets_Type = Unsigned32
_SleVoipStatisticsTxVoicePackets_Object = MibTableColumn
sleVoipStatisticsTxVoicePackets = _SleVoipStatisticsTxVoicePackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 13),
    _SleVoipStatisticsTxVoicePackets_Type()
)
sleVoipStatisticsTxVoicePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsTxVoicePackets.setStatus("current")
_SleVoipStatisticsTxSignalingPackets_Type = Unsigned32
_SleVoipStatisticsTxSignalingPackets_Object = MibTableColumn
sleVoipStatisticsTxSignalingPackets = _SleVoipStatisticsTxSignalingPackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 14),
    _SleVoipStatisticsTxSignalingPackets_Type()
)
sleVoipStatisticsTxSignalingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsTxSignalingPackets.setStatus("current")
_SleVoipStatisticsTxComfortNoisePackets_Type = Unsigned32
_SleVoipStatisticsTxComfortNoisePackets_Object = MibTableColumn
sleVoipStatisticsTxComfortNoisePackets = _SleVoipStatisticsTxComfortNoisePackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 15),
    _SleVoipStatisticsTxComfortNoisePackets_Type()
)
sleVoipStatisticsTxComfortNoisePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsTxComfortNoisePackets.setStatus("current")
_SleVoipStatisticsTotalTransmitDuration_Type = Unsigned32
_SleVoipStatisticsTotalTransmitDuration_Object = MibTableColumn
sleVoipStatisticsTotalTransmitDuration = _SleVoipStatisticsTotalTransmitDuration_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 16),
    _SleVoipStatisticsTotalTransmitDuration_Type()
)
sleVoipStatisticsTotalTransmitDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsTotalTransmitDuration.setStatus("current")
_SleVoipStatisticsVoiceTransmitDuration_Type = Unsigned32
_SleVoipStatisticsVoiceTransmitDuration_Object = MibTableColumn
sleVoipStatisticsVoiceTransmitDuration = _SleVoipStatisticsVoiceTransmitDuration_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 17),
    _SleVoipStatisticsVoiceTransmitDuration_Type()
)
sleVoipStatisticsVoiceTransmitDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsVoiceTransmitDuration.setStatus("current")
_SleVoipStatisticsRxVoicePackets_Type = Unsigned32
_SleVoipStatisticsRxVoicePackets_Object = MibTableColumn
sleVoipStatisticsRxVoicePackets = _SleVoipStatisticsRxVoicePackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 18),
    _SleVoipStatisticsRxVoicePackets_Type()
)
sleVoipStatisticsRxVoicePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsRxVoicePackets.setStatus("current")
_SleVoipStatisticsRxSignalingPackets_Type = Unsigned32
_SleVoipStatisticsRxSignalingPackets_Object = MibTableColumn
sleVoipStatisticsRxSignalingPackets = _SleVoipStatisticsRxSignalingPackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 19),
    _SleVoipStatisticsRxSignalingPackets_Type()
)
sleVoipStatisticsRxSignalingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsRxSignalingPackets.setStatus("current")
_SleVoipStatisticsRxComfortNoisePackets_Type = Unsigned32
_SleVoipStatisticsRxComfortNoisePackets_Object = MibTableColumn
sleVoipStatisticsRxComfortNoisePackets = _SleVoipStatisticsRxComfortNoisePackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 20),
    _SleVoipStatisticsRxComfortNoisePackets_Type()
)
sleVoipStatisticsRxComfortNoisePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsRxComfortNoisePackets.setStatus("current")
_SleVoipStatisticsTotalReceiveDuration_Type = Unsigned32
_SleVoipStatisticsTotalReceiveDuration_Object = MibTableColumn
sleVoipStatisticsTotalReceiveDuration = _SleVoipStatisticsTotalReceiveDuration_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 21),
    _SleVoipStatisticsTotalReceiveDuration_Type()
)
sleVoipStatisticsTotalReceiveDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsTotalReceiveDuration.setStatus("current")
_SleVoipStatisticsVoiceReceiveDuration_Type = Unsigned32
_SleVoipStatisticsVoiceReceiveDuration_Object = MibTableColumn
sleVoipStatisticsVoiceReceiveDuration = _SleVoipStatisticsVoiceReceiveDuration_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 22),
    _SleVoipStatisticsVoiceReceiveDuration_Type()
)
sleVoipStatisticsVoiceReceiveDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsVoiceReceiveDuration.setStatus("current")
_SleVoipStatisticsPacketsOutSequence_Type = Unsigned32
_SleVoipStatisticsPacketsOutSequence_Object = MibTableColumn
sleVoipStatisticsPacketsOutSequence = _SleVoipStatisticsPacketsOutSequence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 23),
    _SleVoipStatisticsPacketsOutSequence_Type()
)
sleVoipStatisticsPacketsOutSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsPacketsOutSequence.setStatus("current")
_SleVoipStatisticsBadProtocolHeaders_Type = Unsigned32
_SleVoipStatisticsBadProtocolHeaders_Object = MibTableColumn
sleVoipStatisticsBadProtocolHeaders = _SleVoipStatisticsBadProtocolHeaders_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 24),
    _SleVoipStatisticsBadProtocolHeaders_Type()
)
sleVoipStatisticsBadProtocolHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsBadProtocolHeaders.setStatus("current")
_SleVoipStatisticsLatePackets_Type = Unsigned32
_SleVoipStatisticsLatePackets_Object = MibTableColumn
sleVoipStatisticsLatePackets = _SleVoipStatisticsLatePackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 25),
    _SleVoipStatisticsLatePackets_Type()
)
sleVoipStatisticsLatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsLatePackets.setStatus("current")
_SleVoipStatisticsEarlyPackets_Type = Unsigned32
_SleVoipStatisticsEarlyPackets_Object = MibTableColumn
sleVoipStatisticsEarlyPackets = _SleVoipStatisticsEarlyPackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 26),
    _SleVoipStatisticsEarlyPackets_Type()
)
sleVoipStatisticsEarlyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsEarlyPackets.setStatus("current")
_SleVoipStatisticsRxVoiceOctets_Type = Unsigned32
_SleVoipStatisticsRxVoiceOctets_Object = MibTableColumn
sleVoipStatisticsRxVoiceOctets = _SleVoipStatisticsRxVoiceOctets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 27),
    _SleVoipStatisticsRxVoiceOctets_Type()
)
sleVoipStatisticsRxVoiceOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsRxVoiceOctets.setStatus("current")
_SleVoipStatisticsLostPackets_Type = Unsigned32
_SleVoipStatisticsLostPackets_Object = MibTableColumn
sleVoipStatisticsLostPackets = _SleVoipStatisticsLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 28),
    _SleVoipStatisticsLostPackets_Type()
)
sleVoipStatisticsLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsLostPackets.setStatus("current")
_SleVoipStatisticsCurrentTransmitPower_Type = Unsigned32
_SleVoipStatisticsCurrentTransmitPower_Object = MibTableColumn
sleVoipStatisticsCurrentTransmitPower = _SleVoipStatisticsCurrentTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 29),
    _SleVoipStatisticsCurrentTransmitPower_Type()
)
sleVoipStatisticsCurrentTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsCurrentTransmitPower.setStatus("current")
_SleVoipStatisticsMeanTransmitPower_Type = Unsigned32
_SleVoipStatisticsMeanTransmitPower_Object = MibTableColumn
sleVoipStatisticsMeanTransmitPower = _SleVoipStatisticsMeanTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 30),
    _SleVoipStatisticsMeanTransmitPower_Type()
)
sleVoipStatisticsMeanTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsMeanTransmitPower.setStatus("current")
_SleVoipStatisticsCurrentReceivePower_Type = Unsigned32
_SleVoipStatisticsCurrentReceivePower_Object = MibTableColumn
sleVoipStatisticsCurrentReceivePower = _SleVoipStatisticsCurrentReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 31),
    _SleVoipStatisticsCurrentReceivePower_Type()
)
sleVoipStatisticsCurrentReceivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsCurrentReceivePower.setStatus("current")
_SleVoipStatisticsMeanReceivePower_Type = Unsigned32
_SleVoipStatisticsMeanReceivePower_Object = MibTableColumn
sleVoipStatisticsMeanReceivePower = _SleVoipStatisticsMeanReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 32),
    _SleVoipStatisticsMeanReceivePower_Type()
)
sleVoipStatisticsMeanReceivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsMeanReceivePower.setStatus("current")
_SleVoipStatisticsBackgroundNoise_Type = Unsigned32
_SleVoipStatisticsBackgroundNoise_Object = MibTableColumn
sleVoipStatisticsBackgroundNoise = _SleVoipStatisticsBackgroundNoise_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 33),
    _SleVoipStatisticsBackgroundNoise_Type()
)
sleVoipStatisticsBackgroundNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsBackgroundNoise.setStatus("current")
_SleVoipStatisticsErlLevel_Type = Unsigned32
_SleVoipStatisticsErlLevel_Object = MibTableColumn
sleVoipStatisticsErlLevel = _SleVoipStatisticsErlLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 34),
    _SleVoipStatisticsErlLevel_Type()
)
sleVoipStatisticsErlLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsErlLevel.setStatus("current")
_SleVoipStatisticsAcomLevel_Type = Unsigned32
_SleVoipStatisticsAcomLevel_Object = MibTableColumn
sleVoipStatisticsAcomLevel = _SleVoipStatisticsAcomLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 35),
    _SleVoipStatisticsAcomLevel_Type()
)
sleVoipStatisticsAcomLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsAcomLevel.setStatus("current")
_SleVoipStatisticsCurrentTransmitActivity_Type = Unsigned32
_SleVoipStatisticsCurrentTransmitActivity_Object = MibTableColumn
sleVoipStatisticsCurrentTransmitActivity = _SleVoipStatisticsCurrentTransmitActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 36),
    _SleVoipStatisticsCurrentTransmitActivity_Type()
)
sleVoipStatisticsCurrentTransmitActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsCurrentTransmitActivity.setStatus("current")
_SleVoipStatisticsCurrentReceiveActivity_Type = Unsigned32
_SleVoipStatisticsCurrentReceiveActivity_Object = MibTableColumn
sleVoipStatisticsCurrentReceiveActivity = _SleVoipStatisticsCurrentReceiveActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 12, 1, 1, 37),
    _SleVoipStatisticsCurrentReceiveActivity_Type()
)
sleVoipStatisticsCurrentReceiveActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleVoipStatisticsCurrentReceiveActivity.setStatus("current")

# Managed Objects groups

sleVoipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 13)
)
sleVoipGroup.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipBaseControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlStatus"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlTimer"),
        ("SLE-VOIP-MIB", "sleVoipProtocol"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipVoiceDSCP"),
        ("SLE-VOIP-MIB", "sleVoipVoiceJitter"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlStatus"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlTimer"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlEncoding"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlUserEncoding"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlComfortNoise"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlEchoCancel"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlPacketLoss"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlVad"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlDSCP"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlJitter"),
        ("SLE-VOIP-MIB", "sleVoipSipUserIndex"),
        ("SLE-VOIP-MIB", "sleVoipSipUserAgent"),
        ("SLE-VOIP-MIB", "sleVoipSipUserAOR"),
        ("SLE-VOIP-MIB", "sleVoipSipUserDisplayName"),
        ("SLE-VOIP-MIB", "sleVoipSipUserUserName"),
        ("SLE-VOIP-MIB", "sleVoipSipUserPassword"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlStatus"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlTimer"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlAgent"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlAOR"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlDisplayName"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlUserName"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlPassword"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentIndex"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentServer"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentPort"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentTypeOfService"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentTransport"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentRegistrar"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentPrimary"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentSecondary"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentProfileName"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentExpireTimer"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlStatus"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlTimer"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlServer"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlPort"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlTypeOfService"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlTransport"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlRegistrar"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlPrimary"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlSecondary"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlProfileName"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlExpireTimer"),
        ("SLE-VOIP-MIB", "sleVoipVoiceIndex"),
        ("SLE-VOIP-MIB", "sleVoipVoiceEncoding"),
        ("SLE-VOIP-MIB", "sleVoipVoiceUserEncoding"),
        ("SLE-VOIP-MIB", "sleVoipVoiceComfortNoise"),
        ("SLE-VOIP-MIB", "sleVoipVoiceEchoCancel"),
        ("SLE-VOIP-MIB", "sleVoipVoicePacketLoss"),
        ("SLE-VOIP-MIB", "sleVoipVoiceVad"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointIndex"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointAgent"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointName"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlStatus"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlTimer"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlAgent"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlName"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentIndex"),
        ("SLE-VOIP-MIB", "sleVoipMgcpCallAgent"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentPort"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentTOS"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentVendor"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentDNS"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlStatus"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlTimer"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlCallAgent"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlPort"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlTOS"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlVendor"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlDNS"),
        ("SLE-VOIP-MIB", "sleVoipPotsStatusIndex"),
        ("SLE-VOIP-MIB", "sleVoipInterface"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileIndex"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileCodecSelection"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfilePacketPeriod"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileSilenceSuppression"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlStatus"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlTimer"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlCodecSelection"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlPacketPeriod"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlSilenceSuppression"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfilePortMin"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileDscpMark"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileOob"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileDtmfEvent"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlStatus"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlTimer"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlPortMin"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlDscpMark"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlOob"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlDtmfEvent"),
        ("SLE-VOIP-MIB", "sleVoipMgcpCallAgentPort"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlCallAgentPort"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentProfileName"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlProfileName"),
        ("SLE-VOIP-MIB", "sleVoipTimerIndex"),
        ("SLE-VOIP-MIB", "sleVoipTimerCriticalTimeout"),
        ("SLE-VOIP-MIB", "sleVoipTimerFirstDigit"),
        ("SLE-VOIP-MIB", "sleVoipTimerIntraDigit"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlStatus"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlTimer"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlCriticalTimeout"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlFirstDigit"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlIntraDigit"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsIndex"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsFormat"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsCallTimer"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsCurrentPlayoutDelay"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsMinPlayoutDelay"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsMaxPlayoutDelay"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsClockOffset"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsPeakJitter"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsInterpolativeConcealment"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsSilenceConcealment"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsOverflowDiscard"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsEndpointDetectionErrors"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsTxVoicePackets"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsTxSignalingPackets"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsTxComfortNoisePackets"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsTotalTransmitDuration"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsVoiceTransmitDuration"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsRxVoicePackets"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsRxSignalingPackets"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsRxComfortNoisePackets"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsTotalReceiveDuration"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsVoiceReceiveDuration"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsPacketsOutSequence"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsBadProtocolHeaders"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsLatePackets"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsEarlyPackets"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsRxVoiceOctets"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsLostPackets"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsCurrentTransmitPower"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsMeanTransmitPower"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsCurrentReceivePower"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsMeanReceivePower"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsBackgroundNoise"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsErlLevel"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsAcomLevel"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsCurrentTransmitActivity"),
        ("SLE-VOIP-MIB", "sleVoipStatisticsCurrentReceiveActivity"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanIndex"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanDigitMap"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlStatus"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlTimer"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlDigitMap"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanPotStatusIndex"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlPotStatusIndex"),
        ("SLE-VOIP-MIB", "sleVoipPotsStatusHookState"),
        ("SLE-VOIP-MIB", "sleVoipPotsStatusRegisterState"),
        ("SLE-VOIP-MIB", "sleVoipRtcp"),
        ("SLE-VOIP-MIB", "sleVoipPotsStatus"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlInterface"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlProtocol"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlFaxmode"),
        ("SLE-VOIP-MIB", "sleVoipFaxmode"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlRtcp"))
)
if mibBuilder.loadTexts:
    sleVoipGroup.setStatus("current")


# Notification objects

sleVoipBaseInterfaceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 3, 1)
)
sleVoipBaseInterfaceChanged.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipBaseControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlInterface"))
)
if mibBuilder.loadTexts:
    sleVoipBaseInterfaceChanged.setStatus(
        "current"
    )

sleVoipBaseProtocolChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 3, 2)
)
sleVoipBaseProtocolChanged.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipBaseControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlProtocol"))
)
if mibBuilder.loadTexts:
    sleVoipBaseProtocolChanged.setStatus(
        "current"
    )

sleVoipBaseRestartStackOnly = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 3, 3)
)
sleVoipBaseRestartStackOnly.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipBaseControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleVoipBaseRestartStackOnly.setStatus(
        "current"
    )

sleVoipBaseRestartAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 3, 4)
)
sleVoipBaseRestartAll.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipBaseControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlReqResult"))
)
if mibBuilder.loadTexts:
    sleVoipBaseRestartAll.setStatus(
        "current"
    )

sleVoipBaseRtcpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 3, 5)
)
sleVoipBaseRtcpChanged.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipBaseControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlRtcp"))
)
if mibBuilder.loadTexts:
    sleVoipBaseRtcpChanged.setStatus(
        "current"
    )

sleVoipBaseFaxmodeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 1, 3, 6)
)
sleVoipBaseFaxmodeChanged.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipBaseControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipBaseControlFaxmode"))
)
if mibBuilder.loadTexts:
    sleVoipBaseFaxmodeChanged.setStatus(
        "current"
    )

sleVoipVoiceEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 3, 1)
)
sleVoipVoiceEnabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipVoiceControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlVad"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlDSCP"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlJitter"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlPacketLoss"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlEchoCancel"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlComfortNoise"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlUserEncoding"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlEncoding"))
)
if mibBuilder.loadTexts:
    sleVoipVoiceEnabled.setStatus(
        "current"
    )

sleVoipVoiceDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 2, 3, 2)
)
sleVoipVoiceDisabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipVoiceControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipVoiceControlIndex"))
)
if mibBuilder.loadTexts:
    sleVoipVoiceDisabled.setStatus(
        "current"
    )

sleVoipSipUserEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 3, 1)
)
sleVoipSipUserEnabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipSipUserControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlAgent"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlAOR"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlDisplayName"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlUserName"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlPassword"))
)
if mibBuilder.loadTexts:
    sleVoipSipUserEnabled.setStatus(
        "current"
    )

sleVoipSipUserDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 3, 3, 2)
)
sleVoipSipUserDisabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipSipUserControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipSipUserControlIndex"))
)
if mibBuilder.loadTexts:
    sleVoipSipUserDisabled.setStatus(
        "current"
    )

sleVoipSipAgentEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 3, 1)
)
sleVoipSipAgentEnabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipSipAgentControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlServer"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlPort"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlTypeOfService"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlTransport"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlRegistrar"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlPrimary"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlSecondary"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlProfileName"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlExpireTimer"))
)
if mibBuilder.loadTexts:
    sleVoipSipAgentEnabled.setStatus(
        "current"
    )

sleVoipSipAgentDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 4, 3, 2)
)
sleVoipSipAgentDisabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipSipAgentControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentControlIndex"))
)
if mibBuilder.loadTexts:
    sleVoipSipAgentDisabled.setStatus(
        "current"
    )

sleVoipMgcpEndpointEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 3, 1)
)
sleVoipMgcpEndpointEnabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlAgent"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlName"))
)
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointEnabled.setStatus(
        "current"
    )

sleVoipMgcpEndpointDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 5, 3, 2)
)
sleVoipMgcpEndpointDisabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointControlIndex"))
)
if mibBuilder.loadTexts:
    sleVoipMgcpEndpointDisabled.setStatus(
        "current"
    )

sleVoipMgcpAgentEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 3, 1)
)
sleVoipMgcpAgentEnabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipMgcpAgentControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlCallAgent"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlPort"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlTOS"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlVendor"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlProfileName"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlDNS"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlCallAgentPort"))
)
if mibBuilder.loadTexts:
    sleVoipMgcpAgentEnabled.setStatus(
        "current"
    )

sleVoipMgcpAgentDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 6, 3, 2)
)
sleVoipMgcpAgentDisabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipMgcpAgentControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentControlIndex"))
)
if mibBuilder.loadTexts:
    sleVoipMgcpAgentDisabled.setStatus(
        "current"
    )

sleVoipMediaProfileEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 3, 1)
)
sleVoipMediaProfileEnabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipMediaProfileControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlSilenceSuppression"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlCodecSelection"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlPacketPeriod"))
)
if mibBuilder.loadTexts:
    sleVoipMediaProfileEnabled.setStatus(
        "current"
    )

sleVoipMediaProfileDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 8, 3, 2)
)
sleVoipMediaProfileDisabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipMediaProfileControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileControlIndex"))
)
if mibBuilder.loadTexts:
    sleVoipMediaProfileDisabled.setStatus(
        "current"
    )

sleVoipRtpProfilePortMinChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 3, 1)
)
sleVoipRtpProfilePortMinChanged.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipRtpProfileControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlPortMin"))
)
if mibBuilder.loadTexts:
    sleVoipRtpProfilePortMinChanged.setStatus(
        "current"
    )

sleVoipRtpProfileDscpMarkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 3, 2)
)
sleVoipRtpProfileDscpMarkChanged.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipRtpProfileControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlDscpMark"))
)
if mibBuilder.loadTexts:
    sleVoipRtpProfileDscpMarkChanged.setStatus(
        "current"
    )

sleVoipRtpProfileOobChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 3, 3)
)
sleVoipRtpProfileOobChanged.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipRtpProfileControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlOob"))
)
if mibBuilder.loadTexts:
    sleVoipRtpProfileOobChanged.setStatus(
        "current"
    )

sleVoipRtpProfileDtmfEventChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 9, 3, 4)
)
sleVoipRtpProfileDtmfEventChanged.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipRtpProfileControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileControlDtmfEvent"))
)
if mibBuilder.loadTexts:
    sleVoipRtpProfileDtmfEventChanged.setStatus(
        "current"
    )

sleVoipTimerEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 3, 1)
)
sleVoipTimerEnabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipTimerControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlCriticalTimeout"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlFirstDigit"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlIntraDigit"))
)
if mibBuilder.loadTexts:
    sleVoipTimerEnabled.setStatus(
        "current"
    )

sleVoipTimerDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 10, 3, 2)
)
sleVoipTimerDisabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipTimerControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipTimerControlIndex"))
)
if mibBuilder.loadTexts:
    sleVoipTimerDisabled.setStatus(
        "current"
    )

sleVoipDialPlanEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 3, 1)
)
sleVoipDialPlanEnabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipDialPlanControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlPotStatusIndex"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlIndex"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlDigitMap"))
)
if mibBuilder.loadTexts:
    sleVoipDialPlanEnabled.setStatus(
        "current"
    )

sleVoipDialPlanDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 11, 3, 2)
)
sleVoipDialPlanDisabled.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipDialPlanControlRequest"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlTimeStamp"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlReqResult"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanControlIndex"))
)
if mibBuilder.loadTexts:
    sleVoipDialPlanDisabled.setStatus(
        "current"
    )


# Notifications groups

sleVoipNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 25, 14)
)
sleVoipNotificationGroup.setObjects(
      *(("SLE-VOIP-MIB", "sleVoipBaseInterfaceChanged"),
        ("SLE-VOIP-MIB", "sleVoipBaseProtocolChanged"),
        ("SLE-VOIP-MIB", "sleVoipVoiceEnabled"),
        ("SLE-VOIP-MIB", "sleVoipVoiceDisabled"),
        ("SLE-VOIP-MIB", "sleVoipSipUserEnabled"),
        ("SLE-VOIP-MIB", "sleVoipSipUserDisabled"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentEnabled"),
        ("SLE-VOIP-MIB", "sleVoipSipAgentDisabled"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointEnabled"),
        ("SLE-VOIP-MIB", "sleVoipMgcpEndpointDisabled"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentEnabled"),
        ("SLE-VOIP-MIB", "sleVoipMgcpAgentDisabled"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileEnabled"),
        ("SLE-VOIP-MIB", "sleVoipMediaProfileDisabled"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfilePortMinChanged"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileDscpMarkChanged"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileOobChanged"),
        ("SLE-VOIP-MIB", "sleVoipRtpProfileDtmfEventChanged"),
        ("SLE-VOIP-MIB", "sleVoipTimerEnabled"),
        ("SLE-VOIP-MIB", "sleVoipTimerDisabled"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanEnabled"),
        ("SLE-VOIP-MIB", "sleVoipBaseRtcpChanged"),
        ("SLE-VOIP-MIB", "sleVoipBaseFaxmodeChanged"),
        ("SLE-VOIP-MIB", "sleVoipDialPlanDisabled"),
        ("SLE-VOIP-MIB", "sleVoipBaseRestartStackOnly"),
        ("SLE-VOIP-MIB", "sleVoipBaseRestartAll"))
)
if mibBuilder.loadTexts:
    sleVoipNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-VOIP-MIB",
    **{"OwnerString": OwnerString,
       "EnableDisableState": EnableDisableState,
       "sleVoip": sleVoip,
       "sleVoipBase": sleVoipBase,
       "sleVoipBaseInfo": sleVoipBaseInfo,
       "sleVoipInterface": sleVoipInterface,
       "sleVoipProtocol": sleVoipProtocol,
       "sleVoipRtcp": sleVoipRtcp,
       "sleVoipFaxmode": sleVoipFaxmode,
       "sleVoipBaseControl": sleVoipBaseControl,
       "sleVoipBaseControlRequest": sleVoipBaseControlRequest,
       "sleVoipBaseControlStatus": sleVoipBaseControlStatus,
       "sleVoipBaseControlTimer": sleVoipBaseControlTimer,
       "sleVoipBaseControlTimeStamp": sleVoipBaseControlTimeStamp,
       "sleVoipBaseControlReqResult": sleVoipBaseControlReqResult,
       "sleVoipBaseControlInterface": sleVoipBaseControlInterface,
       "sleVoipBaseControlProtocol": sleVoipBaseControlProtocol,
       "sleVoipBaseControlRtcp": sleVoipBaseControlRtcp,
       "sleVoipBaseControlFaxmode": sleVoipBaseControlFaxmode,
       "sleVoipBaseNotification": sleVoipBaseNotification,
       "sleVoipBaseInterfaceChanged": sleVoipBaseInterfaceChanged,
       "sleVoipBaseProtocolChanged": sleVoipBaseProtocolChanged,
       "sleVoipBaseRestartStackOnly": sleVoipBaseRestartStackOnly,
       "sleVoipBaseRestartAll": sleVoipBaseRestartAll,
       "sleVoipBaseRtcpChanged": sleVoipBaseRtcpChanged,
       "sleVoipBaseFaxmodeChanged": sleVoipBaseFaxmodeChanged,
       "sleVoipVoice": sleVoipVoice,
       "sleVoipVoiceTable": sleVoipVoiceTable,
       "sleVoipVoiceEntry": sleVoipVoiceEntry,
       "sleVoipVoiceIndex": sleVoipVoiceIndex,
       "sleVoipVoiceEncoding": sleVoipVoiceEncoding,
       "sleVoipVoiceUserEncoding": sleVoipVoiceUserEncoding,
       "sleVoipVoiceComfortNoise": sleVoipVoiceComfortNoise,
       "sleVoipVoiceEchoCancel": sleVoipVoiceEchoCancel,
       "sleVoipVoicePacketLoss": sleVoipVoicePacketLoss,
       "sleVoipVoiceVad": sleVoipVoiceVad,
       "sleVoipVoiceDSCP": sleVoipVoiceDSCP,
       "sleVoipVoiceJitter": sleVoipVoiceJitter,
       "sleVoipVoiceControl": sleVoipVoiceControl,
       "sleVoipVoiceControlRequest": sleVoipVoiceControlRequest,
       "sleVoipVoiceControlStatus": sleVoipVoiceControlStatus,
       "sleVoipVoiceControlTimer": sleVoipVoiceControlTimer,
       "sleVoipVoiceControlTimeStamp": sleVoipVoiceControlTimeStamp,
       "sleVoipVoiceControlReqResult": sleVoipVoiceControlReqResult,
       "sleVoipVoiceControlIndex": sleVoipVoiceControlIndex,
       "sleVoipVoiceControlEncoding": sleVoipVoiceControlEncoding,
       "sleVoipVoiceControlUserEncoding": sleVoipVoiceControlUserEncoding,
       "sleVoipVoiceControlComfortNoise": sleVoipVoiceControlComfortNoise,
       "sleVoipVoiceControlEchoCancel": sleVoipVoiceControlEchoCancel,
       "sleVoipVoiceControlPacketLoss": sleVoipVoiceControlPacketLoss,
       "sleVoipVoiceControlVad": sleVoipVoiceControlVad,
       "sleVoipVoiceControlDSCP": sleVoipVoiceControlDSCP,
       "sleVoipVoiceControlJitter": sleVoipVoiceControlJitter,
       "sleVoiceNotification": sleVoiceNotification,
       "sleVoipVoiceEnabled": sleVoipVoiceEnabled,
       "sleVoipVoiceDisabled": sleVoipVoiceDisabled,
       "sleVoipSipUser": sleVoipSipUser,
       "sleVoipSipUserTable": sleVoipSipUserTable,
       "sleVoipSipUserEntry": sleVoipSipUserEntry,
       "sleVoipSipUserIndex": sleVoipSipUserIndex,
       "sleVoipSipUserAgent": sleVoipSipUserAgent,
       "sleVoipSipUserAOR": sleVoipSipUserAOR,
       "sleVoipSipUserDisplayName": sleVoipSipUserDisplayName,
       "sleVoipSipUserUserName": sleVoipSipUserUserName,
       "sleVoipSipUserPassword": sleVoipSipUserPassword,
       "sleVoipSipUserControl": sleVoipSipUserControl,
       "sleVoipSipUserControlRequest": sleVoipSipUserControlRequest,
       "sleVoipSipUserControlStatus": sleVoipSipUserControlStatus,
       "sleVoipSipUserControlTimer": sleVoipSipUserControlTimer,
       "sleVoipSipUserControlTimeStamp": sleVoipSipUserControlTimeStamp,
       "sleVoipSipUserControlReqResult": sleVoipSipUserControlReqResult,
       "sleVoipSipUserControlIndex": sleVoipSipUserControlIndex,
       "sleVoipSipUserControlAgent": sleVoipSipUserControlAgent,
       "sleVoipSipUserControlAOR": sleVoipSipUserControlAOR,
       "sleVoipSipUserControlDisplayName": sleVoipSipUserControlDisplayName,
       "sleVoipSipUserControlUserName": sleVoipSipUserControlUserName,
       "sleVoipSipUserControlPassword": sleVoipSipUserControlPassword,
       "sleVoipSipUserNotification": sleVoipSipUserNotification,
       "sleVoipSipUserEnabled": sleVoipSipUserEnabled,
       "sleVoipSipUserDisabled": sleVoipSipUserDisabled,
       "sleVoipSipAgent": sleVoipSipAgent,
       "sleVoipSipAgentTable": sleVoipSipAgentTable,
       "sleVoipSipAgentEntry": sleVoipSipAgentEntry,
       "sleVoipSipAgentIndex": sleVoipSipAgentIndex,
       "sleVoipSipAgentServer": sleVoipSipAgentServer,
       "sleVoipSipAgentPort": sleVoipSipAgentPort,
       "sleVoipSipAgentTypeOfService": sleVoipSipAgentTypeOfService,
       "sleVoipSipAgentTransport": sleVoipSipAgentTransport,
       "sleVoipSipAgentRegistrar": sleVoipSipAgentRegistrar,
       "sleVoipSipAgentPrimary": sleVoipSipAgentPrimary,
       "sleVoipSipAgentSecondary": sleVoipSipAgentSecondary,
       "sleVoipSipAgentProfileName": sleVoipSipAgentProfileName,
       "sleVoipSipAgentExpireTimer": sleVoipSipAgentExpireTimer,
       "sleVoipSipAgentControl": sleVoipSipAgentControl,
       "sleVoipSipAgentControlRequest": sleVoipSipAgentControlRequest,
       "sleVoipSipAgentControlStatus": sleVoipSipAgentControlStatus,
       "sleVoipSipAgentControlTimer": sleVoipSipAgentControlTimer,
       "sleVoipSipAgentControlTimeStamp": sleVoipSipAgentControlTimeStamp,
       "sleVoipSipAgentControlReqResult": sleVoipSipAgentControlReqResult,
       "sleVoipSipAgentControlIndex": sleVoipSipAgentControlIndex,
       "sleVoipSipAgentControlServer": sleVoipSipAgentControlServer,
       "sleVoipSipAgentControlPort": sleVoipSipAgentControlPort,
       "sleVoipSipAgentControlTypeOfService": sleVoipSipAgentControlTypeOfService,
       "sleVoipSipAgentControlTransport": sleVoipSipAgentControlTransport,
       "sleVoipSipAgentControlRegistrar": sleVoipSipAgentControlRegistrar,
       "sleVoipSipAgentControlPrimary": sleVoipSipAgentControlPrimary,
       "sleVoipSipAgentControlSecondary": sleVoipSipAgentControlSecondary,
       "sleVoipSipAgentControlProfileName": sleVoipSipAgentControlProfileName,
       "sleVoipSipAgentControlExpireTimer": sleVoipSipAgentControlExpireTimer,
       "sleVoipSipAgentNotification": sleVoipSipAgentNotification,
       "sleVoipSipAgentEnabled": sleVoipSipAgentEnabled,
       "sleVoipSipAgentDisabled": sleVoipSipAgentDisabled,
       "sleVoipMgcpEndpoint": sleVoipMgcpEndpoint,
       "sleVoipMgcpEndpointTable": sleVoipMgcpEndpointTable,
       "sleVoipMgcpEndpointEntry": sleVoipMgcpEndpointEntry,
       "sleVoipMgcpEndpointIndex": sleVoipMgcpEndpointIndex,
       "sleVoipMgcpEndpointAgent": sleVoipMgcpEndpointAgent,
       "sleVoipMgcpEndpointName": sleVoipMgcpEndpointName,
       "sleVoipMgcpEndpointControl": sleVoipMgcpEndpointControl,
       "sleVoipMgcpEndpointControlRequest": sleVoipMgcpEndpointControlRequest,
       "sleVoipMgcpEndpointControlStatus": sleVoipMgcpEndpointControlStatus,
       "sleVoipMgcpEndpointControlTimer": sleVoipMgcpEndpointControlTimer,
       "sleVoipMgcpEndpointControlTimeStamp": sleVoipMgcpEndpointControlTimeStamp,
       "sleVoipMgcpEndpointControlReqResult": sleVoipMgcpEndpointControlReqResult,
       "sleVoipMgcpEndpointControlIndex": sleVoipMgcpEndpointControlIndex,
       "sleVoipMgcpEndpointControlAgent": sleVoipMgcpEndpointControlAgent,
       "sleVoipMgcpEndpointControlName": sleVoipMgcpEndpointControlName,
       "sleVoipMgcpEndpointNotification": sleVoipMgcpEndpointNotification,
       "sleVoipMgcpEndpointEnabled": sleVoipMgcpEndpointEnabled,
       "sleVoipMgcpEndpointDisabled": sleVoipMgcpEndpointDisabled,
       "sleVoipMgcpAgent": sleVoipMgcpAgent,
       "sleVoipMgcpAgentTable": sleVoipMgcpAgentTable,
       "sleVoipMgcpAgentEntry": sleVoipMgcpAgentEntry,
       "sleVoipMgcpAgentIndex": sleVoipMgcpAgentIndex,
       "sleVoipMgcpCallAgent": sleVoipMgcpCallAgent,
       "sleVoipMgcpCallAgentPort": sleVoipMgcpCallAgentPort,
       "sleVoipMgcpAgentPort": sleVoipMgcpAgentPort,
       "sleVoipMgcpAgentTOS": sleVoipMgcpAgentTOS,
       "sleVoipMgcpAgentVendor": sleVoipMgcpAgentVendor,
       "sleVoipMgcpAgentDNS": sleVoipMgcpAgentDNS,
       "sleVoipMgcpAgentProfileName": sleVoipMgcpAgentProfileName,
       "sleVoipMgcpAgentControl": sleVoipMgcpAgentControl,
       "sleVoipMgcpAgentControlRequest": sleVoipMgcpAgentControlRequest,
       "sleVoipMgcpAgentControlStatus": sleVoipMgcpAgentControlStatus,
       "sleVoipMgcpAgentControlTimer": sleVoipMgcpAgentControlTimer,
       "sleVoipMgcpAgentControlTimeStamp": sleVoipMgcpAgentControlTimeStamp,
       "sleVoipMgcpAgentControlReqResult": sleVoipMgcpAgentControlReqResult,
       "sleVoipMgcpAgentControlIndex": sleVoipMgcpAgentControlIndex,
       "sleVoipMgcpAgentControlCallAgent": sleVoipMgcpAgentControlCallAgent,
       "sleVoipMgcpAgentControlCallAgentPort": sleVoipMgcpAgentControlCallAgentPort,
       "sleVoipMgcpAgentControlPort": sleVoipMgcpAgentControlPort,
       "sleVoipMgcpAgentControlTOS": sleVoipMgcpAgentControlTOS,
       "sleVoipMgcpAgentControlVendor": sleVoipMgcpAgentControlVendor,
       "sleVoipMgcpAgentControlDNS": sleVoipMgcpAgentControlDNS,
       "sleVoipMgcpAgentControlProfileName": sleVoipMgcpAgentControlProfileName,
       "sleVoipMgcpAgentNotification": sleVoipMgcpAgentNotification,
       "sleVoipMgcpAgentEnabled": sleVoipMgcpAgentEnabled,
       "sleVoipMgcpAgentDisabled": sleVoipMgcpAgentDisabled,
       "sleVoipPots": sleVoipPots,
       "sleVoipPotsStatusTable": sleVoipPotsStatusTable,
       "sleVoipPotsStatusEntry": sleVoipPotsStatusEntry,
       "sleVoipPotsStatusIndex": sleVoipPotsStatusIndex,
       "sleVoipPotsStatus": sleVoipPotsStatus,
       "sleVoipPotsStatusHookState": sleVoipPotsStatusHookState,
       "sleVoipPotsStatusRegisterState": sleVoipPotsStatusRegisterState,
       "sleVoipMediaProfile": sleVoipMediaProfile,
       "sleVoipMediaProfileTable": sleVoipMediaProfileTable,
       "sleVoipMediaProfileEntry": sleVoipMediaProfileEntry,
       "sleVoipMediaProfileIndex": sleVoipMediaProfileIndex,
       "sleVoipMediaProfileCodecSelection": sleVoipMediaProfileCodecSelection,
       "sleVoipMediaProfilePacketPeriod": sleVoipMediaProfilePacketPeriod,
       "sleVoipMediaProfileSilenceSuppression": sleVoipMediaProfileSilenceSuppression,
       "sleVoipMediaProfileControl": sleVoipMediaProfileControl,
       "sleVoipMediaProfileControlRequest": sleVoipMediaProfileControlRequest,
       "sleVoipMediaProfileControlStatus": sleVoipMediaProfileControlStatus,
       "sleVoipMediaProfileControlTimer": sleVoipMediaProfileControlTimer,
       "sleVoipMediaProfileControlTimeStamp": sleVoipMediaProfileControlTimeStamp,
       "sleVoipMediaProfileControlReqResult": sleVoipMediaProfileControlReqResult,
       "sleVoipMediaProfileControlIndex": sleVoipMediaProfileControlIndex,
       "sleVoipMediaProfileControlCodecSelection": sleVoipMediaProfileControlCodecSelection,
       "sleVoipMediaProfileControlPacketPeriod": sleVoipMediaProfileControlPacketPeriod,
       "sleVoipMediaProfileControlSilenceSuppression": sleVoipMediaProfileControlSilenceSuppression,
       "sleVoipMediaProfileNotification": sleVoipMediaProfileNotification,
       "sleVoipMediaProfileEnabled": sleVoipMediaProfileEnabled,
       "sleVoipMediaProfileDisabled": sleVoipMediaProfileDisabled,
       "sleVoipRtpProfile": sleVoipRtpProfile,
       "sleVoipRtpProfileInfo": sleVoipRtpProfileInfo,
       "sleVoipRtpProfilePortMin": sleVoipRtpProfilePortMin,
       "sleVoipRtpProfileDscpMark": sleVoipRtpProfileDscpMark,
       "sleVoipRtpProfileOob": sleVoipRtpProfileOob,
       "sleVoipRtpProfileDtmfEvent": sleVoipRtpProfileDtmfEvent,
       "sleVoipRtpProfileControl": sleVoipRtpProfileControl,
       "sleVoipRtpProfileControlRequest": sleVoipRtpProfileControlRequest,
       "sleVoipRtpProfileControlStatus": sleVoipRtpProfileControlStatus,
       "sleVoipRtpProfileControlTimer": sleVoipRtpProfileControlTimer,
       "sleVoipRtpProfileControlTimeStamp": sleVoipRtpProfileControlTimeStamp,
       "sleVoipRtpProfileControlReqResult": sleVoipRtpProfileControlReqResult,
       "sleVoipRtpProfileControlPortMin": sleVoipRtpProfileControlPortMin,
       "sleVoipRtpProfileControlDscpMark": sleVoipRtpProfileControlDscpMark,
       "sleVoipRtpProfileControlOob": sleVoipRtpProfileControlOob,
       "sleVoipRtpProfileControlDtmfEvent": sleVoipRtpProfileControlDtmfEvent,
       "sleVoipRtpProfileNotification": sleVoipRtpProfileNotification,
       "sleVoipRtpProfilePortMinChanged": sleVoipRtpProfilePortMinChanged,
       "sleVoipRtpProfileDscpMarkChanged": sleVoipRtpProfileDscpMarkChanged,
       "sleVoipRtpProfileOobChanged": sleVoipRtpProfileOobChanged,
       "sleVoipRtpProfileDtmfEventChanged": sleVoipRtpProfileDtmfEventChanged,
       "sleVoipTimer": sleVoipTimer,
       "sleVoipTimerTable": sleVoipTimerTable,
       "sleVoipTimerEntry": sleVoipTimerEntry,
       "sleVoipTimerIndex": sleVoipTimerIndex,
       "sleVoipTimerCriticalTimeout": sleVoipTimerCriticalTimeout,
       "sleVoipTimerFirstDigit": sleVoipTimerFirstDigit,
       "sleVoipTimerIntraDigit": sleVoipTimerIntraDigit,
       "sleVoipTimerControl": sleVoipTimerControl,
       "sleVoipTimerControlRequest": sleVoipTimerControlRequest,
       "sleVoipTimerControlStatus": sleVoipTimerControlStatus,
       "sleVoipTimerControlTimer": sleVoipTimerControlTimer,
       "sleVoipTimerControlTimeStamp": sleVoipTimerControlTimeStamp,
       "sleVoipTimerControlReqResult": sleVoipTimerControlReqResult,
       "sleVoipTimerControlIndex": sleVoipTimerControlIndex,
       "sleVoipTimerControlCriticalTimeout": sleVoipTimerControlCriticalTimeout,
       "sleVoipTimerControlFirstDigit": sleVoipTimerControlFirstDigit,
       "sleVoipTimerControlIntraDigit": sleVoipTimerControlIntraDigit,
       "sleVoipTimerNotification": sleVoipTimerNotification,
       "sleVoipTimerEnabled": sleVoipTimerEnabled,
       "sleVoipTimerDisabled": sleVoipTimerDisabled,
       "sleVoipDialPlan": sleVoipDialPlan,
       "sleVoipDialPlanTable": sleVoipDialPlanTable,
       "sleVoipDialPlanEntry": sleVoipDialPlanEntry,
       "sleVoipDialPlanPotStatusIndex": sleVoipDialPlanPotStatusIndex,
       "sleVoipDialPlanIndex": sleVoipDialPlanIndex,
       "sleVoipDialPlanDigitMap": sleVoipDialPlanDigitMap,
       "sleVoipDialPlanControl": sleVoipDialPlanControl,
       "sleVoipDialPlanControlRequest": sleVoipDialPlanControlRequest,
       "sleVoipDialPlanControlStatus": sleVoipDialPlanControlStatus,
       "sleVoipDialPlanControlTimer": sleVoipDialPlanControlTimer,
       "sleVoipDialPlanControlTimeStamp": sleVoipDialPlanControlTimeStamp,
       "sleVoipDialPlanControlReqResult": sleVoipDialPlanControlReqResult,
       "sleVoipDialPlanControlPotStatusIndex": sleVoipDialPlanControlPotStatusIndex,
       "sleVoipDialPlanControlIndex": sleVoipDialPlanControlIndex,
       "sleVoipDialPlanControlDigitMap": sleVoipDialPlanControlDigitMap,
       "sleVoipDialPlanNotification": sleVoipDialPlanNotification,
       "sleVoipDialPlanEnabled": sleVoipDialPlanEnabled,
       "sleVoipDialPlanDisabled": sleVoipDialPlanDisabled,
       "sleVoipStatistics": sleVoipStatistics,
       "sleVoipStatisticsTable": sleVoipStatisticsTable,
       "sleVoipStatisticsEntry": sleVoipStatisticsEntry,
       "sleVoipStatisticsIndex": sleVoipStatisticsIndex,
       "sleVoipStatisticsFormat": sleVoipStatisticsFormat,
       "sleVoipStatisticsCallTimer": sleVoipStatisticsCallTimer,
       "sleVoipStatisticsCurrentPlayoutDelay": sleVoipStatisticsCurrentPlayoutDelay,
       "sleVoipStatisticsMinPlayoutDelay": sleVoipStatisticsMinPlayoutDelay,
       "sleVoipStatisticsMaxPlayoutDelay": sleVoipStatisticsMaxPlayoutDelay,
       "sleVoipStatisticsClockOffset": sleVoipStatisticsClockOffset,
       "sleVoipStatisticsPeakJitter": sleVoipStatisticsPeakJitter,
       "sleVoipStatisticsInterpolativeConcealment": sleVoipStatisticsInterpolativeConcealment,
       "sleVoipStatisticsSilenceConcealment": sleVoipStatisticsSilenceConcealment,
       "sleVoipStatisticsOverflowDiscard": sleVoipStatisticsOverflowDiscard,
       "sleVoipStatisticsEndpointDetectionErrors": sleVoipStatisticsEndpointDetectionErrors,
       "sleVoipStatisticsTxVoicePackets": sleVoipStatisticsTxVoicePackets,
       "sleVoipStatisticsTxSignalingPackets": sleVoipStatisticsTxSignalingPackets,
       "sleVoipStatisticsTxComfortNoisePackets": sleVoipStatisticsTxComfortNoisePackets,
       "sleVoipStatisticsTotalTransmitDuration": sleVoipStatisticsTotalTransmitDuration,
       "sleVoipStatisticsVoiceTransmitDuration": sleVoipStatisticsVoiceTransmitDuration,
       "sleVoipStatisticsRxVoicePackets": sleVoipStatisticsRxVoicePackets,
       "sleVoipStatisticsRxSignalingPackets": sleVoipStatisticsRxSignalingPackets,
       "sleVoipStatisticsRxComfortNoisePackets": sleVoipStatisticsRxComfortNoisePackets,
       "sleVoipStatisticsTotalReceiveDuration": sleVoipStatisticsTotalReceiveDuration,
       "sleVoipStatisticsVoiceReceiveDuration": sleVoipStatisticsVoiceReceiveDuration,
       "sleVoipStatisticsPacketsOutSequence": sleVoipStatisticsPacketsOutSequence,
       "sleVoipStatisticsBadProtocolHeaders": sleVoipStatisticsBadProtocolHeaders,
       "sleVoipStatisticsLatePackets": sleVoipStatisticsLatePackets,
       "sleVoipStatisticsEarlyPackets": sleVoipStatisticsEarlyPackets,
       "sleVoipStatisticsRxVoiceOctets": sleVoipStatisticsRxVoiceOctets,
       "sleVoipStatisticsLostPackets": sleVoipStatisticsLostPackets,
       "sleVoipStatisticsCurrentTransmitPower": sleVoipStatisticsCurrentTransmitPower,
       "sleVoipStatisticsMeanTransmitPower": sleVoipStatisticsMeanTransmitPower,
       "sleVoipStatisticsCurrentReceivePower": sleVoipStatisticsCurrentReceivePower,
       "sleVoipStatisticsMeanReceivePower": sleVoipStatisticsMeanReceivePower,
       "sleVoipStatisticsBackgroundNoise": sleVoipStatisticsBackgroundNoise,
       "sleVoipStatisticsErlLevel": sleVoipStatisticsErlLevel,
       "sleVoipStatisticsAcomLevel": sleVoipStatisticsAcomLevel,
       "sleVoipStatisticsCurrentTransmitActivity": sleVoipStatisticsCurrentTransmitActivity,
       "sleVoipStatisticsCurrentReceiveActivity": sleVoipStatisticsCurrentReceiveActivity,
       "sleVoipGroup": sleVoipGroup,
       "sleVoipNotificationGroup": sleVoipNotificationGroup}
)
