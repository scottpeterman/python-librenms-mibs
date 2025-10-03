# SNMP MIB module (VIPTELA-SECURITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-SECURITY
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:09 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_security = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4)
)
if mibBuilder.loadTexts:
    viptela_security.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class AuthenticationType1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class StateEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("up", 1),
          ("down", 2))
    )



class ConnFlagEnum(TextualConvention, Integer32):
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74)
        )
    )
    namedValues = NamedValues(
        *(("nOERR", 0),
          ("aCSRREJ", 1),
          ("sTENTRY", 2),
          ("hSFAIL", 3),
          ("dCERTFL", 4),
          ("nLCERT", 5),
          ("lISFD", 6),
          ("sNOCHECK", 7),
          ("iP-TOS", 8),
          ("tMRALC", 9),
          ("dCONFAIL", 10),
          ("wRKRTO", 11),
          ("vS-TMO", 12),
          ("vB-TMO", 13),
          ("vM-TMO", 14),
          ("vP-TMO", 15),
          ("dISTLOC", 16),
          ("rMGSPR", 17),
          ("pRCHAL", 18),
          ("sYSPRCH", 19),
          ("rECLEN0", 20),
          ("tXCHTOBD", 21),
          ("rDSIGFBD", 22),
          ("sSLNFAIL", 23),
          ("dHSTMO", 24),
          ("nOVS", 25),
          ("nOACTVB", 26),
          ("oRPTMO", 27),
          ("dEVALC", 28),
          ("tUNALC", 29),
          ("cRTREJSER", 30),
          ("vBDEST", 31),
          ("cRTREV", 32),
          ("rXTRDWN", 33),
          ("xTVSTRDN", 34),
          ("nOSLPRCRT", 35),
          ("dUPSER", 36),
          ("sERNTPRES", 37),
          ("cRTVERFL", 38),
          ("bIDNTPR", 39),
          ("bIDNTVRFD", 40),
          ("bDSGVERFL", 41),
          ("mEMALCFL", 42),
          ("uNMSGBDRG", 43),
          ("vSCRTREV", 44),
          ("vECRTREV", 45),
          ("uNAUTHEL", 46),
          ("dISCVBD", 47),
          ("cTORGNMMIS", 48),
          ("nOZTPEN", 49),
          ("nOVMCFG", 50),
          ("cHVERFAIL", 51),
          ("dUPCLHELO", 52),
          ("cERTEXPRD", 53),
          ("sYSIPCHNG", 54),
          ("xTVMTRDN", 55),
          ("mGRTBLCKD", 56),
          ("nONCGN", 57),
          ("xTMOS", 58),
          ("iPTMISS", 59),
          ("oPERDOWN", 60),
          ("nTPRVMINT", 61),
          ("sTNMODETD", 62),
          ("lRNTPEER", 63),
          ("cGNIDCHNGD", 64),
          ("dUPSYSIPDEL", 65),
          ("bIDSIG", 66),
          ("iDREQDECFAIL", 67),
          ("vEYIDBNDFAIL", 68),
          ("cREDFAIL", 69),
          ("rECCABLOBFAIL", 70),
          ("eMBARGOFAIL", 71),
          ("nEWVBNOVMNG", 72),
          ("hWCERTREN", 73),
          ("hWCERTREV", 74))
    )



class AuthenticationEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sha1-hmac", 3),
          ("ah-sha1-hmac", 4),
          ("ah-no-id", 5))
    )



class SessionState(TextualConvention, Integer32):
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
        *(("down", 0),
          ("connect", 1),
          ("handshake", 2),
          ("trying", 3),
          ("challenge", 4),
          ("challenge-resp", 5),
          ("challenge-ack", 6),
          ("up", 7),
          ("tear-down", 8))
    )



class AuthenticationType(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


# MIB Managed Objects in the order of their OIDs

_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2)
)
_ControlConnectionsInfo_ObjectIdentity = ObjectIdentity
controlConnectionsInfo = _ControlConnectionsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 1)
)
_ControlConnectionsInfoRate_Type = String
_ControlConnectionsInfoRate_Object = MibScalar
controlConnectionsInfoRate = _ControlConnectionsInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 1, 1),
    _ControlConnectionsInfoRate_Type()
)
controlConnectionsInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsInfoRate.setStatus("current")
_ControlConnectionsTable_Object = MibTable
controlConnectionsTable = _ControlConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2)
)
if mibBuilder.loadTexts:
    controlConnectionsTable.setStatus("current")
_ControlConnectionsEntry_Object = MibTableRow
controlConnectionsEntry = _ControlConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1)
)
controlConnectionsEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "controlConnectionsInstance"),
    (0, "VIPTELA-SECURITY", "controlConnectionsPeerType"),
    (0, "VIPTELA-SECURITY", "controlConnectionsSiteId"),
    (0, "VIPTELA-SECURITY", "controlConnectionsDomainId"),
    (0, "VIPTELA-SECURITY", "controlConnectionsLocalPrivateIp"),
    (0, "VIPTELA-SECURITY", "controlConnectionsLocalPrivatePort"),
    (0, "VIPTELA-SECURITY", "controlConnectionsPublicIp"),
    (0, "VIPTELA-SECURITY", "controlConnectionsPublicPort"),
)
if mibBuilder.loadTexts:
    controlConnectionsEntry.setStatus("current")
_ControlConnectionsInstance_Type = Unsigned32
_ControlConnectionsInstance_Object = MibTableColumn
controlConnectionsInstance = _ControlConnectionsInstance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 1),
    _ControlConnectionsInstance_Type()
)
controlConnectionsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsInstance.setStatus("current")


class _ControlConnectionsPeerType_Type(Integer32):
    """Custom type controlConnectionsPeerType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )


_ControlConnectionsPeerType_Type.__name__ = "Integer32"
_ControlConnectionsPeerType_Object = MibTableColumn
controlConnectionsPeerType = _ControlConnectionsPeerType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 2),
    _ControlConnectionsPeerType_Type()
)
controlConnectionsPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsPeerType.setStatus("current")
_ControlConnectionsSiteId_Type = Unsigned32
_ControlConnectionsSiteId_Object = MibTableColumn
controlConnectionsSiteId = _ControlConnectionsSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 3),
    _ControlConnectionsSiteId_Type()
)
controlConnectionsSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsSiteId.setStatus("current")
_ControlConnectionsDomainId_Type = Unsigned32
_ControlConnectionsDomainId_Object = MibTableColumn
controlConnectionsDomainId = _ControlConnectionsDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 4),
    _ControlConnectionsDomainId_Type()
)
controlConnectionsDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsDomainId.setStatus("current")
_ControlConnectionsLocalPrivateIp_Type = InetAddressIP
_ControlConnectionsLocalPrivateIp_Object = MibTableColumn
controlConnectionsLocalPrivateIp = _ControlConnectionsLocalPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 5),
    _ControlConnectionsLocalPrivateIp_Type()
)
controlConnectionsLocalPrivateIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsLocalPrivateIp.setStatus("current")
_ControlConnectionsLocalPrivatePort_Type = Unsigned32
_ControlConnectionsLocalPrivatePort_Object = MibTableColumn
controlConnectionsLocalPrivatePort = _ControlConnectionsLocalPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 6),
    _ControlConnectionsLocalPrivatePort_Type()
)
controlConnectionsLocalPrivatePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsLocalPrivatePort.setStatus("current")
_ControlConnectionsPublicIp_Type = InetAddressIP
_ControlConnectionsPublicIp_Object = MibTableColumn
controlConnectionsPublicIp = _ControlConnectionsPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 7),
    _ControlConnectionsPublicIp_Type()
)
controlConnectionsPublicIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsPublicIp.setStatus("current")
_ControlConnectionsPublicPort_Type = Unsigned32
_ControlConnectionsPublicPort_Object = MibTableColumn
controlConnectionsPublicPort = _ControlConnectionsPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 8),
    _ControlConnectionsPublicPort_Type()
)
controlConnectionsPublicPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsPublicPort.setStatus("current")
_ControlConnectionsSystemIp_Type = InetAddressIP
_ControlConnectionsSystemIp_Object = MibTableColumn
controlConnectionsSystemIp = _ControlConnectionsSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 9),
    _ControlConnectionsSystemIp_Type()
)
controlConnectionsSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsSystemIp.setStatus("current")


class _ControlConnectionsProtocol_Type(Integer32):
    """Custom type controlConnectionsProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dtls", 0),
          ("tls", 1))
    )


_ControlConnectionsProtocol_Type.__name__ = "Integer32"
_ControlConnectionsProtocol_Object = MibTableColumn
controlConnectionsProtocol = _ControlConnectionsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 10),
    _ControlConnectionsProtocol_Type()
)
controlConnectionsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsProtocol.setStatus("current")


class _ControlConnectionsLocalColor_Type(Integer32):
    """Custom type controlConnectionsLocalColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_ControlConnectionsLocalColor_Type.__name__ = "Integer32"
_ControlConnectionsLocalColor_Object = MibTableColumn
controlConnectionsLocalColor = _ControlConnectionsLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 11),
    _ControlConnectionsLocalColor_Type()
)
controlConnectionsLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsLocalColor.setStatus("current")


class _ControlConnectionsRemoteColor_Type(Integer32):
    """Custom type controlConnectionsRemoteColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_ControlConnectionsRemoteColor_Type.__name__ = "Integer32"
_ControlConnectionsRemoteColor_Object = MibTableColumn
controlConnectionsRemoteColor = _ControlConnectionsRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 12),
    _ControlConnectionsRemoteColor_Type()
)
controlConnectionsRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRemoteColor.setStatus("current")
_ControlConnectionsPrivateIp_Type = InetAddressIP
_ControlConnectionsPrivateIp_Object = MibTableColumn
controlConnectionsPrivateIp = _ControlConnectionsPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 13),
    _ControlConnectionsPrivateIp_Type()
)
controlConnectionsPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsPrivateIp.setStatus("current")
_ControlConnectionsPrivatePort_Type = Unsigned32
_ControlConnectionsPrivatePort_Object = MibTableColumn
controlConnectionsPrivatePort = _ControlConnectionsPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 14),
    _ControlConnectionsPrivatePort_Type()
)
controlConnectionsPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsPrivatePort.setStatus("current")
_ControlConnectionsState_Type = SessionState
_ControlConnectionsState_Object = MibTableColumn
controlConnectionsState = _ControlConnectionsState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 15),
    _ControlConnectionsState_Type()
)
controlConnectionsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsState.setStatus("current")
_ControlConnectionsLocalEnum_Type = ConnFlagEnum
_ControlConnectionsLocalEnum_Object = MibTableColumn
controlConnectionsLocalEnum = _ControlConnectionsLocalEnum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 16),
    _ControlConnectionsLocalEnum_Type()
)
controlConnectionsLocalEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsLocalEnum.setStatus("current")
_ControlConnectionsRemoteEnum_Type = ConnFlagEnum
_ControlConnectionsRemoteEnum_Object = MibTableColumn
controlConnectionsRemoteEnum = _ControlConnectionsRemoteEnum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 17),
    _ControlConnectionsRemoteEnum_Type()
)
controlConnectionsRemoteEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRemoteEnum.setStatus("current")
_ControlConnectionsLocalStateInfo_Type = String
_ControlConnectionsLocalStateInfo_Object = MibTableColumn
controlConnectionsLocalStateInfo = _ControlConnectionsLocalStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 18),
    _ControlConnectionsLocalStateInfo_Type()
)
controlConnectionsLocalStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsLocalStateInfo.setStatus("current")
_ControlConnectionsRemoteStateInfo_Type = String
_ControlConnectionsRemoteStateInfo_Object = MibTableColumn
controlConnectionsRemoteStateInfo = _ControlConnectionsRemoteStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 19),
    _ControlConnectionsRemoteStateInfo_Type()
)
controlConnectionsRemoteStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRemoteStateInfo.setStatus("current")
_ControlConnectionsUptime_Type = String
_ControlConnectionsUptime_Object = MibTableColumn
controlConnectionsUptime = _ControlConnectionsUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 20),
    _ControlConnectionsUptime_Type()
)
controlConnectionsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsUptime.setStatus("current")
_ControlConnectionsTxHello_Type = Unsigned32
_ControlConnectionsTxHello_Object = MibTableColumn
controlConnectionsTxHello = _ControlConnectionsTxHello_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 21),
    _ControlConnectionsTxHello_Type()
)
controlConnectionsTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxHello.setStatus("current")
_ControlConnectionsTxConnects_Type = Unsigned32
_ControlConnectionsTxConnects_Object = MibTableColumn
controlConnectionsTxConnects = _ControlConnectionsTxConnects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 22),
    _ControlConnectionsTxConnects_Type()
)
controlConnectionsTxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxConnects.setStatus("current")
_ControlConnectionsTxRegisters_Type = Unsigned32
_ControlConnectionsTxRegisters_Object = MibTableColumn
controlConnectionsTxRegisters = _ControlConnectionsTxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 23),
    _ControlConnectionsTxRegisters_Type()
)
controlConnectionsTxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxRegisters.setStatus("current")
_ControlConnectionsTxRegisterReplies_Type = Unsigned32
_ControlConnectionsTxRegisterReplies_Object = MibTableColumn
controlConnectionsTxRegisterReplies = _ControlConnectionsTxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 24),
    _ControlConnectionsTxRegisterReplies_Type()
)
controlConnectionsTxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxRegisterReplies.setStatus("current")
_ControlConnectionsTxChallenge_Type = Unsigned32
_ControlConnectionsTxChallenge_Object = MibTableColumn
controlConnectionsTxChallenge = _ControlConnectionsTxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 25),
    _ControlConnectionsTxChallenge_Type()
)
controlConnectionsTxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxChallenge.setStatus("current")
_ControlConnectionsTxChallengeResp_Type = Unsigned32
_ControlConnectionsTxChallengeResp_Object = MibTableColumn
controlConnectionsTxChallengeResp = _ControlConnectionsTxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 26),
    _ControlConnectionsTxChallengeResp_Type()
)
controlConnectionsTxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxChallengeResp.setStatus("current")
_ControlConnectionsTxChallengeAck_Type = Unsigned32
_ControlConnectionsTxChallengeAck_Object = MibTableColumn
controlConnectionsTxChallengeAck = _ControlConnectionsTxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 27),
    _ControlConnectionsTxChallengeAck_Type()
)
controlConnectionsTxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxChallengeAck.setStatus("current")
_ControlConnectionsTxTeardown_Type = Unsigned32
_ControlConnectionsTxTeardown_Object = MibTableColumn
controlConnectionsTxTeardown = _ControlConnectionsTxTeardown_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 28),
    _ControlConnectionsTxTeardown_Type()
)
controlConnectionsTxTeardown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxTeardown.setStatus("current")
_ControlConnectionsTxTeardownAll_Type = Unsigned32
_ControlConnectionsTxTeardownAll_Object = MibTableColumn
controlConnectionsTxTeardownAll = _ControlConnectionsTxTeardownAll_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 29),
    _ControlConnectionsTxTeardownAll_Type()
)
controlConnectionsTxTeardownAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxTeardownAll.setStatus("current")
_ControlConnectionsTxVmToPeer_Type = Unsigned32
_ControlConnectionsTxVmToPeer_Object = MibTableColumn
controlConnectionsTxVmToPeer = _ControlConnectionsTxVmToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 30),
    _ControlConnectionsTxVmToPeer_Type()
)
controlConnectionsTxVmToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxVmToPeer.setStatus("current")
_ControlConnectionsTxRegisterToVm_Type = Unsigned32
_ControlConnectionsTxRegisterToVm_Object = MibTableColumn
controlConnectionsTxRegisterToVm = _ControlConnectionsTxRegisterToVm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 31),
    _ControlConnectionsTxRegisterToVm_Type()
)
controlConnectionsTxRegisterToVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxRegisterToVm.setStatus("current")
_ControlConnectionsRxHello_Type = Unsigned32
_ControlConnectionsRxHello_Object = MibTableColumn
controlConnectionsRxHello = _ControlConnectionsRxHello_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 32),
    _ControlConnectionsRxHello_Type()
)
controlConnectionsRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxHello.setStatus("current")
_ControlConnectionsRxConnects_Type = Unsigned32
_ControlConnectionsRxConnects_Object = MibTableColumn
controlConnectionsRxConnects = _ControlConnectionsRxConnects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 33),
    _ControlConnectionsRxConnects_Type()
)
controlConnectionsRxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxConnects.setStatus("current")
_ControlConnectionsRxRegisters_Type = Unsigned32
_ControlConnectionsRxRegisters_Object = MibTableColumn
controlConnectionsRxRegisters = _ControlConnectionsRxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 34),
    _ControlConnectionsRxRegisters_Type()
)
controlConnectionsRxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxRegisters.setStatus("current")
_ControlConnectionsRxRegisterReplies_Type = Unsigned32
_ControlConnectionsRxRegisterReplies_Object = MibTableColumn
controlConnectionsRxRegisterReplies = _ControlConnectionsRxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 35),
    _ControlConnectionsRxRegisterReplies_Type()
)
controlConnectionsRxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxRegisterReplies.setStatus("current")
_ControlConnectionsRxChallenge_Type = Unsigned32
_ControlConnectionsRxChallenge_Object = MibTableColumn
controlConnectionsRxChallenge = _ControlConnectionsRxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 36),
    _ControlConnectionsRxChallenge_Type()
)
controlConnectionsRxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxChallenge.setStatus("current")
_ControlConnectionsRxChallengeResp_Type = Unsigned32
_ControlConnectionsRxChallengeResp_Object = MibTableColumn
controlConnectionsRxChallengeResp = _ControlConnectionsRxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 37),
    _ControlConnectionsRxChallengeResp_Type()
)
controlConnectionsRxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxChallengeResp.setStatus("current")
_ControlConnectionsRxChallengeAck_Type = Unsigned32
_ControlConnectionsRxChallengeAck_Object = MibTableColumn
controlConnectionsRxChallengeAck = _ControlConnectionsRxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 38),
    _ControlConnectionsRxChallengeAck_Type()
)
controlConnectionsRxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxChallengeAck.setStatus("current")
_ControlConnectionsRxTeardown_Type = Unsigned32
_ControlConnectionsRxTeardown_Object = MibTableColumn
controlConnectionsRxTeardown = _ControlConnectionsRxTeardown_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 39),
    _ControlConnectionsRxTeardown_Type()
)
controlConnectionsRxTeardown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxTeardown.setStatus("current")
_ControlConnectionsRxVmToPeer_Type = Unsigned32
_ControlConnectionsRxVmToPeer_Object = MibTableColumn
controlConnectionsRxVmToPeer = _ControlConnectionsRxVmToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 40),
    _ControlConnectionsRxVmToPeer_Type()
)
controlConnectionsRxVmToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxVmToPeer.setStatus("current")
_ControlConnectionsRxRegisterToVm_Type = Unsigned32
_ControlConnectionsRxRegisterToVm_Object = MibTableColumn
controlConnectionsRxRegisterToVm = _ControlConnectionsRxRegisterToVm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 41),
    _ControlConnectionsRxRegisterToVm_Type()
)
controlConnectionsRxRegisterToVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxRegisterToVm.setStatus("current")
_ControlConnectionsNegotiatedHelloInterval_Type = Unsigned32
_ControlConnectionsNegotiatedHelloInterval_Object = MibTableColumn
controlConnectionsNegotiatedHelloInterval = _ControlConnectionsNegotiatedHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 42),
    _ControlConnectionsNegotiatedHelloInterval_Type()
)
controlConnectionsNegotiatedHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsNegotiatedHelloInterval.setStatus("current")
_ControlConnectionsNegotiatedHelloTolerance_Type = Unsigned32
_ControlConnectionsNegotiatedHelloTolerance_Object = MibTableColumn
controlConnectionsNegotiatedHelloTolerance = _ControlConnectionsNegotiatedHelloTolerance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 43),
    _ControlConnectionsNegotiatedHelloTolerance_Type()
)
controlConnectionsNegotiatedHelloTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsNegotiatedHelloTolerance.setStatus("current")
_ControlConnectionsConfiguredSystemIp_Type = InetAddressIP
_ControlConnectionsConfiguredSystemIp_Object = MibTableColumn
controlConnectionsConfiguredSystemIp = _ControlConnectionsConfiguredSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 44),
    _ControlConnectionsConfiguredSystemIp_Type()
)
controlConnectionsConfiguredSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsConfiguredSystemIp.setStatus("current")
_ControlConnectionsVOrgName_Type = String
_ControlConnectionsVOrgName_Object = MibTableColumn
controlConnectionsVOrgName = _ControlConnectionsVOrgName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 45),
    _ControlConnectionsVOrgName_Type()
)
controlConnectionsVOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsVOrgName.setStatus("current")
_ControlConnectionsTxCreateCert_Type = Unsigned32
_ControlConnectionsTxCreateCert_Object = MibTableColumn
controlConnectionsTxCreateCert = _ControlConnectionsTxCreateCert_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 46),
    _ControlConnectionsTxCreateCert_Type()
)
controlConnectionsTxCreateCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxCreateCert.setStatus("current")
_ControlConnectionsRxCreateCert_Type = Unsigned32
_ControlConnectionsRxCreateCert_Object = MibTableColumn
controlConnectionsRxCreateCert = _ControlConnectionsRxCreateCert_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 47),
    _ControlConnectionsRxCreateCert_Type()
)
controlConnectionsRxCreateCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxCreateCert.setStatus("current")
_ControlConnectionsTxCreateCertReply_Type = Unsigned32
_ControlConnectionsTxCreateCertReply_Object = MibTableColumn
controlConnectionsTxCreateCertReply = _ControlConnectionsTxCreateCertReply_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 48),
    _ControlConnectionsTxCreateCertReply_Type()
)
controlConnectionsTxCreateCertReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxCreateCertReply.setStatus("current")
_ControlConnectionsRxCreateCertReply_Type = Unsigned32
_ControlConnectionsRxCreateCertReply_Object = MibTableColumn
controlConnectionsRxCreateCertReply = _ControlConnectionsRxCreateCertReply_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 49),
    _ControlConnectionsRxCreateCertReply_Type()
)
controlConnectionsRxCreateCertReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxCreateCertReply.setStatus("current")
_ControlConnectionsBehindProxy_Type = String
_ControlConnectionsBehindProxy_Object = MibTableColumn
controlConnectionsBehindProxy = _ControlConnectionsBehindProxy_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 2, 1, 50),
    _ControlConnectionsBehindProxy_Type()
)
controlConnectionsBehindProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsBehindProxy.setStatus("current")
_ControlConnectionsHistoryTable_Object = MibTable
controlConnectionsHistoryTable = _ControlConnectionsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3)
)
if mibBuilder.loadTexts:
    controlConnectionsHistoryTable.setStatus("current")
_ControlConnectionsHistoryEntry_Object = MibTableRow
controlConnectionsHistoryEntry = _ControlConnectionsHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1)
)
controlConnectionsHistoryEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "controlConnectionsHistoryInstance"),
    (0, "VIPTELA-SECURITY", "controlConnectionsHistoryIndex"),
)
if mibBuilder.loadTexts:
    controlConnectionsHistoryEntry.setStatus("current")
_ControlConnectionsHistoryInstance_Type = Unsigned32
_ControlConnectionsHistoryInstance_Object = MibTableColumn
controlConnectionsHistoryInstance = _ControlConnectionsHistoryInstance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 1),
    _ControlConnectionsHistoryInstance_Type()
)
controlConnectionsHistoryInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsHistoryInstance.setStatus("current")
_ControlConnectionsHistoryIndex_Type = Unsigned32
_ControlConnectionsHistoryIndex_Object = MibTableColumn
controlConnectionsHistoryIndex = _ControlConnectionsHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 2),
    _ControlConnectionsHistoryIndex_Type()
)
controlConnectionsHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsHistoryIndex.setStatus("current")


class _ControlConnectionsHistoryPeerType_Type(Integer32):
    """Custom type controlConnectionsHistoryPeerType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )


_ControlConnectionsHistoryPeerType_Type.__name__ = "Integer32"
_ControlConnectionsHistoryPeerType_Object = MibTableColumn
controlConnectionsHistoryPeerType = _ControlConnectionsHistoryPeerType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 3),
    _ControlConnectionsHistoryPeerType_Type()
)
controlConnectionsHistoryPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryPeerType.setStatus("current")
_ControlConnectionsHistorySiteId_Type = Unsigned32
_ControlConnectionsHistorySiteId_Object = MibTableColumn
controlConnectionsHistorySiteId = _ControlConnectionsHistorySiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 4),
    _ControlConnectionsHistorySiteId_Type()
)
controlConnectionsHistorySiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistorySiteId.setStatus("current")
_ControlConnectionsHistoryDomainId_Type = Unsigned32
_ControlConnectionsHistoryDomainId_Object = MibTableColumn
controlConnectionsHistoryDomainId = _ControlConnectionsHistoryDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 5),
    _ControlConnectionsHistoryDomainId_Type()
)
controlConnectionsHistoryDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryDomainId.setStatus("current")
_ControlConnectionsHistoryPrivateIp_Type = InetAddressIP
_ControlConnectionsHistoryPrivateIp_Object = MibTableColumn
controlConnectionsHistoryPrivateIp = _ControlConnectionsHistoryPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 6),
    _ControlConnectionsHistoryPrivateIp_Type()
)
controlConnectionsHistoryPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryPrivateIp.setStatus("current")
_ControlConnectionsHistoryPrivatePort_Type = Unsigned32
_ControlConnectionsHistoryPrivatePort_Object = MibTableColumn
controlConnectionsHistoryPrivatePort = _ControlConnectionsHistoryPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 7),
    _ControlConnectionsHistoryPrivatePort_Type()
)
controlConnectionsHistoryPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryPrivatePort.setStatus("current")
_ControlConnectionsHistoryPublicIp_Type = InetAddressIP
_ControlConnectionsHistoryPublicIp_Object = MibTableColumn
controlConnectionsHistoryPublicIp = _ControlConnectionsHistoryPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 8),
    _ControlConnectionsHistoryPublicIp_Type()
)
controlConnectionsHistoryPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryPublicIp.setStatus("current")
_ControlConnectionsHistoryPublicPort_Type = Unsigned32
_ControlConnectionsHistoryPublicPort_Object = MibTableColumn
controlConnectionsHistoryPublicPort = _ControlConnectionsHistoryPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 9),
    _ControlConnectionsHistoryPublicPort_Type()
)
controlConnectionsHistoryPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryPublicPort.setStatus("current")
_ControlConnectionsHistorySystemIp_Type = InetAddressIP
_ControlConnectionsHistorySystemIp_Object = MibTableColumn
controlConnectionsHistorySystemIp = _ControlConnectionsHistorySystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 10),
    _ControlConnectionsHistorySystemIp_Type()
)
controlConnectionsHistorySystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistorySystemIp.setStatus("current")


class _ControlConnectionsHistoryProtocol_Type(Integer32):
    """Custom type controlConnectionsHistoryProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dtls", 0),
          ("tls", 1))
    )


_ControlConnectionsHistoryProtocol_Type.__name__ = "Integer32"
_ControlConnectionsHistoryProtocol_Object = MibTableColumn
controlConnectionsHistoryProtocol = _ControlConnectionsHistoryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 11),
    _ControlConnectionsHistoryProtocol_Type()
)
controlConnectionsHistoryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryProtocol.setStatus("current")


class _ControlConnectionsHistoryLocalColor_Type(Integer32):
    """Custom type controlConnectionsHistoryLocalColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_ControlConnectionsHistoryLocalColor_Type.__name__ = "Integer32"
_ControlConnectionsHistoryLocalColor_Object = MibTableColumn
controlConnectionsHistoryLocalColor = _ControlConnectionsHistoryLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 12),
    _ControlConnectionsHistoryLocalColor_Type()
)
controlConnectionsHistoryLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryLocalColor.setStatus("current")


class _ControlConnectionsHistoryRemoteColor_Type(Integer32):
    """Custom type controlConnectionsHistoryRemoteColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_ControlConnectionsHistoryRemoteColor_Type.__name__ = "Integer32"
