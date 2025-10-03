# SNMP MIB module (DASAN-ACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-ACCESS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:52 2025
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

(dasanMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "dasanMgmt")

(Unsigned32,) = mibBuilder.importSymbols(
    "DASAN-TC",
    "Unsigned32")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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
 iso,
 mib_2) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp")


# MODULE-IDENTITY

dasanAccessMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100)
)
if mibBuilder.loadTexts:
    dasanAccessMib.setRevisions(
        ("2005-02-11 21:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DasanAccessGatewayMIBObjects_ObjectIdentity = ObjectIdentity
dasanAccessGatewayMIBObjects = _DasanAccessGatewayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1)
)
_DsAccGwyConfiguration_ObjectIdentity = ObjectIdentity
dsAccGwyConfiguration = _DsAccGwyConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1)
)
_DsAccGwyConfigMgcp_ObjectIdentity = ObjectIdentity
dsAccGwyConfigMgcp = _DsAccGwyConfigMgcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2)
)


class _DsMgcpAddAreaCode_Type(Integer32):
    """Custom type dsMgcpAddAreaCode based on Integer32"""
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


_DsMgcpAddAreaCode_Type.__name__ = "Integer32"
_DsMgcpAddAreaCode_Object = MibScalar
dsMgcpAddAreaCode = _DsMgcpAddAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 1),
    _DsMgcpAddAreaCode_Type()
)
dsMgcpAddAreaCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpAddAreaCode.setStatus("current")


class _DsMgcpAreaCode_Type(DisplayString):
    """Custom type dsMgcpAreaCode based on DisplayString"""
    defaultValue = OctetString("")


_DsMgcpAreaCode_Type.__name__ = "DisplayString"
_DsMgcpAreaCode_Object = MibScalar
dsMgcpAreaCode = _DsMgcpAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 2),
    _DsMgcpAreaCode_Type()
)
dsMgcpAreaCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpAreaCode.setStatus("current")


class _DsMgcpAreaCodeAllows_Type(DisplayString):
    """Custom type dsMgcpAreaCodeAllows based on DisplayString"""
    defaultValue = OctetString("")


_DsMgcpAreaCodeAllows_Type.__name__ = "DisplayString"
_DsMgcpAreaCodeAllows_Object = MibScalar
dsMgcpAreaCodeAllows = _DsMgcpAreaCodeAllows_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 3),
    _DsMgcpAreaCodeAllows_Type()
)
dsMgcpAreaCodeAllows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpAreaCodeAllows.setStatus("current")


class _DsMgcpAreaCodeExceptions_Type(DisplayString):
    """Custom type dsMgcpAreaCodeExceptions based on DisplayString"""
    defaultValue = OctetString("")


_DsMgcpAreaCodeExceptions_Type.__name__ = "DisplayString"
_DsMgcpAreaCodeExceptions_Object = MibScalar
dsMgcpAreaCodeExceptions = _DsMgcpAreaCodeExceptions_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 4),
    _DsMgcpAreaCodeExceptions_Type()
)
dsMgcpAreaCodeExceptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpAreaCodeExceptions.setStatus("current")


class _DsMgcpCallTrace_Type(DisplayString):
    """Custom type dsMgcpCallTrace based on DisplayString"""
    defaultValue = OctetString("")


_DsMgcpCallTrace_Type.__name__ = "DisplayString"
_DsMgcpCallTrace_Object = MibScalar
dsMgcpCallTrace = _DsMgcpCallTrace_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 5),
    _DsMgcpCallTrace_Type()
)
dsMgcpCallTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCallTrace.setStatus("current")


class _DsMgcpEncodePackageName_Type(Integer32):
    """Custom type dsMgcpEncodePackageName based on Integer32"""
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


_DsMgcpEncodePackageName_Type.__name__ = "Integer32"
_DsMgcpEncodePackageName_Object = MibScalar
dsMgcpEncodePackageName = _DsMgcpEncodePackageName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 6),
    _DsMgcpEncodePackageName_Type()
)
dsMgcpEncodePackageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpEncodePackageName.setStatus("current")
_DsMgcpRetransmitStartTimeout_Type = Integer32
_DsMgcpRetransmitStartTimeout_Object = MibScalar
dsMgcpRetransmitStartTimeout = _DsMgcpRetransmitStartTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 7),
    _DsMgcpRetransmitStartTimeout_Type()
)
dsMgcpRetransmitStartTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpRetransmitStartTimeout.setStatus("current")
_DsMgcpRetransmitMaxTimeout_Type = Integer32
_DsMgcpRetransmitMaxTimeout_Object = MibScalar
dsMgcpRetransmitMaxTimeout = _DsMgcpRetransmitMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 8),
    _DsMgcpRetransmitMaxTimeout_Type()
)
dsMgcpRetransmitMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpRetransmitMaxTimeout.setStatus("current")
_DsMgcpRetransmitMax1_Type = Integer32
_DsMgcpRetransmitMax1_Object = MibScalar
dsMgcpRetransmitMax1 = _DsMgcpRetransmitMax1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 11),
    _DsMgcpRetransmitMax1_Type()
)
dsMgcpRetransmitMax1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpRetransmitMax1.setStatus("current")
_DsMgcpRetransmitMax2_Type = Integer32
_DsMgcpRetransmitMax2_Object = MibScalar
dsMgcpRetransmitMax2 = _DsMgcpRetransmitMax2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 12),
    _DsMgcpRetransmitMax2_Type()
)
dsMgcpRetransmitMax2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpRetransmitMax2.setStatus("current")
_DsMgcpRestartMaxwait_Type = Integer32
_DsMgcpRestartMaxwait_Object = MibScalar
dsMgcpRestartMaxwait = _DsMgcpRestartMaxwait_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 13),
    _DsMgcpRestartMaxwait_Type()
)
dsMgcpRestartMaxwait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpRestartMaxwait.setStatus("current")
_DsMgcpDisconnectInit_Type = Integer32
_DsMgcpDisconnectInit_Object = MibScalar
dsMgcpDisconnectInit = _DsMgcpDisconnectInit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 14),
    _DsMgcpDisconnectInit_Type()
)
dsMgcpDisconnectInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpDisconnectInit.setStatus("current")
_DsMgcpDisconnectMin_Type = Integer32
_DsMgcpDisconnectMin_Object = MibScalar
dsMgcpDisconnectMin = _DsMgcpDisconnectMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 15),
    _DsMgcpDisconnectMin_Type()
)
dsMgcpDisconnectMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpDisconnectMin.setStatus("current")
_DsMgcpDisconnectMax_Type = Integer32
_DsMgcpDisconnectMax_Object = MibScalar
dsMgcpDisconnectMax = _DsMgcpDisconnectMax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 16),
    _DsMgcpDisconnectMax_Type()
)
dsMgcpDisconnectMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpDisconnectMax.setStatus("current")