_ControlConnectionsHistoryRemoteColor_Object = MibTableColumn
controlConnectionsHistoryRemoteColor = _ControlConnectionsHistoryRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 13),
    _ControlConnectionsHistoryRemoteColor_Type()
)
controlConnectionsHistoryRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRemoteColor.setStatus("current")
_ControlConnectionsHistoryState_Type = SessionState
_ControlConnectionsHistoryState_Object = MibTableColumn
controlConnectionsHistoryState = _ControlConnectionsHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 14),
    _ControlConnectionsHistoryState_Type()
)
controlConnectionsHistoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryState.setStatus("current")
_ControlConnectionsHistoryLocalEnum_Type = ConnFlagEnum
_ControlConnectionsHistoryLocalEnum_Object = MibTableColumn
controlConnectionsHistoryLocalEnum = _ControlConnectionsHistoryLocalEnum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 15),
    _ControlConnectionsHistoryLocalEnum_Type()
)
controlConnectionsHistoryLocalEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryLocalEnum.setStatus("current")
_ControlConnectionsHistoryRemoteEnum_Type = ConnFlagEnum
_ControlConnectionsHistoryRemoteEnum_Object = MibTableColumn
controlConnectionsHistoryRemoteEnum = _ControlConnectionsHistoryRemoteEnum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 16),
    _ControlConnectionsHistoryRemoteEnum_Type()
)
controlConnectionsHistoryRemoteEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRemoteEnum.setStatus("current")
_ControlConnectionsHistoryLocalStateInfo_Type = String
_ControlConnectionsHistoryLocalStateInfo_Object = MibTableColumn
controlConnectionsHistoryLocalStateInfo = _ControlConnectionsHistoryLocalStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 17),
    _ControlConnectionsHistoryLocalStateInfo_Type()
)
controlConnectionsHistoryLocalStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryLocalStateInfo.setStatus("current")
_ControlConnectionsHistoryRemoteStateInfo_Type = String
_ControlConnectionsHistoryRemoteStateInfo_Object = MibTableColumn
controlConnectionsHistoryRemoteStateInfo = _ControlConnectionsHistoryRemoteStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 18),
    _ControlConnectionsHistoryRemoteStateInfo_Type()
)
controlConnectionsHistoryRemoteStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRemoteStateInfo.setStatus("current")
_ControlConnectionsHistoryDowntime_Type = String
_ControlConnectionsHistoryDowntime_Object = MibTableColumn
controlConnectionsHistoryDowntime = _ControlConnectionsHistoryDowntime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 19),
    _ControlConnectionsHistoryDowntime_Type()
)
controlConnectionsHistoryDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryDowntime.setStatus("current")
_ControlConnectionsHistoryTxHello_Type = Unsigned32
_ControlConnectionsHistoryTxHello_Object = MibTableColumn
controlConnectionsHistoryTxHello = _ControlConnectionsHistoryTxHello_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 20),
    _ControlConnectionsHistoryTxHello_Type()
)
controlConnectionsHistoryTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxHello.setStatus("current")
_ControlConnectionsHistoryTxConnects_Type = Unsigned32
_ControlConnectionsHistoryTxConnects_Object = MibTableColumn
controlConnectionsHistoryTxConnects = _ControlConnectionsHistoryTxConnects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 21),
    _ControlConnectionsHistoryTxConnects_Type()
)
controlConnectionsHistoryTxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxConnects.setStatus("current")
_ControlConnectionsHistoryTxRegisters_Type = Unsigned32
_ControlConnectionsHistoryTxRegisters_Object = MibTableColumn
controlConnectionsHistoryTxRegisters = _ControlConnectionsHistoryTxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 22),
    _ControlConnectionsHistoryTxRegisters_Type()
)
controlConnectionsHistoryTxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxRegisters.setStatus("current")
_ControlConnectionsHistoryTxRegisterReplies_Type = Unsigned32
_ControlConnectionsHistoryTxRegisterReplies_Object = MibTableColumn
controlConnectionsHistoryTxRegisterReplies = _ControlConnectionsHistoryTxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 23),
    _ControlConnectionsHistoryTxRegisterReplies_Type()
)
controlConnectionsHistoryTxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxRegisterReplies.setStatus("current")
_ControlConnectionsHistoryTxChallenge_Type = Unsigned32
_ControlConnectionsHistoryTxChallenge_Object = MibTableColumn
controlConnectionsHistoryTxChallenge = _ControlConnectionsHistoryTxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 24),
    _ControlConnectionsHistoryTxChallenge_Type()
)
controlConnectionsHistoryTxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxChallenge.setStatus("current")
_ControlConnectionsHistoryTxChallengeResp_Type = Unsigned32
_ControlConnectionsHistoryTxChallengeResp_Object = MibTableColumn
controlConnectionsHistoryTxChallengeResp = _ControlConnectionsHistoryTxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 25),
    _ControlConnectionsHistoryTxChallengeResp_Type()
)
controlConnectionsHistoryTxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxChallengeResp.setStatus("current")
_ControlConnectionsHistoryTxChallengeAck_Type = Unsigned32
_ControlConnectionsHistoryTxChallengeAck_Object = MibTableColumn
controlConnectionsHistoryTxChallengeAck = _ControlConnectionsHistoryTxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 26),
    _ControlConnectionsHistoryTxChallengeAck_Type()
)
controlConnectionsHistoryTxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxChallengeAck.setStatus("current")
_ControlConnectionsHistoryTxTeardown_Type = Unsigned32
_ControlConnectionsHistoryTxTeardown_Object = MibTableColumn
controlConnectionsHistoryTxTeardown = _ControlConnectionsHistoryTxTeardown_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 27),
    _ControlConnectionsHistoryTxTeardown_Type()
)
controlConnectionsHistoryTxTeardown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxTeardown.setStatus("current")
_ControlConnectionsHistoryTxTeardownAll_Type = Unsigned32
_ControlConnectionsHistoryTxTeardownAll_Object = MibTableColumn
controlConnectionsHistoryTxTeardownAll = _ControlConnectionsHistoryTxTeardownAll_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 28),
    _ControlConnectionsHistoryTxTeardownAll_Type()
)
controlConnectionsHistoryTxTeardownAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxTeardownAll.setStatus("current")
_ControlConnectionsHistoryTxVmToPeer_Type = Unsigned32
_ControlConnectionsHistoryTxVmToPeer_Object = MibTableColumn
controlConnectionsHistoryTxVmToPeer = _ControlConnectionsHistoryTxVmToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 29),
    _ControlConnectionsHistoryTxVmToPeer_Type()
)
controlConnectionsHistoryTxVmToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxVmToPeer.setStatus("current")
_ControlConnectionsHistoryTxRegisterToVm_Type = Unsigned32
_ControlConnectionsHistoryTxRegisterToVm_Object = MibTableColumn
controlConnectionsHistoryTxRegisterToVm = _ControlConnectionsHistoryTxRegisterToVm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 30),
    _ControlConnectionsHistoryTxRegisterToVm_Type()
)
controlConnectionsHistoryTxRegisterToVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxRegisterToVm.setStatus("current")
_ControlConnectionsHistoryRxHello_Type = Unsigned32
_ControlConnectionsHistoryRxHello_Object = MibTableColumn
controlConnectionsHistoryRxHello = _ControlConnectionsHistoryRxHello_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 31),
    _ControlConnectionsHistoryRxHello_Type()
)
controlConnectionsHistoryRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxHello.setStatus("current")
_ControlConnectionsHistoryRxConnects_Type = Unsigned32
_ControlConnectionsHistoryRxConnects_Object = MibTableColumn
controlConnectionsHistoryRxConnects = _ControlConnectionsHistoryRxConnects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 32),
    _ControlConnectionsHistoryRxConnects_Type()
)
controlConnectionsHistoryRxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxConnects.setStatus("current")
_ControlConnectionsHistoryRxRegisters_Type = Unsigned32
_ControlConnectionsHistoryRxRegisters_Object = MibTableColumn
controlConnectionsHistoryRxRegisters = _ControlConnectionsHistoryRxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 33),
    _ControlConnectionsHistoryRxRegisters_Type()
)
controlConnectionsHistoryRxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxRegisters.setStatus("current")
_ControlConnectionsHistoryRxRegisterReplies_Type = Unsigned32
_ControlConnectionsHistoryRxRegisterReplies_Object = MibTableColumn
controlConnectionsHistoryRxRegisterReplies = _ControlConnectionsHistoryRxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 34),
    _ControlConnectionsHistoryRxRegisterReplies_Type()
)
controlConnectionsHistoryRxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxRegisterReplies.setStatus("current")
_ControlConnectionsHistoryRxChallenge_Type = Unsigned32
_ControlConnectionsHistoryRxChallenge_Object = MibTableColumn
controlConnectionsHistoryRxChallenge = _ControlConnectionsHistoryRxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 35),
    _ControlConnectionsHistoryRxChallenge_Type()
)
controlConnectionsHistoryRxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxChallenge.setStatus("current")
_ControlConnectionsHistoryRxChallengeResp_Type = Unsigned32
_ControlConnectionsHistoryRxChallengeResp_Object = MibTableColumn
controlConnectionsHistoryRxChallengeResp = _ControlConnectionsHistoryRxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 36),
    _ControlConnectionsHistoryRxChallengeResp_Type()
)
controlConnectionsHistoryRxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxChallengeResp.setStatus("current")
_ControlConnectionsHistoryRxChallengeAck_Type = Unsigned32
_ControlConnectionsHistoryRxChallengeAck_Object = MibTableColumn
controlConnectionsHistoryRxChallengeAck = _ControlConnectionsHistoryRxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 37),
    _ControlConnectionsHistoryRxChallengeAck_Type()
)
controlConnectionsHistoryRxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxChallengeAck.setStatus("current")
_ControlConnectionsHistoryRxTeardown_Type = Unsigned32
_ControlConnectionsHistoryRxTeardown_Object = MibTableColumn
controlConnectionsHistoryRxTeardown = _ControlConnectionsHistoryRxTeardown_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 38),
    _ControlConnectionsHistoryRxTeardown_Type()
)
controlConnectionsHistoryRxTeardown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxTeardown.setStatus("current")
_ControlConnectionsHistoryRxVmToPeer_Type = Unsigned32
_ControlConnectionsHistoryRxVmToPeer_Object = MibTableColumn
controlConnectionsHistoryRxVmToPeer = _ControlConnectionsHistoryRxVmToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 39),
    _ControlConnectionsHistoryRxVmToPeer_Type()
)
controlConnectionsHistoryRxVmToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxVmToPeer.setStatus("current")
_ControlConnectionsHistoryRxRegisterToVm_Type = Unsigned32
_ControlConnectionsHistoryRxRegisterToVm_Object = MibTableColumn
controlConnectionsHistoryRxRegisterToVm = _ControlConnectionsHistoryRxRegisterToVm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 40),
    _ControlConnectionsHistoryRxRegisterToVm_Type()
)
controlConnectionsHistoryRxRegisterToVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxRegisterToVm.setStatus("current")
_ControlConnectionsHistoryRepCount_Type = Unsigned32
_ControlConnectionsHistoryRepCount_Object = MibTableColumn
controlConnectionsHistoryRepCount = _ControlConnectionsHistoryRepCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 41),
    _ControlConnectionsHistoryRepCount_Type()
)
controlConnectionsHistoryRepCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRepCount.setStatus("current")
_ControlConnectionsHistoryPrevDowntime_Type = String
_ControlConnectionsHistoryPrevDowntime_Object = MibTableColumn
controlConnectionsHistoryPrevDowntime = _ControlConnectionsHistoryPrevDowntime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 42),
    _ControlConnectionsHistoryPrevDowntime_Type()
)
controlConnectionsHistoryPrevDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryPrevDowntime.setStatus("current")
_ControlConnectionsHistoryConfiguredSystemIp_Type = InetAddressIP
_ControlConnectionsHistoryConfiguredSystemIp_Object = MibTableColumn
controlConnectionsHistoryConfiguredSystemIp = _ControlConnectionsHistoryConfiguredSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 43),
    _ControlConnectionsHistoryConfiguredSystemIp_Type()
)
controlConnectionsHistoryConfiguredSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryConfiguredSystemIp.setStatus("current")
_ControlConnectionsHistoryVHOrgName_Type = String
_ControlConnectionsHistoryVHOrgName_Object = MibTableColumn
controlConnectionsHistoryVHOrgName = _ControlConnectionsHistoryVHOrgName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 44),
    _ControlConnectionsHistoryVHOrgName_Type()
)
controlConnectionsHistoryVHOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryVHOrgName.setStatus("current")
_ControlConnectionsHistoryUuid_Type = String
_ControlConnectionsHistoryUuid_Object = MibTableColumn
controlConnectionsHistoryUuid = _ControlConnectionsHistoryUuid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 45),
    _ControlConnectionsHistoryUuid_Type()
)
controlConnectionsHistoryUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryUuid.setStatus("current")
_ControlConnectionsHistoryTxCreateCert_Type = Unsigned32
_ControlConnectionsHistoryTxCreateCert_Object = MibTableColumn
controlConnectionsHistoryTxCreateCert = _ControlConnectionsHistoryTxCreateCert_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 46),
    _ControlConnectionsHistoryTxCreateCert_Type()
)
controlConnectionsHistoryTxCreateCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxCreateCert.setStatus("current")
_ControlConnectionsHistoryRxCreateCert_Type = Unsigned32
_ControlConnectionsHistoryRxCreateCert_Object = MibTableColumn
controlConnectionsHistoryRxCreateCert = _ControlConnectionsHistoryRxCreateCert_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 47),
    _ControlConnectionsHistoryRxCreateCert_Type()
)
controlConnectionsHistoryRxCreateCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxCreateCert.setStatus("current")
_ControlConnectionsHistoryTxCreateCertReply_Type = Unsigned32
_ControlConnectionsHistoryTxCreateCertReply_Object = MibTableColumn
controlConnectionsHistoryTxCreateCertReply = _ControlConnectionsHistoryTxCreateCertReply_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 48),
    _ControlConnectionsHistoryTxCreateCertReply_Type()
)
controlConnectionsHistoryTxCreateCertReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxCreateCertReply.setStatus("current")
_ControlConnectionsHistoryRxCreateCertReply_Type = Unsigned32
_ControlConnectionsHistoryRxCreateCertReply_Object = MibTableColumn
controlConnectionsHistoryRxCreateCertReply = _ControlConnectionsHistoryRxCreateCertReply_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 3, 1, 49),
    _ControlConnectionsHistoryRxCreateCertReply_Type()
)
controlConnectionsHistoryRxCreateCertReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxCreateCertReply.setStatus("current")
_ControlStatistics_ObjectIdentity = ObjectIdentity
controlStatistics = _ControlStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4)
)
_ControlStatisticsTxPkts_Type = Counter64
_ControlStatisticsTxPkts_Object = MibScalar
controlStatisticsTxPkts = _ControlStatisticsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 1),
    _ControlStatisticsTxPkts_Type()
)
controlStatisticsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxPkts.setStatus("current")
_ControlStatisticsTxOctets_Type = Unsigned32
_ControlStatisticsTxOctets_Object = MibScalar
controlStatisticsTxOctets = _ControlStatisticsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 2),
    _ControlStatisticsTxOctets_Type()
)
controlStatisticsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxOctets.setStatus("current")
_ControlStatisticsTxError_Type = Unsigned32
_ControlStatisticsTxError_Object = MibScalar
controlStatisticsTxError = _ControlStatisticsTxError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 3),
    _ControlStatisticsTxError_Type()
)
controlStatisticsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxError.setStatus("current")
_ControlStatisticsTxBlocked_Type = Unsigned32
_ControlStatisticsTxBlocked_Object = MibScalar
controlStatisticsTxBlocked = _ControlStatisticsTxBlocked_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 4),
    _ControlStatisticsTxBlocked_Type()
)
controlStatisticsTxBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxBlocked.setStatus("current")
_ControlStatisticsTxHello_Type = Counter64
_ControlStatisticsTxHello_Object = MibScalar
controlStatisticsTxHello = _ControlStatisticsTxHello_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 5),
    _ControlStatisticsTxHello_Type()
)
controlStatisticsTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxHello.setStatus("current")
_ControlStatisticsTxConnects_Type = Unsigned32
_ControlStatisticsTxConnects_Object = MibScalar
controlStatisticsTxConnects = _ControlStatisticsTxConnects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 6),
    _ControlStatisticsTxConnects_Type()
)
controlStatisticsTxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxConnects.setStatus("current")
_ControlStatisticsTxRegisters_Type = Unsigned32
_ControlStatisticsTxRegisters_Object = MibScalar
controlStatisticsTxRegisters = _ControlStatisticsTxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 7),
    _ControlStatisticsTxRegisters_Type()
)
controlStatisticsTxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxRegisters.setStatus("current")
_ControlStatisticsTxRegisterReplies_Type = Unsigned32
_ControlStatisticsTxRegisterReplies_Object = MibScalar
controlStatisticsTxRegisterReplies = _ControlStatisticsTxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 8),
    _ControlStatisticsTxRegisterReplies_Type()
)
controlStatisticsTxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxRegisterReplies.setStatus("current")
_ControlStatisticsTxDtlsHandshake_Type = Unsigned32
_ControlStatisticsTxDtlsHandshake_Object = MibScalar
controlStatisticsTxDtlsHandshake = _ControlStatisticsTxDtlsHandshake_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 9),
    _ControlStatisticsTxDtlsHandshake_Type()
)
controlStatisticsTxDtlsHandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxDtlsHandshake.setStatus("current")
_ControlStatisticsTxDtlsHandshakeFailures_Type = Unsigned32
_ControlStatisticsTxDtlsHandshakeFailures_Object = MibScalar
controlStatisticsTxDtlsHandshakeFailures = _ControlStatisticsTxDtlsHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 10),
    _ControlStatisticsTxDtlsHandshakeFailures_Type()
)
controlStatisticsTxDtlsHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxDtlsHandshakeFailures.setStatus("current")
_ControlStatisticsTxDtlsHandshakeDone_Type = Unsigned32
_ControlStatisticsTxDtlsHandshakeDone_Object = MibScalar
controlStatisticsTxDtlsHandshakeDone = _ControlStatisticsTxDtlsHandshakeDone_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 11),
    _ControlStatisticsTxDtlsHandshakeDone_Type()
)
controlStatisticsTxDtlsHandshakeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxDtlsHandshakeDone.setStatus("current")
_ControlStatisticsTxChallenge_Type = Unsigned32
_ControlStatisticsTxChallenge_Object = MibScalar
controlStatisticsTxChallenge = _ControlStatisticsTxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 12),
    _ControlStatisticsTxChallenge_Type()
)
controlStatisticsTxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallenge.setStatus("current")
_ControlStatisticsTxChallengeResp_Type = Unsigned32
_ControlStatisticsTxChallengeResp_Object = MibScalar
controlStatisticsTxChallengeResp = _ControlStatisticsTxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 13),
    _ControlStatisticsTxChallengeResp_Type()
)
controlStatisticsTxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallengeResp.setStatus("current")
_ControlStatisticsTxChallengeAck_Type = Unsigned32
_ControlStatisticsTxChallengeAck_Object = MibScalar
controlStatisticsTxChallengeAck = _ControlStatisticsTxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 14),
    _ControlStatisticsTxChallengeAck_Type()
)
controlStatisticsTxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallengeAck.setStatus("current")
_ControlStatisticsTxChallengeError_Type = Unsigned32
_ControlStatisticsTxChallengeError_Object = MibScalar
controlStatisticsTxChallengeError = _ControlStatisticsTxChallengeError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 15),
    _ControlStatisticsTxChallengeError_Type()
)
controlStatisticsTxChallengeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallengeError.setStatus("current")
_ControlStatisticsTxChallengeRespError_Type = Unsigned32
_ControlStatisticsTxChallengeRespError_Object = MibScalar
controlStatisticsTxChallengeRespError = _ControlStatisticsTxChallengeRespError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 16),
    _ControlStatisticsTxChallengeRespError_Type()
)
controlStatisticsTxChallengeRespError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallengeRespError.setStatus("current")
_ControlStatisticsTxChallengeAckError_Type = Unsigned32
_ControlStatisticsTxChallengeAckError_Object = MibScalar
controlStatisticsTxChallengeAckError = _ControlStatisticsTxChallengeAckError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 17),
    _ControlStatisticsTxChallengeAckError_Type()
)
controlStatisticsTxChallengeAckError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallengeAckError.setStatus("current")
_ControlStatisticsTxChallengeGenError_Type = Unsigned32
_ControlStatisticsTxChallengeGenError_Object = MibScalar
controlStatisticsTxChallengeGenError = _ControlStatisticsTxChallengeGenError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 18),
    _ControlStatisticsTxChallengeGenError_Type()
)
controlStatisticsTxChallengeGenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallengeGenError.setStatus("current")
_ControlStatisticsTxVmanageToPeer_Type = Unsigned32
_ControlStatisticsTxVmanageToPeer_Object = MibScalar
controlStatisticsTxVmanageToPeer = _ControlStatisticsTxVmanageToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 19),
    _ControlStatisticsTxVmanageToPeer_Type()
)
controlStatisticsTxVmanageToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxVmanageToPeer.setStatus("current")
_ControlStatisticsTxRegisterToVmanage_Type = Unsigned32
_ControlStatisticsTxRegisterToVmanage_Object = MibScalar
controlStatisticsTxRegisterToVmanage = _ControlStatisticsTxRegisterToVmanage_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 20),
    _ControlStatisticsTxRegisterToVmanage_Type()
)
controlStatisticsTxRegisterToVmanage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxRegisterToVmanage.setStatus("current")
_ControlStatisticsRxPkts_Type = Counter64
_ControlStatisticsRxPkts_Object = MibScalar
controlStatisticsRxPkts = _ControlStatisticsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 21),
    _ControlStatisticsRxPkts_Type()
)
controlStatisticsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxPkts.setStatus("current")
_ControlStatisticsRxOctets_Type = Unsigned32
_ControlStatisticsRxOctets_Object = MibScalar
controlStatisticsRxOctets = _ControlStatisticsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 22),
    _ControlStatisticsRxOctets_Type()
)
controlStatisticsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxOctets.setStatus("current")
_ControlStatisticsRxError_Type = Unsigned32
_ControlStatisticsRxError_Object = MibScalar
controlStatisticsRxError = _ControlStatisticsRxError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 23),
    _ControlStatisticsRxError_Type()
)
controlStatisticsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxError.setStatus("current")
_ControlStatisticsRxHello_Type = Counter64
_ControlStatisticsRxHello_Object = MibScalar
controlStatisticsRxHello = _ControlStatisticsRxHello_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 24),
    _ControlStatisticsRxHello_Type()
)
controlStatisticsRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxHello.setStatus("current")
_ControlStatisticsRxConnects_Type = Unsigned32
_ControlStatisticsRxConnects_Object = MibScalar
controlStatisticsRxConnects = _ControlStatisticsRxConnects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 25),
    _ControlStatisticsRxConnects_Type()
)
controlStatisticsRxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxConnects.setStatus("current")
_ControlStatisticsRxRegisters_Type = Unsigned32
_ControlStatisticsRxRegisters_Object = MibScalar
controlStatisticsRxRegisters = _ControlStatisticsRxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 26),
    _ControlStatisticsRxRegisters_Type()
)
controlStatisticsRxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxRegisters.setStatus("current")
_ControlStatisticsRxRegisterReplies_Type = Unsigned32
_ControlStatisticsRxRegisterReplies_Object = MibScalar
controlStatisticsRxRegisterReplies = _ControlStatisticsRxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 27),
    _ControlStatisticsRxRegisterReplies_Type()
)
controlStatisticsRxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxRegisterReplies.setStatus("current")
_ControlStatisticsRxDtlsHandshake_Type = Unsigned32
_ControlStatisticsRxDtlsHandshake_Object = MibScalar
controlStatisticsRxDtlsHandshake = _ControlStatisticsRxDtlsHandshake_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 28),
    _ControlStatisticsRxDtlsHandshake_Type()
)
controlStatisticsRxDtlsHandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxDtlsHandshake.setStatus("current")
_ControlStatisticsRxDtlsHandshakeFailures_Type = Unsigned32
_ControlStatisticsRxDtlsHandshakeFailures_Object = MibScalar
controlStatisticsRxDtlsHandshakeFailures = _ControlStatisticsRxDtlsHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 29),
    _ControlStatisticsRxDtlsHandshakeFailures_Type()
)
controlStatisticsRxDtlsHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxDtlsHandshakeFailures.setStatus("current")
_ControlStatisticsRxDtlsHandshakeDone_Type = Unsigned32
_ControlStatisticsRxDtlsHandshakeDone_Object = MibScalar
controlStatisticsRxDtlsHandshakeDone = _ControlStatisticsRxDtlsHandshakeDone_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 30),
    _ControlStatisticsRxDtlsHandshakeDone_Type()
)
controlStatisticsRxDtlsHandshakeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxDtlsHandshakeDone.setStatus("current")
_ControlStatisticsRxChallenge_Type = Unsigned32
_ControlStatisticsRxChallenge_Object = MibScalar
controlStatisticsRxChallenge = _ControlStatisticsRxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 31),
    _ControlStatisticsRxChallenge_Type()
)
controlStatisticsRxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxChallenge.setStatus("current")
_ControlStatisticsRxChallengeResp_Type = Unsigned32
_ControlStatisticsRxChallengeResp_Object = MibScalar
controlStatisticsRxChallengeResp = _ControlStatisticsRxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 32),
    _ControlStatisticsRxChallengeResp_Type()
)
controlStatisticsRxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxChallengeResp.setStatus("current")
_ControlStatisticsRxChallengeAck_Type = Unsigned32
_ControlStatisticsRxChallengeAck_Object = MibScalar
controlStatisticsRxChallengeAck = _ControlStatisticsRxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 33),
    _ControlStatisticsRxChallengeAck_Type()
)
controlStatisticsRxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxChallengeAck.setStatus("current")
_ControlStatisticsChallengeFailures_Type = Unsigned32
_ControlStatisticsChallengeFailures_Object = MibScalar
controlStatisticsChallengeFailures = _ControlStatisticsChallengeFailures_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 34),
    _ControlStatisticsChallengeFailures_Type()
)
controlStatisticsChallengeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsChallengeFailures.setStatus("current")
_ControlStatisticsRxVmanageToPeer_Type = Unsigned32
_ControlStatisticsRxVmanageToPeer_Object = MibScalar
controlStatisticsRxVmanageToPeer = _ControlStatisticsRxVmanageToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 35),
    _ControlStatisticsRxVmanageToPeer_Type()
)
controlStatisticsRxVmanageToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxVmanageToPeer.setStatus("current")
_ControlStatisticsRxRegisterToVmanage_Type = Unsigned32
_ControlStatisticsRxRegisterToVmanage_Object = MibScalar
controlStatisticsRxRegisterToVmanage = _ControlStatisticsRxRegisterToVmanage_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 36),
    _ControlStatisticsRxRegisterToVmanage_Type()
)
controlStatisticsRxRegisterToVmanage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxRegisterToVmanage.setStatus("current")
_ControlStatisticsBidFailuresNeedingReset_Type = Unsigned32
_ControlStatisticsBidFailuresNeedingReset_Object = MibScalar
controlStatisticsBidFailuresNeedingReset = _ControlStatisticsBidFailuresNeedingReset_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 4, 37),
    _ControlStatisticsBidFailuresNeedingReset_Type()
)
controlStatisticsBidFailuresNeedingReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsBidFailuresNeedingReset.setStatus("current")
_ControlLocalProperties_ObjectIdentity = ObjectIdentity
controlLocalProperties = _ControlLocalProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5)
)


class _ControlLocalPropertiesDeviceType_Type(Integer32):
    """Custom type controlLocalPropertiesDeviceType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )


_ControlLocalPropertiesDeviceType_Type.__name__ = "Integer32"
_ControlLocalPropertiesDeviceType_Object = MibScalar
controlLocalPropertiesDeviceType = _ControlLocalPropertiesDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 1),
    _ControlLocalPropertiesDeviceType_Type()
)
controlLocalPropertiesDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesDeviceType.setStatus("current")


class _ControlLocalPropertiesOrganizationName_Type(String):
    """Custom type controlLocalPropertiesOrganizationName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ControlLocalPropertiesOrganizationName_Type.__name__ = "String"
_ControlLocalPropertiesOrganizationName_Object = MibScalar
controlLocalPropertiesOrganizationName = _ControlLocalPropertiesOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 2),
    _ControlLocalPropertiesOrganizationName_Type()
)
controlLocalPropertiesOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesOrganizationName.setStatus("current")
_ControlLocalPropertiesCertificateStatus_Type = String
_ControlLocalPropertiesCertificateStatus_Object = MibScalar
controlLocalPropertiesCertificateStatus = _ControlLocalPropertiesCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 3),
    _ControlLocalPropertiesCertificateStatus_Type()
)
controlLocalPropertiesCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesCertificateStatus.setStatus("current")
_ControlLocalPropertiesRootCaChainStatus_Type = String
_ControlLocalPropertiesRootCaChainStatus_Object = MibScalar
controlLocalPropertiesRootCaChainStatus = _ControlLocalPropertiesRootCaChainStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 4),
    _ControlLocalPropertiesRootCaChainStatus_Type()
)
controlLocalPropertiesRootCaChainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesRootCaChainStatus.setStatus("current")
_ControlLocalPropertiesCertificateValidity_Type = String
_ControlLocalPropertiesCertificateValidity_Object = MibScalar
controlLocalPropertiesCertificateValidity = _ControlLocalPropertiesCertificateValidity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 5),
    _ControlLocalPropertiesCertificateValidity_Type()
)
controlLocalPropertiesCertificateValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesCertificateValidity.setStatus("current")
_ControlLocalPropertiesCertificateNotValidBefore_Type = String
_ControlLocalPropertiesCertificateNotValidBefore_Object = MibScalar
controlLocalPropertiesCertificateNotValidBefore = _ControlLocalPropertiesCertificateNotValidBefore_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 6),
    _ControlLocalPropertiesCertificateNotValidBefore_Type()
)
controlLocalPropertiesCertificateNotValidBefore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesCertificateNotValidBefore.setStatus("current")
_ControlLocalPropertiesCertificateNotValidAfter_Type = String
_ControlLocalPropertiesCertificateNotValidAfter_Object = MibScalar
controlLocalPropertiesCertificateNotValidAfter = _ControlLocalPropertiesCertificateNotValidAfter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 7),
    _ControlLocalPropertiesCertificateNotValidAfter_Type()
)
controlLocalPropertiesCertificateNotValidAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesCertificateNotValidAfter.setStatus("current")
_ControlLocalPropertiesDnsName_Type = String
_ControlLocalPropertiesDnsName_Object = MibScalar
controlLocalPropertiesDnsName = _ControlLocalPropertiesDnsName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 8),
    _ControlLocalPropertiesDnsName_Type()
)
controlLocalPropertiesDnsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesDnsName.setStatus("current")
_ControlLocalPropertiesSiteId_Type = Unsigned32
_ControlLocalPropertiesSiteId_Object = MibScalar
controlLocalPropertiesSiteId = _ControlLocalPropertiesSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 9),
    _ControlLocalPropertiesSiteId_Type()
)
controlLocalPropertiesSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesSiteId.setStatus("current")
_ControlLocalPropertiesDomainId_Type = Unsigned32
_ControlLocalPropertiesDomainId_Object = MibScalar
controlLocalPropertiesDomainId = _ControlLocalPropertiesDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 10),
    _ControlLocalPropertiesDomainId_Type()
)
controlLocalPropertiesDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesDomainId.setStatus("current")


class _ControlLocalPropertiesProtocol_Type(Integer32):
    """Custom type controlLocalPropertiesProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dtls", 0),
          ("tls", 1))
    )


_ControlLocalPropertiesProtocol_Type.__name__ = "Integer32"
_ControlLocalPropertiesProtocol_Object = MibScalar
controlLocalPropertiesProtocol = _ControlLocalPropertiesProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 11),
    _ControlLocalPropertiesProtocol_Type()
)
controlLocalPropertiesProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesProtocol.setStatus("current")
_ControlLocalPropertiesTlsPort_Type = Unsigned32
_ControlLocalPropertiesTlsPort_Object = MibScalar
controlLocalPropertiesTlsPort = _ControlLocalPropertiesTlsPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 12),
    _ControlLocalPropertiesTlsPort_Type()
)
controlLocalPropertiesTlsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesTlsPort.setStatus("current")
_ControlLocalPropertiesSystemIp_Type = InetAddressIP
_ControlLocalPropertiesSystemIp_Object = MibScalar
controlLocalPropertiesSystemIp = _ControlLocalPropertiesSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 13),
    _ControlLocalPropertiesSystemIp_Type()
)
controlLocalPropertiesSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesSystemIp.setStatus("current")
_ControlLocalPropertiesUuid_Type = String
_ControlLocalPropertiesUuid_Object = MibScalar
controlLocalPropertiesUuid = _ControlLocalPropertiesUuid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 14),
    _ControlLocalPropertiesUuid_Type()
)
controlLocalPropertiesUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesUuid.setStatus("current")


class _ControlLocalPropertiesBoardSerial_Type(String):
    """Custom type controlLocalPropertiesBoardSerial based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ControlLocalPropertiesBoardSerial_Type.__name__ = "String"
_ControlLocalPropertiesBoardSerial_Object = MibScalar
controlLocalPropertiesBoardSerial = _ControlLocalPropertiesBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 15),
    _ControlLocalPropertiesBoardSerial_Type()
)
controlLocalPropertiesBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesBoardSerial.setStatus("current")
_ControlLocalPropertiesRegisterInterval_Type = String
_ControlLocalPropertiesRegisterInterval_Object = MibScalar
controlLocalPropertiesRegisterInterval = _ControlLocalPropertiesRegisterInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 16),
    _ControlLocalPropertiesRegisterInterval_Type()
)
controlLocalPropertiesRegisterInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesRegisterInterval.setStatus("deprecated")
_ControlLocalPropertiesRetryInterval_Type = String
_ControlLocalPropertiesRetryInterval_Object = MibScalar
controlLocalPropertiesRetryInterval = _ControlLocalPropertiesRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 17),
    _ControlLocalPropertiesRetryInterval_Type()
)
controlLocalPropertiesRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesRetryInterval.setStatus("current")
_ControlLocalPropertiesNoActivity_Type = String
_ControlLocalPropertiesNoActivity_Object = MibScalar
controlLocalPropertiesNoActivity = _ControlLocalPropertiesNoActivity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 18),
    _ControlLocalPropertiesNoActivity_Type()
)
controlLocalPropertiesNoActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesNoActivity.setStatus("current")
_ControlLocalPropertiesDnsCacheFlushInterval_Type = String
_ControlLocalPropertiesDnsCacheFlushInterval_Object = MibScalar
controlLocalPropertiesDnsCacheFlushInterval = _ControlLocalPropertiesDnsCacheFlushInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 19),
    _ControlLocalPropertiesDnsCacheFlushInterval_Type()
)
controlLocalPropertiesDnsCacheFlushInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesDnsCacheFlushInterval.setStatus("current")
_ControlLocalPropertiesPortHopped_Type = String
_ControlLocalPropertiesPortHopped_Object = MibScalar
controlLocalPropertiesPortHopped = _ControlLocalPropertiesPortHopped_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 20),
    _ControlLocalPropertiesPortHopped_Type()
)
controlLocalPropertiesPortHopped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesPortHopped.setStatus("current")
_ControlLocalPropertiesTimeSincePortHop_Type = String
_ControlLocalPropertiesTimeSincePortHop_Object = MibScalar
controlLocalPropertiesTimeSincePortHop = _ControlLocalPropertiesTimeSincePortHop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 21),
    _ControlLocalPropertiesTimeSincePortHop_Type()
)
controlLocalPropertiesTimeSincePortHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesTimeSincePortHop.setStatus("current")
_ControlLocalPropertiesMaxControllers_Type = UnsignedByte
_ControlLocalPropertiesMaxControllers_Object = MibScalar
controlLocalPropertiesMaxControllers = _ControlLocalPropertiesMaxControllers_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 22),
    _ControlLocalPropertiesMaxControllers_Type()
)
controlLocalPropertiesMaxControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesMaxControllers.setStatus("current")
_ControlLocalPropertiesKeygenInterval_Type = String
_ControlLocalPropertiesKeygenInterval_Object = MibScalar
controlLocalPropertiesKeygenInterval = _ControlLocalPropertiesKeygenInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 23),
    _ControlLocalPropertiesKeygenInterval_Type()
)
controlLocalPropertiesKeygenInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesKeygenInterval.setStatus("current")
_ControlLocalPropertiesIpAddressListTable_Object = MibTable
controlLocalPropertiesIpAddressListTable = _ControlLocalPropertiesIpAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 24)
)
if mibBuilder.loadTexts:
    controlLocalPropertiesIpAddressListTable.setStatus("current")
_ControlLocalPropertiesIpAddressListEntry_Object = MibTableRow
controlLocalPropertiesIpAddressListEntry = _ControlLocalPropertiesIpAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 24, 1)
)
controlLocalPropertiesIpAddressListEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "controlLocalPropertiesIpAddressListIndex"),
)
if mibBuilder.loadTexts:
    controlLocalPropertiesIpAddressListEntry.setStatus("current")
_ControlLocalPropertiesIpAddressListIndex_Type = Unsigned32
_ControlLocalPropertiesIpAddressListIndex_Object = MibTableColumn
controlLocalPropertiesIpAddressListIndex = _ControlLocalPropertiesIpAddressListIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 24, 1, 1),
    _ControlLocalPropertiesIpAddressListIndex_Type()
)
controlLocalPropertiesIpAddressListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlLocalPropertiesIpAddressListIndex.setStatus("current")
_ControlLocalPropertiesIpAddressListIp_Type = InetAddressIP
_ControlLocalPropertiesIpAddressListIp_Object = MibTableColumn
controlLocalPropertiesIpAddressListIp = _ControlLocalPropertiesIpAddressListIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 24, 1, 2),
    _ControlLocalPropertiesIpAddressListIp_Type()
)
controlLocalPropertiesIpAddressListIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesIpAddressListIp.setStatus("current")
_ControlLocalPropertiesIpAddressListPort_Type = Unsigned32
_ControlLocalPropertiesIpAddressListPort_Object = MibTableColumn
controlLocalPropertiesIpAddressListPort = _ControlLocalPropertiesIpAddressListPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 24, 1, 3),
    _ControlLocalPropertiesIpAddressListPort_Type()
)
controlLocalPropertiesIpAddressListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesIpAddressListPort.setStatus("current")
_ControlLocalPropertiesNumberVbondPeers_Type = Unsigned32
_ControlLocalPropertiesNumberVbondPeers_Object = MibScalar
controlLocalPropertiesNumberVbondPeers = _ControlLocalPropertiesNumberVbondPeers_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 25),
    _ControlLocalPropertiesNumberVbondPeers_Type()
)
controlLocalPropertiesNumberVbondPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesNumberVbondPeers.setStatus("current")
_ControlLocalPropertiesVbondAddressListTable_Object = MibTable
controlLocalPropertiesVbondAddressListTable = _ControlLocalPropertiesVbondAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 26)
)
if mibBuilder.loadTexts:
    controlLocalPropertiesVbondAddressListTable.setStatus("current")
_ControlLocalPropertiesVbondAddressListEntry_Object = MibTableRow
controlLocalPropertiesVbondAddressListEntry = _ControlLocalPropertiesVbondAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 26, 1)
)
controlLocalPropertiesVbondAddressListEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "controlLocalPropertiesVbondAddressListIndex"),
)
if mibBuilder.loadTexts:
    controlLocalPropertiesVbondAddressListEntry.setStatus("current")
_ControlLocalPropertiesVbondAddressListIndex_Type = Unsigned32
_ControlLocalPropertiesVbondAddressListIndex_Object = MibTableColumn
controlLocalPropertiesVbondAddressListIndex = _ControlLocalPropertiesVbondAddressListIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 26, 1, 1),
    _ControlLocalPropertiesVbondAddressListIndex_Type()
)
controlLocalPropertiesVbondAddressListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlLocalPropertiesVbondAddressListIndex.setStatus("current")
_ControlLocalPropertiesVbondAddressListIp_Type = InetAddressIP
_ControlLocalPropertiesVbondAddressListIp_Object = MibTableColumn
controlLocalPropertiesVbondAddressListIp = _ControlLocalPropertiesVbondAddressListIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 26, 1, 2),
    _ControlLocalPropertiesVbondAddressListIp_Type()
)
controlLocalPropertiesVbondAddressListIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesVbondAddressListIp.setStatus("current")
_ControlLocalPropertiesVbondAddressListPort_Type = Unsigned32
_ControlLocalPropertiesVbondAddressListPort_Object = MibTableColumn
controlLocalPropertiesVbondAddressListPort = _ControlLocalPropertiesVbondAddressListPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 26, 1, 3),
    _ControlLocalPropertiesVbondAddressListPort_Type()
)
controlLocalPropertiesVbondAddressListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesVbondAddressListPort.setStatus("current")
_ControlLocalPropertiesNumberActiveWanInterfaces_Type = Unsigned32
_ControlLocalPropertiesNumberActiveWanInterfaces_Object = MibScalar
controlLocalPropertiesNumberActiveWanInterfaces = _ControlLocalPropertiesNumberActiveWanInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 27),
    _ControlLocalPropertiesNumberActiveWanInterfaces_Type()
)
controlLocalPropertiesNumberActiveWanInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesNumberActiveWanInterfaces.setStatus("current")
_ControlLocalPropertiesWanInterfaceListTable_Object = MibTable
controlLocalPropertiesWanInterfaceListTable = _ControlLocalPropertiesWanInterfaceListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28)
)
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListTable.setStatus("current")
_ControlLocalPropertiesWanInterfaceListEntry_Object = MibTableRow
controlLocalPropertiesWanInterfaceListEntry = _ControlLocalPropertiesWanInterfaceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1)
)
controlLocalPropertiesWanInterfaceListEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "controlLocalPropertiesWanInterfaceListInstance"),
    (0, "VIPTELA-SECURITY", "controlLocalPropertiesWanInterfaceListIndex"),
)
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListEntry.setStatus("current")
_ControlLocalPropertiesWanInterfaceListIndex_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListIndex_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListIndex = _ControlLocalPropertiesWanInterfaceListIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 1),
    _ControlLocalPropertiesWanInterfaceListIndex_Type()
)
controlLocalPropertiesWanInterfaceListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListIndex.setStatus("current")


class _ControlLocalPropertiesWanInterfaceListInterface_Type(String):
    """Custom type controlLocalPropertiesWanInterfaceListInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ControlLocalPropertiesWanInterfaceListInterface_Type.__name__ = "String"
_ControlLocalPropertiesWanInterfaceListInterface_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListInterface = _ControlLocalPropertiesWanInterfaceListInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 2),
    _ControlLocalPropertiesWanInterfaceListInterface_Type()
)
controlLocalPropertiesWanInterfaceListInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListInterface.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPublicIp_Type = InetAddressIP
_ControlLocalPropertiesWanInterfaceListPublicIp_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPublicIp = _ControlLocalPropertiesWanInterfaceListPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 3),
    _ControlLocalPropertiesWanInterfaceListPublicIp_Type()
)
controlLocalPropertiesWanInterfaceListPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPublicIp.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPublicPort_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListPublicPort_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPublicPort = _ControlLocalPropertiesWanInterfaceListPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 4),
    _ControlLocalPropertiesWanInterfaceListPublicPort_Type()
)
controlLocalPropertiesWanInterfaceListPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPublicPort.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPrivateIp_Type = InetAddressIP
_ControlLocalPropertiesWanInterfaceListPrivateIp_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPrivateIp = _ControlLocalPropertiesWanInterfaceListPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 5),
    _ControlLocalPropertiesWanInterfaceListPrivateIp_Type()
)
controlLocalPropertiesWanInterfaceListPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPrivateIp.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPrivatePort_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListPrivatePort_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPrivatePort = _ControlLocalPropertiesWanInterfaceListPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 6),
    _ControlLocalPropertiesWanInterfaceListPrivatePort_Type()
)
controlLocalPropertiesWanInterfaceListPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPrivatePort.setStatus("current")
_ControlLocalPropertiesWanInterfaceListNumVsmarts_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListNumVsmarts_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListNumVsmarts = _ControlLocalPropertiesWanInterfaceListNumVsmarts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 7),
    _ControlLocalPropertiesWanInterfaceListNumVsmarts_Type()
)
controlLocalPropertiesWanInterfaceListNumVsmarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListNumVsmarts.setStatus("current")
_ControlLocalPropertiesWanInterfaceListNumVmanages_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListNumVmanages_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListNumVmanages = _ControlLocalPropertiesWanInterfaceListNumVmanages_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 8),
    _ControlLocalPropertiesWanInterfaceListNumVmanages_Type()
)
controlLocalPropertiesWanInterfaceListNumVmanages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListNumVmanages.setStatus("current")
_ControlLocalPropertiesWanInterfaceListWeight_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListWeight_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListWeight = _ControlLocalPropertiesWanInterfaceListWeight_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 9),
    _ControlLocalPropertiesWanInterfaceListWeight_Type()
)
controlLocalPropertiesWanInterfaceListWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListWeight.setStatus("current")


class _ControlLocalPropertiesWanInterfaceListColor_Type(Integer32):
    """Custom type controlLocalPropertiesWanInterfaceListColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_ControlLocalPropertiesWanInterfaceListColor_Type.__name__ = "Integer32"
_ControlLocalPropertiesWanInterfaceListColor_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListColor = _ControlLocalPropertiesWanInterfaceListColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 10),
    _ControlLocalPropertiesWanInterfaceListColor_Type()
)
controlLocalPropertiesWanInterfaceListColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListColor.setStatus("current")


class _ControlLocalPropertiesWanInterfaceListCarrier_Type(Integer32):
    """Custom type controlLocalPropertiesWanInterfaceListCarrier based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("carrier1", 2),
          ("carrier2", 3),
          ("carrier3", 4),
          ("carrier4", 5),
          ("carrier5", 6),
          ("carrier6", 7),
          ("carrier7", 8),
          ("carrier8", 9))
    )


_ControlLocalPropertiesWanInterfaceListCarrier_Type.__name__ = "Integer32"
_ControlLocalPropertiesWanInterfaceListCarrier_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListCarrier = _ControlLocalPropertiesWanInterfaceListCarrier_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 11),
    _ControlLocalPropertiesWanInterfaceListCarrier_Type()
)
controlLocalPropertiesWanInterfaceListCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListCarrier.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPreference_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListPreference_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPreference = _ControlLocalPropertiesWanInterfaceListPreference_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 12),
    _ControlLocalPropertiesWanInterfaceListPreference_Type()
)
controlLocalPropertiesWanInterfaceListPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPreference.setStatus("current")
_ControlLocalPropertiesWanInterfaceListAdminState_Type = StateEnum
_ControlLocalPropertiesWanInterfaceListAdminState_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListAdminState = _ControlLocalPropertiesWanInterfaceListAdminState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 13),
    _ControlLocalPropertiesWanInterfaceListAdminState_Type()
)
controlLocalPropertiesWanInterfaceListAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListAdminState.setStatus("current")
_ControlLocalPropertiesWanInterfaceListOperationState_Type = StateEnum
_ControlLocalPropertiesWanInterfaceListOperationState_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListOperationState = _ControlLocalPropertiesWanInterfaceListOperationState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 14),
    _ControlLocalPropertiesWanInterfaceListOperationState_Type()
)
controlLocalPropertiesWanInterfaceListOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListOperationState.setStatus("current")
_ControlLocalPropertiesWanInterfaceListLastConnTime_Type = String
_ControlLocalPropertiesWanInterfaceListLastConnTime_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListLastConnTime = _ControlLocalPropertiesWanInterfaceListLastConnTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 15),
    _ControlLocalPropertiesWanInterfaceListLastConnTime_Type()
)
controlLocalPropertiesWanInterfaceListLastConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListLastConnTime.setStatus("current")
_ControlLocalPropertiesWanInterfaceListRestrictStr_Type = String
_ControlLocalPropertiesWanInterfaceListRestrictStr_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListRestrictStr = _ControlLocalPropertiesWanInterfaceListRestrictStr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 16),
    _ControlLocalPropertiesWanInterfaceListRestrictStr_Type()
)
controlLocalPropertiesWanInterfaceListRestrictStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListRestrictStr.setStatus("current")
_ControlLocalPropertiesWanInterfaceListControlStr_Type = String
_ControlLocalPropertiesWanInterfaceListControlStr_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListControlStr = _ControlLocalPropertiesWanInterfaceListControlStr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 17),
    _ControlLocalPropertiesWanInterfaceListControlStr_Type()
)
controlLocalPropertiesWanInterfaceListControlStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListControlStr.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPerWanMaxControllers_Type = UnsignedByte
_ControlLocalPropertiesWanInterfaceListPerWanMaxControllers_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPerWanMaxControllers = _ControlLocalPropertiesWanInterfaceListPerWanMaxControllers_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 18),
    _ControlLocalPropertiesWanInterfaceListPerWanMaxControllers_Type()
)
controlLocalPropertiesWanInterfaceListPerWanMaxControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPerWanMaxControllers.setStatus("current")
_ControlLocalPropertiesWanInterfaceListInstance_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListInstance_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListInstance = _ControlLocalPropertiesWanInterfaceListInstance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 19),
    _ControlLocalPropertiesWanInterfaceListInstance_Type()
)
controlLocalPropertiesWanInterfaceListInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListInstance.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPrivateIpv6_Type = InetAddressIP
_ControlLocalPropertiesWanInterfaceListPrivateIpv6_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPrivateIpv6 = _ControlLocalPropertiesWanInterfaceListPrivateIpv6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 20),
    _ControlLocalPropertiesWanInterfaceListPrivateIpv6_Type()
)
controlLocalPropertiesWanInterfaceListPrivateIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPrivateIpv6.setStatus("current")
_ControlLocalPropertiesWanInterfaceListSpiChange_Type = String
_ControlLocalPropertiesWanInterfaceListSpiChange_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListSpiChange = _ControlLocalPropertiesWanInterfaceListSpiChange_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 21),
    _ControlLocalPropertiesWanInterfaceListSpiChange_Type()
)
controlLocalPropertiesWanInterfaceListSpiChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListSpiChange.setStatus("current")
_ControlLocalPropertiesWanInterfaceListLastResort_Type = String
_ControlLocalPropertiesWanInterfaceListLastResort_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListLastResort = _ControlLocalPropertiesWanInterfaceListLastResort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 22),
    _ControlLocalPropertiesWanInterfaceListLastResort_Type()
)
controlLocalPropertiesWanInterfaceListLastResort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListLastResort.setStatus("current")
_ControlLocalPropertiesWanInterfaceListWanPortHopped_Type = String
_ControlLocalPropertiesWanInterfaceListWanPortHopped_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListWanPortHopped = _ControlLocalPropertiesWanInterfaceListWanPortHopped_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 23),
    _ControlLocalPropertiesWanInterfaceListWanPortHopped_Type()
)
controlLocalPropertiesWanInterfaceListWanPortHopped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListWanPortHopped.setStatus("current")
_ControlLocalPropertiesWanInterfaceListWanTimeSincePortHop_Type = String
_ControlLocalPropertiesWanInterfaceListWanTimeSincePortHop_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListWanTimeSincePortHop = _ControlLocalPropertiesWanInterfaceListWanTimeSincePortHop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 24),
    _ControlLocalPropertiesWanInterfaceListWanTimeSincePortHop_Type()
)
controlLocalPropertiesWanInterfaceListWanTimeSincePortHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListWanTimeSincePortHop.setStatus("current")
_ControlLocalPropertiesWanInterfaceListVbondAsStunServer_Type = String
_ControlLocalPropertiesWanInterfaceListVbondAsStunServer_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListVbondAsStunServer = _ControlLocalPropertiesWanInterfaceListVbondAsStunServer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 25),
    _ControlLocalPropertiesWanInterfaceListVbondAsStunServer_Type()
)
controlLocalPropertiesWanInterfaceListVbondAsStunServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListVbondAsStunServer.setStatus("current")
_ControlLocalPropertiesWanInterfaceListVmanageConnectionPreference_Type = UnsignedByte
_ControlLocalPropertiesWanInterfaceListVmanageConnectionPreference_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListVmanageConnectionPreference = _ControlLocalPropertiesWanInterfaceListVmanageConnectionPreference_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 26),
    _ControlLocalPropertiesWanInterfaceListVmanageConnectionPreference_Type()
)
controlLocalPropertiesWanInterfaceListVmanageConnectionPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListVmanageConnectionPreference.setStatus("current")
_ControlLocalPropertiesWanInterfaceListLowBandwidthLink_Type = String
_ControlLocalPropertiesWanInterfaceListLowBandwidthLink_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListLowBandwidthLink = _ControlLocalPropertiesWanInterfaceListLowBandwidthLink_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 27),
    _ControlLocalPropertiesWanInterfaceListLowBandwidthLink_Type()
)
controlLocalPropertiesWanInterfaceListLowBandwidthLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListLowBandwidthLink.setStatus("current")
_ControlLocalPropertiesWanInterfaceListNatType_Type = String
_ControlLocalPropertiesWanInterfaceListNatType_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListNatType = _ControlLocalPropertiesWanInterfaceListNatType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 31),
    _ControlLocalPropertiesWanInterfaceListNatType_Type()
)
controlLocalPropertiesWanInterfaceListNatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListNatType.setStatus("current")
_ControlLocalPropertiesWanInterfaceListInterfaceAdminState_Type = StateEnum
_ControlLocalPropertiesWanInterfaceListInterfaceAdminState_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListInterfaceAdminState = _ControlLocalPropertiesWanInterfaceListInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 32),
    _ControlLocalPropertiesWanInterfaceListInterfaceAdminState_Type()
)
controlLocalPropertiesWanInterfaceListInterfaceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListInterfaceAdminState.setStatus("current")
_ControlLocalPropertiesWanInterfaceListInterfaceOperState_Type = StateEnum
_ControlLocalPropertiesWanInterfaceListInterfaceOperState_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListInterfaceOperState = _ControlLocalPropertiesWanInterfaceListInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 28, 1, 33),
    _ControlLocalPropertiesWanInterfaceListInterfaceOperState_Type()
)
controlLocalPropertiesWanInterfaceListInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListInterfaceOperState.setStatus("current")
_ControlLocalPropertiesVedgeListVersion_Type = Counter64
_ControlLocalPropertiesVedgeListVersion_Object = MibScalar
controlLocalPropertiesVedgeListVersion = _ControlLocalPropertiesVedgeListVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 29),
    _ControlLocalPropertiesVedgeListVersion_Type()
)
controlLocalPropertiesVedgeListVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesVedgeListVersion.setStatus("current")
_ControlLocalPropertiesVsmartListVersion_Type = Counter64
_ControlLocalPropertiesVsmartListVersion_Object = MibScalar
controlLocalPropertiesVsmartListVersion = _ControlLocalPropertiesVsmartListVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 30),
    _ControlLocalPropertiesVsmartListVersion_Type()
)
controlLocalPropertiesVsmartListVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesVsmartListVersion.setStatus("current")


class _ControlLocalPropertiesSPOrganizationName_Type(String):
    """Custom type controlLocalPropertiesSPOrganizationName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ControlLocalPropertiesSPOrganizationName_Type.__name__ = "String"