class _DsMgcpCaAddr1_Type(DisplayString):
    """Custom type dsMgcpCaAddr1 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpCaAddr1_Type.__name__ = "DisplayString"
_DsMgcpCaAddr1_Object = MibScalar
dsMgcpCaAddr1 = _DsMgcpCaAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 17),
    _DsMgcpCaAddr1_Type()
)
dsMgcpCaAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaAddr1.setStatus("current")


class _DsMgcpCaAddr2_Type(DisplayString):
    """Custom type dsMgcpCaAddr2 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpCaAddr2_Type.__name__ = "DisplayString"
_DsMgcpCaAddr2_Object = MibScalar
dsMgcpCaAddr2 = _DsMgcpCaAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 18),
    _DsMgcpCaAddr2_Type()
)
dsMgcpCaAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaAddr2.setStatus("current")


class _DsMgcpCaAddr3_Type(DisplayString):
    """Custom type dsMgcpCaAddr3 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpCaAddr3_Type.__name__ = "DisplayString"
_DsMgcpCaAddr3_Object = MibScalar
dsMgcpCaAddr3 = _DsMgcpCaAddr3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 19),
    _DsMgcpCaAddr3_Type()
)
dsMgcpCaAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaAddr3.setStatus("current")


class _DsMgcpCaAddr4_Type(DisplayString):
    """Custom type dsMgcpCaAddr4 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpCaAddr4_Type.__name__ = "DisplayString"
_DsMgcpCaAddr4_Object = MibScalar
dsMgcpCaAddr4 = _DsMgcpCaAddr4_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 20),
    _DsMgcpCaAddr4_Type()
)
dsMgcpCaAddr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaAddr4.setStatus("current")


class _DsMgcpCaAddr5_Type(DisplayString):
    """Custom type dsMgcpCaAddr5 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpCaAddr5_Type.__name__ = "DisplayString"
_DsMgcpCaAddr5_Object = MibScalar
dsMgcpCaAddr5 = _DsMgcpCaAddr5_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 21),
    _DsMgcpCaAddr5_Type()
)
dsMgcpCaAddr5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaAddr5.setStatus("current")


class _DsMgcpCaAddr6_Type(DisplayString):
    """Custom type dsMgcpCaAddr6 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpCaAddr6_Type.__name__ = "DisplayString"
_DsMgcpCaAddr6_Object = MibScalar
dsMgcpCaAddr6 = _DsMgcpCaAddr6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 22),
    _DsMgcpCaAddr6_Type()
)
dsMgcpCaAddr6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaAddr6.setStatus("current")


class _DsMgcpCaAddr7_Type(DisplayString):
    """Custom type dsMgcpCaAddr7 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpCaAddr7_Type.__name__ = "DisplayString"
_DsMgcpCaAddr7_Object = MibScalar
dsMgcpCaAddr7 = _DsMgcpCaAddr7_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 23),
    _DsMgcpCaAddr7_Type()
)
dsMgcpCaAddr7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaAddr7.setStatus("current")


class _DsMgcpCaAddr8_Type(DisplayString):
    """Custom type dsMgcpCaAddr8 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpCaAddr8_Type.__name__ = "DisplayString"
_DsMgcpCaAddr8_Object = MibScalar
dsMgcpCaAddr8 = _DsMgcpCaAddr8_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 24),
    _DsMgcpCaAddr8_Type()
)
dsMgcpCaAddr8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaAddr8.setStatus("current")


class _DsMgcpCaPort1_Type(Integer32):
    """Custom type dsMgcpCaPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsMgcpCaPort1_Type.__name__ = "Integer32"
_DsMgcpCaPort1_Object = MibScalar
dsMgcpCaPort1 = _DsMgcpCaPort1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 25),
    _DsMgcpCaPort1_Type()
)
dsMgcpCaPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaPort1.setStatus("current")


class _DsMgcpCaPort2_Type(Integer32):
    """Custom type dsMgcpCaPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsMgcpCaPort2_Type.__name__ = "Integer32"
_DsMgcpCaPort2_Object = MibScalar
dsMgcpCaPort2 = _DsMgcpCaPort2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 26),
    _DsMgcpCaPort2_Type()
)
dsMgcpCaPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaPort2.setStatus("current")


class _DsMgcpCaPort3_Type(Integer32):
    """Custom type dsMgcpCaPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsMgcpCaPort3_Type.__name__ = "Integer32"
_DsMgcpCaPort3_Object = MibScalar
dsMgcpCaPort3 = _DsMgcpCaPort3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 27),
    _DsMgcpCaPort3_Type()
)
dsMgcpCaPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaPort3.setStatus("current")


class _DsMgcpCaPort4_Type(Integer32):
    """Custom type dsMgcpCaPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsMgcpCaPort4_Type.__name__ = "Integer32"
_DsMgcpCaPort4_Object = MibScalar
dsMgcpCaPort4 = _DsMgcpCaPort4_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 28),
    _DsMgcpCaPort4_Type()
)
dsMgcpCaPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaPort4.setStatus("current")


class _DsMgcpCaPort5_Type(Integer32):
    """Custom type dsMgcpCaPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsMgcpCaPort5_Type.__name__ = "Integer32"
_DsMgcpCaPort5_Object = MibScalar
dsMgcpCaPort5 = _DsMgcpCaPort5_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 29),
    _DsMgcpCaPort5_Type()
)
dsMgcpCaPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaPort5.setStatus("current")


class _DsMgcpCaPort6_Type(Integer32):
    """Custom type dsMgcpCaPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsMgcpCaPort6_Type.__name__ = "Integer32"
_DsMgcpCaPort6_Object = MibScalar
dsMgcpCaPort6 = _DsMgcpCaPort6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 30),
    _DsMgcpCaPort6_Type()
)
dsMgcpCaPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaPort6.setStatus("current")


class _DsMgcpCaPort7_Type(Integer32):
    """Custom type dsMgcpCaPort7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsMgcpCaPort7_Type.__name__ = "Integer32"
_DsMgcpCaPort7_Object = MibScalar
dsMgcpCaPort7 = _DsMgcpCaPort7_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 31),
    _DsMgcpCaPort7_Type()
)
dsMgcpCaPort7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaPort7.setStatus("current")


class _DsMgcpCaPort8_Type(Integer32):
    """Custom type dsMgcpCaPort8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsMgcpCaPort8_Type.__name__ = "Integer32"
_DsMgcpCaPort8_Object = MibScalar
dsMgcpCaPort8 = _DsMgcpCaPort8_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 32),
    _DsMgcpCaPort8_Type()
)
dsMgcpCaPort8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpCaPort8.setStatus("current")


class _DsMgcpMgAddr_Type(DisplayString):
    """Custom type dsMgcpMgAddr based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpMgAddr_Type.__name__ = "DisplayString"
_DsMgcpMgAddr_Object = MibScalar
dsMgcpMgAddr = _DsMgcpMgAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 33),
    _DsMgcpMgAddr_Type()
)
dsMgcpMgAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpMgAddr.setStatus("current")


class _DsMgcpMgPort_Type(Integer32):
    """Custom type dsMgcpMgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsMgcpMgPort_Type.__name__ = "Integer32"
_DsMgcpMgPort_Object = MibScalar
dsMgcpMgPort = _DsMgcpMgPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 34),
    _DsMgcpMgPort_Type()
)
dsMgcpMgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpMgPort.setStatus("current")
_DsMgcpStatus_Type = OctetString
_DsMgcpStatus_Object = MibScalar
dsMgcpStatus = _DsMgcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 35),
    _DsMgcpStatus_Type()
)
dsMgcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMgcpStatus.setStatus("current")
_DsMgcpEndpointIdTable_Object = MibTable
dsMgcpEndpointIdTable = _DsMgcpEndpointIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 50)
)
if mibBuilder.loadTexts:
    dsMgcpEndpointIdTable.setStatus("current")
_DsMgcpEndpointIdEntry_Object = MibTableRow
dsMgcpEndpointIdEntry = _DsMgcpEndpointIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 50, 1)
)
dsMgcpEndpointIdEntry.setIndexNames(
    (0, "DASAN-ACCESS-MIB", "dsMgcpEndpointIdIndex"),
)
if mibBuilder.loadTexts:
    dsMgcpEndpointIdEntry.setStatus("current")
_DsMgcpEndpointIdIndex_Type = Integer32
_DsMgcpEndpointIdIndex_Object = MibTableColumn
dsMgcpEndpointIdIndex = _DsMgcpEndpointIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 50, 1, 1),
    _DsMgcpEndpointIdIndex_Type()
)
dsMgcpEndpointIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMgcpEndpointIdIndex.setStatus("current")
_DsMgcpEndpointId_Type = OctetString
_DsMgcpEndpointId_Object = MibTableColumn
dsMgcpEndpointId = _DsMgcpEndpointId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 50, 1, 2),
    _DsMgcpEndpointId_Type()
)
dsMgcpEndpointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMgcpEndpointId.setStatus("current")
_DsMgcpTraceTable_Object = MibTable
dsMgcpTraceTable = _DsMgcpTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 51)
)
if mibBuilder.loadTexts:
    dsMgcpTraceTable.setStatus("current")
_DsMgcpTraceEntry_Object = MibTableRow
dsMgcpTraceEntry = _DsMgcpTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 51, 1)
)
dsMgcpTraceEntry.setIndexNames(
    (0, "DASAN-ACCESS-MIB", "dsMgcpTraceMessageIndex"),
)
if mibBuilder.loadTexts:
    dsMgcpTraceEntry.setStatus("current")
_DsMgcpTraceMessageIndex_Type = Integer32
_DsMgcpTraceMessageIndex_Object = MibTableColumn
dsMgcpTraceMessageIndex = _DsMgcpTraceMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 51, 1, 3),
    _DsMgcpTraceMessageIndex_Type()
)
dsMgcpTraceMessageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMgcpTraceMessageIndex.setStatus("current")
_DsMgcpTraceMessageTime_Type = DisplayString
_DsMgcpTraceMessageTime_Object = MibTableColumn
dsMgcpTraceMessageTime = _DsMgcpTraceMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 51, 1, 4),
    _DsMgcpTraceMessageTime_Type()
)
dsMgcpTraceMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMgcpTraceMessageTime.setStatus("current")