_ControlLocalPropertiesSPOrganizationName_Object = MibScalar
controlLocalPropertiesSPOrganizationName = _ControlLocalPropertiesSPOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 31),
    _ControlLocalPropertiesSPOrganizationName_Type()
)
controlLocalPropertiesSPOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesSPOrganizationName.setStatus("current")


class _ControlLocalPropertiesToken_Type(String):
    """Custom type controlLocalPropertiesToken based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ControlLocalPropertiesToken_Type.__name__ = "String"
_ControlLocalPropertiesToken_Object = MibScalar
controlLocalPropertiesToken = _ControlLocalPropertiesToken_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 32),
    _ControlLocalPropertiesToken_Type()
)
controlLocalPropertiesToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesToken.setStatus("current")
_ControlLocalPropertiesCloudHosted_Type = String
_ControlLocalPropertiesCloudHosted_Object = MibScalar
controlLocalPropertiesCloudHosted = _ControlLocalPropertiesCloudHosted_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 33),
    _ControlLocalPropertiesCloudHosted_Type()
)
controlLocalPropertiesCloudHosted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesCloudHosted.setStatus("current")
_ControlLocalPropertiesEmbargoCheck_Type = String
_ControlLocalPropertiesEmbargoCheck_Object = MibScalar
controlLocalPropertiesEmbargoCheck = _ControlLocalPropertiesEmbargoCheck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 34),
    _ControlLocalPropertiesEmbargoCheck_Type()
)
controlLocalPropertiesEmbargoCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesEmbargoCheck.setStatus("current")


class _ControlLocalPropertiesEnterpriseSerial_Type(String):
    """Custom type controlLocalPropertiesEnterpriseSerial based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ControlLocalPropertiesEnterpriseSerial_Type.__name__ = "String"
_ControlLocalPropertiesEnterpriseSerial_Object = MibScalar
controlLocalPropertiesEnterpriseSerial = _ControlLocalPropertiesEnterpriseSerial_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 35),
    _ControlLocalPropertiesEnterpriseSerial_Type()
)
controlLocalPropertiesEnterpriseSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesEnterpriseSerial.setStatus("current")
_ControlLocalPropertiesEnterpriseCertificateStatus_Type = String
_ControlLocalPropertiesEnterpriseCertificateStatus_Object = MibScalar
controlLocalPropertiesEnterpriseCertificateStatus = _ControlLocalPropertiesEnterpriseCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 36),
    _ControlLocalPropertiesEnterpriseCertificateStatus_Type()
)
controlLocalPropertiesEnterpriseCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesEnterpriseCertificateStatus.setStatus("current")
_ControlLocalPropertiesEnterpriseCertificateValidity_Type = String
_ControlLocalPropertiesEnterpriseCertificateValidity_Object = MibScalar
controlLocalPropertiesEnterpriseCertificateValidity = _ControlLocalPropertiesEnterpriseCertificateValidity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 37),
    _ControlLocalPropertiesEnterpriseCertificateValidity_Type()
)
controlLocalPropertiesEnterpriseCertificateValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesEnterpriseCertificateValidity.setStatus("current")
_ControlLocalPropertiesEnterpriseCertificateNotValidBefore_Type = String
_ControlLocalPropertiesEnterpriseCertificateNotValidBefore_Object = MibScalar
controlLocalPropertiesEnterpriseCertificateNotValidBefore = _ControlLocalPropertiesEnterpriseCertificateNotValidBefore_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 38),
    _ControlLocalPropertiesEnterpriseCertificateNotValidBefore_Type()
)
controlLocalPropertiesEnterpriseCertificateNotValidBefore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesEnterpriseCertificateNotValidBefore.setStatus("current")
_ControlLocalPropertiesEnterpriseCertificateNotValidAfter_Type = String
_ControlLocalPropertiesEnterpriseCertificateNotValidAfter_Object = MibScalar
controlLocalPropertiesEnterpriseCertificateNotValidAfter = _ControlLocalPropertiesEnterpriseCertificateNotValidAfter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 39),
    _ControlLocalPropertiesEnterpriseCertificateNotValidAfter_Type()
)
controlLocalPropertiesEnterpriseCertificateNotValidAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesEnterpriseCertificateNotValidAfter.setStatus("current")
_ControlLocalPropertiesPairwiseKeying_Type = String
_ControlLocalPropertiesPairwiseKeying_Object = MibScalar
controlLocalPropertiesPairwiseKeying = _ControlLocalPropertiesPairwiseKeying_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 40),
    _ControlLocalPropertiesPairwiseKeying_Type()
)
controlLocalPropertiesPairwiseKeying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesPairwiseKeying.setStatus("current")
_ControlLocalPropertiesCdbLocked_Type = TruthValue
_ControlLocalPropertiesCdbLocked_Object = MibScalar
controlLocalPropertiesCdbLocked = _ControlLocalPropertiesCdbLocked_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 41),
    _ControlLocalPropertiesCdbLocked_Type()
)
controlLocalPropertiesCdbLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesCdbLocked.setStatus("current")


class _ControlLocalPropertiesSubjectSerialNumber_Type(String):
    """Custom type controlLocalPropertiesSubjectSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_ControlLocalPropertiesSubjectSerialNumber_Type.__name__ = "String"
_ControlLocalPropertiesSubjectSerialNumber_Object = MibScalar
controlLocalPropertiesSubjectSerialNumber = _ControlLocalPropertiesSubjectSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 5, 42),
    _ControlLocalPropertiesSubjectSerialNumber_Type()
)
controlLocalPropertiesSubjectSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesSubjectSerialNumber.setStatus("current")
_ControlValidVsmartsTable_Object = MibTable
controlValidVsmartsTable = _ControlValidVsmartsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 6)
)
if mibBuilder.loadTexts:
    controlValidVsmartsTable.setStatus("current")
_ControlValidVsmartsEntry_Object = MibTableRow
controlValidVsmartsEntry = _ControlValidVsmartsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 6, 1)
)
controlValidVsmartsEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "controlValidVsmartsSerialNumber"),
    (0, "VIPTELA-SECURITY", "controlValidVsmartsOrg"),
)
if mibBuilder.loadTexts:
    controlValidVsmartsEntry.setStatus("current")


class _ControlValidVsmartsSerialNumber_Type(String):
    """Custom type controlValidVsmartsSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ControlValidVsmartsSerialNumber_Type.__name__ = "String"
_ControlValidVsmartsSerialNumber_Object = MibTableColumn
controlValidVsmartsSerialNumber = _ControlValidVsmartsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 6, 1, 1),
    _ControlValidVsmartsSerialNumber_Type()
)
controlValidVsmartsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlValidVsmartsSerialNumber.setStatus("current")
_ControlValidVsmartsOrg_Type = String
_ControlValidVsmartsOrg_Object = MibTableColumn
controlValidVsmartsOrg = _ControlValidVsmartsOrg_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 6, 1, 2),
    _ControlValidVsmartsOrg_Type()
)
controlValidVsmartsOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlValidVsmartsOrg.setStatus("current")
_ControlValidVedgesTable_Object = MibTable
controlValidVedgesTable = _ControlValidVedgesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 7)
)
if mibBuilder.loadTexts:
    controlValidVedgesTable.setStatus("current")
_ControlValidVedgesEntry_Object = MibTableRow
controlValidVedgesEntry = _ControlValidVedgesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 7, 1)
)
controlValidVedgesEntry.setIndexNames(
    (1, "VIPTELA-SECURITY", "controlValidVedgesChassisNumber"),
)
if mibBuilder.loadTexts:
    controlValidVedgesEntry.setStatus("current")


class _ControlValidVedgesChassisNumber_Type(String):
    """Custom type controlValidVedgesChassisNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ControlValidVedgesChassisNumber_Type.__name__ = "String"
_ControlValidVedgesChassisNumber_Object = MibTableColumn
controlValidVedgesChassisNumber = _ControlValidVedgesChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 7, 1, 1),
    _ControlValidVedgesChassisNumber_Type()
)
controlValidVedgesChassisNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlValidVedgesChassisNumber.setStatus("current")


class _ControlValidVedgesSerialNumber_Type(String):
    """Custom type controlValidVedgesSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ControlValidVedgesSerialNumber_Type.__name__ = "String"
_ControlValidVedgesSerialNumber_Object = MibTableColumn
controlValidVedgesSerialNumber = _ControlValidVedgesSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 7, 1, 2),
    _ControlValidVedgesSerialNumber_Type()
)
controlValidVedgesSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlValidVedgesSerialNumber.setStatus("current")


class _ControlValidVedgesValidity_Type(Integer32):
    """Custom type controlValidVedgesValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("staging", 3))
    )


_ControlValidVedgesValidity_Type.__name__ = "Integer32"
_ControlValidVedgesValidity_Object = MibTableColumn
controlValidVedgesValidity = _ControlValidVedgesValidity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 7, 1, 3),
    _ControlValidVedgesValidity_Type()
)
controlValidVedgesValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlValidVedgesValidity.setStatus("current")
_ControlValidVedgesOrg_Type = String
_ControlValidVedgesOrg_Object = MibTableColumn
controlValidVedgesOrg = _ControlValidVedgesOrg_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 7, 1, 4),
    _ControlValidVedgesOrg_Type()
)
controlValidVedgesOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlValidVedgesOrg.setStatus("current")


class _ControlValidVedgesHardwareInstalledSerialNumber_Type(String):
    """Custom type controlValidVedgesHardwareInstalledSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ControlValidVedgesHardwareInstalledSerialNumber_Type.__name__ = "String"
_ControlValidVedgesHardwareInstalledSerialNumber_Object = MibTableColumn
controlValidVedgesHardwareInstalledSerialNumber = _ControlValidVedgesHardwareInstalledSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 7, 1, 5),
    _ControlValidVedgesHardwareInstalledSerialNumber_Type()
)
controlValidVedgesHardwareInstalledSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlValidVedgesHardwareInstalledSerialNumber.setStatus("current")


class _ControlValidVedgesSubjectSerialNumber_Type(String):
    """Custom type controlValidVedgesSubjectSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_ControlValidVedgesSubjectSerialNumber_Type.__name__ = "String"
_ControlValidVedgesSubjectSerialNumber_Object = MibTableColumn
controlValidVedgesSubjectSerialNumber = _ControlValidVedgesSubjectSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 7, 1, 6),
    _ControlValidVedgesSubjectSerialNumber_Type()
)
controlValidVedgesSubjectSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlValidVedgesSubjectSerialNumber.setStatus("current")
_ControlSummaryTable_Object = MibTable
controlSummaryTable = _ControlSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 8)
)
if mibBuilder.loadTexts:
    controlSummaryTable.setStatus("current")
_ControlSummaryEntry_Object = MibTableRow
controlSummaryEntry = _ControlSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 8, 1)
)
controlSummaryEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "controlSummaryInstance"),
)
if mibBuilder.loadTexts:
    controlSummaryEntry.setStatus("current")
_ControlSummaryInstance_Type = Unsigned32
_ControlSummaryInstance_Object = MibTableColumn
controlSummaryInstance = _ControlSummaryInstance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 8, 1, 1),
    _ControlSummaryInstance_Type()
)
controlSummaryInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlSummaryInstance.setStatus("current")
_ControlSummaryVbondCounts_Type = UnsignedShort
_ControlSummaryVbondCounts_Object = MibTableColumn
controlSummaryVbondCounts = _ControlSummaryVbondCounts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 8, 1, 2),
    _ControlSummaryVbondCounts_Type()
)
controlSummaryVbondCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryVbondCounts.setStatus("current")
_ControlSummaryVmanageCounts_Type = UnsignedShort
_ControlSummaryVmanageCounts_Object = MibTableColumn
controlSummaryVmanageCounts = _ControlSummaryVmanageCounts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 8, 1, 3),
    _ControlSummaryVmanageCounts_Type()
)
controlSummaryVmanageCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryVmanageCounts.setStatus("current")
_ControlSummaryVsmartCounts_Type = UnsignedShort
_ControlSummaryVsmartCounts_Object = MibTableColumn
controlSummaryVsmartCounts = _ControlSummaryVsmartCounts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 8, 1, 4),
    _ControlSummaryVsmartCounts_Type()
)
controlSummaryVsmartCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryVsmartCounts.setStatus("current")
_ControlSummaryVedgeCounts_Type = UnsignedShort
_ControlSummaryVedgeCounts_Object = MibTableColumn
controlSummaryVedgeCounts = _ControlSummaryVedgeCounts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 8, 1, 5),
    _ControlSummaryVedgeCounts_Type()
)
controlSummaryVedgeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryVedgeCounts.setStatus("current")


class _ControlSummaryProtocol_Type(Integer32):
    """Custom type controlSummaryProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dtls", 0),
          ("tls", 1))
    )


_ControlSummaryProtocol_Type.__name__ = "Integer32"
_ControlSummaryProtocol_Object = MibTableColumn
controlSummaryProtocol = _ControlSummaryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 8, 1, 6),
    _ControlSummaryProtocol_Type()
)
controlSummaryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryProtocol.setStatus("current")
_ControlSummaryListeningIp_Type = InetAddressIP
_ControlSummaryListeningIp_Object = MibTableColumn
controlSummaryListeningIp = _ControlSummaryListeningIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 8, 1, 7),
    _ControlSummaryListeningIp_Type()
)
controlSummaryListeningIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlSummaryListeningIp.setStatus("current")
_ControlSummaryListeningPort_Type = Unsigned32
_ControlSummaryListeningPort_Object = MibTableColumn
controlSummaryListeningPort = _ControlSummaryListeningPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 8, 1, 8),
    _ControlSummaryListeningPort_Type()
)
controlSummaryListeningPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlSummaryListeningPort.setStatus("current")
_ControlSummaryListeningIpv6_Type = InetAddressIP
_ControlSummaryListeningIpv6_Object = MibTableColumn
controlSummaryListeningIpv6 = _ControlSummaryListeningIpv6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 8, 1, 9),
    _ControlSummaryListeningIpv6_Type()
)
controlSummaryListeningIpv6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlSummaryListeningIpv6.setStatus("current")
_ControlSummaryValidControllerCounts_Type = UnsignedShort
_ControlSummaryValidControllerCounts_Object = MibTableColumn
controlSummaryValidControllerCounts = _ControlSummaryValidControllerCounts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 8, 1, 10),
    _ControlSummaryValidControllerCounts_Type()
)
controlSummaryValidControllerCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryValidControllerCounts.setStatus("current")
_ControlAffinity_ObjectIdentity = ObjectIdentity
controlAffinity = _ControlAffinity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9)
)
_ControlAffinityConfigTable_Object = MibTable
controlAffinityConfigTable = _ControlAffinityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 1)
)
if mibBuilder.loadTexts:
    controlAffinityConfigTable.setStatus("current")
_ControlAffinityConfigEntry_Object = MibTableRow
controlAffinityConfigEntry = _ControlAffinityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 1, 1)
)
controlAffinityConfigEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "controlAffinityConfigAffcIndex"),
)
if mibBuilder.loadTexts:
    controlAffinityConfigEntry.setStatus("current")
_ControlAffinityConfigAffcIndex_Type = Unsigned32
_ControlAffinityConfigAffcIndex_Object = MibTableColumn
controlAffinityConfigAffcIndex = _ControlAffinityConfigAffcIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 1, 1, 1),
    _ControlAffinityConfigAffcIndex_Type()
)
controlAffinityConfigAffcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcIndex.setStatus("current")


class _ControlAffinityConfigAffcInterface_Type(String):
    """Custom type controlAffinityConfigAffcInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ControlAffinityConfigAffcInterface_Type.__name__ = "String"
_ControlAffinityConfigAffcInterface_Object = MibTableColumn
controlAffinityConfigAffcInterface = _ControlAffinityConfigAffcInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 1, 1, 2),
    _ControlAffinityConfigAffcInterface_Type()
)
controlAffinityConfigAffcInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcInterface.setStatus("current")
_ControlAffinityConfigAffcErvc_Type = Unsigned32
_ControlAffinityConfigAffcErvc_Object = MibTableColumn
controlAffinityConfigAffcErvc = _ControlAffinityConfigAffcErvc_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 1, 1, 3),
    _ControlAffinityConfigAffcErvc_Type()
)
controlAffinityConfigAffcErvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcErvc.setStatus("current")
_ControlAffinityConfigAffcEcl_Type = String
_ControlAffinityConfigAffcEcl_Object = MibTableColumn
controlAffinityConfigAffcEcl = _ControlAffinityConfigAffcEcl_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 1, 1, 4),
    _ControlAffinityConfigAffcEcl_Type()
)
controlAffinityConfigAffcEcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcEcl.setStatus("current")
_ControlAffinityConfigAffcCcl_Type = String
_ControlAffinityConfigAffcCcl_Object = MibTableColumn
controlAffinityConfigAffcCcl = _ControlAffinityConfigAffcCcl_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 1, 1, 5),
    _ControlAffinityConfigAffcCcl_Type()
)
controlAffinityConfigAffcCcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcCcl.setStatus("current")
_ControlAffinityConfigAffcEquil_Type = String
_ControlAffinityConfigAffcEquil_Object = MibTableColumn
controlAffinityConfigAffcEquil = _ControlAffinityConfigAffcEquil_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 1, 1, 6),
    _ControlAffinityConfigAffcEquil_Type()
)
controlAffinityConfigAffcEquil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcEquil.setStatus("current")
_ControlAffinityConfigAffcLastResort_Type = String
_ControlAffinityConfigAffcLastResort_Object = MibTableColumn
controlAffinityConfigAffcLastResort = _ControlAffinityConfigAffcLastResort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 1, 1, 7),
    _ControlAffinityConfigAffcLastResort_Type()
)
controlAffinityConfigAffcLastResort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcLastResort.setStatus("current")
_ControlAffinityStatusTable_Object = MibTable
controlAffinityStatusTable = _ControlAffinityStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 2)
)
if mibBuilder.loadTexts:
    controlAffinityStatusTable.setStatus("current")
_ControlAffinityStatusEntry_Object = MibTableRow
controlAffinityStatusEntry = _ControlAffinityStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 2, 1)
)
controlAffinityStatusEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "controlAffinityStatusAffsIndex"),
)
if mibBuilder.loadTexts:
    controlAffinityStatusEntry.setStatus("current")
_ControlAffinityStatusAffsIndex_Type = Unsigned32
_ControlAffinityStatusAffsIndex_Object = MibTableColumn
controlAffinityStatusAffsIndex = _ControlAffinityStatusAffsIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 2, 1, 1),
    _ControlAffinityStatusAffsIndex_Type()
)
controlAffinityStatusAffsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlAffinityStatusAffsIndex.setStatus("current")


class _ControlAffinityStatusAffsInterface_Type(String):
    """Custom type controlAffinityStatusAffsInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ControlAffinityStatusAffsInterface_Type.__name__ = "String"
_ControlAffinityStatusAffsInterface_Object = MibTableColumn
controlAffinityStatusAffsInterface = _ControlAffinityStatusAffsInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 2, 1, 2),
    _ControlAffinityStatusAffsInterface_Type()
)
controlAffinityStatusAffsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityStatusAffsInterface.setStatus("current")
_ControlAffinityStatusAffsAcc_Type = String
_ControlAffinityStatusAffsAcc_Object = MibTableColumn
controlAffinityStatusAffsAcc = _ControlAffinityStatusAffsAcc_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 2, 1, 3),
    _ControlAffinityStatusAffsAcc_Type()
)
controlAffinityStatusAffsAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityStatusAffsAcc.setStatus("current")
_ControlAffinityStatusAffsUcc_Type = String
_ControlAffinityStatusAffsUcc_Object = MibTableColumn
controlAffinityStatusAffsUcc = _ControlAffinityStatusAffsUcc_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 2, 1, 4),
    _ControlAffinityStatusAffsUcc_Type()
)
controlAffinityStatusAffsUcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityStatusAffsUcc.setStatus("current")
_ControlAffinityStatusAffsAc_Type = String
_ControlAffinityStatusAffsAc_Object = MibTableColumn
controlAffinityStatusAffsAc = _ControlAffinityStatusAffsAc_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 9, 2, 1, 5),
    _ControlAffinityStatusAffsAc_Type()
)
controlAffinityStatusAffsAc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityStatusAffsAc.setStatus("current")
_ControlValidVmanageIdTable_Object = MibTable
controlValidVmanageIdTable = _ControlValidVmanageIdTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 10)
)
if mibBuilder.loadTexts:
    controlValidVmanageIdTable.setStatus("current")
_ControlValidVmanageIdEntry_Object = MibTableRow
controlValidVmanageIdEntry = _ControlValidVmanageIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 10, 1)
)
controlValidVmanageIdEntry.setIndexNames(
    (1, "VIPTELA-SECURITY", "controlValidVManageIdChassisNumbers"),
)
if mibBuilder.loadTexts:
    controlValidVmanageIdEntry.setStatus("current")


class _ControlValidVManageIdChassisNumbers_Type(String):
    """Custom type controlValidVManageIdChassisNumbers based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ControlValidVManageIdChassisNumbers_Type.__name__ = "String"
_ControlValidVManageIdChassisNumbers_Object = MibTableColumn
controlValidVManageIdChassisNumbers = _ControlValidVManageIdChassisNumbers_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 2, 10, 1, 1),
    _ControlValidVManageIdChassisNumbers_Type()
)
controlValidVManageIdChassisNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlValidVManageIdChassisNumbers.setStatus("current")
_Orchestrator_ObjectIdentity = ObjectIdentity
orchestrator = _Orchestrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3)
)
_OrchestratorConnectionsTable_Object = MibTable
orchestratorConnectionsTable = _OrchestratorConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1)
)
if mibBuilder.loadTexts:
    orchestratorConnectionsTable.setStatus("current")
_OrchestratorConnectionsEntry_Object = MibTableRow
orchestratorConnectionsEntry = _OrchestratorConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1)
)
orchestratorConnectionsEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "orchestratorConnectionsInstance"),
    (0, "VIPTELA-SECURITY", "orchestratorConnectionsPeerType"),
    (0, "VIPTELA-SECURITY", "orchestratorConnectionsSiteId"),
    (0, "VIPTELA-SECURITY", "orchestratorConnectionsDomainId"),
    (0, "VIPTELA-SECURITY", "orchestratorConnectionsLocalPrivateIp"),
    (0, "VIPTELA-SECURITY", "orchestratorConnectionsLocalPrivatePort"),
    (0, "VIPTELA-SECURITY", "orchestratorConnectionsPublicIp"),
    (0, "VIPTELA-SECURITY", "orchestratorConnectionsPublicPort"),
)
if mibBuilder.loadTexts:
    orchestratorConnectionsEntry.setStatus("current")
_OrchestratorConnectionsInstance_Type = Unsigned32
_OrchestratorConnectionsInstance_Object = MibTableColumn
orchestratorConnectionsInstance = _OrchestratorConnectionsInstance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 1),
    _OrchestratorConnectionsInstance_Type()
)
orchestratorConnectionsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorConnectionsInstance.setStatus("current")


class _OrchestratorConnectionsPeerType_Type(Integer32):
    """Custom type orchestratorConnectionsPeerType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )


_OrchestratorConnectionsPeerType_Type.__name__ = "Integer32"
_OrchestratorConnectionsPeerType_Object = MibTableColumn
orchestratorConnectionsPeerType = _OrchestratorConnectionsPeerType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 2),
    _OrchestratorConnectionsPeerType_Type()
)
orchestratorConnectionsPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorConnectionsPeerType.setStatus("current")
_OrchestratorConnectionsSiteId_Type = Unsigned32
_OrchestratorConnectionsSiteId_Object = MibTableColumn
orchestratorConnectionsSiteId = _OrchestratorConnectionsSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 3),
    _OrchestratorConnectionsSiteId_Type()
)
orchestratorConnectionsSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorConnectionsSiteId.setStatus("current")
_OrchestratorConnectionsDomainId_Type = Unsigned32
_OrchestratorConnectionsDomainId_Object = MibTableColumn
orchestratorConnectionsDomainId = _OrchestratorConnectionsDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 4),
    _OrchestratorConnectionsDomainId_Type()
)
orchestratorConnectionsDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorConnectionsDomainId.setStatus("current")


class _OrchestratorConnectionsProtocol_Type(Integer32):
    """Custom type orchestratorConnectionsProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dtls", 0),
          ("tls", 1))
    )


_OrchestratorConnectionsProtocol_Type.__name__ = "Integer32"
_OrchestratorConnectionsProtocol_Object = MibTableColumn
orchestratorConnectionsProtocol = _OrchestratorConnectionsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 5),
    _OrchestratorConnectionsProtocol_Type()
)
orchestratorConnectionsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsProtocol.setStatus("current")
_OrchestratorConnectionsLocalPrivateIp_Type = InetAddressIP
_OrchestratorConnectionsLocalPrivateIp_Object = MibTableColumn
orchestratorConnectionsLocalPrivateIp = _OrchestratorConnectionsLocalPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 6),
    _OrchestratorConnectionsLocalPrivateIp_Type()
)
orchestratorConnectionsLocalPrivateIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorConnectionsLocalPrivateIp.setStatus("current")
_OrchestratorConnectionsLocalPrivatePort_Type = Unsigned32
_OrchestratorConnectionsLocalPrivatePort_Object = MibTableColumn
orchestratorConnectionsLocalPrivatePort = _OrchestratorConnectionsLocalPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 7),
    _OrchestratorConnectionsLocalPrivatePort_Type()
)
orchestratorConnectionsLocalPrivatePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorConnectionsLocalPrivatePort.setStatus("current")
_OrchestratorConnectionsPublicIp_Type = InetAddressIP
_OrchestratorConnectionsPublicIp_Object = MibTableColumn
orchestratorConnectionsPublicIp = _OrchestratorConnectionsPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 8),
    _OrchestratorConnectionsPublicIp_Type()
)
orchestratorConnectionsPublicIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorConnectionsPublicIp.setStatus("current")
_OrchestratorConnectionsPublicPort_Type = Unsigned32
_OrchestratorConnectionsPublicPort_Object = MibTableColumn
orchestratorConnectionsPublicPort = _OrchestratorConnectionsPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 9),
    _OrchestratorConnectionsPublicPort_Type()
)
orchestratorConnectionsPublicPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorConnectionsPublicPort.setStatus("current")
_OrchestratorConnectionsSystemIp_Type = InetAddressIP
_OrchestratorConnectionsSystemIp_Object = MibTableColumn
orchestratorConnectionsSystemIp = _OrchestratorConnectionsSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 10),
    _OrchestratorConnectionsSystemIp_Type()
)
orchestratorConnectionsSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsSystemIp.setStatus("current")


class _OrchestratorConnectionsLocalColor_Type(Integer32):
    """Custom type orchestratorConnectionsLocalColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OrchestratorConnectionsLocalColor_Type.__name__ = "Integer32"
_OrchestratorConnectionsLocalColor_Object = MibTableColumn
orchestratorConnectionsLocalColor = _OrchestratorConnectionsLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 11),
    _OrchestratorConnectionsLocalColor_Type()
)
orchestratorConnectionsLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsLocalColor.setStatus("current")


class _OrchestratorConnectionsRemoteColor_Type(Integer32):
    """Custom type orchestratorConnectionsRemoteColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OrchestratorConnectionsRemoteColor_Type.__name__ = "Integer32"
_OrchestratorConnectionsRemoteColor_Object = MibTableColumn
orchestratorConnectionsRemoteColor = _OrchestratorConnectionsRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 12),
    _OrchestratorConnectionsRemoteColor_Type()
)
orchestratorConnectionsRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRemoteColor.setStatus("current")
_OrchestratorConnectionsPrivateIp_Type = InetAddressIP
_OrchestratorConnectionsPrivateIp_Object = MibTableColumn
orchestratorConnectionsPrivateIp = _OrchestratorConnectionsPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 13),
    _OrchestratorConnectionsPrivateIp_Type()
)
orchestratorConnectionsPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsPrivateIp.setStatus("current")
_OrchestratorConnectionsPrivatePort_Type = Unsigned32
_OrchestratorConnectionsPrivatePort_Object = MibTableColumn
orchestratorConnectionsPrivatePort = _OrchestratorConnectionsPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 14),
    _OrchestratorConnectionsPrivatePort_Type()
)
orchestratorConnectionsPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsPrivatePort.setStatus("current")
_OrchestratorConnectionsState_Type = SessionState
_OrchestratorConnectionsState_Object = MibTableColumn
orchestratorConnectionsState = _OrchestratorConnectionsState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 15),
    _OrchestratorConnectionsState_Type()
)
orchestratorConnectionsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsState.setStatus("current")
_OrchestratorConnectionsLocalEnum_Type = ConnFlagEnum
_OrchestratorConnectionsLocalEnum_Object = MibTableColumn
orchestratorConnectionsLocalEnum = _OrchestratorConnectionsLocalEnum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 16),
    _OrchestratorConnectionsLocalEnum_Type()
)
orchestratorConnectionsLocalEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsLocalEnum.setStatus("current")
_OrchestratorConnectionsRemoteEnum_Type = ConnFlagEnum
_OrchestratorConnectionsRemoteEnum_Object = MibTableColumn
orchestratorConnectionsRemoteEnum = _OrchestratorConnectionsRemoteEnum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 17),
    _OrchestratorConnectionsRemoteEnum_Type()
)
orchestratorConnectionsRemoteEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRemoteEnum.setStatus("current")
_OrchestratorConnectionsLocalStateInfo_Type = String
_OrchestratorConnectionsLocalStateInfo_Object = MibTableColumn
orchestratorConnectionsLocalStateInfo = _OrchestratorConnectionsLocalStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 18),
    _OrchestratorConnectionsLocalStateInfo_Type()
)
orchestratorConnectionsLocalStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsLocalStateInfo.setStatus("current")
_OrchestratorConnectionsRemoteStateInfo_Type = String
_OrchestratorConnectionsRemoteStateInfo_Object = MibTableColumn
orchestratorConnectionsRemoteStateInfo = _OrchestratorConnectionsRemoteStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 19),
    _OrchestratorConnectionsRemoteStateInfo_Type()
)
orchestratorConnectionsRemoteStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRemoteStateInfo.setStatus("current")
_OrchestratorConnectionsUptime_Type = String
_OrchestratorConnectionsUptime_Object = MibTableColumn
orchestratorConnectionsUptime = _OrchestratorConnectionsUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 20),
    _OrchestratorConnectionsUptime_Type()
)
orchestratorConnectionsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsUptime.setStatus("current")
_OrchestratorConnectionsTxHello_Type = Unsigned32
_OrchestratorConnectionsTxHello_Object = MibTableColumn
orchestratorConnectionsTxHello = _OrchestratorConnectionsTxHello_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 21),
    _OrchestratorConnectionsTxHello_Type()
)
orchestratorConnectionsTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxHello.setStatus("current")
_OrchestratorConnectionsTxConnects_Type = Unsigned32
_OrchestratorConnectionsTxConnects_Object = MibTableColumn
orchestratorConnectionsTxConnects = _OrchestratorConnectionsTxConnects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 22),
    _OrchestratorConnectionsTxConnects_Type()
)
orchestratorConnectionsTxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxConnects.setStatus("current")
_OrchestratorConnectionsTxRegisters_Type = Unsigned32
_OrchestratorConnectionsTxRegisters_Object = MibTableColumn
orchestratorConnectionsTxRegisters = _OrchestratorConnectionsTxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 23),
    _OrchestratorConnectionsTxRegisters_Type()
)
orchestratorConnectionsTxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxRegisters.setStatus("current")
_OrchestratorConnectionsTxRegisterReplies_Type = Unsigned32
_OrchestratorConnectionsTxRegisterReplies_Object = MibTableColumn
orchestratorConnectionsTxRegisterReplies = _OrchestratorConnectionsTxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 24),
    _OrchestratorConnectionsTxRegisterReplies_Type()
)
orchestratorConnectionsTxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxRegisterReplies.setStatus("current")
_OrchestratorConnectionsTxChallenge_Type = Unsigned32
_OrchestratorConnectionsTxChallenge_Object = MibTableColumn
orchestratorConnectionsTxChallenge = _OrchestratorConnectionsTxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 25),
    _OrchestratorConnectionsTxChallenge_Type()
)
orchestratorConnectionsTxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxChallenge.setStatus("current")
_OrchestratorConnectionsTxChallengeResp_Type = Unsigned32
_OrchestratorConnectionsTxChallengeResp_Object = MibTableColumn
orchestratorConnectionsTxChallengeResp = _OrchestratorConnectionsTxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 26),
    _OrchestratorConnectionsTxChallengeResp_Type()
)
orchestratorConnectionsTxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxChallengeResp.setStatus("current")
_OrchestratorConnectionsTxChallengeAck_Type = Unsigned32
_OrchestratorConnectionsTxChallengeAck_Object = MibTableColumn
orchestratorConnectionsTxChallengeAck = _OrchestratorConnectionsTxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 27),
    _OrchestratorConnectionsTxChallengeAck_Type()
)
orchestratorConnectionsTxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxChallengeAck.setStatus("current")
_OrchestratorConnectionsTxTeardown_Type = Unsigned32
_OrchestratorConnectionsTxTeardown_Object = MibTableColumn
orchestratorConnectionsTxTeardown = _OrchestratorConnectionsTxTeardown_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 28),
    _OrchestratorConnectionsTxTeardown_Type()
)
orchestratorConnectionsTxTeardown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxTeardown.setStatus("current")
_OrchestratorConnectionsTxTeardownAll_Type = Unsigned32
_OrchestratorConnectionsTxTeardownAll_Object = MibTableColumn
orchestratorConnectionsTxTeardownAll = _OrchestratorConnectionsTxTeardownAll_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 29),
    _OrchestratorConnectionsTxTeardownAll_Type()
)
orchestratorConnectionsTxTeardownAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxTeardownAll.setStatus("current")
_OrchestratorConnectionsTxVmToPeer_Type = Unsigned32
_OrchestratorConnectionsTxVmToPeer_Object = MibTableColumn
orchestratorConnectionsTxVmToPeer = _OrchestratorConnectionsTxVmToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 30),
    _OrchestratorConnectionsTxVmToPeer_Type()
)
orchestratorConnectionsTxVmToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxVmToPeer.setStatus("current")
_OrchestratorConnectionsTxRegisterToVm_Type = Unsigned32
_OrchestratorConnectionsTxRegisterToVm_Object = MibTableColumn
orchestratorConnectionsTxRegisterToVm = _OrchestratorConnectionsTxRegisterToVm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 31),
    _OrchestratorConnectionsTxRegisterToVm_Type()
)
orchestratorConnectionsTxRegisterToVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxRegisterToVm.setStatus("current")
_OrchestratorConnectionsRxHello_Type = Unsigned32
_OrchestratorConnectionsRxHello_Object = MibTableColumn
orchestratorConnectionsRxHello = _OrchestratorConnectionsRxHello_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 32),
    _OrchestratorConnectionsRxHello_Type()
)
orchestratorConnectionsRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRxHello.setStatus("current")
_OrchestratorConnectionsRxConnects_Type = Unsigned32
_OrchestratorConnectionsRxConnects_Object = MibTableColumn
orchestratorConnectionsRxConnects = _OrchestratorConnectionsRxConnects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 33),
    _OrchestratorConnectionsRxConnects_Type()
)
orchestratorConnectionsRxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRxConnects.setStatus("current")
_OrchestratorConnectionsRxRegisters_Type = Unsigned32
_OrchestratorConnectionsRxRegisters_Object = MibTableColumn
orchestratorConnectionsRxRegisters = _OrchestratorConnectionsRxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 34),
    _OrchestratorConnectionsRxRegisters_Type()
)
orchestratorConnectionsRxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRxRegisters.setStatus("current")
_OrchestratorConnectionsRxRegisterReplies_Type = Unsigned32
_OrchestratorConnectionsRxRegisterReplies_Object = MibTableColumn
orchestratorConnectionsRxRegisterReplies = _OrchestratorConnectionsRxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 35),
    _OrchestratorConnectionsRxRegisterReplies_Type()
)
orchestratorConnectionsRxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRxRegisterReplies.setStatus("current")
_OrchestratorConnectionsRxChallenge_Type = Unsigned32
_OrchestratorConnectionsRxChallenge_Object = MibTableColumn
orchestratorConnectionsRxChallenge = _OrchestratorConnectionsRxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 36),
    _OrchestratorConnectionsRxChallenge_Type()
)
orchestratorConnectionsRxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRxChallenge.setStatus("current")
_OrchestratorConnectionsRxChallengeResp_Type = Unsigned32
_OrchestratorConnectionsRxChallengeResp_Object = MibTableColumn
orchestratorConnectionsRxChallengeResp = _OrchestratorConnectionsRxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 37),
    _OrchestratorConnectionsRxChallengeResp_Type()
)
orchestratorConnectionsRxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRxChallengeResp.setStatus("current")
_OrchestratorConnectionsRxChallengeAck_Type = Unsigned32
_OrchestratorConnectionsRxChallengeAck_Object = MibTableColumn
orchestratorConnectionsRxChallengeAck = _OrchestratorConnectionsRxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 38),
    _OrchestratorConnectionsRxChallengeAck_Type()
)
orchestratorConnectionsRxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRxChallengeAck.setStatus("current")
_OrchestratorConnectionsRxTeardown_Type = Unsigned32
_OrchestratorConnectionsRxTeardown_Object = MibTableColumn
orchestratorConnectionsRxTeardown = _OrchestratorConnectionsRxTeardown_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 39),
    _OrchestratorConnectionsRxTeardown_Type()
)
orchestratorConnectionsRxTeardown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRxTeardown.setStatus("current")
_OrchestratorConnectionsRxVmToPeer_Type = Unsigned32
_OrchestratorConnectionsRxVmToPeer_Object = MibTableColumn
orchestratorConnectionsRxVmToPeer = _OrchestratorConnectionsRxVmToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 40),
    _OrchestratorConnectionsRxVmToPeer_Type()
)
orchestratorConnectionsRxVmToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRxVmToPeer.setStatus("current")
_OrchestratorConnectionsRxRegisterToVm_Type = Unsigned32
_OrchestratorConnectionsRxRegisterToVm_Object = MibTableColumn
orchestratorConnectionsRxRegisterToVm = _OrchestratorConnectionsRxRegisterToVm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 41),
    _OrchestratorConnectionsRxRegisterToVm_Type()
)
orchestratorConnectionsRxRegisterToVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRxRegisterToVm.setStatus("current")
_OrchestratorConnectionsNegotiatedHelloInterval_Type = Unsigned32
_OrchestratorConnectionsNegotiatedHelloInterval_Object = MibTableColumn
orchestratorConnectionsNegotiatedHelloInterval = _OrchestratorConnectionsNegotiatedHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 42),
    _OrchestratorConnectionsNegotiatedHelloInterval_Type()
)
orchestratorConnectionsNegotiatedHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsNegotiatedHelloInterval.setStatus("current")
_OrchestratorConnectionsNegotiatedHelloTolerance_Type = Unsigned32
_OrchestratorConnectionsNegotiatedHelloTolerance_Object = MibTableColumn
orchestratorConnectionsNegotiatedHelloTolerance = _OrchestratorConnectionsNegotiatedHelloTolerance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 43),
    _OrchestratorConnectionsNegotiatedHelloTolerance_Type()
)
orchestratorConnectionsNegotiatedHelloTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsNegotiatedHelloTolerance.setStatus("current")
_OrchestratorConnectionsOrgname_Type = String
_OrchestratorConnectionsOrgname_Object = MibTableColumn
orchestratorConnectionsOrgname = _OrchestratorConnectionsOrgname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 44),
    _OrchestratorConnectionsOrgname_Type()
)
orchestratorConnectionsOrgname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsOrgname.setStatus("current")
_OrchestratorConnectionsSporgname_Type = String
_OrchestratorConnectionsSporgname_Object = MibTableColumn
orchestratorConnectionsSporgname = _OrchestratorConnectionsSporgname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 45),
    _OrchestratorConnectionsSporgname_Type()
)
orchestratorConnectionsSporgname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsSporgname.setStatus("current")
_OrchestratorConnectionsTxCreateCert_Type = Unsigned32
_OrchestratorConnectionsTxCreateCert_Object = MibTableColumn
orchestratorConnectionsTxCreateCert = _OrchestratorConnectionsTxCreateCert_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 46),
    _OrchestratorConnectionsTxCreateCert_Type()
)
orchestratorConnectionsTxCreateCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxCreateCert.setStatus("current")
_OrchestratorConnectionsRxCreateCert_Type = Unsigned32
_OrchestratorConnectionsRxCreateCert_Object = MibTableColumn
orchestratorConnectionsRxCreateCert = _OrchestratorConnectionsRxCreateCert_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 47),
    _OrchestratorConnectionsRxCreateCert_Type()
)
orchestratorConnectionsRxCreateCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRxCreateCert.setStatus("current")
_OrchestratorConnectionsTxCreateCertReply_Type = Unsigned32
_OrchestratorConnectionsTxCreateCertReply_Object = MibTableColumn
orchestratorConnectionsTxCreateCertReply = _OrchestratorConnectionsTxCreateCertReply_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 48),
    _OrchestratorConnectionsTxCreateCertReply_Type()
)
orchestratorConnectionsTxCreateCertReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsTxCreateCertReply.setStatus("current")
_OrchestratorConnectionsRxCreateCertReply_Type = Unsigned32
_OrchestratorConnectionsRxCreateCertReply_Object = MibTableColumn
orchestratorConnectionsRxCreateCertReply = _OrchestratorConnectionsRxCreateCertReply_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 49),
    _OrchestratorConnectionsRxCreateCertReply_Type()
)
orchestratorConnectionsRxCreateCertReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsRxCreateCertReply.setStatus("current")
_OrchestratorConnectionsCloudHosted_Type = TruthValue
_OrchestratorConnectionsCloudHosted_Object = MibTableColumn
orchestratorConnectionsCloudHosted = _OrchestratorConnectionsCloudHosted_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 1, 1, 50),
    _OrchestratorConnectionsCloudHosted_Type()
)
orchestratorConnectionsCloudHosted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsCloudHosted.setStatus("current")
_OrchestratorConnectionsHistoryTable_Object = MibTable
orchestratorConnectionsHistoryTable = _OrchestratorConnectionsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2)
)
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTable.setStatus("current")
_OrchestratorConnectionsHistoryEntry_Object = MibTableRow
orchestratorConnectionsHistoryEntry = _OrchestratorConnectionsHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1)
)
orchestratorConnectionsHistoryEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "orchestratorConnectionsHistoryInstance"),
    (0, "VIPTELA-SECURITY", "orchestratorConnectionsHistoryIndex"),
)
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryEntry.setStatus("current")
_OrchestratorConnectionsHistoryInstance_Type = Unsigned32
_OrchestratorConnectionsHistoryInstance_Object = MibTableColumn
orchestratorConnectionsHistoryInstance = _OrchestratorConnectionsHistoryInstance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 1),
    _OrchestratorConnectionsHistoryInstance_Type()
)
orchestratorConnectionsHistoryInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryInstance.setStatus("current")
_OrchestratorConnectionsHistoryIndex_Type = Unsigned32
_OrchestratorConnectionsHistoryIndex_Object = MibTableColumn
orchestratorConnectionsHistoryIndex = _OrchestratorConnectionsHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 2),
    _OrchestratorConnectionsHistoryIndex_Type()
)
orchestratorConnectionsHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryIndex.setStatus("current")


class _OrchestratorConnectionsHistoryPeerType_Type(Integer32):
    """Custom type orchestratorConnectionsHistoryPeerType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )


_OrchestratorConnectionsHistoryPeerType_Type.__name__ = "Integer32"
_OrchestratorConnectionsHistoryPeerType_Object = MibTableColumn
orchestratorConnectionsHistoryPeerType = _OrchestratorConnectionsHistoryPeerType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 3),
    _OrchestratorConnectionsHistoryPeerType_Type()
)
orchestratorConnectionsHistoryPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryPeerType.setStatus("current")
_OrchestratorConnectionsHistorySiteId_Type = Unsigned32
_OrchestratorConnectionsHistorySiteId_Object = MibTableColumn
orchestratorConnectionsHistorySiteId = _OrchestratorConnectionsHistorySiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 4),
    _OrchestratorConnectionsHistorySiteId_Type()
)
orchestratorConnectionsHistorySiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistorySiteId.setStatus("current")
_OrchestratorConnectionsHistoryDomainId_Type = Unsigned32
_OrchestratorConnectionsHistoryDomainId_Object = MibTableColumn
orchestratorConnectionsHistoryDomainId = _OrchestratorConnectionsHistoryDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 5),
    _OrchestratorConnectionsHistoryDomainId_Type()
)
orchestratorConnectionsHistoryDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryDomainId.setStatus("current")


class _OrchestratorConnectionsHistoryProtocol_Type(Integer32):
    """Custom type orchestratorConnectionsHistoryProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dtls", 0),
          ("tls", 1))
    )


_OrchestratorConnectionsHistoryProtocol_Type.__name__ = "Integer32"
_OrchestratorConnectionsHistoryProtocol_Object = MibTableColumn
orchestratorConnectionsHistoryProtocol = _OrchestratorConnectionsHistoryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 6),
    _OrchestratorConnectionsHistoryProtocol_Type()
)
orchestratorConnectionsHistoryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryProtocol.setStatus("current")
_OrchestratorConnectionsHistoryPrivateIp_Type = InetAddressIP
_OrchestratorConnectionsHistoryPrivateIp_Object = MibTableColumn
orchestratorConnectionsHistoryPrivateIp = _OrchestratorConnectionsHistoryPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 7),
    _OrchestratorConnectionsHistoryPrivateIp_Type()
)
orchestratorConnectionsHistoryPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryPrivateIp.setStatus("current")
_OrchestratorConnectionsHistoryPrivatePort_Type = Unsigned32
_OrchestratorConnectionsHistoryPrivatePort_Object = MibTableColumn
orchestratorConnectionsHistoryPrivatePort = _OrchestratorConnectionsHistoryPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 8),
    _OrchestratorConnectionsHistoryPrivatePort_Type()
)
orchestratorConnectionsHistoryPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryPrivatePort.setStatus("current")
_OrchestratorConnectionsHistoryPublicIp_Type = InetAddressIP
_OrchestratorConnectionsHistoryPublicIp_Object = MibTableColumn
orchestratorConnectionsHistoryPublicIp = _OrchestratorConnectionsHistoryPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 9),
    _OrchestratorConnectionsHistoryPublicIp_Type()
)
orchestratorConnectionsHistoryPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryPublicIp.setStatus("current")
_OrchestratorConnectionsHistoryPublicPort_Type = Unsigned32
_OrchestratorConnectionsHistoryPublicPort_Object = MibTableColumn
orchestratorConnectionsHistoryPublicPort = _OrchestratorConnectionsHistoryPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 10),
    _OrchestratorConnectionsHistoryPublicPort_Type()
)
orchestratorConnectionsHistoryPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryPublicPort.setStatus("current")
_OrchestratorConnectionsHistorySystemIp_Type = InetAddressIP
_OrchestratorConnectionsHistorySystemIp_Object = MibTableColumn
orchestratorConnectionsHistorySystemIp = _OrchestratorConnectionsHistorySystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 11),
    _OrchestratorConnectionsHistorySystemIp_Type()
)
orchestratorConnectionsHistorySystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistorySystemIp.setStatus("current")


class _OrchestratorConnectionsHistoryLocalColor_Type(Integer32):
    """Custom type orchestratorConnectionsHistoryLocalColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OrchestratorConnectionsHistoryLocalColor_Type.__name__ = "Integer32"
_OrchestratorConnectionsHistoryLocalColor_Object = MibTableColumn
orchestratorConnectionsHistoryLocalColor = _OrchestratorConnectionsHistoryLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 12),
    _OrchestratorConnectionsHistoryLocalColor_Type()
)
orchestratorConnectionsHistoryLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryLocalColor.setStatus("current")


class _OrchestratorConnectionsHistoryRemoteColor_Type(Integer32):
    """Custom type orchestratorConnectionsHistoryRemoteColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_OrchestratorConnectionsHistoryRemoteColor_Type.__name__ = "Integer32"
_OrchestratorConnectionsHistoryRemoteColor_Object = MibTableColumn
orchestratorConnectionsHistoryRemoteColor = _OrchestratorConnectionsHistoryRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 13),
    _OrchestratorConnectionsHistoryRemoteColor_Type()
)
orchestratorConnectionsHistoryRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRemoteColor.setStatus("current")
_OrchestratorConnectionsHistoryState_Type = SessionState
_OrchestratorConnectionsHistoryState_Object = MibTableColumn
orchestratorConnectionsHistoryState = _OrchestratorConnectionsHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 14),
    _OrchestratorConnectionsHistoryState_Type()
)
orchestratorConnectionsHistoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryState.setStatus("current")
_OrchestratorConnectionsHistoryLocalEnum_Type = ConnFlagEnum
_OrchestratorConnectionsHistoryLocalEnum_Object = MibTableColumn
orchestratorConnectionsHistoryLocalEnum = _OrchestratorConnectionsHistoryLocalEnum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 15),
    _OrchestratorConnectionsHistoryLocalEnum_Type()
)
orchestratorConnectionsHistoryLocalEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryLocalEnum.setStatus("current")
_OrchestratorConnectionsHistoryRemoteEnum_Type = ConnFlagEnum
_OrchestratorConnectionsHistoryRemoteEnum_Object = MibTableColumn
orchestratorConnectionsHistoryRemoteEnum = _OrchestratorConnectionsHistoryRemoteEnum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 16),
    _OrchestratorConnectionsHistoryRemoteEnum_Type()
)
orchestratorConnectionsHistoryRemoteEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRemoteEnum.setStatus("current")
_OrchestratorConnectionsHistoryLocalStateInfo_Type = String
_OrchestratorConnectionsHistoryLocalStateInfo_Object = MibTableColumn
orchestratorConnectionsHistoryLocalStateInfo = _OrchestratorConnectionsHistoryLocalStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 17),
    _OrchestratorConnectionsHistoryLocalStateInfo_Type()
)
orchestratorConnectionsHistoryLocalStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryLocalStateInfo.setStatus("current")
_OrchestratorConnectionsHistoryRemoteStateInfo_Type = String
_OrchestratorConnectionsHistoryRemoteStateInfo_Object = MibTableColumn
orchestratorConnectionsHistoryRemoteStateInfo = _OrchestratorConnectionsHistoryRemoteStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 18),
    _OrchestratorConnectionsHistoryRemoteStateInfo_Type()
)
orchestratorConnectionsHistoryRemoteStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRemoteStateInfo.setStatus("current")
_OrchestratorConnectionsHistoryLocalPrivateIp_Type = InetAddressIP
_OrchestratorConnectionsHistoryLocalPrivateIp_Object = MibTableColumn
orchestratorConnectionsHistoryLocalPrivateIp = _OrchestratorConnectionsHistoryLocalPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 19),
    _OrchestratorConnectionsHistoryLocalPrivateIp_Type()
)
orchestratorConnectionsHistoryLocalPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryLocalPrivateIp.setStatus("current")
_OrchestratorConnectionsHistoryLocalPrivatePort_Type = Unsigned32
_OrchestratorConnectionsHistoryLocalPrivatePort_Object = MibTableColumn
orchestratorConnectionsHistoryLocalPrivatePort = _OrchestratorConnectionsHistoryLocalPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 20),
    _OrchestratorConnectionsHistoryLocalPrivatePort_Type()
)
orchestratorConnectionsHistoryLocalPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryLocalPrivatePort.setStatus("current")
_OrchestratorConnectionsHistoryDowntime_Type = String
_OrchestratorConnectionsHistoryDowntime_Object = MibTableColumn
orchestratorConnectionsHistoryDowntime = _OrchestratorConnectionsHistoryDowntime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 21),
    _OrchestratorConnectionsHistoryDowntime_Type()
)
orchestratorConnectionsHistoryDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryDowntime.setStatus("current")
_OrchestratorConnectionsHistoryTxHello_Type = Unsigned32
_OrchestratorConnectionsHistoryTxHello_Object = MibTableColumn
orchestratorConnectionsHistoryTxHello = _OrchestratorConnectionsHistoryTxHello_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 22),
    _OrchestratorConnectionsHistoryTxHello_Type()
)
orchestratorConnectionsHistoryTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxHello.setStatus("current")
_OrchestratorConnectionsHistoryTxConnects_Type = Unsigned32
_OrchestratorConnectionsHistoryTxConnects_Object = MibTableColumn
orchestratorConnectionsHistoryTxConnects = _OrchestratorConnectionsHistoryTxConnects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 23),
    _OrchestratorConnectionsHistoryTxConnects_Type()
)
orchestratorConnectionsHistoryTxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxConnects.setStatus("current")
_OrchestratorConnectionsHistoryTxRegisters_Type = Unsigned32
_OrchestratorConnectionsHistoryTxRegisters_Object = MibTableColumn
orchestratorConnectionsHistoryTxRegisters = _OrchestratorConnectionsHistoryTxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 24),
    _OrchestratorConnectionsHistoryTxRegisters_Type()
)
orchestratorConnectionsHistoryTxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxRegisters.setStatus("current")
_OrchestratorConnectionsHistoryTxRegisterReplies_Type = Unsigned32
_OrchestratorConnectionsHistoryTxRegisterReplies_Object = MibTableColumn
orchestratorConnectionsHistoryTxRegisterReplies = _OrchestratorConnectionsHistoryTxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 25),
    _OrchestratorConnectionsHistoryTxRegisterReplies_Type()
)
orchestratorConnectionsHistoryTxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxRegisterReplies.setStatus("current")
_OrchestratorConnectionsHistoryTxChallenge_Type = Unsigned32
_OrchestratorConnectionsHistoryTxChallenge_Object = MibTableColumn
orchestratorConnectionsHistoryTxChallenge = _OrchestratorConnectionsHistoryTxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 26),
    _OrchestratorConnectionsHistoryTxChallenge_Type()
)
orchestratorConnectionsHistoryTxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxChallenge.setStatus("current")
_OrchestratorConnectionsHistoryTxChallengeResp_Type = Unsigned32
_OrchestratorConnectionsHistoryTxChallengeResp_Object = MibTableColumn
orchestratorConnectionsHistoryTxChallengeResp = _OrchestratorConnectionsHistoryTxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 27),
    _OrchestratorConnectionsHistoryTxChallengeResp_Type()
)
orchestratorConnectionsHistoryTxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxChallengeResp.setStatus("current")
_OrchestratorConnectionsHistoryTxChallengeAck_Type = Unsigned32
_OrchestratorConnectionsHistoryTxChallengeAck_Object = MibTableColumn
orchestratorConnectionsHistoryTxChallengeAck = _OrchestratorConnectionsHistoryTxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 28),
    _OrchestratorConnectionsHistoryTxChallengeAck_Type()
)
orchestratorConnectionsHistoryTxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxChallengeAck.setStatus("current")
_OrchestratorConnectionsHistoryTxTeardown_Type = Unsigned32
_OrchestratorConnectionsHistoryTxTeardown_Object = MibTableColumn
orchestratorConnectionsHistoryTxTeardown = _OrchestratorConnectionsHistoryTxTeardown_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 29),
    _OrchestratorConnectionsHistoryTxTeardown_Type()
)
orchestratorConnectionsHistoryTxTeardown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxTeardown.setStatus("current")
_OrchestratorConnectionsHistoryTxTeardownAll_Type = Unsigned32
_OrchestratorConnectionsHistoryTxTeardownAll_Object = MibTableColumn
orchestratorConnectionsHistoryTxTeardownAll = _OrchestratorConnectionsHistoryTxTeardownAll_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 30),
    _OrchestratorConnectionsHistoryTxTeardownAll_Type()
)
orchestratorConnectionsHistoryTxTeardownAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxTeardownAll.setStatus("current")
_OrchestratorConnectionsHistoryTxVmToPeer_Type = Unsigned32
_OrchestratorConnectionsHistoryTxVmToPeer_Object = MibTableColumn
orchestratorConnectionsHistoryTxVmToPeer = _OrchestratorConnectionsHistoryTxVmToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 31),
    _OrchestratorConnectionsHistoryTxVmToPeer_Type()
)
orchestratorConnectionsHistoryTxVmToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxVmToPeer.setStatus("current")
_OrchestratorConnectionsHistoryTxRegisterToVm_Type = Unsigned32
_OrchestratorConnectionsHistoryTxRegisterToVm_Object = MibTableColumn
orchestratorConnectionsHistoryTxRegisterToVm = _OrchestratorConnectionsHistoryTxRegisterToVm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 32),
    _OrchestratorConnectionsHistoryTxRegisterToVm_Type()
)
orchestratorConnectionsHistoryTxRegisterToVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxRegisterToVm.setStatus("current")
_OrchestratorConnectionsHistoryRxHello_Type = Unsigned32
_OrchestratorConnectionsHistoryRxHello_Object = MibTableColumn
orchestratorConnectionsHistoryRxHello = _OrchestratorConnectionsHistoryRxHello_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 33),
    _OrchestratorConnectionsHistoryRxHello_Type()
)
orchestratorConnectionsHistoryRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRxHello.setStatus("current")
_OrchestratorConnectionsHistoryRxConnects_Type = Unsigned32
_OrchestratorConnectionsHistoryRxConnects_Object = MibTableColumn
orchestratorConnectionsHistoryRxConnects = _OrchestratorConnectionsHistoryRxConnects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 34),
    _OrchestratorConnectionsHistoryRxConnects_Type()
)
orchestratorConnectionsHistoryRxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRxConnects.setStatus("current")
_OrchestratorConnectionsHistoryRxRegisters_Type = Unsigned32
_OrchestratorConnectionsHistoryRxRegisters_Object = MibTableColumn
orchestratorConnectionsHistoryRxRegisters = _OrchestratorConnectionsHistoryRxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 35),
    _OrchestratorConnectionsHistoryRxRegisters_Type()
)
orchestratorConnectionsHistoryRxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRxRegisters.setStatus("current")
_OrchestratorConnectionsHistoryRxRegisterReplies_Type = Unsigned32
_OrchestratorConnectionsHistoryRxRegisterReplies_Object = MibTableColumn
orchestratorConnectionsHistoryRxRegisterReplies = _OrchestratorConnectionsHistoryRxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 36),
    _OrchestratorConnectionsHistoryRxRegisterReplies_Type()
)
orchestratorConnectionsHistoryRxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRxRegisterReplies.setStatus("current")
_OrchestratorConnectionsHistoryRxChallenge_Type = Unsigned32
_OrchestratorConnectionsHistoryRxChallenge_Object = MibTableColumn
orchestratorConnectionsHistoryRxChallenge = _OrchestratorConnectionsHistoryRxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 37),
    _OrchestratorConnectionsHistoryRxChallenge_Type()
)
orchestratorConnectionsHistoryRxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRxChallenge.setStatus("current")
_OrchestratorConnectionsHistoryRxChallengeResp_Type = Unsigned32
_OrchestratorConnectionsHistoryRxChallengeResp_Object = MibTableColumn
orchestratorConnectionsHistoryRxChallengeResp = _OrchestratorConnectionsHistoryRxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 38),
    _OrchestratorConnectionsHistoryRxChallengeResp_Type()
)
orchestratorConnectionsHistoryRxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRxChallengeResp.setStatus("current")
_OrchestratorConnectionsHistoryRxChallengeAck_Type = Unsigned32
_OrchestratorConnectionsHistoryRxChallengeAck_Object = MibTableColumn
orchestratorConnectionsHistoryRxChallengeAck = _OrchestratorConnectionsHistoryRxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 39),
    _OrchestratorConnectionsHistoryRxChallengeAck_Type()
)
orchestratorConnectionsHistoryRxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRxChallengeAck.setStatus("current")
_OrchestratorConnectionsHistoryRxTeardown_Type = Unsigned32
_OrchestratorConnectionsHistoryRxTeardown_Object = MibTableColumn
orchestratorConnectionsHistoryRxTeardown = _OrchestratorConnectionsHistoryRxTeardown_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 40),
    _OrchestratorConnectionsHistoryRxTeardown_Type()
)
orchestratorConnectionsHistoryRxTeardown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRxTeardown.setStatus("current")
_OrchestratorConnectionsHistoryRxVmToPeer_Type = Unsigned32
_OrchestratorConnectionsHistoryRxVmToPeer_Object = MibTableColumn
orchestratorConnectionsHistoryRxVmToPeer = _OrchestratorConnectionsHistoryRxVmToPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 41),
    _OrchestratorConnectionsHistoryRxVmToPeer_Type()
)
orchestratorConnectionsHistoryRxVmToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRxVmToPeer.setStatus("current")
_OrchestratorConnectionsHistoryRxRegisterToVm_Type = Unsigned32
_OrchestratorConnectionsHistoryRxRegisterToVm_Object = MibTableColumn
orchestratorConnectionsHistoryRxRegisterToVm = _OrchestratorConnectionsHistoryRxRegisterToVm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 42),
    _OrchestratorConnectionsHistoryRxRegisterToVm_Type()
)
orchestratorConnectionsHistoryRxRegisterToVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRxRegisterToVm.setStatus("current")
_OrchestratorConnectionsHistoryRepCount_Type = Unsigned32
_OrchestratorConnectionsHistoryRepCount_Object = MibTableColumn
orchestratorConnectionsHistoryRepCount = _OrchestratorConnectionsHistoryRepCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 43),
    _OrchestratorConnectionsHistoryRepCount_Type()
)
orchestratorConnectionsHistoryRepCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRepCount.setStatus("current")
_OrchestratorConnectionsHistoryPrevDowntime_Type = String
_OrchestratorConnectionsHistoryPrevDowntime_Object = MibTableColumn
orchestratorConnectionsHistoryPrevDowntime = _OrchestratorConnectionsHistoryPrevDowntime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 44),
    _OrchestratorConnectionsHistoryPrevDowntime_Type()
)
orchestratorConnectionsHistoryPrevDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryPrevDowntime.setStatus("current")
_OrchestratorConnectionsHistoryHOrgname_Type = String
_OrchestratorConnectionsHistoryHOrgname_Object = MibTableColumn
orchestratorConnectionsHistoryHOrgname = _OrchestratorConnectionsHistoryHOrgname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 45),
    _OrchestratorConnectionsHistoryHOrgname_Type()
)
orchestratorConnectionsHistoryHOrgname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryHOrgname.setStatus("current")
_OrchestratorConnectionsHistoryHSporgname_Type = String
_OrchestratorConnectionsHistoryHSporgname_Object = MibTableColumn
orchestratorConnectionsHistoryHSporgname = _OrchestratorConnectionsHistoryHSporgname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 46),
    _OrchestratorConnectionsHistoryHSporgname_Type()
)
orchestratorConnectionsHistoryHSporgname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryHSporgname.setStatus("current")
_OrchestratorConnectionsHistoryUuid_Type = String
_OrchestratorConnectionsHistoryUuid_Object = MibTableColumn
orchestratorConnectionsHistoryUuid = _OrchestratorConnectionsHistoryUuid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 47),
    _OrchestratorConnectionsHistoryUuid_Type()
)
orchestratorConnectionsHistoryUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryUuid.setStatus("current")
_OrchestratorConnectionsHistoryTxCreateCert_Type = Unsigned32
_OrchestratorConnectionsHistoryTxCreateCert_Object = MibTableColumn
orchestratorConnectionsHistoryTxCreateCert = _OrchestratorConnectionsHistoryTxCreateCert_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 48),
    _OrchestratorConnectionsHistoryTxCreateCert_Type()
)
orchestratorConnectionsHistoryTxCreateCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxCreateCert.setStatus("current")
_OrchestratorConnectionsHistoryRxCreateCert_Type = Unsigned32
_OrchestratorConnectionsHistoryRxCreateCert_Object = MibTableColumn
orchestratorConnectionsHistoryRxCreateCert = _OrchestratorConnectionsHistoryRxCreateCert_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 49),
    _OrchestratorConnectionsHistoryRxCreateCert_Type()
)
orchestratorConnectionsHistoryRxCreateCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRxCreateCert.setStatus("current")
_OrchestratorConnectionsHistoryTxCreateCertReply_Type = Unsigned32
_OrchestratorConnectionsHistoryTxCreateCertReply_Object = MibTableColumn
orchestratorConnectionsHistoryTxCreateCertReply = _OrchestratorConnectionsHistoryTxCreateCertReply_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 50),
    _OrchestratorConnectionsHistoryTxCreateCertReply_Type()
)
orchestratorConnectionsHistoryTxCreateCertReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryTxCreateCertReply.setStatus("current")
_OrchestratorConnectionsHistoryRxCreateCertReply_Type = Unsigned32
_OrchestratorConnectionsHistoryRxCreateCertReply_Object = MibTableColumn
orchestratorConnectionsHistoryRxCreateCertReply = _OrchestratorConnectionsHistoryRxCreateCertReply_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 2, 1, 51),
    _OrchestratorConnectionsHistoryRxCreateCertReply_Type()
)
orchestratorConnectionsHistoryRxCreateCertReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorConnectionsHistoryRxCreateCertReply.setStatus("current")
_OrchestratorStatistics_ObjectIdentity = ObjectIdentity
orchestratorStatistics = _OrchestratorStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3)
)
_OrchestratorStatisticsTxPkts_Type = ConfdString
_OrchestratorStatisticsTxPkts_Object = MibScalar
orchestratorStatisticsTxPkts = _OrchestratorStatisticsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 1),
    _OrchestratorStatisticsTxPkts_Type()
)
orchestratorStatisticsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxPkts.setStatus("current")
_OrchestratorStatisticsTxOctets_Type = Unsigned32
_OrchestratorStatisticsTxOctets_Object = MibScalar
orchestratorStatisticsTxOctets = _OrchestratorStatisticsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 2),
    _OrchestratorStatisticsTxOctets_Type()
)
orchestratorStatisticsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxOctets.setStatus("current")
_OrchestratorStatisticsTxError_Type = Unsigned32
_OrchestratorStatisticsTxError_Object = MibScalar
orchestratorStatisticsTxError = _OrchestratorStatisticsTxError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 3),
    _OrchestratorStatisticsTxError_Type()
)
orchestratorStatisticsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxError.setStatus("current")
_OrchestratorStatisticsTxBlocked_Type = Unsigned32
_OrchestratorStatisticsTxBlocked_Object = MibScalar
orchestratorStatisticsTxBlocked = _OrchestratorStatisticsTxBlocked_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 4),
    _OrchestratorStatisticsTxBlocked_Type()
)
orchestratorStatisticsTxBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxBlocked.setStatus("current")
_OrchestratorStatisticsTxConnects_Type = Unsigned32
_OrchestratorStatisticsTxConnects_Object = MibScalar
orchestratorStatisticsTxConnects = _OrchestratorStatisticsTxConnects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 5),
    _OrchestratorStatisticsTxConnects_Type()
)
orchestratorStatisticsTxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxConnects.setStatus("current")
_OrchestratorStatisticsTxRegisters_Type = Unsigned32
_OrchestratorStatisticsTxRegisters_Object = MibScalar
orchestratorStatisticsTxRegisters = _OrchestratorStatisticsTxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 6),
    _OrchestratorStatisticsTxRegisters_Type()
)
orchestratorStatisticsTxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxRegisters.setStatus("current")
_OrchestratorStatisticsTxRegisterReplies_Type = Unsigned32
_OrchestratorStatisticsTxRegisterReplies_Object = MibScalar
orchestratorStatisticsTxRegisterReplies = _OrchestratorStatisticsTxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 7),
    _OrchestratorStatisticsTxRegisterReplies_Type()
)
orchestratorStatisticsTxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxRegisterReplies.setStatus("current")
_OrchestratorStatisticsTxDtlsHandshake_Type = Unsigned32
_OrchestratorStatisticsTxDtlsHandshake_Object = MibScalar
orchestratorStatisticsTxDtlsHandshake = _OrchestratorStatisticsTxDtlsHandshake_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 8),
    _OrchestratorStatisticsTxDtlsHandshake_Type()
)
orchestratorStatisticsTxDtlsHandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxDtlsHandshake.setStatus("current")
_OrchestratorStatisticsTxDtlsHandshakeFailures_Type = Unsigned32
_OrchestratorStatisticsTxDtlsHandshakeFailures_Object = MibScalar
orchestratorStatisticsTxDtlsHandshakeFailures = _OrchestratorStatisticsTxDtlsHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 9),
    _OrchestratorStatisticsTxDtlsHandshakeFailures_Type()
)
orchestratorStatisticsTxDtlsHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxDtlsHandshakeFailures.setStatus("current")
_OrchestratorStatisticsTxDtlsHandshakeDone_Type = Unsigned32
_OrchestratorStatisticsTxDtlsHandshakeDone_Object = MibScalar
orchestratorStatisticsTxDtlsHandshakeDone = _OrchestratorStatisticsTxDtlsHandshakeDone_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 10),
    _OrchestratorStatisticsTxDtlsHandshakeDone_Type()
)
orchestratorStatisticsTxDtlsHandshakeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxDtlsHandshakeDone.setStatus("current")
_OrchestratorStatisticsTxChallenge_Type = Unsigned32
_OrchestratorStatisticsTxChallenge_Object = MibScalar
orchestratorStatisticsTxChallenge = _OrchestratorStatisticsTxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 11),
    _OrchestratorStatisticsTxChallenge_Type()
)
orchestratorStatisticsTxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxChallenge.setStatus("current")
_OrchestratorStatisticsTxChallengeResp_Type = Unsigned32
_OrchestratorStatisticsTxChallengeResp_Object = MibScalar
orchestratorStatisticsTxChallengeResp = _OrchestratorStatisticsTxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 12),
    _OrchestratorStatisticsTxChallengeResp_Type()
)
orchestratorStatisticsTxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxChallengeResp.setStatus("current")
_OrchestratorStatisticsTxChallengeAck_Type = Unsigned32
_OrchestratorStatisticsTxChallengeAck_Object = MibScalar
orchestratorStatisticsTxChallengeAck = _OrchestratorStatisticsTxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 13),
    _OrchestratorStatisticsTxChallengeAck_Type()
)
orchestratorStatisticsTxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxChallengeAck.setStatus("current")
_OrchestratorStatisticsTxChallengeError_Type = Unsigned32
_OrchestratorStatisticsTxChallengeError_Object = MibScalar
orchestratorStatisticsTxChallengeError = _OrchestratorStatisticsTxChallengeError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 14),
    _OrchestratorStatisticsTxChallengeError_Type()
)
orchestratorStatisticsTxChallengeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxChallengeError.setStatus("current")
_OrchestratorStatisticsTxChallengeRespError_Type = Unsigned32
_OrchestratorStatisticsTxChallengeRespError_Object = MibScalar
orchestratorStatisticsTxChallengeRespError = _OrchestratorStatisticsTxChallengeRespError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 15),
    _OrchestratorStatisticsTxChallengeRespError_Type()
)
orchestratorStatisticsTxChallengeRespError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxChallengeRespError.setStatus("current")
_OrchestratorStatisticsTxChallengeAckError_Type = Unsigned32
_OrchestratorStatisticsTxChallengeAckError_Object = MibScalar
orchestratorStatisticsTxChallengeAckError = _OrchestratorStatisticsTxChallengeAckError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 16),
    _OrchestratorStatisticsTxChallengeAckError_Type()
)
orchestratorStatisticsTxChallengeAckError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxChallengeAckError.setStatus("current")
_OrchestratorStatisticsTxChallengeGenError_Type = Unsigned32
_OrchestratorStatisticsTxChallengeGenError_Object = MibScalar
orchestratorStatisticsTxChallengeGenError = _OrchestratorStatisticsTxChallengeGenError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 17),
    _OrchestratorStatisticsTxChallengeGenError_Type()
)
orchestratorStatisticsTxChallengeGenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsTxChallengeGenError.setStatus("current")
_OrchestratorStatisticsRxPkts_Type = ConfdString
_OrchestratorStatisticsRxPkts_Object = MibScalar
orchestratorStatisticsRxPkts = _OrchestratorStatisticsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 18),
    _OrchestratorStatisticsRxPkts_Type()
)
orchestratorStatisticsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsRxPkts.setStatus("current")
_OrchestratorStatisticsRxOctets_Type = Unsigned32
_OrchestratorStatisticsRxOctets_Object = MibScalar
orchestratorStatisticsRxOctets = _OrchestratorStatisticsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 19),
    _OrchestratorStatisticsRxOctets_Type()
)
orchestratorStatisticsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsRxOctets.setStatus("current")
_OrchestratorStatisticsRxError_Type = Unsigned32
_OrchestratorStatisticsRxError_Object = MibScalar
orchestratorStatisticsRxError = _OrchestratorStatisticsRxError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 20),
    _OrchestratorStatisticsRxError_Type()
)
orchestratorStatisticsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsRxError.setStatus("current")
_OrchestratorStatisticsRxConnects_Type = Unsigned32
_OrchestratorStatisticsRxConnects_Object = MibScalar
orchestratorStatisticsRxConnects = _OrchestratorStatisticsRxConnects_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 21),
    _OrchestratorStatisticsRxConnects_Type()
)
orchestratorStatisticsRxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsRxConnects.setStatus("current")
_OrchestratorStatisticsRxRegisters_Type = Unsigned32
_OrchestratorStatisticsRxRegisters_Object = MibScalar
orchestratorStatisticsRxRegisters = _OrchestratorStatisticsRxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 22),
    _OrchestratorStatisticsRxRegisters_Type()
)
orchestratorStatisticsRxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsRxRegisters.setStatus("current")
_OrchestratorStatisticsRxRegisterReplies_Type = Unsigned32
_OrchestratorStatisticsRxRegisterReplies_Object = MibScalar
orchestratorStatisticsRxRegisterReplies = _OrchestratorStatisticsRxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 23),
    _OrchestratorStatisticsRxRegisterReplies_Type()
)
orchestratorStatisticsRxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsRxRegisterReplies.setStatus("current")
_OrchestratorStatisticsRxDtlsHandshake_Type = Unsigned32
_OrchestratorStatisticsRxDtlsHandshake_Object = MibScalar
orchestratorStatisticsRxDtlsHandshake = _OrchestratorStatisticsRxDtlsHandshake_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 24),
    _OrchestratorStatisticsRxDtlsHandshake_Type()
)
orchestratorStatisticsRxDtlsHandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsRxDtlsHandshake.setStatus("current")
_OrchestratorStatisticsRxDtlsHandshakeFailures_Type = Unsigned32
_OrchestratorStatisticsRxDtlsHandshakeFailures_Object = MibScalar
orchestratorStatisticsRxDtlsHandshakeFailures = _OrchestratorStatisticsRxDtlsHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 25),
    _OrchestratorStatisticsRxDtlsHandshakeFailures_Type()
)
orchestratorStatisticsRxDtlsHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsRxDtlsHandshakeFailures.setStatus("current")
_OrchestratorStatisticsRxDtlsHandshakeDone_Type = Unsigned32
_OrchestratorStatisticsRxDtlsHandshakeDone_Object = MibScalar
orchestratorStatisticsRxDtlsHandshakeDone = _OrchestratorStatisticsRxDtlsHandshakeDone_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 26),
    _OrchestratorStatisticsRxDtlsHandshakeDone_Type()
)
orchestratorStatisticsRxDtlsHandshakeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsRxDtlsHandshakeDone.setStatus("current")
_OrchestratorStatisticsRxChallenge_Type = Unsigned32
_OrchestratorStatisticsRxChallenge_Object = MibScalar
orchestratorStatisticsRxChallenge = _OrchestratorStatisticsRxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 27),
    _OrchestratorStatisticsRxChallenge_Type()
)
orchestratorStatisticsRxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsRxChallenge.setStatus("current")
_OrchestratorStatisticsRxChallengeResp_Type = Unsigned32
_OrchestratorStatisticsRxChallengeResp_Object = MibScalar
orchestratorStatisticsRxChallengeResp = _OrchestratorStatisticsRxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 28),
    _OrchestratorStatisticsRxChallengeResp_Type()
)
orchestratorStatisticsRxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsRxChallengeResp.setStatus("current")
_OrchestratorStatisticsRxChallengeAck_Type = Unsigned32
_OrchestratorStatisticsRxChallengeAck_Object = MibScalar
orchestratorStatisticsRxChallengeAck = _OrchestratorStatisticsRxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 29),
    _OrchestratorStatisticsRxChallengeAck_Type()
)
orchestratorStatisticsRxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsRxChallengeAck.setStatus("current")
_OrchestratorStatisticsChallengeFailures_Type = Unsigned32
_OrchestratorStatisticsChallengeFailures_Object = MibScalar
orchestratorStatisticsChallengeFailures = _OrchestratorStatisticsChallengeFailures_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 3, 30),
    _OrchestratorStatisticsChallengeFailures_Type()
)
orchestratorStatisticsChallengeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorStatisticsChallengeFailures.setStatus("current")
_OrchestratorLocalProperties_ObjectIdentity = ObjectIdentity
orchestratorLocalProperties = _OrchestratorLocalProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4)
)


class _OrchestratorLocalPropertiesDeviceType_Type(Integer32):
    """Custom type orchestratorLocalPropertiesDeviceType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )


_OrchestratorLocalPropertiesDeviceType_Type.__name__ = "Integer32"
_OrchestratorLocalPropertiesDeviceType_Object = MibScalar
orchestratorLocalPropertiesDeviceType = _OrchestratorLocalPropertiesDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 1),
    _OrchestratorLocalPropertiesDeviceType_Type()
)
orchestratorLocalPropertiesDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesDeviceType.setStatus("current")


class _OrchestratorLocalPropertiesOrganizationName_Type(String):
    """Custom type orchestratorLocalPropertiesOrganizationName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OrchestratorLocalPropertiesOrganizationName_Type.__name__ = "String"
_OrchestratorLocalPropertiesOrganizationName_Object = MibScalar
orchestratorLocalPropertiesOrganizationName = _OrchestratorLocalPropertiesOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 2),
    _OrchestratorLocalPropertiesOrganizationName_Type()
)
orchestratorLocalPropertiesOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesOrganizationName.setStatus("current")
_OrchestratorLocalPropertiesCertificateStatus_Type = String
_OrchestratorLocalPropertiesCertificateStatus_Object = MibScalar
orchestratorLocalPropertiesCertificateStatus = _OrchestratorLocalPropertiesCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 3),
    _OrchestratorLocalPropertiesCertificateStatus_Type()
)
orchestratorLocalPropertiesCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesCertificateStatus.setStatus("current")
_OrchestratorLocalPropertiesRootCaChainStatus_Type = String
_OrchestratorLocalPropertiesRootCaChainStatus_Object = MibScalar
orchestratorLocalPropertiesRootCaChainStatus = _OrchestratorLocalPropertiesRootCaChainStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 4),
    _OrchestratorLocalPropertiesRootCaChainStatus_Type()
)
orchestratorLocalPropertiesRootCaChainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesRootCaChainStatus.setStatus("current")
_OrchestratorLocalPropertiesCertificateValidity_Type = String
_OrchestratorLocalPropertiesCertificateValidity_Object = MibScalar
orchestratorLocalPropertiesCertificateValidity = _OrchestratorLocalPropertiesCertificateValidity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 5),
    _OrchestratorLocalPropertiesCertificateValidity_Type()
)
orchestratorLocalPropertiesCertificateValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesCertificateValidity.setStatus("current")
_OrchestratorLocalPropertiesCertificateNotValidBefore_Type = String
_OrchestratorLocalPropertiesCertificateNotValidBefore_Object = MibScalar
orchestratorLocalPropertiesCertificateNotValidBefore = _OrchestratorLocalPropertiesCertificateNotValidBefore_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 6),
    _OrchestratorLocalPropertiesCertificateNotValidBefore_Type()
)
orchestratorLocalPropertiesCertificateNotValidBefore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesCertificateNotValidBefore.setStatus("current")
_OrchestratorLocalPropertiesCertificateNotValidAfter_Type = String
_OrchestratorLocalPropertiesCertificateNotValidAfter_Object = MibScalar
orchestratorLocalPropertiesCertificateNotValidAfter = _OrchestratorLocalPropertiesCertificateNotValidAfter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 7),
    _OrchestratorLocalPropertiesCertificateNotValidAfter_Type()
)
orchestratorLocalPropertiesCertificateNotValidAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesCertificateNotValidAfter.setStatus("current")
_OrchestratorLocalPropertiesUuid_Type = String
_OrchestratorLocalPropertiesUuid_Object = MibScalar
orchestratorLocalPropertiesUuid = _OrchestratorLocalPropertiesUuid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 8),
    _OrchestratorLocalPropertiesUuid_Type()
)
orchestratorLocalPropertiesUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesUuid.setStatus("current")


class _OrchestratorLocalPropertiesBoardSerial_Type(String):
    """Custom type orchestratorLocalPropertiesBoardSerial based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_OrchestratorLocalPropertiesBoardSerial_Type.__name__ = "String"
_OrchestratorLocalPropertiesBoardSerial_Object = MibScalar
orchestratorLocalPropertiesBoardSerial = _OrchestratorLocalPropertiesBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 9),
    _OrchestratorLocalPropertiesBoardSerial_Type()
)
orchestratorLocalPropertiesBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesBoardSerial.setStatus("current")
_OrchestratorLocalPropertiesNumberActiveWanInterfaces_Type = Unsigned32
_OrchestratorLocalPropertiesNumberActiveWanInterfaces_Object = MibScalar
orchestratorLocalPropertiesNumberActiveWanInterfaces = _OrchestratorLocalPropertiesNumberActiveWanInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 10),
    _OrchestratorLocalPropertiesNumberActiveWanInterfaces_Type()
)
orchestratorLocalPropertiesNumberActiveWanInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesNumberActiveWanInterfaces.setStatus("current")


class _OrchestratorLocalPropertiesProtocol_Type(Integer32):
    """Custom type orchestratorLocalPropertiesProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dtls", 0),
          ("tls", 1))
    )


_OrchestratorLocalPropertiesProtocol_Type.__name__ = "Integer32"
_OrchestratorLocalPropertiesProtocol_Object = MibScalar
orchestratorLocalPropertiesProtocol = _OrchestratorLocalPropertiesProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 11),
    _OrchestratorLocalPropertiesProtocol_Type()
)
orchestratorLocalPropertiesProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesProtocol.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListTable_Object = MibTable
orchestratorLocalPropertiesWanInterfaceListTable = _OrchestratorLocalPropertiesWanInterfaceListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12)
)
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListTable.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListEntry_Object = MibTableRow
orchestratorLocalPropertiesWanInterfaceListEntry = _OrchestratorLocalPropertiesWanInterfaceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12, 1)
)
orchestratorLocalPropertiesWanInterfaceListEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "orchestratorLocalPropertiesWanInterfaceListInstance"),
    (0, "VIPTELA-SECURITY", "orchestratorLocalPropertiesWanInterfaceListIndex"),
)
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListEntry.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListIndex_Type = Unsigned32
_OrchestratorLocalPropertiesWanInterfaceListIndex_Object = MibTableColumn
orchestratorLocalPropertiesWanInterfaceListIndex = _OrchestratorLocalPropertiesWanInterfaceListIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12, 1, 1),
    _OrchestratorLocalPropertiesWanInterfaceListIndex_Type()
)
orchestratorLocalPropertiesWanInterfaceListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListIndex.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListIp_Type = InetAddressIP
_OrchestratorLocalPropertiesWanInterfaceListIp_Object = MibTableColumn
orchestratorLocalPropertiesWanInterfaceListIp = _OrchestratorLocalPropertiesWanInterfaceListIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12, 1, 2),
    _OrchestratorLocalPropertiesWanInterfaceListIp_Type()
)
orchestratorLocalPropertiesWanInterfaceListIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListIp.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListPort_Type = Unsigned32
_OrchestratorLocalPropertiesWanInterfaceListPort_Object = MibTableColumn
orchestratorLocalPropertiesWanInterfaceListPort = _OrchestratorLocalPropertiesWanInterfaceListPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12, 1, 3),
    _OrchestratorLocalPropertiesWanInterfaceListPort_Type()
)
orchestratorLocalPropertiesWanInterfaceListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListPort.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListNumVsmarts_Type = Unsigned32
_OrchestratorLocalPropertiesWanInterfaceListNumVsmarts_Object = MibTableColumn
orchestratorLocalPropertiesWanInterfaceListNumVsmarts = _OrchestratorLocalPropertiesWanInterfaceListNumVsmarts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12, 1, 4),
    _OrchestratorLocalPropertiesWanInterfaceListNumVsmarts_Type()
)
orchestratorLocalPropertiesWanInterfaceListNumVsmarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListNumVsmarts.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListNumVmanages_Type = Unsigned32
_OrchestratorLocalPropertiesWanInterfaceListNumVmanages_Object = MibTableColumn
orchestratorLocalPropertiesWanInterfaceListNumVmanages = _OrchestratorLocalPropertiesWanInterfaceListNumVmanages_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12, 1, 5),
    _OrchestratorLocalPropertiesWanInterfaceListNumVmanages_Type()
)
orchestratorLocalPropertiesWanInterfaceListNumVmanages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListNumVmanages.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListAdminState_Type = StateEnum
_OrchestratorLocalPropertiesWanInterfaceListAdminState_Object = MibTableColumn
orchestratorLocalPropertiesWanInterfaceListAdminState = _OrchestratorLocalPropertiesWanInterfaceListAdminState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12, 1, 6),
    _OrchestratorLocalPropertiesWanInterfaceListAdminState_Type()
)
orchestratorLocalPropertiesWanInterfaceListAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListAdminState.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListOperationState_Type = StateEnum
_OrchestratorLocalPropertiesWanInterfaceListOperationState_Object = MibTableColumn
orchestratorLocalPropertiesWanInterfaceListOperationState = _OrchestratorLocalPropertiesWanInterfaceListOperationState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12, 1, 7),
    _OrchestratorLocalPropertiesWanInterfaceListOperationState_Type()
)
orchestratorLocalPropertiesWanInterfaceListOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListOperationState.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListLastConnTime_Type = String
_OrchestratorLocalPropertiesWanInterfaceListLastConnTime_Object = MibTableColumn
orchestratorLocalPropertiesWanInterfaceListLastConnTime = _OrchestratorLocalPropertiesWanInterfaceListLastConnTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12, 1, 8),
    _OrchestratorLocalPropertiesWanInterfaceListLastConnTime_Type()
)
orchestratorLocalPropertiesWanInterfaceListLastConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListLastConnTime.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListInstance_Type = Unsigned32
_OrchestratorLocalPropertiesWanInterfaceListInstance_Object = MibTableColumn
orchestratorLocalPropertiesWanInterfaceListInstance = _OrchestratorLocalPropertiesWanInterfaceListInstance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12, 1, 9),
    _OrchestratorLocalPropertiesWanInterfaceListInstance_Type()
)
orchestratorLocalPropertiesWanInterfaceListInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListInstance.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListInterfaceAdminState_Type = StateEnum
_OrchestratorLocalPropertiesWanInterfaceListInterfaceAdminState_Object = MibTableColumn
orchestratorLocalPropertiesWanInterfaceListInterfaceAdminState = _OrchestratorLocalPropertiesWanInterfaceListInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12, 1, 10),
    _OrchestratorLocalPropertiesWanInterfaceListInterfaceAdminState_Type()
)
orchestratorLocalPropertiesWanInterfaceListInterfaceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListInterfaceAdminState.setStatus("current")
_OrchestratorLocalPropertiesWanInterfaceListInterfaceOperState_Type = StateEnum
_OrchestratorLocalPropertiesWanInterfaceListInterfaceOperState_Object = MibTableColumn
orchestratorLocalPropertiesWanInterfaceListInterfaceOperState = _OrchestratorLocalPropertiesWanInterfaceListInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 12, 1, 11),
    _OrchestratorLocalPropertiesWanInterfaceListInterfaceOperState_Type()
)
orchestratorLocalPropertiesWanInterfaceListInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesWanInterfaceListInterfaceOperState.setStatus("current")
_OrchestratorLocalPropertiesSystemIp_Type = InetAddressIP
_OrchestratorLocalPropertiesSystemIp_Object = MibScalar
orchestratorLocalPropertiesSystemIp = _OrchestratorLocalPropertiesSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 13),
    _OrchestratorLocalPropertiesSystemIp_Type()
)
orchestratorLocalPropertiesSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesSystemIp.setStatus("current")
_OrchestratorLocalPropertiesVedgeListVersion_Type = Counter64
_OrchestratorLocalPropertiesVedgeListVersion_Object = MibScalar
orchestratorLocalPropertiesVedgeListVersion = _OrchestratorLocalPropertiesVedgeListVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 14),
    _OrchestratorLocalPropertiesVedgeListVersion_Type()
)
orchestratorLocalPropertiesVedgeListVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesVedgeListVersion.setStatus("current")
_OrchestratorLocalPropertiesVsmartListVersion_Type = Counter64
_OrchestratorLocalPropertiesVsmartListVersion_Object = MibScalar
orchestratorLocalPropertiesVsmartListVersion = _OrchestratorLocalPropertiesVsmartListVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 15),
    _OrchestratorLocalPropertiesVsmartListVersion_Type()
)
orchestratorLocalPropertiesVsmartListVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesVsmartListVersion.setStatus("current")


class _OrchestratorLocalPropertiesSPOrganizationName_Type(String):
    """Custom type orchestratorLocalPropertiesSPOrganizationName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OrchestratorLocalPropertiesSPOrganizationName_Type.__name__ = "String"
_OrchestratorLocalPropertiesSPOrganizationName_Object = MibScalar
orchestratorLocalPropertiesSPOrganizationName = _OrchestratorLocalPropertiesSPOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 4, 16),
    _OrchestratorLocalPropertiesSPOrganizationName_Type()
)
orchestratorLocalPropertiesSPOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorLocalPropertiesSPOrganizationName.setStatus("current")
_OrchestratorValidVsmartsTable_Object = MibTable
orchestratorValidVsmartsTable = _OrchestratorValidVsmartsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 5)
)
if mibBuilder.loadTexts:
    orchestratorValidVsmartsTable.setStatus("current")
_OrchestratorValidVsmartsEntry_Object = MibTableRow
orchestratorValidVsmartsEntry = _OrchestratorValidVsmartsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 5, 1)
)
orchestratorValidVsmartsEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "orchestratorValidVsmartsSerialNumber"),
    (0, "VIPTELA-SECURITY", "orchestratorValidVsmartsOrg"),
)
if mibBuilder.loadTexts:
    orchestratorValidVsmartsEntry.setStatus("current")


class _OrchestratorValidVsmartsSerialNumber_Type(String):
    """Custom type orchestratorValidVsmartsSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_OrchestratorValidVsmartsSerialNumber_Type.__name__ = "String"
_OrchestratorValidVsmartsSerialNumber_Object = MibTableColumn
orchestratorValidVsmartsSerialNumber = _OrchestratorValidVsmartsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 5, 1, 1),
    _OrchestratorValidVsmartsSerialNumber_Type()
)
orchestratorValidVsmartsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorValidVsmartsSerialNumber.setStatus("current")
_OrchestratorValidVsmartsOrg_Type = String
_OrchestratorValidVsmartsOrg_Object = MibTableColumn
orchestratorValidVsmartsOrg = _OrchestratorValidVsmartsOrg_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 5, 1, 2),
    _OrchestratorValidVsmartsOrg_Type()
)
orchestratorValidVsmartsOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorValidVsmartsOrg.setStatus("current")
_OrchestratorValidVedgesTable_Object = MibTable
orchestratorValidVedgesTable = _OrchestratorValidVedgesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 6)
)
if mibBuilder.loadTexts:
    orchestratorValidVedgesTable.setStatus("current")
_OrchestratorValidVedgesEntry_Object = MibTableRow
orchestratorValidVedgesEntry = _OrchestratorValidVedgesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 6, 1)
)
orchestratorValidVedgesEntry.setIndexNames(
    (1, "VIPTELA-SECURITY", "orchestratorValidVedgesChassisNumber"),
)
if mibBuilder.loadTexts:
    orchestratorValidVedgesEntry.setStatus("current")


class _OrchestratorValidVedgesChassisNumber_Type(String):
    """Custom type orchestratorValidVedgesChassisNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_OrchestratorValidVedgesChassisNumber_Type.__name__ = "String"
_OrchestratorValidVedgesChassisNumber_Object = MibTableColumn
orchestratorValidVedgesChassisNumber = _OrchestratorValidVedgesChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 6, 1, 1),
    _OrchestratorValidVedgesChassisNumber_Type()
)
orchestratorValidVedgesChassisNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorValidVedgesChassisNumber.setStatus("current")


class _OrchestratorValidVedgesSerialNumber_Type(String):
    """Custom type orchestratorValidVedgesSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_OrchestratorValidVedgesSerialNumber_Type.__name__ = "String"
_OrchestratorValidVedgesSerialNumber_Object = MibTableColumn
orchestratorValidVedgesSerialNumber = _OrchestratorValidVedgesSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 6, 1, 2),
    _OrchestratorValidVedgesSerialNumber_Type()
)
orchestratorValidVedgesSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorValidVedgesSerialNumber.setStatus("current")


class _OrchestratorValidVedgesValidity_Type(Integer32):
    """Custom type orchestratorValidVedgesValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("staging", 3))
    )


_OrchestratorValidVedgesValidity_Type.__name__ = "Integer32"
_OrchestratorValidVedgesValidity_Object = MibTableColumn
orchestratorValidVedgesValidity = _OrchestratorValidVedgesValidity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 6, 1, 3),
    _OrchestratorValidVedgesValidity_Type()
)
orchestratorValidVedgesValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorValidVedgesValidity.setStatus("current")
_OrchestratorValidVedgesOrg_Type = String
_OrchestratorValidVedgesOrg_Object = MibTableColumn
orchestratorValidVedgesOrg = _OrchestratorValidVedgesOrg_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 6, 1, 4),
    _OrchestratorValidVedgesOrg_Type()
)
orchestratorValidVedgesOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorValidVedgesOrg.setStatus("current")


class _OrchestratorValidVedgesInstalledSerialNumber_Type(String):
    """Custom type orchestratorValidVedgesInstalledSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_OrchestratorValidVedgesInstalledSerialNumber_Type.__name__ = "String"
_OrchestratorValidVedgesInstalledSerialNumber_Object = MibTableColumn
orchestratorValidVedgesInstalledSerialNumber = _OrchestratorValidVedgesInstalledSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 6, 1, 5),
    _OrchestratorValidVedgesInstalledSerialNumber_Type()
)
orchestratorValidVedgesInstalledSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorValidVedgesInstalledSerialNumber.setStatus("current")


class _OrchestratorValidVedgesSubjectSerialNumber_Type(String):
    """Custom type orchestratorValidVedgesSubjectSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_OrchestratorValidVedgesSubjectSerialNumber_Type.__name__ = "String"
_OrchestratorValidVedgesSubjectSerialNumber_Object = MibTableColumn
orchestratorValidVedgesSubjectSerialNumber = _OrchestratorValidVedgesSubjectSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 6, 1, 6),
    _OrchestratorValidVedgesSubjectSerialNumber_Type()
)
orchestratorValidVedgesSubjectSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorValidVedgesSubjectSerialNumber.setStatus("current")
_OrchestratorSummaryTable_Object = MibTable
orchestratorSummaryTable = _OrchestratorSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 7)
)
if mibBuilder.loadTexts:
    orchestratorSummaryTable.setStatus("current")
_OrchestratorSummaryEntry_Object = MibTableRow
orchestratorSummaryEntry = _OrchestratorSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 7, 1)
)
orchestratorSummaryEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "orchestratorSummaryInstance"),
)
if mibBuilder.loadTexts:
    orchestratorSummaryEntry.setStatus("current")
_OrchestratorSummaryInstance_Type = Unsigned32
_OrchestratorSummaryInstance_Object = MibTableColumn
orchestratorSummaryInstance = _OrchestratorSummaryInstance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 7, 1, 1),
    _OrchestratorSummaryInstance_Type()
)
orchestratorSummaryInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorSummaryInstance.setStatus("current")
_OrchestratorSummaryVmanageCounts_Type = UnsignedShort
_OrchestratorSummaryVmanageCounts_Object = MibTableColumn
orchestratorSummaryVmanageCounts = _OrchestratorSummaryVmanageCounts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 7, 1, 2),
    _OrchestratorSummaryVmanageCounts_Type()
)
orchestratorSummaryVmanageCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorSummaryVmanageCounts.setStatus("current")
_OrchestratorSummaryVsmartCounts_Type = UnsignedShort
_OrchestratorSummaryVsmartCounts_Object = MibTableColumn
orchestratorSummaryVsmartCounts = _OrchestratorSummaryVsmartCounts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 7, 1, 3),
    _OrchestratorSummaryVsmartCounts_Type()
)
orchestratorSummaryVsmartCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorSummaryVsmartCounts.setStatus("current")
_OrchestratorSummaryVedgeCounts_Type = UnsignedShort
_OrchestratorSummaryVedgeCounts_Object = MibTableColumn
orchestratorSummaryVedgeCounts = _OrchestratorSummaryVedgeCounts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 7, 1, 4),
    _OrchestratorSummaryVedgeCounts_Type()
)
orchestratorSummaryVedgeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorSummaryVedgeCounts.setStatus("current")


class _OrchestratorSummaryProtocol_Type(Integer32):
    """Custom type orchestratorSummaryProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dtls", 0),
          ("tls", 1))
    )


_OrchestratorSummaryProtocol_Type.__name__ = "Integer32"
_OrchestratorSummaryProtocol_Object = MibTableColumn
orchestratorSummaryProtocol = _OrchestratorSummaryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 7, 1, 5),
    _OrchestratorSummaryProtocol_Type()
)
orchestratorSummaryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorSummaryProtocol.setStatus("current")
_OrchestratorSummaryListeningIp_Type = InetAddressIP
_OrchestratorSummaryListeningIp_Object = MibTableColumn
orchestratorSummaryListeningIp = _OrchestratorSummaryListeningIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 7, 1, 6),
    _OrchestratorSummaryListeningIp_Type()
)
orchestratorSummaryListeningIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorSummaryListeningIp.setStatus("current")
_OrchestratorSummaryListeningPort_Type = Unsigned32
_OrchestratorSummaryListeningPort_Object = MibTableColumn
orchestratorSummaryListeningPort = _OrchestratorSummaryListeningPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 7, 1, 7),
    _OrchestratorSummaryListeningPort_Type()
)
orchestratorSummaryListeningPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorSummaryListeningPort.setStatus("current")
_OrchestratorSummaryListeningIpv6_Type = InetAddressIP
_OrchestratorSummaryListeningIpv6_Object = MibTableColumn
orchestratorSummaryListeningIpv6 = _OrchestratorSummaryListeningIpv6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 7, 1, 8),
    _OrchestratorSummaryListeningIpv6_Type()
)
orchestratorSummaryListeningIpv6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorSummaryListeningIpv6.setStatus("current")
_OrchestratorSummaryValidControllerCounts_Type = UnsignedShort
_OrchestratorSummaryValidControllerCounts_Object = MibTableColumn
orchestratorSummaryValidControllerCounts = _OrchestratorSummaryValidControllerCounts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 7, 1, 9),
    _OrchestratorSummaryValidControllerCounts_Type()
)
orchestratorSummaryValidControllerCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorSummaryValidControllerCounts.setStatus("current")
_OrchestratorValidVmanageIdTable_Object = MibTable
orchestratorValidVmanageIdTable = _OrchestratorValidVmanageIdTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 8)
)
if mibBuilder.loadTexts:
    orchestratorValidVmanageIdTable.setStatus("current")
_OrchestratorValidVmanageIdEntry_Object = MibTableRow
orchestratorValidVmanageIdEntry = _OrchestratorValidVmanageIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 8, 1)
)
orchestratorValidVmanageIdEntry.setIndexNames(
    (1, "VIPTELA-SECURITY", "orchestratorValidVManageIdChassisNumbers"),
)
if mibBuilder.loadTexts:
    orchestratorValidVmanageIdEntry.setStatus("current")


class _OrchestratorValidVManageIdChassisNumbers_Type(String):
    """Custom type orchestratorValidVManageIdChassisNumbers based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_OrchestratorValidVManageIdChassisNumbers_Type.__name__ = "String"
_OrchestratorValidVManageIdChassisNumbers_Object = MibTableColumn
orchestratorValidVManageIdChassisNumbers = _OrchestratorValidVManageIdChassisNumbers_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 8, 1, 1),
    _OrchestratorValidVManageIdChassisNumbers_Type()
)
orchestratorValidVManageIdChassisNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorValidVManageIdChassisNumbers.setStatus("current")
_OrchestratorReverseProxyMappingTable_Object = MibTable
orchestratorReverseProxyMappingTable = _OrchestratorReverseProxyMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 9)
)
if mibBuilder.loadTexts:
    orchestratorReverseProxyMappingTable.setStatus("current")
_OrchestratorReverseProxyMapping_Object = MibTableRow
orchestratorReverseProxyMapping = _OrchestratorReverseProxyMapping_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 9, 1)
)
orchestratorReverseProxyMapping.setIndexNames(
    (0, "VIPTELA-SECURITY", "orchestratorReverseProxyMappingUuid"),
    (0, "VIPTELA-SECURITY", "orchestratorReverseProxyMappingPrivateIp"),
    (0, "VIPTELA-SECURITY", "orchestratorReverseProxyMappingPrivatePort"),
)
if mibBuilder.loadTexts:
    orchestratorReverseProxyMapping.setStatus("current")
_OrchestratorReverseProxyMappingUuid_Type = String
_OrchestratorReverseProxyMappingUuid_Object = MibTableColumn
orchestratorReverseProxyMappingUuid = _OrchestratorReverseProxyMappingUuid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 9, 1, 1),
    _OrchestratorReverseProxyMappingUuid_Type()
)
orchestratorReverseProxyMappingUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorReverseProxyMappingUuid.setStatus("current")
_OrchestratorReverseProxyMappingPrivateIp_Type = InetAddressIP
_OrchestratorReverseProxyMappingPrivateIp_Object = MibTableColumn
orchestratorReverseProxyMappingPrivateIp = _OrchestratorReverseProxyMappingPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 9, 1, 2),
    _OrchestratorReverseProxyMappingPrivateIp_Type()
)
orchestratorReverseProxyMappingPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorReverseProxyMappingPrivateIp.setStatus("current")
_OrchestratorReverseProxyMappingPrivatePort_Type = UnsignedShort
_OrchestratorReverseProxyMappingPrivatePort_Object = MibTableColumn
orchestratorReverseProxyMappingPrivatePort = _OrchestratorReverseProxyMappingPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 9, 1, 3),
    _OrchestratorReverseProxyMappingPrivatePort_Type()
)
orchestratorReverseProxyMappingPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorReverseProxyMappingPrivatePort.setStatus("current")
_OrchestratorReverseProxyMappingProxyIp_Type = InetAddressIP
_OrchestratorReverseProxyMappingProxyIp_Object = MibTableColumn
orchestratorReverseProxyMappingProxyIp = _OrchestratorReverseProxyMappingProxyIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 9, 1, 4),
    _OrchestratorReverseProxyMappingProxyIp_Type()
)
orchestratorReverseProxyMappingProxyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorReverseProxyMappingProxyIp.setStatus("current")
_OrchestratorReverseProxyMappingProxyPort_Type = UnsignedShort
_OrchestratorReverseProxyMappingProxyPort_Object = MibTableColumn
orchestratorReverseProxyMappingProxyPort = _OrchestratorReverseProxyMappingProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 9, 1, 5),
    _OrchestratorReverseProxyMappingProxyPort_Type()
)
orchestratorReverseProxyMappingProxyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorReverseProxyMappingProxyPort.setStatus("current")
_OrchestratorUnclaimedVedgesTable_Object = MibTable
orchestratorUnclaimedVedgesTable = _OrchestratorUnclaimedVedgesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 10)
)
if mibBuilder.loadTexts:
    orchestratorUnclaimedVedgesTable.setStatus("current")
_OrchestratorUnclaimedVedgesEntry_Object = MibTableRow
orchestratorUnclaimedVedgesEntry = _OrchestratorUnclaimedVedgesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 10, 1)
)
orchestratorUnclaimedVedgesEntry.setIndexNames(
    (1, "VIPTELA-SECURITY", "orchestratorUnclaimedVedgesChassisNumber"),
)
if mibBuilder.loadTexts:
    orchestratorUnclaimedVedgesEntry.setStatus("current")


class _OrchestratorUnclaimedVedgesChassisNumber_Type(String):
    """Custom type orchestratorUnclaimedVedgesChassisNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_OrchestratorUnclaimedVedgesChassisNumber_Type.__name__ = "String"
_OrchestratorUnclaimedVedgesChassisNumber_Object = MibTableColumn
orchestratorUnclaimedVedgesChassisNumber = _OrchestratorUnclaimedVedgesChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 10, 1, 1),
    _OrchestratorUnclaimedVedgesChassisNumber_Type()
)
orchestratorUnclaimedVedgesChassisNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    orchestratorUnclaimedVedgesChassisNumber.setStatus("current")


class _OrchestratorUnclaimedVedgesSerialNumber_Type(String):
    """Custom type orchestratorUnclaimedVedgesSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_OrchestratorUnclaimedVedgesSerialNumber_Type.__name__ = "String"
_OrchestratorUnclaimedVedgesSerialNumber_Object = MibTableColumn
orchestratorUnclaimedVedgesSerialNumber = _OrchestratorUnclaimedVedgesSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 10, 1, 2),
    _OrchestratorUnclaimedVedgesSerialNumber_Type()
)
orchestratorUnclaimedVedgesSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorUnclaimedVedgesSerialNumber.setStatus("current")


class _OrchestratorUnclaimedVedgesSubjectSerialNumber_Type(String):
    """Custom type orchestratorUnclaimedVedgesSubjectSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_OrchestratorUnclaimedVedgesSubjectSerialNumber_Type.__name__ = "String"
_OrchestratorUnclaimedVedgesSubjectSerialNumber_Object = MibTableColumn
orchestratorUnclaimedVedgesSubjectSerialNumber = _OrchestratorUnclaimedVedgesSubjectSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 10, 1, 3),
    _OrchestratorUnclaimedVedgesSubjectSerialNumber_Type()
)
orchestratorUnclaimedVedgesSubjectSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorUnclaimedVedgesSubjectSerialNumber.setStatus("current")


class _OrchestratorUnclaimedVedgesOrg_Type(String):
    """Custom type orchestratorUnclaimedVedgesOrg based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OrchestratorUnclaimedVedgesOrg_Type.__name__ = "String"
_OrchestratorUnclaimedVedgesOrg_Object = MibTableColumn
orchestratorUnclaimedVedgesOrg = _OrchestratorUnclaimedVedgesOrg_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 3, 10, 1, 4),
    _OrchestratorUnclaimedVedgesOrg_Type()
)
orchestratorUnclaimedVedgesOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orchestratorUnclaimedVedgesOrg.setStatus("current")
_Ipsec_ObjectIdentity = ObjectIdentity
ipsec = _Ipsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4)
)
_IpsecLocalSaTable_Object = MibTable
ipsecLocalSaTable = _IpsecLocalSaTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 1)
)
if mibBuilder.loadTexts:
    ipsecLocalSaTable.setStatus("current")
_IpsecLocalSaEntry_Object = MibTableRow
ipsecLocalSaEntry = _IpsecLocalSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 1, 1)
)
ipsecLocalSaEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "ipsecLocalSaTlocAddress"),
    (0, "VIPTELA-SECURITY", "ipsecLocalSaTlocColor"),
    (0, "VIPTELA-SECURITY", "ipsecLocalSaSpi"),
    (0, "VIPTELA-SECURITY", "ipsecLocalSaTlocIndex"),
)
if mibBuilder.loadTexts:
    ipsecLocalSaEntry.setStatus("current")
_IpsecLocalSaTlocAddress_Type = InetAddressIP
_IpsecLocalSaTlocAddress_Object = MibTableColumn
ipsecLocalSaTlocAddress = _IpsecLocalSaTlocAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 1, 1, 1),
    _IpsecLocalSaTlocAddress_Type()
)
ipsecLocalSaTlocAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecLocalSaTlocAddress.setStatus("current")


class _IpsecLocalSaTlocColor_Type(Integer32):
    """Custom type ipsecLocalSaTlocColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_IpsecLocalSaTlocColor_Type.__name__ = "Integer32"
_IpsecLocalSaTlocColor_Object = MibTableColumn
ipsecLocalSaTlocColor = _IpsecLocalSaTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 1, 1, 2),
    _IpsecLocalSaTlocColor_Type()
)
ipsecLocalSaTlocColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecLocalSaTlocColor.setStatus("current")
_IpsecLocalSaSpi_Type = Unsigned32
_IpsecLocalSaSpi_Object = MibTableColumn
ipsecLocalSaSpi = _IpsecLocalSaSpi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 1, 1, 3),
    _IpsecLocalSaSpi_Type()
)
ipsecLocalSaSpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecLocalSaSpi.setStatus("current")
_IpsecLocalSaTlocIndex_Type = Unsigned32
_IpsecLocalSaTlocIndex_Object = MibTableColumn
ipsecLocalSaTlocIndex = _IpsecLocalSaTlocIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 1, 1, 4),
    _IpsecLocalSaTlocIndex_Type()
)
ipsecLocalSaTlocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecLocalSaTlocIndex.setStatus("current")
_IpsecLocalSaIp_Type = InetAddressIP
_IpsecLocalSaIp_Object = MibTableColumn
ipsecLocalSaIp = _IpsecLocalSaIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 1, 1, 5),
    _IpsecLocalSaIp_Type()
)
ipsecLocalSaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecLocalSaIp.setStatus("current")
_IpsecLocalSaPort_Type = Unsigned32
_IpsecLocalSaPort_Object = MibTableColumn
ipsecLocalSaPort = _IpsecLocalSaPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 1, 1, 6),
    _IpsecLocalSaPort_Type()
)
ipsecLocalSaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecLocalSaPort.setStatus("current")
_IpsecLocalSaEncryptKeyHash_Type = String
_IpsecLocalSaEncryptKeyHash_Object = MibTableColumn
ipsecLocalSaEncryptKeyHash = _IpsecLocalSaEncryptKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 1, 1, 7),
    _IpsecLocalSaEncryptKeyHash_Type()
)
ipsecLocalSaEncryptKeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecLocalSaEncryptKeyHash.setStatus("current")
_IpsecLocalSaAuthKeyHash_Type = String
_IpsecLocalSaAuthKeyHash_Object = MibTableColumn
ipsecLocalSaAuthKeyHash = _IpsecLocalSaAuthKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 1, 1, 8),
    _IpsecLocalSaAuthKeyHash_Type()
)
ipsecLocalSaAuthKeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecLocalSaAuthKeyHash.setStatus("current")
_IpsecLocalSaIpv6_Type = InetAddressIP
_IpsecLocalSaIpv6_Object = MibTableColumn
ipsecLocalSaIpv6 = _IpsecLocalSaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 1, 1, 9),
    _IpsecLocalSaIpv6_Type()
)
ipsecLocalSaIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecLocalSaIpv6.setStatus("current")
_IpsecInboundConnectionsTable_Object = MibTable
ipsecInboundConnectionsTable = _IpsecInboundConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2)
)
if mibBuilder.loadTexts:
    ipsecInboundConnectionsTable.setStatus("current")
_IpsecInboundConnectionsEntry_Object = MibTableRow
ipsecInboundConnectionsEntry = _IpsecInboundConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1)
)
ipsecInboundConnectionsEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "ipsecInboundConnectionsLocalTlocAddress"),
    (0, "VIPTELA-SECURITY", "ipsecInboundConnectionsLocalTlocColor"),
    (0, "VIPTELA-SECURITY", "ipsecInboundConnectionsRemoteTlocAddress"),
    (0, "VIPTELA-SECURITY", "ipsecInboundConnectionsRemoteTlocColor"),
    (0, "VIPTELA-SECURITY", "ipsecInboundConnectionsLocalTlocIndex"),
    (0, "VIPTELA-SECURITY", "ipsecInboundConnectionsRemoteTlocIndex"),
)
if mibBuilder.loadTexts:
    ipsecInboundConnectionsEntry.setStatus("current")
_IpsecInboundConnectionsLocalTlocAddress_Type = InetAddressIP
_IpsecInboundConnectionsLocalTlocAddress_Object = MibTableColumn
ipsecInboundConnectionsLocalTlocAddress = _IpsecInboundConnectionsLocalTlocAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 1),
    _IpsecInboundConnectionsLocalTlocAddress_Type()
)
ipsecInboundConnectionsLocalTlocAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsLocalTlocAddress.setStatus("current")


class _IpsecInboundConnectionsLocalTlocColor_Type(Integer32):
    """Custom type ipsecInboundConnectionsLocalTlocColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_IpsecInboundConnectionsLocalTlocColor_Type.__name__ = "Integer32"
_IpsecInboundConnectionsLocalTlocColor_Object = MibTableColumn
ipsecInboundConnectionsLocalTlocColor = _IpsecInboundConnectionsLocalTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 2),
    _IpsecInboundConnectionsLocalTlocColor_Type()
)
ipsecInboundConnectionsLocalTlocColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsLocalTlocColor.setStatus("current")
_IpsecInboundConnectionsRemoteTlocAddress_Type = InetAddressIP
_IpsecInboundConnectionsRemoteTlocAddress_Object = MibTableColumn
ipsecInboundConnectionsRemoteTlocAddress = _IpsecInboundConnectionsRemoteTlocAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 3),
    _IpsecInboundConnectionsRemoteTlocAddress_Type()
)
ipsecInboundConnectionsRemoteTlocAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsRemoteTlocAddress.setStatus("current")