class _DsMgcpTraceMessageDirection_Type(Integer32):
    """Custom type dsMgcpTraceMessageDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("received", 0),
          ("sent", 1))
    )


_DsMgcpTraceMessageDirection_Type.__name__ = "Integer32"
_DsMgcpTraceMessageDirection_Object = MibTableColumn
dsMgcpTraceMessageDirection = _DsMgcpTraceMessageDirection_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 51, 1, 5),
    _DsMgcpTraceMessageDirection_Type()
)
dsMgcpTraceMessageDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMgcpTraceMessageDirection.setStatus("current")
_DsMgcpTraceMessageContent_Type = DisplayString
_DsMgcpTraceMessageContent_Object = MibTableColumn
dsMgcpTraceMessageContent = _DsMgcpTraceMessageContent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 2, 51, 1, 6),
    _DsMgcpTraceMessageContent_Type()
)
dsMgcpTraceMessageContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMgcpTraceMessageContent.setStatus("current")
_DsAccGwyConfigGlobal_ObjectIdentity = ObjectIdentity
dsAccGwyConfigGlobal = _DsAccGwyConfigGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 3)
)


class _DsAccGwyConfigGlobalDigitmap_Type(DisplayString):
    """Custom type dsAccGwyConfigGlobalDigitmap based on DisplayString"""
    defaultValue = OctetString("x.T")


_DsAccGwyConfigGlobalDigitmap_Type.__name__ = "DisplayString"
_DsAccGwyConfigGlobalDigitmap_Object = MibScalar
dsAccGwyConfigGlobalDigitmap = _DsAccGwyConfigGlobalDigitmap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 3, 1),
    _DsAccGwyConfigGlobalDigitmap_Type()
)
dsAccGwyConfigGlobalDigitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAccGwyConfigGlobalDigitmap.setStatus("current")


class _DsAccGwyConfigGlobalSwitchDhcp_Type(DisplayString):
    """Custom type dsAccGwyConfigGlobalSwitchDhcp based on DisplayString"""
    defaultValue = OctetString("off")


_DsAccGwyConfigGlobalSwitchDhcp_Type.__name__ = "DisplayString"
_DsAccGwyConfigGlobalSwitchDhcp_Object = MibScalar
dsAccGwyConfigGlobalSwitchDhcp = _DsAccGwyConfigGlobalSwitchDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 3, 2),
    _DsAccGwyConfigGlobalSwitchDhcp_Type()
)
dsAccGwyConfigGlobalSwitchDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAccGwyConfigGlobalSwitchDhcp.setStatus("current")
_DsAccGwyUpsStatus_Type = DisplayString
_DsAccGwyUpsStatus_Object = MibScalar
dsAccGwyUpsStatus = _DsAccGwyUpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 3, 3),
    _DsAccGwyUpsStatus_Type()
)
dsAccGwyUpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAccGwyUpsStatus.setStatus("current")
_DsAccGwyAutoConfigServer_Type = IpAddress
_DsAccGwyAutoConfigServer_Object = MibScalar
dsAccGwyAutoConfigServer = _DsAccGwyAutoConfigServer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 3, 4),
    _DsAccGwyAutoConfigServer_Type()
)
dsAccGwyAutoConfigServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAccGwyAutoConfigServer.setStatus("current")
_DsAccGwyAutoUpgradeServer_Type = IpAddress
_DsAccGwyAutoUpgradeServer_Object = MibScalar
dsAccGwyAutoUpgradeServer = _DsAccGwyAutoUpgradeServer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 3, 5),
    _DsAccGwyAutoUpgradeServer_Type()
)
dsAccGwyAutoUpgradeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAccGwyAutoUpgradeServer.setStatus("current")
_DsAccGwyConfigSlot_ObjectIdentity = ObjectIdentity
dsAccGwyConfigSlot = _DsAccGwyConfigSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4)
)
_DsAccGwyConfigSlotTable_Object = MibTable
dsAccGwyConfigSlotTable = _DsAccGwyConfigSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dsAccGwyConfigSlotTable.setStatus("current")
_DsAccGwyConfigSlotEntry_Object = MibTableRow
dsAccGwyConfigSlotEntry = _DsAccGwyConfigSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1)
)
dsAccGwyConfigSlotEntry.setIndexNames(
    (0, "DASAN-ACCESS-MIB", "dsAccSlotIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyConfigSlotEntry.setStatus("current")
_DsAccSlotIndex_Type = Integer32
_DsAccSlotIndex_Object = MibTableColumn
dsAccSlotIndex = _DsAccSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 1),
    _DsAccSlotIndex_Type()
)
dsAccSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAccSlotIndex.setStatus("current")


class _DsSlotCodecType_Type(DisplayString):
    """Custom type dsSlotCodecType based on DisplayString"""
    defaultValue = OctetString("")


_DsSlotCodecType_Type.__name__ = "DisplayString"
_DsSlotCodecType_Object = MibTableColumn
dsSlotCodecType = _DsSlotCodecType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 2),
    _DsSlotCodecType_Type()
)
dsSlotCodecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotCodecType.setStatus("current")


class _DsSlotCodecPacketizationPeriodG711_Type(Integer32):
    """Custom type dsSlotCodecPacketizationPeriodG711 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("p10", 10),
          ("p20", 20),
          ("p30", 30))
    )


_DsSlotCodecPacketizationPeriodG711_Type.__name__ = "Integer32"
_DsSlotCodecPacketizationPeriodG711_Object = MibTableColumn
dsSlotCodecPacketizationPeriodG711 = _DsSlotCodecPacketizationPeriodG711_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 3),
    _DsSlotCodecPacketizationPeriodG711_Type()
)
dsSlotCodecPacketizationPeriodG711.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotCodecPacketizationPeriodG711.setStatus("current")


class _DsSlotCodecPacketizationPeriodG723_Type(Integer32):
    """Custom type dsSlotCodecPacketizationPeriodG723 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(30,
              60)
        )
    )
    namedValues = NamedValues(
        *(("p30", 30),
          ("p60", 60))
    )


_DsSlotCodecPacketizationPeriodG723_Type.__name__ = "Integer32"
_DsSlotCodecPacketizationPeriodG723_Object = MibTableColumn
dsSlotCodecPacketizationPeriodG723 = _DsSlotCodecPacketizationPeriodG723_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 4),
    _DsSlotCodecPacketizationPeriodG723_Type()
)
dsSlotCodecPacketizationPeriodG723.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotCodecPacketizationPeriodG723.setStatus("current")


class _DsSlotCodecPacketizationPeriodG729_Type(Integer32):
    """Custom type dsSlotCodecPacketizationPeriodG729 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("p10", 10),
          ("p20", 20),
          ("p30", 30))
    )


_DsSlotCodecPacketizationPeriodG729_Type.__name__ = "Integer32"
_DsSlotCodecPacketizationPeriodG729_Object = MibTableColumn
dsSlotCodecPacketizationPeriodG729 = _DsSlotCodecPacketizationPeriodG729_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 5),
    _DsSlotCodecPacketizationPeriodG729_Type()
)
dsSlotCodecPacketizationPeriodG729.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotCodecPacketizationPeriodG729.setStatus("current")


class _DsSlotJitterbuffer_Type(DisplayString):
    """Custom type dsSlotJitterbuffer based on DisplayString"""
    defaultValue = OctetString("dynamic 20 200 20")


_DsSlotJitterbuffer_Type.__name__ = "DisplayString"
_DsSlotJitterbuffer_Object = MibTableColumn
dsSlotJitterbuffer = _DsSlotJitterbuffer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 6),
    _DsSlotJitterbuffer_Type()
)
dsSlotJitterbuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSlotJitterbuffer.setStatus("current")


class _DsSlotRingonTime_Type(Integer32):
    """Custom type dsSlotRingonTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1000),
    )


_DsSlotRingonTime_Type.__name__ = "Integer32"
_DsSlotRingonTime_Object = MibTableColumn
dsSlotRingonTime = _DsSlotRingonTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 9),
    _DsSlotRingonTime_Type()
)
dsSlotRingonTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotRingonTime.setStatus("current")


class _DsSlotRingoffTime_Type(Integer32):
    """Custom type dsSlotRingoffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2000),
    )


_DsSlotRingoffTime_Type.__name__ = "Integer32"
_DsSlotRingoffTime_Object = MibTableColumn
dsSlotRingoffTime = _DsSlotRingoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 10),
    _DsSlotRingoffTime_Type()
)
dsSlotRingoffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotRingoffTime.setStatus("current")


class _DsSlotHookflashMin_Type(Integer32):
    """Custom type dsSlotHookflashMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 600),
    )


_DsSlotHookflashMin_Type.__name__ = "Integer32"
_DsSlotHookflashMin_Object = MibTableColumn
dsSlotHookflashMin = _DsSlotHookflashMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 11),
    _DsSlotHookflashMin_Type()
)
dsSlotHookflashMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotHookflashMin.setStatus("current")


class _DsSlotHookflashMax_Type(Integer32):
    """Custom type dsSlotHookflashMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_DsSlotHookflashMax_Type.__name__ = "Integer32"
_DsSlotHookflashMax_Object = MibTableColumn
dsSlotHookflashMax = _DsSlotHookflashMax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 12),
    _DsSlotHookflashMax_Type()
)
dsSlotHookflashMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotHookflashMax.setStatus("current")


class _DsSlotInterdigitTimeout_Type(Integer32):
    """Custom type dsSlotInterdigitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_DsSlotInterdigitTimeout_Type.__name__ = "Integer32"
_DsSlotInterdigitTimeout_Object = MibTableColumn
dsSlotInterdigitTimeout = _DsSlotInterdigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 13),
    _DsSlotInterdigitTimeout_Type()
)
dsSlotInterdigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotInterdigitTimeout.setStatus("current")


class _DsSlotEce_Type(DisplayString):
    """Custom type dsSlotEce based on DisplayString"""
    defaultValue = OctetString("on 15")


_DsSlotEce_Type.__name__ = "DisplayString"
_DsSlotEce_Object = MibTableColumn
dsSlotEce = _DsSlotEce_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 14),
    _DsSlotEce_Type()
)
dsSlotEce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSlotEce.setStatus("current")


class _DsSlotFax_Type(Integer32):
    """Custom type dsSlotFax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("t30", 1),
          ("t38", 2))
    )


_DsSlotFax_Type.__name__ = "Integer32"
_DsSlotFax_Object = MibTableColumn
dsSlotFax = _DsSlotFax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 15),
    _DsSlotFax_Type()
)
dsSlotFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotFax.setStatus("current")


class _DsSlotCid_Type(Integer32):
    """Custom type dsSlotCid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("belcore", 1),
          ("ntt", 2))
    )


_DsSlotCid_Type.__name__ = "Integer32"
_DsSlotCid_Object = MibTableColumn
dsSlotCid = _DsSlotCid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 16),
    _DsSlotCid_Type()
)
dsSlotCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotCid.setStatus("current")


class _DsSlotVad_Type(Integer32):
    """Custom type dsSlotVad based on Integer32"""
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


_DsSlotVad_Type.__name__ = "Integer32"
_DsSlotVad_Object = MibTableColumn
dsSlotVad = _DsSlotVad_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 17),
    _DsSlotVad_Type()
)
dsSlotVad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotVad.setStatus("current")


class _DsSlotCng_Type(Integer32):
    """Custom type dsSlotCng based on Integer32"""
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


_DsSlotCng_Type.__name__ = "Integer32"
_DsSlotCng_Object = MibTableColumn
dsSlotCng = _DsSlotCng_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 18),
    _DsSlotCng_Type()
)
dsSlotCng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotCng.setStatus("current")


class _DsSlotOobdtmf_Type(Integer32):
    """Custom type dsSlotOobdtmf based on Integer32"""
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


_DsSlotOobdtmf_Type.__name__ = "Integer32"
_DsSlotOobdtmf_Object = MibTableColumn
dsSlotOobdtmf = _DsSlotOobdtmf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 19),
    _DsSlotOobdtmf_Type()
)
dsSlotOobdtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotOobdtmf.setStatus("current")


class _DsSlotNetworkHostname_Type(DisplayString):
    """Custom type dsSlotNetworkHostname based on DisplayString"""
    defaultValue = OctetString("access")


_DsSlotNetworkHostname_Type.__name__ = "DisplayString"
_DsSlotNetworkHostname_Object = MibTableColumn
dsSlotNetworkHostname = _DsSlotNetworkHostname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 20),
    _DsSlotNetworkHostname_Type()
)
dsSlotNetworkHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSlotNetworkHostname.setStatus("current")


class _DsSlotNetworkDhcp_Type(Integer32):
    """Custom type dsSlotNetworkDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("on-syslog", 2))
    )