class _IpsecInboundConnectionsRemoteTlocColor_Type(Integer32):
    """Custom type ipsecInboundConnectionsRemoteTlocColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_IpsecInboundConnectionsRemoteTlocColor_Type.__name__ = "Integer32"
_IpsecInboundConnectionsRemoteTlocColor_Object = MibTableColumn
ipsecInboundConnectionsRemoteTlocColor = _IpsecInboundConnectionsRemoteTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 4),
    _IpsecInboundConnectionsRemoteTlocColor_Type()
)
ipsecInboundConnectionsRemoteTlocColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsRemoteTlocColor.setStatus("current")
_IpsecInboundConnectionsLocalTlocIndex_Type = Unsigned32
_IpsecInboundConnectionsLocalTlocIndex_Object = MibTableColumn
ipsecInboundConnectionsLocalTlocIndex = _IpsecInboundConnectionsLocalTlocIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 5),
    _IpsecInboundConnectionsLocalTlocIndex_Type()
)
ipsecInboundConnectionsLocalTlocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsLocalTlocIndex.setStatus("current")
_IpsecInboundConnectionsRemoteTlocIndex_Type = Unsigned32
_IpsecInboundConnectionsRemoteTlocIndex_Object = MibTableColumn
ipsecInboundConnectionsRemoteTlocIndex = _IpsecInboundConnectionsRemoteTlocIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 6),
    _IpsecInboundConnectionsRemoteTlocIndex_Type()
)
ipsecInboundConnectionsRemoteTlocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsRemoteTlocIndex.setStatus("current")
_IpsecInboundConnectionsSourceIp_Type = InetAddressIP
_IpsecInboundConnectionsSourceIp_Object = MibTableColumn
ipsecInboundConnectionsSourceIp = _IpsecInboundConnectionsSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 7),
    _IpsecInboundConnectionsSourceIp_Type()
)
ipsecInboundConnectionsSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsSourceIp.setStatus("current")
_IpsecInboundConnectionsSourcePort_Type = Unsigned32
_IpsecInboundConnectionsSourcePort_Object = MibTableColumn
ipsecInboundConnectionsSourcePort = _IpsecInboundConnectionsSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 8),
    _IpsecInboundConnectionsSourcePort_Type()
)
ipsecInboundConnectionsSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsSourcePort.setStatus("current")
_IpsecInboundConnectionsDestIp_Type = InetAddressIP
_IpsecInboundConnectionsDestIp_Object = MibTableColumn
ipsecInboundConnectionsDestIp = _IpsecInboundConnectionsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 9),
    _IpsecInboundConnectionsDestIp_Type()
)
ipsecInboundConnectionsDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsDestIp.setStatus("current")
_IpsecInboundConnectionsDestPort_Type = Unsigned32
_IpsecInboundConnectionsDestPort_Object = MibTableColumn
ipsecInboundConnectionsDestPort = _IpsecInboundConnectionsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 10),
    _IpsecInboundConnectionsDestPort_Type()
)
ipsecInboundConnectionsDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsDestPort.setStatus("current")
_IpsecInboundConnectionsNegotiatedEncryptionAlgo_Type = String
_IpsecInboundConnectionsNegotiatedEncryptionAlgo_Object = MibTableColumn
ipsecInboundConnectionsNegotiatedEncryptionAlgo = _IpsecInboundConnectionsNegotiatedEncryptionAlgo_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 11),
    _IpsecInboundConnectionsNegotiatedEncryptionAlgo_Type()
)
ipsecInboundConnectionsNegotiatedEncryptionAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsNegotiatedEncryptionAlgo.setStatus("current")
_IpsecInboundConnectionsTcSpiPerTun_Type = Unsigned32
_IpsecInboundConnectionsTcSpiPerTun_Object = MibTableColumn
ipsecInboundConnectionsTcSpiPerTun = _IpsecInboundConnectionsTcSpiPerTun_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 12),
    _IpsecInboundConnectionsTcSpiPerTun_Type()
)
ipsecInboundConnectionsTcSpiPerTun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsTcSpiPerTun.setStatus("current")
_IpsecInboundConnectionsPkeyHash_Type = String
_IpsecInboundConnectionsPkeyHash_Object = MibTableColumn
ipsecInboundConnectionsPkeyHash = _IpsecInboundConnectionsPkeyHash_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 13),
    _IpsecInboundConnectionsPkeyHash_Type()
)
ipsecInboundConnectionsPkeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsPkeyHash.setStatus("current")
_IpsecInboundConnectionsPeerSpi_Type = String
_IpsecInboundConnectionsPeerSpi_Object = MibTableColumn
ipsecInboundConnectionsPeerSpi = _IpsecInboundConnectionsPeerSpi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 2, 1, 14),
    _IpsecInboundConnectionsPeerSpi_Type()
)
ipsecInboundConnectionsPeerSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsPeerSpi.setStatus("current")
_IpsecOutboundConnectionsTable_Object = MibTable
ipsecOutboundConnectionsTable = _IpsecOutboundConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3)
)
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsTable.setStatus("current")
_IpsecOutboundConnectionsEntry_Object = MibTableRow
ipsecOutboundConnectionsEntry = _IpsecOutboundConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1)
)
ipsecOutboundConnectionsEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "ipsecOutboundConnectionsSourceIp"),
    (0, "VIPTELA-SECURITY", "ipsecOutboundConnectionsSourcePort"),
    (0, "VIPTELA-SECURITY", "ipsecOutboundConnectionsDestIp"),
    (0, "VIPTELA-SECURITY", "ipsecOutboundConnectionsDestPort"),
    (0, "VIPTELA-SECURITY", "ipsecOutboundConnectionsSpi"),
    (0, "VIPTELA-SECURITY", "ipsecOutboundConnectionsTlocIndex"),
)
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsEntry.setStatus("current")
_IpsecOutboundConnectionsSourceIp_Type = InetAddressIP
_IpsecOutboundConnectionsSourceIp_Object = MibTableColumn
ipsecOutboundConnectionsSourceIp = _IpsecOutboundConnectionsSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 1),
    _IpsecOutboundConnectionsSourceIp_Type()
)
ipsecOutboundConnectionsSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsSourceIp.setStatus("current")
_IpsecOutboundConnectionsSourcePort_Type = Unsigned32
_IpsecOutboundConnectionsSourcePort_Object = MibTableColumn
ipsecOutboundConnectionsSourcePort = _IpsecOutboundConnectionsSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 2),
    _IpsecOutboundConnectionsSourcePort_Type()
)
ipsecOutboundConnectionsSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsSourcePort.setStatus("current")
_IpsecOutboundConnectionsDestIp_Type = InetAddressIP
_IpsecOutboundConnectionsDestIp_Object = MibTableColumn
ipsecOutboundConnectionsDestIp = _IpsecOutboundConnectionsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 3),
    _IpsecOutboundConnectionsDestIp_Type()
)
ipsecOutboundConnectionsDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsDestIp.setStatus("current")
_IpsecOutboundConnectionsDestPort_Type = Unsigned32
_IpsecOutboundConnectionsDestPort_Object = MibTableColumn
ipsecOutboundConnectionsDestPort = _IpsecOutboundConnectionsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 4),
    _IpsecOutboundConnectionsDestPort_Type()
)
ipsecOutboundConnectionsDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsDestPort.setStatus("current")
_IpsecOutboundConnectionsSpi_Type = Unsigned32
_IpsecOutboundConnectionsSpi_Object = MibTableColumn
ipsecOutboundConnectionsSpi = _IpsecOutboundConnectionsSpi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 5),
    _IpsecOutboundConnectionsSpi_Type()
)
ipsecOutboundConnectionsSpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsSpi.setStatus("current")
_IpsecOutboundConnectionsTlocIndex_Type = Unsigned32
_IpsecOutboundConnectionsTlocIndex_Object = MibTableColumn
ipsecOutboundConnectionsTlocIndex = _IpsecOutboundConnectionsTlocIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 6),
    _IpsecOutboundConnectionsTlocIndex_Type()
)
ipsecOutboundConnectionsTlocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsTlocIndex.setStatus("current")
_IpsecOutboundConnectionsTunnelMtu_Type = Unsigned32
_IpsecOutboundConnectionsTunnelMtu_Object = MibTableColumn
ipsecOutboundConnectionsTunnelMtu = _IpsecOutboundConnectionsTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 7),
    _IpsecOutboundConnectionsTunnelMtu_Type()
)
ipsecOutboundConnectionsTunnelMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsTunnelMtu.setStatus("current")
_IpsecOutboundConnectionsRemoteTlocAddress_Type = InetAddressIP
_IpsecOutboundConnectionsRemoteTlocAddress_Object = MibTableColumn
ipsecOutboundConnectionsRemoteTlocAddress = _IpsecOutboundConnectionsRemoteTlocAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 8),
    _IpsecOutboundConnectionsRemoteTlocAddress_Type()
)
ipsecOutboundConnectionsRemoteTlocAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsRemoteTlocAddress.setStatus("current")


class _IpsecOutboundConnectionsRemoteTlocColor_Type(Integer32):
    """Custom type ipsecOutboundConnectionsRemoteTlocColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_IpsecOutboundConnectionsRemoteTlocColor_Type.__name__ = "Integer32"
_IpsecOutboundConnectionsRemoteTlocColor_Object = MibTableColumn
ipsecOutboundConnectionsRemoteTlocColor = _IpsecOutboundConnectionsRemoteTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 9),
    _IpsecOutboundConnectionsRemoteTlocColor_Type()
)
ipsecOutboundConnectionsRemoteTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsRemoteTlocColor.setStatus("current")
_IpsecOutboundConnectionsAuthenticationUsed_Type = String
_IpsecOutboundConnectionsAuthenticationUsed_Object = MibTableColumn
ipsecOutboundConnectionsAuthenticationUsed = _IpsecOutboundConnectionsAuthenticationUsed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 10),
    _IpsecOutboundConnectionsAuthenticationUsed_Type()
)
ipsecOutboundConnectionsAuthenticationUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsAuthenticationUsed.setStatus("current")
_IpsecOutboundConnectionsEncryptKeyHash_Type = String
_IpsecOutboundConnectionsEncryptKeyHash_Object = MibTableColumn
ipsecOutboundConnectionsEncryptKeyHash = _IpsecOutboundConnectionsEncryptKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 11),
    _IpsecOutboundConnectionsEncryptKeyHash_Type()
)
ipsecOutboundConnectionsEncryptKeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsEncryptKeyHash.setStatus("current")
_IpsecOutboundConnectionsAuthKeyHash_Type = String
_IpsecOutboundConnectionsAuthKeyHash_Object = MibTableColumn
ipsecOutboundConnectionsAuthKeyHash = _IpsecOutboundConnectionsAuthKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 12),
    _IpsecOutboundConnectionsAuthKeyHash_Type()
)
ipsecOutboundConnectionsAuthKeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsAuthKeyHash.setStatus("current")
_IpsecOutboundConnectionsNegotiatedAlgo_Type = String
_IpsecOutboundConnectionsNegotiatedAlgo_Object = MibTableColumn
ipsecOutboundConnectionsNegotiatedAlgo = _IpsecOutboundConnectionsNegotiatedAlgo_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 13),
    _IpsecOutboundConnectionsNegotiatedAlgo_Type()
)
ipsecOutboundConnectionsNegotiatedAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsNegotiatedAlgo.setStatus("current")
_IpsecOutboundConnectionsTcSpiPerTun_Type = Unsigned32
_IpsecOutboundConnectionsTcSpiPerTun_Object = MibTableColumn
ipsecOutboundConnectionsTcSpiPerTun = _IpsecOutboundConnectionsTcSpiPerTun_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 14),
    _IpsecOutboundConnectionsTcSpiPerTun_Type()
)
ipsecOutboundConnectionsTcSpiPerTun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsTcSpiPerTun.setStatus("current")
_IpsecOutboundConnectionsPkeyHash_Type = String
_IpsecOutboundConnectionsPkeyHash_Object = MibTableColumn
ipsecOutboundConnectionsPkeyHash = _IpsecOutboundConnectionsPkeyHash_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 15),
    _IpsecOutboundConnectionsPkeyHash_Type()
)
ipsecOutboundConnectionsPkeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsPkeyHash.setStatus("current")
_IpsecOutboundConnectionsPeerSpi_Type = String
_IpsecOutboundConnectionsPeerSpi_Object = MibTableColumn
ipsecOutboundConnectionsPeerSpi = _IpsecOutboundConnectionsPeerSpi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 16),
    _IpsecOutboundConnectionsPeerSpi_Type()
)
ipsecOutboundConnectionsPeerSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsPeerSpi.setStatus("current")
_IpsecOutboundConnectionsLocalTlocAddress_Type = InetAddressIP
_IpsecOutboundConnectionsLocalTlocAddress_Object = MibTableColumn
ipsecOutboundConnectionsLocalTlocAddress = _IpsecOutboundConnectionsLocalTlocAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 17),
    _IpsecOutboundConnectionsLocalTlocAddress_Type()
)
ipsecOutboundConnectionsLocalTlocAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsLocalTlocAddress.setStatus("current")


class _IpsecOutboundConnectionsLocalTlocColor_Type(Integer32):
    """Custom type ipsecOutboundConnectionsLocalTlocColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_IpsecOutboundConnectionsLocalTlocColor_Type.__name__ = "Integer32"
_IpsecOutboundConnectionsLocalTlocColor_Object = MibTableColumn
ipsecOutboundConnectionsLocalTlocColor = _IpsecOutboundConnectionsLocalTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 3, 1, 18),
    _IpsecOutboundConnectionsLocalTlocColor_Type()
)
ipsecOutboundConnectionsLocalTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsLocalTlocColor.setStatus("current")
_IpsecIke_ObjectIdentity = ObjectIdentity
ipsecIke = _IpsecIke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4)
)
_IpsecIkeInboundConnectionsTable_Object = MibTable
ipsecIkeInboundConnectionsTable = _IpsecIkeInboundConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 1)
)
if mibBuilder.loadTexts:
    ipsecIkeInboundConnectionsTable.setStatus("current")
_IpsecIkeInboundConnectionsEntry_Object = MibTableRow
ipsecIkeInboundConnectionsEntry = _IpsecIkeInboundConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 1, 1)
)
ipsecIkeInboundConnectionsEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "ipsecIkeInboundConnectionsSourceIp"),
    (0, "VIPTELA-SECURITY", "ipsecIkeInboundConnectionsSourcePort"),
    (0, "VIPTELA-SECURITY", "ipsecIkeInboundConnectionsDestIp"),
    (0, "VIPTELA-SECURITY", "ipsecIkeInboundConnectionsDestPort"),
)
if mibBuilder.loadTexts:
    ipsecIkeInboundConnectionsEntry.setStatus("current")
_IpsecIkeInboundConnectionsSourceIp_Type = InetAddressIP
_IpsecIkeInboundConnectionsSourceIp_Object = MibTableColumn
ipsecIkeInboundConnectionsSourceIp = _IpsecIkeInboundConnectionsSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 1, 1, 1),
    _IpsecIkeInboundConnectionsSourceIp_Type()
)
ipsecIkeInboundConnectionsSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecIkeInboundConnectionsSourceIp.setStatus("current")
_IpsecIkeInboundConnectionsSourcePort_Type = Unsigned32
_IpsecIkeInboundConnectionsSourcePort_Object = MibTableColumn
ipsecIkeInboundConnectionsSourcePort = _IpsecIkeInboundConnectionsSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 1, 1, 2),
    _IpsecIkeInboundConnectionsSourcePort_Type()
)
ipsecIkeInboundConnectionsSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecIkeInboundConnectionsSourcePort.setStatus("current")
_IpsecIkeInboundConnectionsDestIp_Type = InetAddressIP
_IpsecIkeInboundConnectionsDestIp_Object = MibTableColumn
ipsecIkeInboundConnectionsDestIp = _IpsecIkeInboundConnectionsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 1, 1, 3),
    _IpsecIkeInboundConnectionsDestIp_Type()
)
ipsecIkeInboundConnectionsDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecIkeInboundConnectionsDestIp.setStatus("current")
_IpsecIkeInboundConnectionsDestPort_Type = Unsigned32
_IpsecIkeInboundConnectionsDestPort_Object = MibTableColumn
ipsecIkeInboundConnectionsDestPort = _IpsecIkeInboundConnectionsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 1, 1, 4),
    _IpsecIkeInboundConnectionsDestPort_Type()
)
ipsecIkeInboundConnectionsDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecIkeInboundConnectionsDestPort.setStatus("current")
_IpsecIkeInboundConnectionsNewSpi_Type = Unsigned32
_IpsecIkeInboundConnectionsNewSpi_Object = MibTableColumn
ipsecIkeInboundConnectionsNewSpi = _IpsecIkeInboundConnectionsNewSpi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 1, 1, 5),
    _IpsecIkeInboundConnectionsNewSpi_Type()
)
ipsecIkeInboundConnectionsNewSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeInboundConnectionsNewSpi.setStatus("current")
_IpsecIkeInboundConnectionsOldSpi_Type = Unsigned32
_IpsecIkeInboundConnectionsOldSpi_Object = MibTableColumn
ipsecIkeInboundConnectionsOldSpi = _IpsecIkeInboundConnectionsOldSpi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 1, 1, 6),
    _IpsecIkeInboundConnectionsOldSpi_Type()
)
ipsecIkeInboundConnectionsOldSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeInboundConnectionsOldSpi.setStatus("current")
_IpsecIkeInboundConnectionsCipherSuite_Type = String
_IpsecIkeInboundConnectionsCipherSuite_Object = MibTableColumn
ipsecIkeInboundConnectionsCipherSuite = _IpsecIkeInboundConnectionsCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 1, 1, 7),
    _IpsecIkeInboundConnectionsCipherSuite_Type()
)
ipsecIkeInboundConnectionsCipherSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeInboundConnectionsCipherSuite.setStatus("current")
_IpsecIkeInboundConnectionsNewKeyHash_Type = String
_IpsecIkeInboundConnectionsNewKeyHash_Object = MibTableColumn
ipsecIkeInboundConnectionsNewKeyHash = _IpsecIkeInboundConnectionsNewKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 1, 1, 8),
    _IpsecIkeInboundConnectionsNewKeyHash_Type()
)
ipsecIkeInboundConnectionsNewKeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeInboundConnectionsNewKeyHash.setStatus("current")
_IpsecIkeInboundConnectionsOldKeyHash_Type = String
_IpsecIkeInboundConnectionsOldKeyHash_Object = MibTableColumn
ipsecIkeInboundConnectionsOldKeyHash = _IpsecIkeInboundConnectionsOldKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 1, 1, 9),
    _IpsecIkeInboundConnectionsOldKeyHash_Type()
)
ipsecIkeInboundConnectionsOldKeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeInboundConnectionsOldKeyHash.setStatus("current")
_IpsecIkeInboundConnectionsExtSeq_Type = String
_IpsecIkeInboundConnectionsExtSeq_Object = MibTableColumn
ipsecIkeInboundConnectionsExtSeq = _IpsecIkeInboundConnectionsExtSeq_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 1, 1, 10),
    _IpsecIkeInboundConnectionsExtSeq_Type()
)
ipsecIkeInboundConnectionsExtSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeInboundConnectionsExtSeq.setStatus("current")
_IpsecIkeOutboundConnectionsTable_Object = MibTable
ipsecIkeOutboundConnectionsTable = _IpsecIkeOutboundConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 2)
)
if mibBuilder.loadTexts:
    ipsecIkeOutboundConnectionsTable.setStatus("current")
_IpsecIkeOutboundConnectionsEntry_Object = MibTableRow
ipsecIkeOutboundConnectionsEntry = _IpsecIkeOutboundConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 2, 1)
)
ipsecIkeOutboundConnectionsEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "ipsecIkeOutboundConnectionsSourceIp"),
    (0, "VIPTELA-SECURITY", "ipsecIkeOutboundConnectionsSourcePort"),
    (0, "VIPTELA-SECURITY", "ipsecIkeOutboundConnectionsDestIp"),
    (0, "VIPTELA-SECURITY", "ipsecIkeOutboundConnectionsDestPort"),
    (0, "VIPTELA-SECURITY", "ipsecIkeOutboundConnectionsSpi"),
)
if mibBuilder.loadTexts:
    ipsecIkeOutboundConnectionsEntry.setStatus("current")
_IpsecIkeOutboundConnectionsSourceIp_Type = InetAddressIP
_IpsecIkeOutboundConnectionsSourceIp_Object = MibTableColumn
ipsecIkeOutboundConnectionsSourceIp = _IpsecIkeOutboundConnectionsSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 2, 1, 1),
    _IpsecIkeOutboundConnectionsSourceIp_Type()
)
ipsecIkeOutboundConnectionsSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecIkeOutboundConnectionsSourceIp.setStatus("current")
_IpsecIkeOutboundConnectionsSourcePort_Type = Unsigned32
_IpsecIkeOutboundConnectionsSourcePort_Object = MibTableColumn
ipsecIkeOutboundConnectionsSourcePort = _IpsecIkeOutboundConnectionsSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 2, 1, 2),
    _IpsecIkeOutboundConnectionsSourcePort_Type()
)
ipsecIkeOutboundConnectionsSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecIkeOutboundConnectionsSourcePort.setStatus("current")
_IpsecIkeOutboundConnectionsDestIp_Type = InetAddressIP
_IpsecIkeOutboundConnectionsDestIp_Object = MibTableColumn
ipsecIkeOutboundConnectionsDestIp = _IpsecIkeOutboundConnectionsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 2, 1, 3),
    _IpsecIkeOutboundConnectionsDestIp_Type()
)
ipsecIkeOutboundConnectionsDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecIkeOutboundConnectionsDestIp.setStatus("current")
_IpsecIkeOutboundConnectionsDestPort_Type = Unsigned32
_IpsecIkeOutboundConnectionsDestPort_Object = MibTableColumn
ipsecIkeOutboundConnectionsDestPort = _IpsecIkeOutboundConnectionsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 2, 1, 4),
    _IpsecIkeOutboundConnectionsDestPort_Type()
)
ipsecIkeOutboundConnectionsDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecIkeOutboundConnectionsDestPort.setStatus("current")
_IpsecIkeOutboundConnectionsSpi_Type = Unsigned32
_IpsecIkeOutboundConnectionsSpi_Object = MibTableColumn
ipsecIkeOutboundConnectionsSpi = _IpsecIkeOutboundConnectionsSpi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 2, 1, 5),
    _IpsecIkeOutboundConnectionsSpi_Type()
)
ipsecIkeOutboundConnectionsSpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecIkeOutboundConnectionsSpi.setStatus("current")
_IpsecIkeOutboundConnectionsCipherSuite_Type = String
_IpsecIkeOutboundConnectionsCipherSuite_Object = MibTableColumn
ipsecIkeOutboundConnectionsCipherSuite = _IpsecIkeOutboundConnectionsCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 2, 1, 6),
    _IpsecIkeOutboundConnectionsCipherSuite_Type()
)
ipsecIkeOutboundConnectionsCipherSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeOutboundConnectionsCipherSuite.setStatus("current")
_IpsecIkeOutboundConnectionsKeyHash_Type = String
_IpsecIkeOutboundConnectionsKeyHash_Object = MibTableColumn
ipsecIkeOutboundConnectionsKeyHash = _IpsecIkeOutboundConnectionsKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 2, 1, 7),
    _IpsecIkeOutboundConnectionsKeyHash_Type()
)
ipsecIkeOutboundConnectionsKeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeOutboundConnectionsKeyHash.setStatus("current")
_IpsecIkeOutboundConnectionsTunnelMtu_Type = Unsigned32
_IpsecIkeOutboundConnectionsTunnelMtu_Object = MibTableColumn
ipsecIkeOutboundConnectionsTunnelMtu = _IpsecIkeOutboundConnectionsTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 2, 1, 8),
    _IpsecIkeOutboundConnectionsTunnelMtu_Type()
)
ipsecIkeOutboundConnectionsTunnelMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeOutboundConnectionsTunnelMtu.setStatus("current")
_IpsecIkeOutboundConnectionsExtSeq_Type = String
_IpsecIkeOutboundConnectionsExtSeq_Object = MibTableColumn
ipsecIkeOutboundConnectionsExtSeq = _IpsecIkeOutboundConnectionsExtSeq_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 2, 1, 9),
    _IpsecIkeOutboundConnectionsExtSeq_Type()
)
ipsecIkeOutboundConnectionsExtSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeOutboundConnectionsExtSeq.setStatus("current")
_IpsecIkeSessionsTable_Object = MibTable
ipsecIkeSessionsTable = _IpsecIkeSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3)
)
if mibBuilder.loadTexts:
    ipsecIkeSessionsTable.setStatus("current")
_IpsecIkeSessionsEntry_Object = MibTableRow
ipsecIkeSessionsEntry = _IpsecIkeSessionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1)
)
ipsecIkeSessionsEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "ipsecIkeSessionsVpnId"),
    (1, "VIPTELA-SECURITY", "ipsecIkeSessionsIfName"),
)
if mibBuilder.loadTexts:
    ipsecIkeSessionsEntry.setStatus("current")


class _IpsecIkeSessionsVpnId_Type(Unsigned32):
    """Custom type ipsecIkeSessionsVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpsecIkeSessionsVpnId_Type.__name__ = "Unsigned32"
_IpsecIkeSessionsVpnId_Object = MibTableColumn
ipsecIkeSessionsVpnId = _IpsecIkeSessionsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 1),
    _IpsecIkeSessionsVpnId_Type()
)
ipsecIkeSessionsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecIkeSessionsVpnId.setStatus("current")
_IpsecIkeSessionsIfName_Type = String
_IpsecIkeSessionsIfName_Object = MibTableColumn
ipsecIkeSessionsIfName = _IpsecIkeSessionsIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 2),
    _IpsecIkeSessionsIfName_Type()
)
ipsecIkeSessionsIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecIkeSessionsIfName.setStatus("current")
_IpsecIkeSessionsVersion_Type = UnsignedByte
_IpsecIkeSessionsVersion_Object = MibTableColumn
ipsecIkeSessionsVersion = _IpsecIkeSessionsVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 3),
    _IpsecIkeSessionsVersion_Type()
)
ipsecIkeSessionsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSessionsVersion.setStatus("current")
_IpsecIkeSessionsSourceIp_Type = InetAddressIP
_IpsecIkeSessionsSourceIp_Object = MibTableColumn
ipsecIkeSessionsSourceIp = _IpsecIkeSessionsSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 4),
    _IpsecIkeSessionsSourceIp_Type()
)
ipsecIkeSessionsSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSessionsSourceIp.setStatus("current")
_IpsecIkeSessionsSourcePort_Type = Unsigned32
_IpsecIkeSessionsSourcePort_Object = MibTableColumn
ipsecIkeSessionsSourcePort = _IpsecIkeSessionsSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 5),
    _IpsecIkeSessionsSourcePort_Type()
)
ipsecIkeSessionsSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSessionsSourcePort.setStatus("current")
_IpsecIkeSessionsDestIp_Type = InetAddressIP
_IpsecIkeSessionsDestIp_Object = MibTableColumn
ipsecIkeSessionsDestIp = _IpsecIkeSessionsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 6),
    _IpsecIkeSessionsDestIp_Type()
)
ipsecIkeSessionsDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSessionsDestIp.setStatus("current")
_IpsecIkeSessionsDestPort_Type = Unsigned32
_IpsecIkeSessionsDestPort_Object = MibTableColumn
ipsecIkeSessionsDestPort = _IpsecIkeSessionsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 7),
    _IpsecIkeSessionsDestPort_Type()
)
ipsecIkeSessionsDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSessionsDestPort.setStatus("current")
_IpsecIkeSessionsInitiatorSpi_Type = String
_IpsecIkeSessionsInitiatorSpi_Object = MibTableColumn
ipsecIkeSessionsInitiatorSpi = _IpsecIkeSessionsInitiatorSpi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 8),
    _IpsecIkeSessionsInitiatorSpi_Type()
)
ipsecIkeSessionsInitiatorSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSessionsInitiatorSpi.setStatus("current")
_IpsecIkeSessionsResponderSpi_Type = String
_IpsecIkeSessionsResponderSpi_Object = MibTableColumn
ipsecIkeSessionsResponderSpi = _IpsecIkeSessionsResponderSpi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 9),
    _IpsecIkeSessionsResponderSpi_Type()
)
ipsecIkeSessionsResponderSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSessionsResponderSpi.setStatus("current")
_IpsecIkeSessionsCipherSuite_Type = String
_IpsecIkeSessionsCipherSuite_Object = MibTableColumn
ipsecIkeSessionsCipherSuite = _IpsecIkeSessionsCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 10),
    _IpsecIkeSessionsCipherSuite_Type()
)
ipsecIkeSessionsCipherSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSessionsCipherSuite.setStatus("current")
_IpsecIkeSessionsDhGroup_Type = String
_IpsecIkeSessionsDhGroup_Object = MibTableColumn
ipsecIkeSessionsDhGroup = _IpsecIkeSessionsDhGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 11),
    _IpsecIkeSessionsDhGroup_Type()
)
ipsecIkeSessionsDhGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSessionsDhGroup.setStatus("current")
_IpsecIkeSessionsState_Type = String
_IpsecIkeSessionsState_Object = MibTableColumn
ipsecIkeSessionsState = _IpsecIkeSessionsState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 12),
    _IpsecIkeSessionsState_Type()
)
ipsecIkeSessionsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSessionsState.setStatus("current")
_IpsecIkeSessionsUptime_Type = String
_IpsecIkeSessionsUptime_Object = MibTableColumn
ipsecIkeSessionsUptime = _IpsecIkeSessionsUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 13),
    _IpsecIkeSessionsUptime_Type()
)
ipsecIkeSessionsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSessionsUptime.setStatus("current")
_IpsecIkeSessionsTunnelUptime_Type = String
_IpsecIkeSessionsTunnelUptime_Object = MibTableColumn
ipsecIkeSessionsTunnelUptime = _IpsecIkeSessionsTunnelUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 4, 4, 3, 1, 14),
    _IpsecIkeSessionsTunnelUptime_Type()
)
ipsecIkeSessionsTunnelUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSessionsTunnelUptime.setStatus("current")
_Tunnel_ObjectIdentity = ObjectIdentity
tunnel = _Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5)
)
_TunnelStatisticsTable_Object = MibTable
tunnelStatisticsTable = _TunnelStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1)
)
if mibBuilder.loadTexts:
    tunnelStatisticsTable.setStatus("current")
_TunnelStatisticsEntry_Object = MibTableRow
tunnelStatisticsEntry = _TunnelStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1)
)
tunnelStatisticsEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "tunnelStatisticsTunnelProtocol"),
    (0, "VIPTELA-SECURITY", "tunnelStatisticsSourceIp"),
    (0, "VIPTELA-SECURITY", "tunnelStatisticsDestIp"),
    (0, "VIPTELA-SECURITY", "tunnelStatisticsSourcePort"),
    (0, "VIPTELA-SECURITY", "tunnelStatisticsDestPort"),
)
if mibBuilder.loadTexts:
    tunnelStatisticsEntry.setStatus("current")


class _TunnelStatisticsTunnelProtocol_Type(Integer32):
    """Custom type tunnelStatisticsTunnelProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_TunnelStatisticsTunnelProtocol_Type.__name__ = "Integer32"
_TunnelStatisticsTunnelProtocol_Object = MibTableColumn
tunnelStatisticsTunnelProtocol = _TunnelStatisticsTunnelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 1),
    _TunnelStatisticsTunnelProtocol_Type()
)
tunnelStatisticsTunnelProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsTunnelProtocol.setStatus("current")
_TunnelStatisticsSourceIp_Type = InetAddressIP
_TunnelStatisticsSourceIp_Object = MibTableColumn
tunnelStatisticsSourceIp = _TunnelStatisticsSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 2),
    _TunnelStatisticsSourceIp_Type()
)
tunnelStatisticsSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelStatisticsSourceIp.setStatus("current")
_TunnelStatisticsDestIp_Type = InetAddressIP
_TunnelStatisticsDestIp_Object = MibTableColumn
tunnelStatisticsDestIp = _TunnelStatisticsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 3),
    _TunnelStatisticsDestIp_Type()
)
tunnelStatisticsDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelStatisticsDestIp.setStatus("current")
_TunnelStatisticsSourcePort_Type = Unsigned32
_TunnelStatisticsSourcePort_Object = MibTableColumn
tunnelStatisticsSourcePort = _TunnelStatisticsSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 4),
    _TunnelStatisticsSourcePort_Type()
)
tunnelStatisticsSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelStatisticsSourcePort.setStatus("current")
_TunnelStatisticsDestPort_Type = Unsigned32
_TunnelStatisticsDestPort_Object = MibTableColumn
tunnelStatisticsDestPort = _TunnelStatisticsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 5),
    _TunnelStatisticsDestPort_Type()
)
tunnelStatisticsDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelStatisticsDestPort.setStatus("current")
_TunnelStatisticsSystemIp_Type = InetAddressIP
_TunnelStatisticsSystemIp_Object = MibTableColumn
tunnelStatisticsSystemIp = _TunnelStatisticsSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 6),
    _TunnelStatisticsSystemIp_Type()
)
tunnelStatisticsSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsSystemIp.setStatus("current")


class _TunnelStatisticsLocalColor_Type(Integer32):
    """Custom type tunnelStatisticsLocalColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_TunnelStatisticsLocalColor_Type.__name__ = "Integer32"
_TunnelStatisticsLocalColor_Object = MibTableColumn
tunnelStatisticsLocalColor = _TunnelStatisticsLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 7),
    _TunnelStatisticsLocalColor_Type()
)
tunnelStatisticsLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsLocalColor.setStatus("current")


class _TunnelStatisticsRemoteColor_Type(Integer32):
    """Custom type tunnelStatisticsRemoteColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_TunnelStatisticsRemoteColor_Type.__name__ = "Integer32"
_TunnelStatisticsRemoteColor_Object = MibTableColumn
tunnelStatisticsRemoteColor = _TunnelStatisticsRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 8),
    _TunnelStatisticsRemoteColor_Type()
)
tunnelStatisticsRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsRemoteColor.setStatus("current")
_TunnelStatisticsTunnelMtu_Type = Unsigned32
_TunnelStatisticsTunnelMtu_Object = MibTableColumn
tunnelStatisticsTunnelMtu = _TunnelStatisticsTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 9),
    _TunnelStatisticsTunnelMtu_Type()
)
tunnelStatisticsTunnelMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsTunnelMtu.setStatus("current")
_TunnelStatisticsTxPkts_Type = Counter64
_TunnelStatisticsTxPkts_Object = MibTableColumn
tunnelStatisticsTxPkts = _TunnelStatisticsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 10),
    _TunnelStatisticsTxPkts_Type()
)
tunnelStatisticsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsTxPkts.setStatus("current")
_TunnelStatisticsTxOctets_Type = Counter64
_TunnelStatisticsTxOctets_Object = MibTableColumn
tunnelStatisticsTxOctets = _TunnelStatisticsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 11),
    _TunnelStatisticsTxOctets_Type()
)
tunnelStatisticsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsTxOctets.setStatus("current")
_TunnelStatisticsRxPkts_Type = Counter64
_TunnelStatisticsRxPkts_Object = MibTableColumn
tunnelStatisticsRxPkts = _TunnelStatisticsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 12),
    _TunnelStatisticsRxPkts_Type()
)
tunnelStatisticsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsRxPkts.setStatus("current")
_TunnelStatisticsRxOctets_Type = Counter64
_TunnelStatisticsRxOctets_Object = MibTableColumn
tunnelStatisticsRxOctets = _TunnelStatisticsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 13),
    _TunnelStatisticsRxOctets_Type()
)
tunnelStatisticsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsRxOctets.setStatus("current")
_TunnelStatisticsIpsecDecryptInbound_Type = Counter64
_TunnelStatisticsIpsecDecryptInbound_Object = MibTableColumn
tunnelStatisticsIpsecDecryptInbound = _TunnelStatisticsIpsecDecryptInbound_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 14),
    _TunnelStatisticsIpsecDecryptInbound_Type()
)
tunnelStatisticsIpsecDecryptInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIpsecDecryptInbound.setStatus("current")
_TunnelStatisticsIpsecRxAuthFailures_Type = Counter64
_TunnelStatisticsIpsecRxAuthFailures_Object = MibTableColumn
tunnelStatisticsIpsecRxAuthFailures = _TunnelStatisticsIpsecRxAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 15),
    _TunnelStatisticsIpsecRxAuthFailures_Type()
)
tunnelStatisticsIpsecRxAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIpsecRxAuthFailures.setStatus("current")
_TunnelStatisticsIpsecRxFailures_Type = Counter64
_TunnelStatisticsIpsecRxFailures_Object = MibTableColumn
tunnelStatisticsIpsecRxFailures = _TunnelStatisticsIpsecRxFailures_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 16),
    _TunnelStatisticsIpsecRxFailures_Type()
)
tunnelStatisticsIpsecRxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIpsecRxFailures.setStatus("current")
_TunnelStatisticsIpsecEncryptOutbound_Type = Counter64
_TunnelStatisticsIpsecEncryptOutbound_Object = MibTableColumn
tunnelStatisticsIpsecEncryptOutbound = _TunnelStatisticsIpsecEncryptOutbound_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 17),
    _TunnelStatisticsIpsecEncryptOutbound_Type()
)
tunnelStatisticsIpsecEncryptOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIpsecEncryptOutbound.setStatus("current")
_TunnelStatisticsIpsecTxAuthFailures_Type = Counter64
_TunnelStatisticsIpsecTxAuthFailures_Object = MibTableColumn
tunnelStatisticsIpsecTxAuthFailures = _TunnelStatisticsIpsecTxAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 18),
    _TunnelStatisticsIpsecTxAuthFailures_Type()
)
tunnelStatisticsIpsecTxAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIpsecTxAuthFailures.setStatus("current")
_TunnelStatisticsIpsecTxFailures_Type = Counter64
_TunnelStatisticsIpsecTxFailures_Object = MibTableColumn
tunnelStatisticsIpsecTxFailures = _TunnelStatisticsIpsecTxFailures_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 19),
    _TunnelStatisticsIpsecTxFailures_Type()
)
tunnelStatisticsIpsecTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIpsecTxFailures.setStatus("current")
_TunnelStatisticsTcpMssAdjust_Type = Unsigned32
_TunnelStatisticsTcpMssAdjust_Object = MibTableColumn
tunnelStatisticsTcpMssAdjust = _TunnelStatisticsTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 20),
    _TunnelStatisticsTcpMssAdjust_Type()
)
tunnelStatisticsTcpMssAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsTcpMssAdjust.setStatus("current")
_TunnelStatisticsBfdTxPkts_Type = Counter64
_TunnelStatisticsBfdTxPkts_Object = MibTableColumn
tunnelStatisticsBfdTxPkts = _TunnelStatisticsBfdTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 21),
    _TunnelStatisticsBfdTxPkts_Type()
)
tunnelStatisticsBfdTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBfdTxPkts.setStatus("current")
_TunnelStatisticsBfdRxPkts_Type = Counter64
_TunnelStatisticsBfdRxPkts_Object = MibTableColumn
tunnelStatisticsBfdRxPkts = _TunnelStatisticsBfdRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 22),
    _TunnelStatisticsBfdRxPkts_Type()
)
tunnelStatisticsBfdRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBfdRxPkts.setStatus("current")
_TunnelStatisticsBfdTxOctets_Type = Counter64
_TunnelStatisticsBfdTxOctets_Object = MibTableColumn
tunnelStatisticsBfdTxOctets = _TunnelStatisticsBfdTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 23),
    _TunnelStatisticsBfdTxOctets_Type()
)
tunnelStatisticsBfdTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBfdTxOctets.setStatus("current")
_TunnelStatisticsBfdRxOctets_Type = Counter64
_TunnelStatisticsBfdRxOctets_Object = MibTableColumn
tunnelStatisticsBfdRxOctets = _TunnelStatisticsBfdRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 24),
    _TunnelStatisticsBfdRxOctets_Type()
)
tunnelStatisticsBfdRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBfdRxOctets.setStatus("current")
_TunnelStatisticsPmtuTxPkts_Type = Counter64
_TunnelStatisticsPmtuTxPkts_Object = MibTableColumn
tunnelStatisticsPmtuTxPkts = _TunnelStatisticsPmtuTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 25),
    _TunnelStatisticsPmtuTxPkts_Type()
)
tunnelStatisticsPmtuTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPmtuTxPkts.setStatus("current")
_TunnelStatisticsPmtuRxPkts_Type = Counter64
_TunnelStatisticsPmtuRxPkts_Object = MibTableColumn
tunnelStatisticsPmtuRxPkts = _TunnelStatisticsPmtuRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 26),
    _TunnelStatisticsPmtuRxPkts_Type()
)
tunnelStatisticsPmtuRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPmtuRxPkts.setStatus("current")
_TunnelStatisticsPmtuTxOctets_Type = Counter64
_TunnelStatisticsPmtuTxOctets_Object = MibTableColumn
tunnelStatisticsPmtuTxOctets = _TunnelStatisticsPmtuTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 27),
    _TunnelStatisticsPmtuTxOctets_Type()
)
tunnelStatisticsPmtuTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPmtuTxOctets.setStatus("current")
_TunnelStatisticsPmtuRxOctets_Type = Counter64
_TunnelStatisticsPmtuRxOctets_Object = MibTableColumn
tunnelStatisticsPmtuRxOctets = _TunnelStatisticsPmtuRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 28),
    _TunnelStatisticsPmtuRxOctets_Type()
)
tunnelStatisticsPmtuRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPmtuRxOctets.setStatus("current")
_TunnelStatisticsFecRxDataPkts_Type = Unsigned32
_TunnelStatisticsFecRxDataPkts_Object = MibTableColumn
tunnelStatisticsFecRxDataPkts = _TunnelStatisticsFecRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 29),
    _TunnelStatisticsFecRxDataPkts_Type()
)
tunnelStatisticsFecRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecRxDataPkts.setStatus("current")
_TunnelStatisticsFecRxParityPkts_Type = Unsigned32
_TunnelStatisticsFecRxParityPkts_Object = MibTableColumn
tunnelStatisticsFecRxParityPkts = _TunnelStatisticsFecRxParityPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 30),
    _TunnelStatisticsFecRxParityPkts_Type()
)
tunnelStatisticsFecRxParityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecRxParityPkts.setStatus("current")
_TunnelStatisticsFecTxDataPkts_Type = Unsigned32
_TunnelStatisticsFecTxDataPkts_Object = MibTableColumn
tunnelStatisticsFecTxDataPkts = _TunnelStatisticsFecTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 31),
    _TunnelStatisticsFecTxDataPkts_Type()
)
tunnelStatisticsFecTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecTxDataPkts.setStatus("current")
_TunnelStatisticsFecTxParityPkts_Type = Unsigned32
_TunnelStatisticsFecTxParityPkts_Object = MibTableColumn
tunnelStatisticsFecTxParityPkts = _TunnelStatisticsFecTxParityPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 32),
    _TunnelStatisticsFecTxParityPkts_Type()
)
tunnelStatisticsFecTxParityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecTxParityPkts.setStatus("current")
_TunnelStatisticsFecReconstructPkts_Type = Unsigned32
_TunnelStatisticsFecReconstructPkts_Object = MibTableColumn
tunnelStatisticsFecReconstructPkts = _TunnelStatisticsFecReconstructPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 33),
    _TunnelStatisticsFecReconstructPkts_Type()
)
tunnelStatisticsFecReconstructPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecReconstructPkts.setStatus("current")
_TunnelStatisticsFecCapable_Type = TruthValue
_TunnelStatisticsFecCapable_Object = MibTableColumn
tunnelStatisticsFecCapable = _TunnelStatisticsFecCapable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 34),
    _TunnelStatisticsFecCapable_Type()
)
tunnelStatisticsFecCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecCapable.setStatus("current")
_TunnelStatisticsFecDynamic_Type = TruthValue
_TunnelStatisticsFecDynamic_Object = MibTableColumn
tunnelStatisticsFecDynamic = _TunnelStatisticsFecDynamic_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 35),
    _TunnelStatisticsFecDynamic_Type()
)
tunnelStatisticsFecDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecDynamic.setStatus("current")
_TunnelStatisticsPktDupRxPkts_Type = Unsigned32
_TunnelStatisticsPktDupRxPkts_Object = MibTableColumn
tunnelStatisticsPktDupRxPkts = _TunnelStatisticsPktDupRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 36),
    _TunnelStatisticsPktDupRxPkts_Type()
)
tunnelStatisticsPktDupRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPktDupRxPkts.setStatus("current")
_TunnelStatisticsPktDupRxOtherPkts_Type = Unsigned32
_TunnelStatisticsPktDupRxOtherPkts_Object = MibTableColumn
tunnelStatisticsPktDupRxOtherPkts = _TunnelStatisticsPktDupRxOtherPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 37),
    _TunnelStatisticsPktDupRxOtherPkts_Type()
)
tunnelStatisticsPktDupRxOtherPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPktDupRxOtherPkts.setStatus("current")
_TunnelStatisticsPktDupRxThisPkts_Type = Unsigned32
_TunnelStatisticsPktDupRxThisPkts_Object = MibTableColumn
tunnelStatisticsPktDupRxThisPkts = _TunnelStatisticsPktDupRxThisPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 38),
    _TunnelStatisticsPktDupRxThisPkts_Type()
)
tunnelStatisticsPktDupRxThisPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPktDupRxThisPkts.setStatus("current")
_TunnelStatisticsPktDupTxPkts_Type = Unsigned32
_TunnelStatisticsPktDupTxPkts_Object = MibTableColumn
tunnelStatisticsPktDupTxPkts = _TunnelStatisticsPktDupTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 39),
    _TunnelStatisticsPktDupTxPkts_Type()
)
tunnelStatisticsPktDupTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPktDupTxPkts.setStatus("current")
_TunnelStatisticsPktDupTxOtherPkts_Type = Unsigned32
_TunnelStatisticsPktDupTxOtherPkts_Object = MibTableColumn
tunnelStatisticsPktDupTxOtherPkts = _TunnelStatisticsPktDupTxOtherPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 40),
    _TunnelStatisticsPktDupTxOtherPkts_Type()
)
tunnelStatisticsPktDupTxOtherPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPktDupTxOtherPkts.setStatus("current")
_TunnelStatisticsPktDupCapable_Type = TruthValue
_TunnelStatisticsPktDupCapable_Object = MibTableColumn
tunnelStatisticsPktDupCapable = _TunnelStatisticsPktDupCapable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 1, 1, 41),
    _TunnelStatisticsPktDupCapable_Type()
)
tunnelStatisticsPktDupCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPktDupCapable.setStatus("current")
_TunnelGreKeepalivesTable_Object = MibTable
tunnelGreKeepalivesTable = _TunnelGreKeepalivesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2)
)
if mibBuilder.loadTexts:
    tunnelGreKeepalivesTable.setStatus("current")
_TunnelGreKeepalivesEntry_Object = MibTableRow
tunnelGreKeepalivesEntry = _TunnelGreKeepalivesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1)
)
tunnelGreKeepalivesEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "tunnelGreKeepalivesVpnId"),
    (0, "VIPTELA-SECURITY", "tunnelGreKeepalivesIfName"),
)
if mibBuilder.loadTexts:
    tunnelGreKeepalivesEntry.setStatus("current")


class _TunnelGreKeepalivesVpnId_Type(Unsigned32):
    """Custom type tunnelGreKeepalivesVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_TunnelGreKeepalivesVpnId_Type.__name__ = "Unsigned32"