_DsSlotNetworkDhcp_Type.__name__ = "Integer32"
_DsSlotNetworkDhcp_Object = MibTableColumn
dsSlotNetworkDhcp = _DsSlotNetworkDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 21),
    _DsSlotNetworkDhcp_Type()
)
dsSlotNetworkDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotNetworkDhcp.setStatus("current")


class _DsSlotNetworkIpaddress_Type(DisplayString):
    """Custom type dsSlotNetworkIpaddress based on DisplayString"""
    defaultValue = OctetString("192.168.1.2")


_DsSlotNetworkIpaddress_Type.__name__ = "DisplayString"
_DsSlotNetworkIpaddress_Object = MibTableColumn
dsSlotNetworkIpaddress = _DsSlotNetworkIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 22),
    _DsSlotNetworkIpaddress_Type()
)
dsSlotNetworkIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotNetworkIpaddress.setStatus("current")


class _DsSlotNetworkSubnetmask_Type(DisplayString):
    """Custom type dsSlotNetworkSubnetmask based on DisplayString"""
    defaultValue = OctetString("255.255.255.0")


_DsSlotNetworkSubnetmask_Type.__name__ = "DisplayString"
_DsSlotNetworkSubnetmask_Object = MibTableColumn
dsSlotNetworkSubnetmask = _DsSlotNetworkSubnetmask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 23),
    _DsSlotNetworkSubnetmask_Type()
)
dsSlotNetworkSubnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotNetworkSubnetmask.setStatus("current")


class _DsSlotNetworkRouter_Type(DisplayString):
    """Custom type dsSlotNetworkRouter based on DisplayString"""
    defaultValue = OctetString("192.168.1.1")


_DsSlotNetworkRouter_Type.__name__ = "DisplayString"
_DsSlotNetworkRouter_Object = MibTableColumn
dsSlotNetworkRouter = _DsSlotNetworkRouter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 24),
    _DsSlotNetworkRouter_Type()
)
dsSlotNetworkRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotNetworkRouter.setStatus("current")


class _DsSlotNetworkNameserver_Type(DisplayString):
    """Custom type dsSlotNetworkNameserver based on DisplayString"""
    defaultValue = OctetString("168.126.63.1")


_DsSlotNetworkNameserver_Type.__name__ = "DisplayString"
_DsSlotNetworkNameserver_Object = MibTableColumn
dsSlotNetworkNameserver = _DsSlotNetworkNameserver_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 25),
    _DsSlotNetworkNameserver_Type()
)
dsSlotNetworkNameserver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSlotNetworkNameserver.setStatus("current")
_DsSlotVersion_Type = DisplayString
_DsSlotVersion_Object = MibTableColumn
dsSlotVersion = _DsSlotVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 26),
    _DsSlotVersion_Type()
)
dsSlotVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSlotVersion.setStatus("current")


class _DsSlotInstallStatus_Type(Integer32):
    """Custom type dsSlotInstallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("removed", 2))
    )


_DsSlotInstallStatus_Type.__name__ = "Integer32"
_DsSlotInstallStatus_Object = MibTableColumn
dsSlotInstallStatus = _DsSlotInstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 4, 2, 1, 27),
    _DsSlotInstallStatus_Type()
)
dsSlotInstallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSlotInstallStatus.setStatus("current")
_DsAccGwyConfigPort_ObjectIdentity = ObjectIdentity
dsAccGwyConfigPort = _DsAccGwyConfigPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 5)
)
_DsAccGwyConfigPortTable_Object = MibTable
dsAccGwyConfigPortTable = _DsAccGwyConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    dsAccGwyConfigPortTable.setStatus("current")
_DsAccGwyConfigPortEntry_Object = MibTableRow
dsAccGwyConfigPortEntry = _DsAccGwyConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 5, 2, 1)
)
dsAccGwyConfigPortEntry.setIndexNames(
    (0, "DASAN-ACCESS-MIB", "dsAccPortIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyConfigPortEntry.setStatus("current")
_DsAccPortIndex_Type = Integer32
_DsAccPortIndex_Object = MibTableColumn
dsAccPortIndex = _DsAccPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 5, 2, 1, 1),
    _DsAccPortIndex_Type()
)
dsAccPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAccPortIndex.setStatus("current")


class _DsPortIvol_Type(Integer32):
    """Custom type dsPortIvol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_DsPortIvol_Type.__name__ = "Integer32"
_DsPortIvol_Object = MibTableColumn
dsPortIvol = _DsPortIvol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 5, 2, 1, 2),
    _DsPortIvol_Type()
)
dsPortIvol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsPortIvol.setStatus("current")


class _DsPortOvol_Type(Integer32):
    """Custom type dsPortOvol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_DsPortOvol_Type.__name__ = "Integer32"
_DsPortOvol_Object = MibTableColumn
dsPortOvol = _DsPortOvol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 5, 2, 1, 3),
    _DsPortOvol_Type()
)
dsPortOvol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsPortOvol.setStatus("current")
_DsPortStatus_Type = DisplayString
_DsPortStatus_Object = MibTableColumn
dsPortStatus = _DsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 5, 2, 1, 4),
    _DsPortStatus_Type()
)
dsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsPortStatus.setStatus("current")
_DsPortStatistics_Type = DisplayString
_DsPortStatistics_Object = MibTableColumn
dsPortStatistics = _DsPortStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 5, 2, 1, 5),
    _DsPortStatistics_Type()
)
dsPortStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsPortStatistics.setStatus("current")


class _DsPortPortBlock_Type(Integer32):
    """Custom type dsPortPortBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unblock", 0),
          ("block", 1))
    )


_DsPortPortBlock_Type.__name__ = "Integer32"
_DsPortPortBlock_Object = MibTableColumn
dsPortPortBlock = _DsPortPortBlock_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 1, 5, 2, 1, 6),
    _DsPortPortBlock_Type()
)
dsPortPortBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsPortPortBlock.setStatus("current")
_DsAccGwyControl_ObjectIdentity = ObjectIdentity
dsAccGwyControl = _DsAccGwyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2)
)
_DsAccGwyControlMgcp_ObjectIdentity = ObjectIdentity
dsAccGwyControlMgcp = _DsAccGwyControlMgcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2, 1)
)


class _DsControlMgcpRestart_Type(Integer32):
    """Custom type dsControlMgcpRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_DsControlMgcpRestart_Type.__name__ = "Integer32"
_DsControlMgcpRestart_Object = MibScalar
dsControlMgcpRestart = _DsControlMgcpRestart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2, 1, 1),
    _DsControlMgcpRestart_Type()
)
dsControlMgcpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsControlMgcpRestart.setStatus("current")
_DsAccGwyControlTable_ObjectIdentity = ObjectIdentity
dsAccGwyControlTable = _DsAccGwyControlTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2, 2)
)
_DsAccGwyControlSlotTable_Object = MibTable
dsAccGwyControlSlotTable = _DsAccGwyControlSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyControlSlotTable.setStatus("current")
_DsAccGwyControlSlotEntry_Object = MibTableRow
dsAccGwyControlSlotEntry = _DsAccGwyControlSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2, 2, 1, 1)
)
dsAccGwyControlSlotEntry.setIndexNames(
    (0, "DASAN-ACCESS-MIB", "dsControlSlotIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyControlSlotEntry.setStatus("current")
_DsControlSlotIndex_Type = Integer32
_DsControlSlotIndex_Object = MibTableColumn
dsControlSlotIndex = _DsControlSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2, 2, 1, 1, 1),
    _DsControlSlotIndex_Type()
)
dsControlSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsControlSlotIndex.setStatus("current")


class _DsControlSlotRestart_Type(Integer32):
    """Custom type dsControlSlotRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_DsControlSlotRestart_Type.__name__ = "Integer32"
_DsControlSlotRestart_Object = MibTableColumn
dsControlSlotRestart = _DsControlSlotRestart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2, 2, 1, 1, 2),
    _DsControlSlotRestart_Type()
)
dsControlSlotRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsControlSlotRestart.setStatus("current")
_DsAccGwyControlPortTable_Object = MibTable
dsAccGwyControlPortTable = _DsAccGwyControlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dsAccGwyControlPortTable.setStatus("current")
_DsAccGwyControlPortEntry_Object = MibTableRow
dsAccGwyControlPortEntry = _DsAccGwyControlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2, 2, 2, 1)
)
dsAccGwyControlPortEntry.setIndexNames(
    (0, "DASAN-ACCESS-MIB", "dsControlPortIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyControlPortEntry.setStatus("current")
_DsControlPortIndex_Type = Integer32
_DsControlPortIndex_Object = MibTableColumn
dsControlPortIndex = _DsControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2, 2, 2, 1, 1),
    _DsControlPortIndex_Type()
)
dsControlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsControlPortIndex.setStatus("current")


class _DsControlPortReset_Type(Integer32):
    """Custom type dsControlPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_DsControlPortReset_Type.__name__ = "Integer32"
_DsControlPortReset_Object = MibTableColumn
dsControlPortReset = _DsControlPortReset_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2, 2, 2, 1, 2),
    _DsControlPortReset_Type()
)
dsControlPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsControlPortReset.setStatus("current")


class _DsControlPortTestRing_Type(Integer32):
    """Custom type dsControlPortTestRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stop", 0),
          ("start", 1))
    )