_TunnelGreKeepalivesVpnId_Object = MibTableColumn
tunnelGreKeepalivesVpnId = _TunnelGreKeepalivesVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 1),
    _TunnelGreKeepalivesVpnId_Type()
)
tunnelGreKeepalivesVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesVpnId.setStatus("current")
_TunnelGreKeepalivesIfName_Type = String
_TunnelGreKeepalivesIfName_Object = MibTableColumn
tunnelGreKeepalivesIfName = _TunnelGreKeepalivesIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 2),
    _TunnelGreKeepalivesIfName_Type()
)
tunnelGreKeepalivesIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesIfName.setStatus("current")
_TunnelGreKeepalivesSourceIp_Type = InetAddressIP
_TunnelGreKeepalivesSourceIp_Object = MibTableColumn
tunnelGreKeepalivesSourceIp = _TunnelGreKeepalivesSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 3),
    _TunnelGreKeepalivesSourceIp_Type()
)
tunnelGreKeepalivesSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesSourceIp.setStatus("current")
_TunnelGreKeepalivesDestIp_Type = InetAddressIP
_TunnelGreKeepalivesDestIp_Object = MibTableColumn
tunnelGreKeepalivesDestIp = _TunnelGreKeepalivesDestIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 4),
    _TunnelGreKeepalivesDestIp_Type()
)
tunnelGreKeepalivesDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesDestIp.setStatus("current")


class _TunnelGreKeepalivesAdminState_Type(Integer32):
    """Custom type tunnelGreKeepalivesAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("invalid", 2))
    )


_TunnelGreKeepalivesAdminState_Type.__name__ = "Integer32"
_TunnelGreKeepalivesAdminState_Object = MibTableColumn
tunnelGreKeepalivesAdminState = _TunnelGreKeepalivesAdminState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 5),
    _TunnelGreKeepalivesAdminState_Type()
)
tunnelGreKeepalivesAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesAdminState.setStatus("current")


class _TunnelGreKeepalivesOperState_Type(Integer32):
    """Custom type tunnelGreKeepalivesOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("invalid", 2))
    )


_TunnelGreKeepalivesOperState_Type.__name__ = "Integer32"
_TunnelGreKeepalivesOperState_Object = MibTableColumn
tunnelGreKeepalivesOperState = _TunnelGreKeepalivesOperState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 6),
    _TunnelGreKeepalivesOperState_Type()
)
tunnelGreKeepalivesOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesOperState.setStatus("current")
_TunnelGreKeepalivesKaEnabled_Type = TruthValue
_TunnelGreKeepalivesKaEnabled_Object = MibTableColumn
tunnelGreKeepalivesKaEnabled = _TunnelGreKeepalivesKaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 7),
    _TunnelGreKeepalivesKaEnabled_Type()
)
tunnelGreKeepalivesKaEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesKaEnabled.setStatus("current")
_TunnelGreKeepalivesRemoteTxPackets_Type = Counter64
_TunnelGreKeepalivesRemoteTxPackets_Object = MibTableColumn
tunnelGreKeepalivesRemoteTxPackets = _TunnelGreKeepalivesRemoteTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 8),
    _TunnelGreKeepalivesRemoteTxPackets_Type()
)
tunnelGreKeepalivesRemoteTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesRemoteTxPackets.setStatus("current")
_TunnelGreKeepalivesRemoteRxPackets_Type = Counter64
_TunnelGreKeepalivesRemoteRxPackets_Object = MibTableColumn
tunnelGreKeepalivesRemoteRxPackets = _TunnelGreKeepalivesRemoteRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 9),
    _TunnelGreKeepalivesRemoteRxPackets_Type()
)
tunnelGreKeepalivesRemoteRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesRemoteRxPackets.setStatus("current")
_TunnelGreKeepalivesTxPackets_Type = Counter64
_TunnelGreKeepalivesTxPackets_Object = MibTableColumn
tunnelGreKeepalivesTxPackets = _TunnelGreKeepalivesTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 10),
    _TunnelGreKeepalivesTxPackets_Type()
)
tunnelGreKeepalivesTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesTxPackets.setStatus("current")
_TunnelGreKeepalivesRxPackets_Type = Counter64
_TunnelGreKeepalivesRxPackets_Object = MibTableColumn
tunnelGreKeepalivesRxPackets = _TunnelGreKeepalivesRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 11),
    _TunnelGreKeepalivesRxPackets_Type()
)
tunnelGreKeepalivesRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesRxPackets.setStatus("current")
_TunnelGreKeepalivesTxErrors_Type = Counter32
_TunnelGreKeepalivesTxErrors_Object = MibTableColumn
tunnelGreKeepalivesTxErrors = _TunnelGreKeepalivesTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 12),
    _TunnelGreKeepalivesTxErrors_Type()
)
tunnelGreKeepalivesTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesTxErrors.setStatus("current")
_TunnelGreKeepalivesRxErrors_Type = Counter32
_TunnelGreKeepalivesRxErrors_Object = MibTableColumn
tunnelGreKeepalivesRxErrors = _TunnelGreKeepalivesRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 13),
    _TunnelGreKeepalivesRxErrors_Type()
)
tunnelGreKeepalivesRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesRxErrors.setStatus("current")


class _TunnelGreKeepalivesBaseIfOperStatus_Type(String):
    """Custom type tunnelGreKeepalivesBaseIfOperStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_TunnelGreKeepalivesBaseIfOperStatus_Type.__name__ = "String"
_TunnelGreKeepalivesBaseIfOperStatus_Object = MibTableColumn
tunnelGreKeepalivesBaseIfOperStatus = _TunnelGreKeepalivesBaseIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 14),
    _TunnelGreKeepalivesBaseIfOperStatus_Type()
)
tunnelGreKeepalivesBaseIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesBaseIfOperStatus.setStatus("current")
_TunnelGreKeepalivesTransitions_Type = Counter32
_TunnelGreKeepalivesTransitions_Object = MibTableColumn
tunnelGreKeepalivesTransitions = _TunnelGreKeepalivesTransitions_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 5, 2, 1, 15),
    _TunnelGreKeepalivesTransitions_Type()
)
tunnelGreKeepalivesTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGreKeepalivesTransitions.setStatus("current")
_SecurityInfo_ObjectIdentity = ObjectIdentity
securityInfo = _SecurityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 6)
)
_SecurityInfoAuthenticationType_Type = String
_SecurityInfoAuthenticationType_Object = MibScalar
securityInfoAuthenticationType = _SecurityInfoAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 6, 1),
    _SecurityInfoAuthenticationType_Type()
)
securityInfoAuthenticationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoAuthenticationType.setStatus("current")
_SecurityInfoRekey_Type = Unsigned32
_SecurityInfoRekey_Object = MibScalar
securityInfoRekey = _SecurityInfoRekey_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 6, 2),
    _SecurityInfoRekey_Type()
)
securityInfoRekey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoRekey.setStatus("current")
_SecurityInfoReplayWindow_Type = Unsigned32
_SecurityInfoReplayWindow_Object = MibScalar
securityInfoReplayWindow = _SecurityInfoReplayWindow_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 6, 3),
    _SecurityInfoReplayWindow_Type()
)
securityInfoReplayWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoReplayWindow.setStatus("current")
_SecurityInfoEncryptionSupported_Type = String
_SecurityInfoEncryptionSupported_Object = MibScalar
securityInfoEncryptionSupported = _SecurityInfoEncryptionSupported_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 6, 4),
    _SecurityInfoEncryptionSupported_Type()
)
securityInfoEncryptionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoEncryptionSupported.setStatus("current")
_SecurityInfoFipsMode_Type = String
_SecurityInfoFipsMode_Object = MibScalar
securityInfoFipsMode = _SecurityInfoFipsMode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 6, 5),
    _SecurityInfoFipsMode_Type()
)
securityInfoFipsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoFipsMode.setStatus("current")
_SecurityInfoPairwiseKeying_Type = String
_SecurityInfoPairwiseKeying_Object = MibScalar
securityInfoPairwiseKeying = _SecurityInfoPairwiseKeying_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 6, 6),
    _SecurityInfoPairwiseKeying_Type()
)
securityInfoPairwiseKeying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoPairwiseKeying.setStatus("current")
_Ztp_ObjectIdentity = ObjectIdentity
ztp = _Ztp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 4, 7)
)
_ZtpEntriesTable_Object = MibTable
ztpEntriesTable = _ZtpEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 7, 1)
)
if mibBuilder.loadTexts:
    ztpEntriesTable.setStatus("current")
_ZtpEntriesEntry_Object = MibTableRow
ztpEntriesEntry = _ZtpEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 7, 1, 1)
)
ztpEntriesEntry.setIndexNames(
    (0, "VIPTELA-SECURITY", "ztpEntriesIndex"),
)
if mibBuilder.loadTexts:
    ztpEntriesEntry.setStatus("current")
_ZtpEntriesIndex_Type = Unsigned32
_ZtpEntriesIndex_Object = MibTableColumn
ztpEntriesIndex = _ZtpEntriesIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 7, 1, 1, 1),
    _ZtpEntriesIndex_Type()
)
ztpEntriesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztpEntriesIndex.setStatus("current")


class _ZtpEntriesChassisNumber_Type(String):
    """Custom type ztpEntriesChassisNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ZtpEntriesChassisNumber_Type.__name__ = "String"
_ZtpEntriesChassisNumber_Object = MibTableColumn
ztpEntriesChassisNumber = _ZtpEntriesChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 7, 1, 1, 2),
    _ZtpEntriesChassisNumber_Type()
)
ztpEntriesChassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztpEntriesChassisNumber.setStatus("current")


class _ZtpEntriesSerialNumber_Type(String):
    """Custom type ztpEntriesSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ZtpEntriesSerialNumber_Type.__name__ = "String"
_ZtpEntriesSerialNumber_Object = MibTableColumn
ztpEntriesSerialNumber = _ZtpEntriesSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 7, 1, 1, 3),
    _ZtpEntriesSerialNumber_Type()
)
ztpEntriesSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztpEntriesSerialNumber.setStatus("current")


class _ZtpEntriesValidity_Type(String):
    """Custom type ztpEntriesValidity based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZtpEntriesValidity_Type.__name__ = "String"
_ZtpEntriesValidity_Object = MibTableColumn
ztpEntriesValidity = _ZtpEntriesValidity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 7, 1, 1, 4),
    _ZtpEntriesValidity_Type()
)
ztpEntriesValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztpEntriesValidity.setStatus("current")


class _ZtpEntriesVbondIp_Type(String):
    """Custom type ztpEntriesVbondIp based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ZtpEntriesVbondIp_Type.__name__ = "String"
_ZtpEntriesVbondIp_Object = MibTableColumn
ztpEntriesVbondIp = _ZtpEntriesVbondIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 7, 1, 1, 5),
    _ZtpEntriesVbondIp_Type()
)
ztpEntriesVbondIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztpEntriesVbondIp.setStatus("current")
_ZtpEntriesVbondPort_Type = UnsignedShort
_ZtpEntriesVbondPort_Object = MibTableColumn
ztpEntriesVbondPort = _ZtpEntriesVbondPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 7, 1, 1, 6),
    _ZtpEntriesVbondPort_Type()
)
ztpEntriesVbondPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztpEntriesVbondPort.setStatus("current")


class _ZtpEntriesOrganizationName_Type(String):
    """Custom type ztpEntriesOrganizationName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ZtpEntriesOrganizationName_Type.__name__ = "String"
_ZtpEntriesOrganizationName_Object = MibTableColumn
ztpEntriesOrganizationName = _ZtpEntriesOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 7, 1, 1, 7),
    _ZtpEntriesOrganizationName_Type()
)
ztpEntriesOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztpEntriesOrganizationName.setStatus("current")