_DsControlPortTestRing_Type.__name__ = "Integer32"
_DsControlPortTestRing_Object = MibTableColumn
dsControlPortTestRing = _DsControlPortTestRing_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 1, 2, 2, 2, 1, 3),
    _DsControlPortTestRing_Type()
)
dsControlPortTestRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsControlPortTestRing.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-ACCESS-MIB",
    **{"dasanAccessMib": dasanAccessMib,
       "dasanAccessGatewayMIBObjects": dasanAccessGatewayMIBObjects,
       "dsAccGwyConfiguration": dsAccGwyConfiguration,
       "dsAccGwyConfigMgcp": dsAccGwyConfigMgcp,
       "dsMgcpAddAreaCode": dsMgcpAddAreaCode,
       "dsMgcpAreaCode": dsMgcpAreaCode,
       "dsMgcpAreaCodeAllows": dsMgcpAreaCodeAllows,
       "dsMgcpAreaCodeExceptions": dsMgcpAreaCodeExceptions,
       "dsMgcpCallTrace": dsMgcpCallTrace,
       "dsMgcpEncodePackageName": dsMgcpEncodePackageName,
       "dsMgcpRetransmitStartTimeout": dsMgcpRetransmitStartTimeout,
       "dsMgcpRetransmitMaxTimeout": dsMgcpRetransmitMaxTimeout,
       "dsMgcpRetransmitMax1": dsMgcpRetransmitMax1,
       "dsMgcpRetransmitMax2": dsMgcpRetransmitMax2,
       "dsMgcpRestartMaxwait": dsMgcpRestartMaxwait,
       "dsMgcpDisconnectInit": dsMgcpDisconnectInit,
       "dsMgcpDisconnectMin": dsMgcpDisconnectMin,
       "dsMgcpDisconnectMax": dsMgcpDisconnectMax,
       "dsMgcpCaAddr1": dsMgcpCaAddr1,
       "dsMgcpCaAddr2": dsMgcpCaAddr2,
       "dsMgcpCaAddr3": dsMgcpCaAddr3,
       "dsMgcpCaAddr4": dsMgcpCaAddr4,
       "dsMgcpCaAddr5": dsMgcpCaAddr5,
       "dsMgcpCaAddr6": dsMgcpCaAddr6,
       "dsMgcpCaAddr7": dsMgcpCaAddr7,
       "dsMgcpCaAddr8": dsMgcpCaAddr8,
       "dsMgcpCaPort1": dsMgcpCaPort1,
       "dsMgcpCaPort2": dsMgcpCaPort2,
       "dsMgcpCaPort3": dsMgcpCaPort3,
       "dsMgcpCaPort4": dsMgcpCaPort4,
       "dsMgcpCaPort5": dsMgcpCaPort5,
       "dsMgcpCaPort6": dsMgcpCaPort6,
       "dsMgcpCaPort7": dsMgcpCaPort7,
       "dsMgcpCaPort8": dsMgcpCaPort8,
       "dsMgcpMgAddr": dsMgcpMgAddr,
       "dsMgcpMgPort": dsMgcpMgPort,
       "dsMgcpStatus": dsMgcpStatus,
       "dsMgcpEndpointIdTable": dsMgcpEndpointIdTable,
       "dsMgcpEndpointIdEntry": dsMgcpEndpointIdEntry,
       "dsMgcpEndpointIdIndex": dsMgcpEndpointIdIndex,
       "dsMgcpEndpointId": dsMgcpEndpointId,
       "dsMgcpTraceTable": dsMgcpTraceTable,
       "dsMgcpTraceEntry": dsMgcpTraceEntry,
       "dsMgcpTraceMessageIndex": dsMgcpTraceMessageIndex,
       "dsMgcpTraceMessageTime": dsMgcpTraceMessageTime,
       "dsMgcpTraceMessageDirection": dsMgcpTraceMessageDirection,
       "dsMgcpTraceMessageContent": dsMgcpTraceMessageContent,
       "dsAccGwyConfigGlobal": dsAccGwyConfigGlobal,
       "dsAccGwyConfigGlobalDigitmap": dsAccGwyConfigGlobalDigitmap,
       "dsAccGwyConfigGlobalSwitchDhcp": dsAccGwyConfigGlobalSwitchDhcp,
       "dsAccGwyUpsStatus": dsAccGwyUpsStatus,
       "dsAccGwyAutoConfigServer": dsAccGwyAutoConfigServer,
       "dsAccGwyAutoUpgradeServer": dsAccGwyAutoUpgradeServer,
       "dsAccGwyConfigSlot": dsAccGwyConfigSlot,
       "dsAccGwyConfigSlotTable": dsAccGwyConfigSlotTable,
       "dsAccGwyConfigSlotEntry": dsAccGwyConfigSlotEntry,
       "dsAccSlotIndex": dsAccSlotIndex,
       "dsSlotCodecType": dsSlotCodecType,
       "dsSlotCodecPacketizationPeriodG711": dsSlotCodecPacketizationPeriodG711,
       "dsSlotCodecPacketizationPeriodG723": dsSlotCodecPacketizationPeriodG723,
       "dsSlotCodecPacketizationPeriodG729": dsSlotCodecPacketizationPeriodG729,
       "dsSlotJitterbuffer": dsSlotJitterbuffer,
       "dsSlotRingonTime": dsSlotRingonTime,
       "dsSlotRingoffTime": dsSlotRingoffTime,
       "dsSlotHookflashMin": dsSlotHookflashMin,
       "dsSlotHookflashMax": dsSlotHookflashMax,
       "dsSlotInterdigitTimeout": dsSlotInterdigitTimeout,
       "dsSlotEce": dsSlotEce,
       "dsSlotFax": dsSlotFax,
       "dsSlotCid": dsSlotCid,
       "dsSlotVad": dsSlotVad,
       "dsSlotCng": dsSlotCng,
       "dsSlotOobdtmf": dsSlotOobdtmf,
       "dsSlotNetworkHostname": dsSlotNetworkHostname,
       "dsSlotNetworkDhcp": dsSlotNetworkDhcp,
       "dsSlotNetworkIpaddress": dsSlotNetworkIpaddress,
       "dsSlotNetworkSubnetmask": dsSlotNetworkSubnetmask,
       "dsSlotNetworkRouter": dsSlotNetworkRouter,
       "dsSlotNetworkNameserver": dsSlotNetworkNameserver,
       "dsSlotVersion": dsSlotVersion,
       "dsSlotInstallStatus": dsSlotInstallStatus,
       "dsAccGwyConfigPort": dsAccGwyConfigPort,
       "dsAccGwyConfigPortTable": dsAccGwyConfigPortTable,
       "dsAccGwyConfigPortEntry": dsAccGwyConfigPortEntry,
       "dsAccPortIndex": dsAccPortIndex,
       "dsPortIvol": dsPortIvol,
       "dsPortOvol": dsPortOvol,
       "dsPortStatus": dsPortStatus,
       "dsPortStatistics": dsPortStatistics,
       "dsPortPortBlock": dsPortPortBlock,
       "dsAccGwyControl": dsAccGwyControl,
       "dsAccGwyControlMgcp": dsAccGwyControlMgcp,
       "dsControlMgcpRestart": dsControlMgcpRestart,
       "dsAccGwyControlTable": dsAccGwyControlTable,
       "dsAccGwyControlSlotTable": dsAccGwyControlSlotTable,
       "dsAccGwyControlSlotEntry": dsAccGwyControlSlotEntry,
       "dsControlSlotIndex": dsControlSlotIndex,
       "dsControlSlotRestart": dsControlSlotRestart,
       "dsAccGwyControlPortTable": dsAccGwyControlPortTable,
       "dsAccGwyControlPortEntry": dsAccGwyControlPortEntry,
       "dsControlPortIndex": dsControlPortIndex,
       "dsControlPortReset": dsControlPortReset,
       "dsControlPortTestRing": dsControlPortTestRing}
)