class _ZtpEntriesRootCertPath_Type(String):
    """Custom type ztpEntriesRootCertPath based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ZtpEntriesRootCertPath_Type.__name__ = "String"
_ZtpEntriesRootCertPath_Object = MibTableColumn
ztpEntriesRootCertPath = _ZtpEntriesRootCertPath_Object(
    (1, 3, 6, 1, 4, 1, 41916, 4, 7, 1, 1, 8),
    _ZtpEntriesRootCertPath_Type()
)
ztpEntriesRootCertPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztpEntriesRootCertPath.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-SECURITY",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "InetAddressIP": InetAddressIP,
       "String": String,
       "AuthenticationType1": AuthenticationType1,
       "StateEnum": StateEnum,
       "ConnFlagEnum": ConnFlagEnum,
       "AuthenticationEnum": AuthenticationEnum,
       "SessionState": SessionState,
       "AuthenticationType": AuthenticationType,
       "viptela-security": viptela_security,
       "control": control,
       "controlConnectionsInfo": controlConnectionsInfo,
       "controlConnectionsInfoRate": controlConnectionsInfoRate,
       "controlConnectionsTable": controlConnectionsTable,
       "controlConnectionsEntry": controlConnectionsEntry,
       "controlConnectionsInstance": controlConnectionsInstance,
       "controlConnectionsPeerType": controlConnectionsPeerType,
       "controlConnectionsSiteId": controlConnectionsSiteId,
       "controlConnectionsDomainId": controlConnectionsDomainId,
       "controlConnectionsLocalPrivateIp": controlConnectionsLocalPrivateIp,
       "controlConnectionsLocalPrivatePort": controlConnectionsLocalPrivatePort,
       "controlConnectionsPublicIp": controlConnectionsPublicIp,
       "controlConnectionsPublicPort": controlConnectionsPublicPort,
       "controlConnectionsSystemIp": controlConnectionsSystemIp,
       "controlConnectionsProtocol": controlConnectionsProtocol,
       "controlConnectionsLocalColor": controlConnectionsLocalColor,
       "controlConnectionsRemoteColor": controlConnectionsRemoteColor,
       "controlConnectionsPrivateIp": controlConnectionsPrivateIp,
       "controlConnectionsPrivatePort": controlConnectionsPrivatePort,
       "controlConnectionsState": controlConnectionsState,
       "controlConnectionsLocalEnum": controlConnectionsLocalEnum,
       "controlConnectionsRemoteEnum": controlConnectionsRemoteEnum,
       "controlConnectionsLocalStateInfo": controlConnectionsLocalStateInfo,
       "controlConnectionsRemoteStateInfo": controlConnectionsRemoteStateInfo,
       "controlConnectionsUptime": controlConnectionsUptime,
       "controlConnectionsTxHello": controlConnectionsTxHello,
       "controlConnectionsTxConnects": controlConnectionsTxConnects,
       "controlConnectionsTxRegisters": controlConnectionsTxRegisters,
       "controlConnectionsTxRegisterReplies": controlConnectionsTxRegisterReplies,
       "controlConnectionsTxChallenge": controlConnectionsTxChallenge,
       "controlConnectionsTxChallengeResp": controlConnectionsTxChallengeResp,
       "controlConnectionsTxChallengeAck": controlConnectionsTxChallengeAck,
       "controlConnectionsTxTeardown": controlConnectionsTxTeardown,
       "controlConnectionsTxTeardownAll": controlConnectionsTxTeardownAll,
       "controlConnectionsTxVmToPeer": controlConnectionsTxVmToPeer,
       "controlConnectionsTxRegisterToVm": controlConnectionsTxRegisterToVm,
       "controlConnectionsRxHello": controlConnectionsRxHello,
       "controlConnectionsRxConnects": controlConnectionsRxConnects,
       "controlConnectionsRxRegisters": controlConnectionsRxRegisters,
       "controlConnectionsRxRegisterReplies": controlConnectionsRxRegisterReplies,
       "controlConnectionsRxChallenge": controlConnectionsRxChallenge,
       "controlConnectionsRxChallengeResp": controlConnectionsRxChallengeResp,
       "controlConnectionsRxChallengeAck": controlConnectionsRxChallengeAck,
       "controlConnectionsRxTeardown": controlConnectionsRxTeardown,
       "controlConnectionsRxVmToPeer": controlConnectionsRxVmToPeer,
       "controlConnectionsRxRegisterToVm": controlConnectionsRxRegisterToVm,
       "controlConnectionsNegotiatedHelloInterval": controlConnectionsNegotiatedHelloInterval,
       "controlConnectionsNegotiatedHelloTolerance": controlConnectionsNegotiatedHelloTolerance,
       "controlConnectionsConfiguredSystemIp": controlConnectionsConfiguredSystemIp,
       "controlConnectionsVOrgName": controlConnectionsVOrgName,
       "controlConnectionsTxCreateCert": controlConnectionsTxCreateCert,
       "controlConnectionsRxCreateCert": controlConnectionsRxCreateCert,
       "controlConnectionsTxCreateCertReply": controlConnectionsTxCreateCertReply,
       "controlConnectionsRxCreateCertReply": controlConnectionsRxCreateCertReply,
       "controlConnectionsBehindProxy": controlConnectionsBehindProxy,
       "controlConnectionsHistoryTable": controlConnectionsHistoryTable,
       "controlConnectionsHistoryEntry": controlConnectionsHistoryEntry,
       "controlConnectionsHistoryInstance": controlConnectionsHistoryInstance,
       "controlConnectionsHistoryIndex": controlConnectionsHistoryIndex,
       "controlConnectionsHistoryPeerType": controlConnectionsHistoryPeerType,
       "controlConnectionsHistorySiteId": controlConnectionsHistorySiteId,
       "controlConnectionsHistoryDomainId": controlConnectionsHistoryDomainId,
       "controlConnectionsHistoryPrivateIp": controlConnectionsHistoryPrivateIp,
       "controlConnectionsHistoryPrivatePort": controlConnectionsHistoryPrivatePort,
       "controlConnectionsHistoryPublicIp": controlConnectionsHistoryPublicIp,
       "controlConnectionsHistoryPublicPort": controlConnectionsHistoryPublicPort,
       "controlConnectionsHistorySystemIp": controlConnectionsHistorySystemIp,
       "controlConnectionsHistoryProtocol": controlConnectionsHistoryProtocol,
       "controlConnectionsHistoryLocalColor": controlConnectionsHistoryLocalColor,
       "controlConnectionsHistoryRemoteColor": controlConnectionsHistoryRemoteColor,
       "controlConnectionsHistoryState": controlConnectionsHistoryState,
       "controlConnectionsHistoryLocalEnum": controlConnectionsHistoryLocalEnum,
       "controlConnectionsHistoryRemoteEnum": controlConnectionsHistoryRemoteEnum,
       "controlConnectionsHistoryLocalStateInfo": controlConnectionsHistoryLocalStateInfo,
       "controlConnectionsHistoryRemoteStateInfo": controlConnectionsHistoryRemoteStateInfo,
       "controlConnectionsHistoryDowntime": controlConnectionsHistoryDowntime,
       "controlConnectionsHistoryTxHello": controlConnectionsHistoryTxHello,
       "controlConnectionsHistoryTxConnects": controlConnectionsHistoryTxConnects,
       "controlConnectionsHistoryTxRegisters": controlConnectionsHistoryTxRegisters,
       "controlConnectionsHistoryTxRegisterReplies": controlConnectionsHistoryTxRegisterReplies,
       "controlConnectionsHistoryTxChallenge": controlConnectionsHistoryTxChallenge,
       "controlConnectionsHistoryTxChallengeResp": controlConnectionsHistoryTxChallengeResp,
       "controlConnectionsHistoryTxChallengeAck": controlConnectionsHistoryTxChallengeAck,
       "controlConnectionsHistoryTxTeardown": controlConnectionsHistoryTxTeardown,
       "controlConnectionsHistoryTxTeardownAll": controlConnectionsHistoryTxTeardownAll,
       "controlConnectionsHistoryTxVmToPeer": controlConnectionsHistoryTxVmToPeer,
       "controlConnectionsHistoryTxRegisterToVm": controlConnectionsHistoryTxRegisterToVm,
       "controlConnectionsHistoryRxHello": controlConnectionsHistoryRxHello,
       "controlConnectionsHistoryRxConnects": controlConnectionsHistoryRxConnects,
       "controlConnectionsHistoryRxRegisters": controlConnectionsHistoryRxRegisters,
       "controlConnectionsHistoryRxRegisterReplies": controlConnectionsHistoryRxRegisterReplies,
       "controlConnectionsHistoryRxChallenge": controlConnectionsHistoryRxChallenge,
       "controlConnectionsHistoryRxChallengeResp": controlConnectionsHistoryRxChallengeResp,
       "controlConnectionsHistoryRxChallengeAck": controlConnectionsHistoryRxChallengeAck,
       "controlConnectionsHistoryRxTeardown": controlConnectionsHistoryRxTeardown,
       "controlConnectionsHistoryRxVmToPeer": controlConnectionsHistoryRxVmToPeer,
       "controlConnectionsHistoryRxRegisterToVm": controlConnectionsHistoryRxRegisterToVm,
       "controlConnectionsHistoryRepCount": controlConnectionsHistoryRepCount,
       "controlConnectionsHistoryPrevDowntime": controlConnectionsHistoryPrevDowntime,
       "controlConnectionsHistoryConfiguredSystemIp": controlConnectionsHistoryConfiguredSystemIp,
       "controlConnectionsHistoryVHOrgName": controlConnectionsHistoryVHOrgName,
       "controlConnectionsHistoryUuid": controlConnectionsHistoryUuid,
       "controlConnectionsHistoryTxCreateCert": controlConnectionsHistoryTxCreateCert,
       "controlConnectionsHistoryRxCreateCert": controlConnectionsHistoryRxCreateCert,
       "controlConnectionsHistoryTxCreateCertReply": controlConnectionsHistoryTxCreateCertReply,
       "controlConnectionsHistoryRxCreateCertReply": controlConnectionsHistoryRxCreateCertReply,
       "controlStatistics": controlStatistics,
       "controlStatisticsTxPkts": controlStatisticsTxPkts,
       "controlStatisticsTxOctets": controlStatisticsTxOctets,
       "controlStatisticsTxError": controlStatisticsTxError,
       "controlStatisticsTxBlocked": controlStatisticsTxBlocked,
       "controlStatisticsTxHello": controlStatisticsTxHello,
       "controlStatisticsTxConnects": controlStatisticsTxConnects,
       "controlStatisticsTxRegisters": controlStatisticsTxRegisters,
       "controlStatisticsTxRegisterReplies": controlStatisticsTxRegisterReplies,
       "controlStatisticsTxDtlsHandshake": controlStatisticsTxDtlsHandshake,
       "controlStatisticsTxDtlsHandshakeFailures": controlStatisticsTxDtlsHandshakeFailures,
       "controlStatisticsTxDtlsHandshakeDone": controlStatisticsTxDtlsHandshakeDone,
       "controlStatisticsTxChallenge": controlStatisticsTxChallenge,
       "controlStatisticsTxChallengeResp": controlStatisticsTxChallengeResp,
       "controlStatisticsTxChallengeAck": controlStatisticsTxChallengeAck,
       "controlStatisticsTxChallengeError": controlStatisticsTxChallengeError,
       "controlStatisticsTxChallengeRespError": controlStatisticsTxChallengeRespError,
       "controlStatisticsTxChallengeAckError": controlStatisticsTxChallengeAckError,
       "controlStatisticsTxChallengeGenError": controlStatisticsTxChallengeGenError,
       "controlStatisticsTxVmanageToPeer": controlStatisticsTxVmanageToPeer,
       "controlStatisticsTxRegisterToVmanage": controlStatisticsTxRegisterToVmanage,
       "controlStatisticsRxPkts": controlStatisticsRxPkts,
       "controlStatisticsRxOctets": controlStatisticsRxOctets,
       "controlStatisticsRxError": controlStatisticsRxError,
       "controlStatisticsRxHello": controlStatisticsRxHello,
       "controlStatisticsRxConnects": controlStatisticsRxConnects,
       "controlStatisticsRxRegisters": controlStatisticsRxRegisters,
       "controlStatisticsRxRegisterReplies": controlStatisticsRxRegisterReplies,
       "controlStatisticsRxDtlsHandshake": controlStatisticsRxDtlsHandshake,
       "controlStatisticsRxDtlsHandshakeFailures": controlStatisticsRxDtlsHandshakeFailures,
       "controlStatisticsRxDtlsHandshakeDone": controlStatisticsRxDtlsHandshakeDone,
       "controlStatisticsRxChallenge": controlStatisticsRxChallenge,
       "controlStatisticsRxChallengeResp": controlStatisticsRxChallengeResp,
       "controlStatisticsRxChallengeAck": controlStatisticsRxChallengeAck,
       "controlStatisticsChallengeFailures": controlStatisticsChallengeFailures,
       "controlStatisticsRxVmanageToPeer": controlStatisticsRxVmanageToPeer,
       "controlStatisticsRxRegisterToVmanage": controlStatisticsRxRegisterToVmanage,
       "controlStatisticsBidFailuresNeedingReset": controlStatisticsBidFailuresNeedingReset,
       "controlLocalProperties": controlLocalProperties,
       "controlLocalPropertiesDeviceType": controlLocalPropertiesDeviceType,
       "controlLocalPropertiesOrganizationName": controlLocalPropertiesOrganizationName,
       "controlLocalPropertiesCertificateStatus": controlLocalPropertiesCertificateStatus,
       "controlLocalPropertiesRootCaChainStatus": controlLocalPropertiesRootCaChainStatus,
       "controlLocalPropertiesCertificateValidity": controlLocalPropertiesCertificateValidity,
       "controlLocalPropertiesCertificateNotValidBefore": controlLocalPropertiesCertificateNotValidBefore,
       "controlLocalPropertiesCertificateNotValidAfter": controlLocalPropertiesCertificateNotValidAfter,
       "controlLocalPropertiesDnsName": controlLocalPropertiesDnsName,
       "controlLocalPropertiesSiteId": controlLocalPropertiesSiteId,
       "controlLocalPropertiesDomainId": controlLocalPropertiesDomainId,
       "controlLocalPropertiesProtocol": controlLocalPropertiesProtocol,
       "controlLocalPropertiesTlsPort": controlLocalPropertiesTlsPort,
       "controlLocalPropertiesSystemIp": controlLocalPropertiesSystemIp,
       "controlLocalPropertiesUuid": controlLocalPropertiesUuid,
       "controlLocalPropertiesBoardSerial": controlLocalPropertiesBoardSerial,
       "controlLocalPropertiesRegisterInterval": controlLocalPropertiesRegisterInterval,
       "controlLocalPropertiesRetryInterval": controlLocalPropertiesRetryInterval,
       "controlLocalPropertiesNoActivity": controlLocalPropertiesNoActivity,
       "controlLocalPropertiesDnsCacheFlushInterval": controlLocalPropertiesDnsCacheFlushInterval,
       "controlLocalPropertiesPortHopped": controlLocalPropertiesPortHopped,
       "controlLocalPropertiesTimeSincePortHop": controlLocalPropertiesTimeSincePortHop,
       "controlLocalPropertiesMaxControllers": controlLocalPropertiesMaxControllers,
       "controlLocalPropertiesKeygenInterval": controlLocalPropertiesKeygenInterval,
       "controlLocalPropertiesIpAddressListTable": controlLocalPropertiesIpAddressListTable,
       "controlLocalPropertiesIpAddressListEntry": controlLocalPropertiesIpAddressListEntry,
       "controlLocalPropertiesIpAddressListIndex": controlLocalPropertiesIpAddressListIndex,
       "controlLocalPropertiesIpAddressListIp": controlLocalPropertiesIpAddressListIp,
       "controlLocalPropertiesIpAddressListPort": controlLocalPropertiesIpAddressListPort,
       "controlLocalPropertiesNumberVbondPeers": controlLocalPropertiesNumberVbondPeers,
       "controlLocalPropertiesVbondAddressListTable": controlLocalPropertiesVbondAddressListTable,
       "controlLocalPropertiesVbondAddressListEntry": controlLocalPropertiesVbondAddressListEntry,
       "controlLocalPropertiesVbondAddressListIndex": controlLocalPropertiesVbondAddressListIndex,
       "controlLocalPropertiesVbondAddressListIp": controlLocalPropertiesVbondAddressListIp,
       "controlLocalPropertiesVbondAddressListPort": controlLocalPropertiesVbondAddressListPort,
       "controlLocalPropertiesNumberActiveWanInterfaces": controlLocalPropertiesNumberActiveWanInterfaces,
       "controlLocalPropertiesWanInterfaceListTable": controlLocalPropertiesWanInterfaceListTable,
       "controlLocalPropertiesWanInterfaceListEntry": controlLocalPropertiesWanInterfaceListEntry,
       "controlLocalPropertiesWanInterfaceListIndex": controlLocalPropertiesWanInterfaceListIndex,
       "controlLocalPropertiesWanInterfaceListInterface": controlLocalPropertiesWanInterfaceListInterface,
       "controlLocalPropertiesWanInterfaceListPublicIp": controlLocalPropertiesWanInterfaceListPublicIp,
       "controlLocalPropertiesWanInterfaceListPublicPort": controlLocalPropertiesWanInterfaceListPublicPort,
       "controlLocalPropertiesWanInterfaceListPrivateIp": controlLocalPropertiesWanInterfaceListPrivateIp,
       "controlLocalPropertiesWanInterfaceListPrivatePort": controlLocalPropertiesWanInterfaceListPrivatePort,
       "controlLocalPropertiesWanInterfaceListNumVsmarts": controlLocalPropertiesWanInterfaceListNumVsmarts,
       "controlLocalPropertiesWanInterfaceListNumVmanages": controlLocalPropertiesWanInterfaceListNumVmanages,
       "controlLocalPropertiesWanInterfaceListWeight": controlLocalPropertiesWanInterfaceListWeight,
       "controlLocalPropertiesWanInterfaceListColor": controlLocalPropertiesWanInterfaceListColor,
       "controlLocalPropertiesWanInterfaceListCarrier": controlLocalPropertiesWanInterfaceListCarrier,
       "controlLocalPropertiesWanInterfaceListPreference": controlLocalPropertiesWanInterfaceListPreference,
       "controlLocalPropertiesWanInterfaceListAdminState": controlLocalPropertiesWanInterfaceListAdminState,
       "controlLocalPropertiesWanInterfaceListOperationState": controlLocalPropertiesWanInterfaceListOperationState,
       "controlLocalPropertiesWanInterfaceListLastConnTime": controlLocalPropertiesWanInterfaceListLastConnTime,
       "controlLocalPropertiesWanInterfaceListRestrictStr": controlLocalPropertiesWanInterfaceListRestrictStr,
       "controlLocalPropertiesWanInterfaceListControlStr": controlLocalPropertiesWanInterfaceListControlStr,
       "controlLocalPropertiesWanInterfaceListPerWanMaxControllers": controlLocalPropertiesWanInterfaceListPerWanMaxControllers,
       "controlLocalPropertiesWanInterfaceListInstance": controlLocalPropertiesWanInterfaceListInstance,
       "controlLocalPropertiesWanInterfaceListPrivateIpv6": controlLocalPropertiesWanInterfaceListPrivateIpv6,
       "controlLocalPropertiesWanInterfaceListSpiChange": controlLocalPropertiesWanInterfaceListSpiChange,
       "controlLocalPropertiesWanInterfaceListLastResort": controlLocalPropertiesWanInterfaceListLastResort,
       "controlLocalPropertiesWanInterfaceListWanPortHopped": controlLocalPropertiesWanInterfaceListWanPortHopped,
       "controlLocalPropertiesWanInterfaceListWanTimeSincePortHop": controlLocalPropertiesWanInterfaceListWanTimeSincePortHop,
       "controlLocalPropertiesWanInterfaceListVbondAsStunServer": controlLocalPropertiesWanInterfaceListVbondAsStunServer,
       "controlLocalPropertiesWanInterfaceListVmanageConnectionPreference": controlLocalPropertiesWanInterfaceListVmanageConnectionPreference,
       "controlLocalPropertiesWanInterfaceListLowBandwidthLink": controlLocalPropertiesWanInterfaceListLowBandwidthLink,
       "controlLocalPropertiesWanInterfaceListNatType": controlLocalPropertiesWanInterfaceListNatType,
       "controlLocalPropertiesWanInterfaceListInterfaceAdminState": controlLocalPropertiesWanInterfaceListInterfaceAdminState,
       "controlLocalPropertiesWanInterfaceListInterfaceOperState": controlLocalPropertiesWanInterfaceListInterfaceOperState,
       "controlLocalPropertiesVedgeListVersion": controlLocalPropertiesVedgeListVersion,
       "controlLocalPropertiesVsmartListVersion": controlLocalPropertiesVsmartListVersion,
       "controlLocalPropertiesSPOrganizationName": controlLocalPropertiesSPOrganizationName,
       "controlLocalPropertiesToken": controlLocalPropertiesToken,
       "controlLocalPropertiesCloudHosted": controlLocalPropertiesCloudHosted,
       "controlLocalPropertiesEmbargoCheck": controlLocalPropertiesEmbargoCheck,
       "controlLocalPropertiesEnterpriseSerial": controlLocalPropertiesEnterpriseSerial,
       "controlLocalPropertiesEnterpriseCertificateStatus": controlLocalPropertiesEnterpriseCertificateStatus,
       "controlLocalPropertiesEnterpriseCertificateValidity": controlLocalPropertiesEnterpriseCertificateValidity,
       "controlLocalPropertiesEnterpriseCertificateNotValidBefore": controlLocalPropertiesEnterpriseCertificateNotValidBefore,
       "controlLocalPropertiesEnterpriseCertificateNotValidAfter": controlLocalPropertiesEnterpriseCertificateNotValidAfter,
       "controlLocalPropertiesPairwiseKeying": controlLocalPropertiesPairwiseKeying,
       "controlLocalPropertiesCdbLocked": controlLocalPropertiesCdbLocked,
       "controlLocalPropertiesSubjectSerialNumber": controlLocalPropertiesSubjectSerialNumber,
       "controlValidVsmartsTable": controlValidVsmartsTable,
       "controlValidVsmartsEntry": controlValidVsmartsEntry,
       "controlValidVsmartsSerialNumber": controlValidVsmartsSerialNumber,
       "controlValidVsmartsOrg": controlValidVsmartsOrg,
       "controlValidVedgesTable": controlValidVedgesTable,
       "controlValidVedgesEntry": controlValidVedgesEntry,
       "controlValidVedgesChassisNumber": controlValidVedgesChassisNumber,
       "controlValidVedgesSerialNumber": controlValidVedgesSerialNumber,
       "controlValidVedgesValidity": controlValidVedgesValidity,
       "controlValidVedgesOrg": controlValidVedgesOrg,
       "controlValidVedgesHardwareInstalledSerialNumber": controlValidVedgesHardwareInstalledSerialNumber,
       "controlValidVedgesSubjectSerialNumber": controlValidVedgesSubjectSerialNumber,
       "controlSummaryTable": controlSummaryTable,
       "controlSummaryEntry": controlSummaryEntry,
       "controlSummaryInstance": controlSummaryInstance,
       "controlSummaryVbondCounts": controlSummaryVbondCounts,
       "controlSummaryVmanageCounts": controlSummaryVmanageCounts,
       "controlSummaryVsmartCounts": controlSummaryVsmartCounts,
       "controlSummaryVedgeCounts": controlSummaryVedgeCounts,
       "controlSummaryProtocol": controlSummaryProtocol,
       "controlSummaryListeningIp": controlSummaryListeningIp,
       "controlSummaryListeningPort": controlSummaryListeningPort,
       "controlSummaryListeningIpv6": controlSummaryListeningIpv6,
       "controlSummaryValidControllerCounts": controlSummaryValidControllerCounts,
       "controlAffinity": controlAffinity,
       "controlAffinityConfigTable": controlAffinityConfigTable,
       "controlAffinityConfigEntry": controlAffinityConfigEntry,
       "controlAffinityConfigAffcIndex": controlAffinityConfigAffcIndex,
       "controlAffinityConfigAffcInterface": controlAffinityConfigAffcInterface,
       "controlAffinityConfigAffcErvc": controlAffinityConfigAffcErvc,
       "controlAffinityConfigAffcEcl": controlAffinityConfigAffcEcl,
       "controlAffinityConfigAffcCcl": controlAffinityConfigAffcCcl,
       "controlAffinityConfigAffcEquil": controlAffinityConfigAffcEquil,
       "controlAffinityConfigAffcLastResort": controlAffinityConfigAffcLastResort,
       "controlAffinityStatusTable": controlAffinityStatusTable,
       "controlAffinityStatusEntry": controlAffinityStatusEntry,
       "controlAffinityStatusAffsIndex": controlAffinityStatusAffsIndex,
       "controlAffinityStatusAffsInterface": controlAffinityStatusAffsInterface,
       "controlAffinityStatusAffsAcc": controlAffinityStatusAffsAcc,
       "controlAffinityStatusAffsUcc": controlAffinityStatusAffsUcc,
       "controlAffinityStatusAffsAc": controlAffinityStatusAffsAc,
       "controlValidVmanageIdTable": controlValidVmanageIdTable,
       "controlValidVmanageIdEntry": controlValidVmanageIdEntry,
       "controlValidVManageIdChassisNumbers": controlValidVManageIdChassisNumbers,
       "orchestrator": orchestrator,
       "orchestratorConnectionsTable": orchestratorConnectionsTable,
       "orchestratorConnectionsEntry": orchestratorConnectionsEntry,
       "orchestratorConnectionsInstance": orchestratorConnectionsInstance,
       "orchestratorConnectionsPeerType": orchestratorConnectionsPeerType,
       "orchestratorConnectionsSiteId": orchestratorConnectionsSiteId,
       "orchestratorConnectionsDomainId": orchestratorConnectionsDomainId,
       "orchestratorConnectionsProtocol": orchestratorConnectionsProtocol,
       "orchestratorConnectionsLocalPrivateIp": orchestratorConnectionsLocalPrivateIp,
       "orchestratorConnectionsLocalPrivatePort": orchestratorConnectionsLocalPrivatePort,
       "orchestratorConnectionsPublicIp": orchestratorConnectionsPublicIp,
       "orchestratorConnectionsPublicPort": orchestratorConnectionsPublicPort,
       "orchestratorConnectionsSystemIp": orchestratorConnectionsSystemIp,
       "orchestratorConnectionsLocalColor": orchestratorConnectionsLocalColor,
       "orchestratorConnectionsRemoteColor": orchestratorConnectionsRemoteColor,
       "orchestratorConnectionsPrivateIp": orchestratorConnectionsPrivateIp,
       "orchestratorConnectionsPrivatePort": orchestratorConnectionsPrivatePort,
       "orchestratorConnectionsState": orchestratorConnectionsState,
       "orchestratorConnectionsLocalEnum": orchestratorConnectionsLocalEnum,
       "orchestratorConnectionsRemoteEnum": orchestratorConnectionsRemoteEnum,
       "orchestratorConnectionsLocalStateInfo": orchestratorConnectionsLocalStateInfo,
       "orchestratorConnectionsRemoteStateInfo": orchestratorConnectionsRemoteStateInfo,
       "orchestratorConnectionsUptime": orchestratorConnectionsUptime,
       "orchestratorConnectionsTxHello": orchestratorConnectionsTxHello,
       "orchestratorConnectionsTxConnects": orchestratorConnectionsTxConnects,
       "orchestratorConnectionsTxRegisters": orchestratorConnectionsTxRegisters,
       "orchestratorConnectionsTxRegisterReplies": orchestratorConnectionsTxRegisterReplies,
       "orchestratorConnectionsTxChallenge": orchestratorConnectionsTxChallenge,
       "orchestratorConnectionsTxChallengeResp": orchestratorConnectionsTxChallengeResp,
       "orchestratorConnectionsTxChallengeAck": orchestratorConnectionsTxChallengeAck,
       "orchestratorConnectionsTxTeardown": orchestratorConnectionsTxTeardown,
       "orchestratorConnectionsTxTeardownAll": orchestratorConnectionsTxTeardownAll,
       "orchestratorConnectionsTxVmToPeer": orchestratorConnectionsTxVmToPeer,
       "orchestratorConnectionsTxRegisterToVm": orchestratorConnectionsTxRegisterToVm,
       "orchestratorConnectionsRxHello": orchestratorConnectionsRxHello,
       "orchestratorConnectionsRxConnects": orchestratorConnectionsRxConnects,
       "orchestratorConnectionsRxRegisters": orchestratorConnectionsRxRegisters,
       "orchestratorConnectionsRxRegisterReplies": orchestratorConnectionsRxRegisterReplies,
       "orchestratorConnectionsRxChallenge": orchestratorConnectionsRxChallenge,
       "orchestratorConnectionsRxChallengeResp": orchestratorConnectionsRxChallengeResp,
       "orchestratorConnectionsRxChallengeAck": orchestratorConnectionsRxChallengeAck,
       "orchestratorConnectionsRxTeardown": orchestratorConnectionsRxTeardown,
       "orchestratorConnectionsRxVmToPeer": orchestratorConnectionsRxVmToPeer,
       "orchestratorConnectionsRxRegisterToVm": orchestratorConnectionsRxRegisterToVm,
       "orchestratorConnectionsNegotiatedHelloInterval": orchestratorConnectionsNegotiatedHelloInterval,
       "orchestratorConnectionsNegotiatedHelloTolerance": orchestratorConnectionsNegotiatedHelloTolerance,
       "orchestratorConnectionsOrgname": orchestratorConnectionsOrgname,
       "orchestratorConnectionsSporgname": orchestratorConnectionsSporgname,
       "orchestratorConnectionsTxCreateCert": orchestratorConnectionsTxCreateCert,
       "orchestratorConnectionsRxCreateCert": orchestratorConnectionsRxCreateCert,
       "orchestratorConnectionsTxCreateCertReply": orchestratorConnectionsTxCreateCertReply,
       "orchestratorConnectionsRxCreateCertReply": orchestratorConnectionsRxCreateCertReply,
       "orchestratorConnectionsCloudHosted": orchestratorConnectionsCloudHosted,
       "orchestratorConnectionsHistoryTable": orchestratorConnectionsHistoryTable,
       "orchestratorConnectionsHistoryEntry": orchestratorConnectionsHistoryEntry,
       "orchestratorConnectionsHistoryInstance": orchestratorConnectionsHistoryInstance,
       "orchestratorConnectionsHistoryIndex": orchestratorConnectionsHistoryIndex,
       "orchestratorConnectionsHistoryPeerType": orchestratorConnectionsHistoryPeerType,
       "orchestratorConnectionsHistorySiteId": orchestratorConnectionsHistorySiteId,
       "orchestratorConnectionsHistoryDomainId": orchestratorConnectionsHistoryDomainId,
       "orchestratorConnectionsHistoryProtocol": orchestratorConnectionsHistoryProtocol,
       "orchestratorConnectionsHistoryPrivateIp": orchestratorConnectionsHistoryPrivateIp,
       "orchestratorConnectionsHistoryPrivatePort": orchestratorConnectionsHistoryPrivatePort,
       "orchestratorConnectionsHistoryPublicIp": orchestratorConnectionsHistoryPublicIp,
       "orchestratorConnectionsHistoryPublicPort": orchestratorConnectionsHistoryPublicPort,
       "orchestratorConnectionsHistorySystemIp": orchestratorConnectionsHistorySystemIp,
       "orchestratorConnectionsHistoryLocalColor": orchestratorConnectionsHistoryLocalColor,
       "orchestratorConnectionsHistoryRemoteColor": orchestratorConnectionsHistoryRemoteColor,
       "orchestratorConnectionsHistoryState": orchestratorConnectionsHistoryState,
       "orchestratorConnectionsHistoryLocalEnum": orchestratorConnectionsHistoryLocalEnum,
       "orchestratorConnectionsHistoryRemoteEnum": orchestratorConnectionsHistoryRemoteEnum,
       "orchestratorConnectionsHistoryLocalStateInfo": orchestratorConnectionsHistoryLocalStateInfo,
       "orchestratorConnectionsHistoryRemoteStateInfo": orchestratorConnectionsHistoryRemoteStateInfo,
       "orchestratorConnectionsHistoryLocalPrivateIp": orchestratorConnectionsHistoryLocalPrivateIp,
       "orchestratorConnectionsHistoryLocalPrivatePort": orchestratorConnectionsHistoryLocalPrivatePort,
       "orchestratorConnectionsHistoryDowntime": orchestratorConnectionsHistoryDowntime,
       "orchestratorConnectionsHistoryTxHello": orchestratorConnectionsHistoryTxHello,
       "orchestratorConnectionsHistoryTxConnects": orchestratorConnectionsHistoryTxConnects,
       "orchestratorConnectionsHistoryTxRegisters": orchestratorConnectionsHistoryTxRegisters,
       "orchestratorConnectionsHistoryTxRegisterReplies": orchestratorConnectionsHistoryTxRegisterReplies,
       "orchestratorConnectionsHistoryTxChallenge": orchestratorConnectionsHistoryTxChallenge,
       "orchestratorConnectionsHistoryTxChallengeResp": orchestratorConnectionsHistoryTxChallengeResp,
       "orchestratorConnectionsHistoryTxChallengeAck": orchestratorConnectionsHistoryTxChallengeAck,
       "orchestratorConnectionsHistoryTxTeardown": orchestratorConnectionsHistoryTxTeardown,
       "orchestratorConnectionsHistoryTxTeardownAll": orchestratorConnectionsHistoryTxTeardownAll,
       "orchestratorConnectionsHistoryTxVmToPeer": orchestratorConnectionsHistoryTxVmToPeer,
       "orchestratorConnectionsHistoryTxRegisterToVm": orchestratorConnectionsHistoryTxRegisterToVm,
       "orchestratorConnectionsHistoryRxHello": orchestratorConnectionsHistoryRxHello,
       "orchestratorConnectionsHistoryRxConnects": orchestratorConnectionsHistoryRxConnects,
       "orchestratorConnectionsHistoryRxRegisters": orchestratorConnectionsHistoryRxRegisters,
       "orchestratorConnectionsHistoryRxRegisterReplies": orchestratorConnectionsHistoryRxRegisterReplies,
       "orchestratorConnectionsHistoryRxChallenge": orchestratorConnectionsHistoryRxChallenge,
       "orchestratorConnectionsHistoryRxChallengeResp": orchestratorConnectionsHistoryRxChallengeResp,
       "orchestratorConnectionsHistoryRxChallengeAck": orchestratorConnectionsHistoryRxChallengeAck,
       "orchestratorConnectionsHistoryRxTeardown": orchestratorConnectionsHistoryRxTeardown,
       "orchestratorConnectionsHistoryRxVmToPeer": orchestratorConnectionsHistoryRxVmToPeer,
       "orchestratorConnectionsHistoryRxRegisterToVm": orchestratorConnectionsHistoryRxRegisterToVm,
       "orchestratorConnectionsHistoryRepCount": orchestratorConnectionsHistoryRepCount,
       "orchestratorConnectionsHistoryPrevDowntime": orchestratorConnectionsHistoryPrevDowntime,
       "orchestratorConnectionsHistoryHOrgname": orchestratorConnectionsHistoryHOrgname,
       "orchestratorConnectionsHistoryHSporgname": orchestratorConnectionsHistoryHSporgname,
       "orchestratorConnectionsHistoryUuid": orchestratorConnectionsHistoryUuid,
       "orchestratorConnectionsHistoryTxCreateCert": orchestratorConnectionsHistoryTxCreateCert,
       "orchestratorConnectionsHistoryRxCreateCert": orchestratorConnectionsHistoryRxCreateCert,
       "orchestratorConnectionsHistoryTxCreateCertReply": orchestratorConnectionsHistoryTxCreateCertReply,
       "orchestratorConnectionsHistoryRxCreateCertReply": orchestratorConnectionsHistoryRxCreateCertReply,
       "orchestratorStatistics": orchestratorStatistics,
       "orchestratorStatisticsTxPkts": orchestratorStatisticsTxPkts,
       "orchestratorStatisticsTxOctets": orchestratorStatisticsTxOctets,
       "orchestratorStatisticsTxError": orchestratorStatisticsTxError,
       "orchestratorStatisticsTxBlocked": orchestratorStatisticsTxBlocked,
       "orchestratorStatisticsTxConnects": orchestratorStatisticsTxConnects,
       "orchestratorStatisticsTxRegisters": orchestratorStatisticsTxRegisters,
       "orchestratorStatisticsTxRegisterReplies": orchestratorStatisticsTxRegisterReplies,
       "orchestratorStatisticsTxDtlsHandshake": orchestratorStatisticsTxDtlsHandshake,
       "orchestratorStatisticsTxDtlsHandshakeFailures": orchestratorStatisticsTxDtlsHandshakeFailures,
       "orchestratorStatisticsTxDtlsHandshakeDone": orchestratorStatisticsTxDtlsHandshakeDone,
       "orchestratorStatisticsTxChallenge": orchestratorStatisticsTxChallenge,
       "orchestratorStatisticsTxChallengeResp": orchestratorStatisticsTxChallengeResp,
       "orchestratorStatisticsTxChallengeAck": orchestratorStatisticsTxChallengeAck,
       "orchestratorStatisticsTxChallengeError": orchestratorStatisticsTxChallengeError,
       "orchestratorStatisticsTxChallengeRespError": orchestratorStatisticsTxChallengeRespError,
       "orchestratorStatisticsTxChallengeAckError": orchestratorStatisticsTxChallengeAckError,
       "orchestratorStatisticsTxChallengeGenError": orchestratorStatisticsTxChallengeGenError,
       "orchestratorStatisticsRxPkts": orchestratorStatisticsRxPkts,
       "orchestratorStatisticsRxOctets": orchestratorStatisticsRxOctets,
       "orchestratorStatisticsRxError": orchestratorStatisticsRxError,
       "orchestratorStatisticsRxConnects": orchestratorStatisticsRxConnects,
       "orchestratorStatisticsRxRegisters": orchestratorStatisticsRxRegisters,
       "orchestratorStatisticsRxRegisterReplies": orchestratorStatisticsRxRegisterReplies,
       "orchestratorStatisticsRxDtlsHandshake": orchestratorStatisticsRxDtlsHandshake,
       "orchestratorStatisticsRxDtlsHandshakeFailures": orchestratorStatisticsRxDtlsHandshakeFailures,
       "orchestratorStatisticsRxDtlsHandshakeDone": orchestratorStatisticsRxDtlsHandshakeDone,
       "orchestratorStatisticsRxChallenge": orchestratorStatisticsRxChallenge,
       "orchestratorStatisticsRxChallengeResp": orchestratorStatisticsRxChallengeResp,
       "orchestratorStatisticsRxChallengeAck": orchestratorStatisticsRxChallengeAck,
       "orchestratorStatisticsChallengeFailures": orchestratorStatisticsChallengeFailures,
       "orchestratorLocalProperties": orchestratorLocalProperties,
       "orchestratorLocalPropertiesDeviceType": orchestratorLocalPropertiesDeviceType,
       "orchestratorLocalPropertiesOrganizationName": orchestratorLocalPropertiesOrganizationName,
       "orchestratorLocalPropertiesCertificateStatus": orchestratorLocalPropertiesCertificateStatus,
       "orchestratorLocalPropertiesRootCaChainStatus": orchestratorLocalPropertiesRootCaChainStatus,
       "orchestratorLocalPropertiesCertificateValidity": orchestratorLocalPropertiesCertificateValidity,
       "orchestratorLocalPropertiesCertificateNotValidBefore": orchestratorLocalPropertiesCertificateNotValidBefore,
       "orchestratorLocalPropertiesCertificateNotValidAfter": orchestratorLocalPropertiesCertificateNotValidAfter,
       "orchestratorLocalPropertiesUuid": orchestratorLocalPropertiesUuid,
       "orchestratorLocalPropertiesBoardSerial": orchestratorLocalPropertiesBoardSerial,
       "orchestratorLocalPropertiesNumberActiveWanInterfaces": orchestratorLocalPropertiesNumberActiveWanInterfaces,
       "orchestratorLocalPropertiesProtocol": orchestratorLocalPropertiesProtocol,
       "orchestratorLocalPropertiesWanInterfaceListTable": orchestratorLocalPropertiesWanInterfaceListTable,
       "orchestratorLocalPropertiesWanInterfaceListEntry": orchestratorLocalPropertiesWanInterfaceListEntry,
       "orchestratorLocalPropertiesWanInterfaceListIndex": orchestratorLocalPropertiesWanInterfaceListIndex,
       "orchestratorLocalPropertiesWanInterfaceListIp": orchestratorLocalPropertiesWanInterfaceListIp,
       "orchestratorLocalPropertiesWanInterfaceListPort": orchestratorLocalPropertiesWanInterfaceListPort,
       "orchestratorLocalPropertiesWanInterfaceListNumVsmarts": orchestratorLocalPropertiesWanInterfaceListNumVsmarts,
       "orchestratorLocalPropertiesWanInterfaceListNumVmanages": orchestratorLocalPropertiesWanInterfaceListNumVmanages,
       "orchestratorLocalPropertiesWanInterfaceListAdminState": orchestratorLocalPropertiesWanInterfaceListAdminState,
       "orchestratorLocalPropertiesWanInterfaceListOperationState": orchestratorLocalPropertiesWanInterfaceListOperationState,
       "orchestratorLocalPropertiesWanInterfaceListLastConnTime": orchestratorLocalPropertiesWanInterfaceListLastConnTime,
       "orchestratorLocalPropertiesWanInterfaceListInstance": orchestratorLocalPropertiesWanInterfaceListInstance,
       "orchestratorLocalPropertiesWanInterfaceListInterfaceAdminState": orchestratorLocalPropertiesWanInterfaceListInterfaceAdminState,
       "orchestratorLocalPropertiesWanInterfaceListInterfaceOperState": orchestratorLocalPropertiesWanInterfaceListInterfaceOperState,
       "orchestratorLocalPropertiesSystemIp": orchestratorLocalPropertiesSystemIp,
       "orchestratorLocalPropertiesVedgeListVersion": orchestratorLocalPropertiesVedgeListVersion,
       "orchestratorLocalPropertiesVsmartListVersion": orchestratorLocalPropertiesVsmartListVersion,
       "orchestratorLocalPropertiesSPOrganizationName": orchestratorLocalPropertiesSPOrganizationName,
       "orchestratorValidVsmartsTable": orchestratorValidVsmartsTable,
       "orchestratorValidVsmartsEntry": orchestratorValidVsmartsEntry,
       "orchestratorValidVsmartsSerialNumber": orchestratorValidVsmartsSerialNumber,
       "orchestratorValidVsmartsOrg": orchestratorValidVsmartsOrg,
       "orchestratorValidVedgesTable": orchestratorValidVedgesTable,
       "orchestratorValidVedgesEntry": orchestratorValidVedgesEntry,
       "orchestratorValidVedgesChassisNumber": orchestratorValidVedgesChassisNumber,
       "orchestratorValidVedgesSerialNumber": orchestratorValidVedgesSerialNumber,
       "orchestratorValidVedgesValidity": orchestratorValidVedgesValidity,
       "orchestratorValidVedgesOrg": orchestratorValidVedgesOrg,
       "orchestratorValidVedgesInstalledSerialNumber": orchestratorValidVedgesInstalledSerialNumber,
       "orchestratorValidVedgesSubjectSerialNumber": orchestratorValidVedgesSubjectSerialNumber,
       "orchestratorSummaryTable": orchestratorSummaryTable,
       "orchestratorSummaryEntry": orchestratorSummaryEntry,
       "orchestratorSummaryInstance": orchestratorSummaryInstance,
       "orchestratorSummaryVmanageCounts": orchestratorSummaryVmanageCounts,
       "orchestratorSummaryVsmartCounts": orchestratorSummaryVsmartCounts,
       "orchestratorSummaryVedgeCounts": orchestratorSummaryVedgeCounts,
       "orchestratorSummaryProtocol": orchestratorSummaryProtocol,
       "orchestratorSummaryListeningIp": orchestratorSummaryListeningIp,
       "orchestratorSummaryListeningPort": orchestratorSummaryListeningPort,
       "orchestratorSummaryListeningIpv6": orchestratorSummaryListeningIpv6,
       "orchestratorSummaryValidControllerCounts": orchestratorSummaryValidControllerCounts,
       "orchestratorValidVmanageIdTable": orchestratorValidVmanageIdTable,
       "orchestratorValidVmanageIdEntry": orchestratorValidVmanageIdEntry,
       "orchestratorValidVManageIdChassisNumbers": orchestratorValidVManageIdChassisNumbers,
       "orchestratorReverseProxyMappingTable": orchestratorReverseProxyMappingTable,
       "orchestratorReverseProxyMapping": orchestratorReverseProxyMapping,
       "orchestratorReverseProxyMappingUuid": orchestratorReverseProxyMappingUuid,
       "orchestratorReverseProxyMappingPrivateIp": orchestratorReverseProxyMappingPrivateIp,
       "orchestratorReverseProxyMappingPrivatePort": orchestratorReverseProxyMappingPrivatePort,
       "orchestratorReverseProxyMappingProxyIp": orchestratorReverseProxyMappingProxyIp,
       "orchestratorReverseProxyMappingProxyPort": orchestratorReverseProxyMappingProxyPort,
       "orchestratorUnclaimedVedgesTable": orchestratorUnclaimedVedgesTable,
       "orchestratorUnclaimedVedgesEntry": orchestratorUnclaimedVedgesEntry,
       "orchestratorUnclaimedVedgesChassisNumber": orchestratorUnclaimedVedgesChassisNumber,
       "orchestratorUnclaimedVedgesSerialNumber": orchestratorUnclaimedVedgesSerialNumber,
       "orchestratorUnclaimedVedgesSubjectSerialNumber": orchestratorUnclaimedVedgesSubjectSerialNumber,
       "orchestratorUnclaimedVedgesOrg": orchestratorUnclaimedVedgesOrg,
       "ipsec": ipsec,
       "ipsecLocalSaTable": ipsecLocalSaTable,
       "ipsecLocalSaEntry": ipsecLocalSaEntry,
       "ipsecLocalSaTlocAddress": ipsecLocalSaTlocAddress,
       "ipsecLocalSaTlocColor": ipsecLocalSaTlocColor,
       "ipsecLocalSaSpi": ipsecLocalSaSpi,
       "ipsecLocalSaTlocIndex": ipsecLocalSaTlocIndex,
       "ipsecLocalSaIp": ipsecLocalSaIp,
       "ipsecLocalSaPort": ipsecLocalSaPort,
       "ipsecLocalSaEncryptKeyHash": ipsecLocalSaEncryptKeyHash,
       "ipsecLocalSaAuthKeyHash": ipsecLocalSaAuthKeyHash,
       "ipsecLocalSaIpv6": ipsecLocalSaIpv6,
       "ipsecInboundConnectionsTable": ipsecInboundConnectionsTable,
       "ipsecInboundConnectionsEntry": ipsecInboundConnectionsEntry,
       "ipsecInboundConnectionsLocalTlocAddress": ipsecInboundConnectionsLocalTlocAddress,
       "ipsecInboundConnectionsLocalTlocColor": ipsecInboundConnectionsLocalTlocColor,
       "ipsecInboundConnectionsRemoteTlocAddress": ipsecInboundConnectionsRemoteTlocAddress,
       "ipsecInboundConnectionsRemoteTlocColor": ipsecInboundConnectionsRemoteTlocColor,
       "ipsecInboundConnectionsLocalTlocIndex": ipsecInboundConnectionsLocalTlocIndex,
       "ipsecInboundConnectionsRemoteTlocIndex": ipsecInboundConnectionsRemoteTlocIndex,
       "ipsecInboundConnectionsSourceIp": ipsecInboundConnectionsSourceIp,
       "ipsecInboundConnectionsSourcePort": ipsecInboundConnectionsSourcePort,
       "ipsecInboundConnectionsDestIp": ipsecInboundConnectionsDestIp,
       "ipsecInboundConnectionsDestPort": ipsecInboundConnectionsDestPort,
       "ipsecInboundConnectionsNegotiatedEncryptionAlgo": ipsecInboundConnectionsNegotiatedEncryptionAlgo,
       "ipsecInboundConnectionsTcSpiPerTun": ipsecInboundConnectionsTcSpiPerTun,
       "ipsecInboundConnectionsPkeyHash": ipsecInboundConnectionsPkeyHash,
       "ipsecInboundConnectionsPeerSpi": ipsecInboundConnectionsPeerSpi,
       "ipsecOutboundConnectionsTable": ipsecOutboundConnectionsTable,
       "ipsecOutboundConnectionsEntry": ipsecOutboundConnectionsEntry,
       "ipsecOutboundConnectionsSourceIp": ipsecOutboundConnectionsSourceIp,
       "ipsecOutboundConnectionsSourcePort": ipsecOutboundConnectionsSourcePort,
       "ipsecOutboundConnectionsDestIp": ipsecOutboundConnectionsDestIp,
       "ipsecOutboundConnectionsDestPort": ipsecOutboundConnectionsDestPort,
       "ipsecOutboundConnectionsSpi": ipsecOutboundConnectionsSpi,
       "ipsecOutboundConnectionsTlocIndex": ipsecOutboundConnectionsTlocIndex,
       "ipsecOutboundConnectionsTunnelMtu": ipsecOutboundConnectionsTunnelMtu,
       "ipsecOutboundConnectionsRemoteTlocAddress": ipsecOutboundConnectionsRemoteTlocAddress,
       "ipsecOutboundConnectionsRemoteTlocColor": ipsecOutboundConnectionsRemoteTlocColor,
       "ipsecOutboundConnectionsAuthenticationUsed": ipsecOutboundConnectionsAuthenticationUsed,
       "ipsecOutboundConnectionsEncryptKeyHash": ipsecOutboundConnectionsEncryptKeyHash,
       "ipsecOutboundConnectionsAuthKeyHash": ipsecOutboundConnectionsAuthKeyHash,
       "ipsecOutboundConnectionsNegotiatedAlgo": ipsecOutboundConnectionsNegotiatedAlgo,
       "ipsecOutboundConnectionsTcSpiPerTun": ipsecOutboundConnectionsTcSpiPerTun,
       "ipsecOutboundConnectionsPkeyHash": ipsecOutboundConnectionsPkeyHash,
       "ipsecOutboundConnectionsPeerSpi": ipsecOutboundConnectionsPeerSpi,
       "ipsecOutboundConnectionsLocalTlocAddress": ipsecOutboundConnectionsLocalTlocAddress,
       "ipsecOutboundConnectionsLocalTlocColor": ipsecOutboundConnectionsLocalTlocColor,
       "ipsecIke": ipsecIke,
       "ipsecIkeInboundConnectionsTable": ipsecIkeInboundConnectionsTable,
       "ipsecIkeInboundConnectionsEntry": ipsecIkeInboundConnectionsEntry,
       "ipsecIkeInboundConnectionsSourceIp": ipsecIkeInboundConnectionsSourceIp,
       "ipsecIkeInboundConnectionsSourcePort": ipsecIkeInboundConnectionsSourcePort,
       "ipsecIkeInboundConnectionsDestIp": ipsecIkeInboundConnectionsDestIp,
       "ipsecIkeInboundConnectionsDestPort": ipsecIkeInboundConnectionsDestPort,
       "ipsecIkeInboundConnectionsNewSpi": ipsecIkeInboundConnectionsNewSpi,
       "ipsecIkeInboundConnectionsOldSpi": ipsecIkeInboundConnectionsOldSpi,
       "ipsecIkeInboundConnectionsCipherSuite": ipsecIkeInboundConnectionsCipherSuite,
       "ipsecIkeInboundConnectionsNewKeyHash": ipsecIkeInboundConnectionsNewKeyHash,
       "ipsecIkeInboundConnectionsOldKeyHash": ipsecIkeInboundConnectionsOldKeyHash,
       "ipsecIkeInboundConnectionsExtSeq": ipsecIkeInboundConnectionsExtSeq,
       "ipsecIkeOutboundConnectionsTable": ipsecIkeOutboundConnectionsTable,
       "ipsecIkeOutboundConnectionsEntry": ipsecIkeOutboundConnectionsEntry,
       "ipsecIkeOutboundConnectionsSourceIp": ipsecIkeOutboundConnectionsSourceIp,
       "ipsecIkeOutboundConnectionsSourcePort": ipsecIkeOutboundConnectionsSourcePort,
       "ipsecIkeOutboundConnectionsDestIp": ipsecIkeOutboundConnectionsDestIp,
       "ipsecIkeOutboundConnectionsDestPort": ipsecIkeOutboundConnectionsDestPort,
       "ipsecIkeOutboundConnectionsSpi": ipsecIkeOutboundConnectionsSpi,
       "ipsecIkeOutboundConnectionsCipherSuite": ipsecIkeOutboundConnectionsCipherSuite,
       "ipsecIkeOutboundConnectionsKeyHash": ipsecIkeOutboundConnectionsKeyHash,
       "ipsecIkeOutboundConnectionsTunnelMtu": ipsecIkeOutboundConnectionsTunnelMtu,
       "ipsecIkeOutboundConnectionsExtSeq": ipsecIkeOutboundConnectionsExtSeq,
       "ipsecIkeSessionsTable": ipsecIkeSessionsTable,
       "ipsecIkeSessionsEntry": ipsecIkeSessionsEntry,
       "ipsecIkeSessionsVpnId": ipsecIkeSessionsVpnId,
       "ipsecIkeSessionsIfName": ipsecIkeSessionsIfName,
       "ipsecIkeSessionsVersion": ipsecIkeSessionsVersion,
       "ipsecIkeSessionsSourceIp": ipsecIkeSessionsSourceIp,
       "ipsecIkeSessionsSourcePort": ipsecIkeSessionsSourcePort,
       "ipsecIkeSessionsDestIp": ipsecIkeSessionsDestIp,
       "ipsecIkeSessionsDestPort": ipsecIkeSessionsDestPort,
       "ipsecIkeSessionsInitiatorSpi": ipsecIkeSessionsInitiatorSpi,
       "ipsecIkeSessionsResponderSpi": ipsecIkeSessionsResponderSpi,
       "ipsecIkeSessionsCipherSuite": ipsecIkeSessionsCipherSuite,
       "ipsecIkeSessionsDhGroup": ipsecIkeSessionsDhGroup,
       "ipsecIkeSessionsState": ipsecIkeSessionsState,
       "ipsecIkeSessionsUptime": ipsecIkeSessionsUptime,
       "ipsecIkeSessionsTunnelUptime": ipsecIkeSessionsTunnelUptime,
       "tunnel": tunnel,
       "tunnelStatisticsTable": tunnelStatisticsTable,
       "tunnelStatisticsEntry": tunnelStatisticsEntry,
       "tunnelStatisticsTunnelProtocol": tunnelStatisticsTunnelProtocol,
       "tunnelStatisticsSourceIp": tunnelStatisticsSourceIp,
       "tunnelStatisticsDestIp": tunnelStatisticsDestIp,
       "tunnelStatisticsSourcePort": tunnelStatisticsSourcePort,
       "tunnelStatisticsDestPort": tunnelStatisticsDestPort,
       "tunnelStatisticsSystemIp": tunnelStatisticsSystemIp,
       "tunnelStatisticsLocalColor": tunnelStatisticsLocalColor,
       "tunnelStatisticsRemoteColor": tunnelStatisticsRemoteColor,
       "tunnelStatisticsTunnelMtu": tunnelStatisticsTunnelMtu,
       "tunnelStatisticsTxPkts": tunnelStatisticsTxPkts,
       "tunnelStatisticsTxOctets": tunnelStatisticsTxOctets,
       "tunnelStatisticsRxPkts": tunnelStatisticsRxPkts,
       "tunnelStatisticsRxOctets": tunnelStatisticsRxOctets,
       "tunnelStatisticsIpsecDecryptInbound": tunnelStatisticsIpsecDecryptInbound,
       "tunnelStatisticsIpsecRxAuthFailures": tunnelStatisticsIpsecRxAuthFailures,
       "tunnelStatisticsIpsecRxFailures": tunnelStatisticsIpsecRxFailures,
       "tunnelStatisticsIpsecEncryptOutbound": tunnelStatisticsIpsecEncryptOutbound,
       "tunnelStatisticsIpsecTxAuthFailures": tunnelStatisticsIpsecTxAuthFailures,
       "tunnelStatisticsIpsecTxFailures": tunnelStatisticsIpsecTxFailures,
       "tunnelStatisticsTcpMssAdjust": tunnelStatisticsTcpMssAdjust,
       "tunnelStatisticsBfdTxPkts": tunnelStatisticsBfdTxPkts,
       "tunnelStatisticsBfdRxPkts": tunnelStatisticsBfdRxPkts,
       "tunnelStatisticsBfdTxOctets": tunnelStatisticsBfdTxOctets,
       "tunnelStatisticsBfdRxOctets": tunnelStatisticsBfdRxOctets,
       "tunnelStatisticsPmtuTxPkts": tunnelStatisticsPmtuTxPkts,
       "tunnelStatisticsPmtuRxPkts": tunnelStatisticsPmtuRxPkts,
       "tunnelStatisticsPmtuTxOctets": tunnelStatisticsPmtuTxOctets,
       "tunnelStatisticsPmtuRxOctets": tunnelStatisticsPmtuRxOctets,
       "tunnelStatisticsFecRxDataPkts": tunnelStatisticsFecRxDataPkts,
       "tunnelStatisticsFecRxParityPkts": tunnelStatisticsFecRxParityPkts,
       "tunnelStatisticsFecTxDataPkts": tunnelStatisticsFecTxDataPkts,
       "tunnelStatisticsFecTxParityPkts": tunnelStatisticsFecTxParityPkts,
       "tunnelStatisticsFecReconstructPkts": tunnelStatisticsFecReconstructPkts,
       "tunnelStatisticsFecCapable": tunnelStatisticsFecCapable,
       "tunnelStatisticsFecDynamic": tunnelStatisticsFecDynamic,
       "tunnelStatisticsPktDupRxPkts": tunnelStatisticsPktDupRxPkts,
       "tunnelStatisticsPktDupRxOtherPkts": tunnelStatisticsPktDupRxOtherPkts,
       "tunnelStatisticsPktDupRxThisPkts": tunnelStatisticsPktDupRxThisPkts,
       "tunnelStatisticsPktDupTxPkts": tunnelStatisticsPktDupTxPkts,
       "tunnelStatisticsPktDupTxOtherPkts": tunnelStatisticsPktDupTxOtherPkts,
       "tunnelStatisticsPktDupCapable": tunnelStatisticsPktDupCapable,
       "tunnelGreKeepalivesTable": tunnelGreKeepalivesTable,
       "tunnelGreKeepalivesEntry": tunnelGreKeepalivesEntry,
       "tunnelGreKeepalivesVpnId": tunnelGreKeepalivesVpnId,
       "tunnelGreKeepalivesIfName": tunnelGreKeepalivesIfName,
       "tunnelGreKeepalivesSourceIp": tunnelGreKeepalivesSourceIp,
       "tunnelGreKeepalivesDestIp": tunnelGreKeepalivesDestIp,
       "tunnelGreKeepalivesAdminState": tunnelGreKeepalivesAdminState,
       "tunnelGreKeepalivesOperState": tunnelGreKeepalivesOperState,
       "tunnelGreKeepalivesKaEnabled": tunnelGreKeepalivesKaEnabled,
       "tunnelGreKeepalivesRemoteTxPackets": tunnelGreKeepalivesRemoteTxPackets,
       "tunnelGreKeepalivesRemoteRxPackets": tunnelGreKeepalivesRemoteRxPackets,
       "tunnelGreKeepalivesTxPackets": tunnelGreKeepalivesTxPackets,
       "tunnelGreKeepalivesRxPackets": tunnelGreKeepalivesRxPackets,
       "tunnelGreKeepalivesTxErrors": tunnelGreKeepalivesTxErrors,
       "tunnelGreKeepalivesRxErrors": tunnelGreKeepalivesRxErrors,
       "tunnelGreKeepalivesBaseIfOperStatus": tunnelGreKeepalivesBaseIfOperStatus,
       "tunnelGreKeepalivesTransitions": tunnelGreKeepalivesTransitions,
       "securityInfo": securityInfo,
       "securityInfoAuthenticationType": securityInfoAuthenticationType,
       "securityInfoRekey": securityInfoRekey,
       "securityInfoReplayWindow": securityInfoReplayWindow,
       "securityInfoEncryptionSupported": securityInfoEncryptionSupported,
       "securityInfoFipsMode": securityInfoFipsMode,
       "securityInfoPairwiseKeying": securityInfoPairwiseKeying,
       "ztp": ztp,
       "ztpEntriesTable": ztpEntriesTable,
       "ztpEntriesEntry": ztpEntriesEntry,
       "ztpEntriesIndex": ztpEntriesIndex,
       "ztpEntriesChassisNumber": ztpEntriesChassisNumber,
       "ztpEntriesSerialNumber": ztpEntriesSerialNumber,
       "ztpEntriesValidity": ztpEntriesValidity,
       "ztpEntriesVbondIp": ztpEntriesVbondIp,
       "ztpEntriesVbondPort": ztpEntriesVbondPort,
       "ztpEntriesOrganizationName": ztpEntriesOrganizationName,
       "ztpEntriesRootCertPath": ztpEntriesRootCertPath}
)
