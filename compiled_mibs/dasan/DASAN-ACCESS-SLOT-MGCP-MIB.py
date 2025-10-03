# SNMP MIB module (DASAN-ACCESS-SLOT-MGCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-ACCESS-SLOT-MGCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:55 2025
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

_DasanAccGatewayMIBObjects_ObjectIdentity = ObjectIdentity
dasanAccGatewayMIBObjects = _DasanAccGatewayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2)
)
_DsAccGwyMgcp_ObjectIdentity = ObjectIdentity
dsAccGwyMgcp = _DsAccGwyMgcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2)
)
_DsAccGwyMgcpConfiguration_ObjectIdentity = ObjectIdentity
dsAccGwyMgcpConfiguration = _DsAccGwyMgcpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1)
)
_DsAccGwyConfigMgcpSlot_ObjectIdentity = ObjectIdentity
dsAccGwyConfigMgcpSlot = _DsAccGwyConfigMgcpSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1)
)
_DsAccGwyConfigMgcpSlotTable_Object = MibTable
dsAccGwyConfigMgcpSlotTable = _DsAccGwyConfigMgcpSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyConfigMgcpSlotTable.setStatus("current")
_DsAccGwyConfigMgcpSlotEntry_Object = MibTableRow
dsAccGwyConfigMgcpSlotEntry = _DsAccGwyConfigMgcpSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1)
)
dsAccGwyConfigMgcpSlotEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-MGCP-MIB", "dsMgcpSlotIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyConfigMgcpSlotEntry.setStatus("current")
_DsMgcpSlotIndex_Type = Integer32
_DsMgcpSlotIndex_Object = MibTableColumn
dsMgcpSlotIndex = _DsMgcpSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 1),
    _DsMgcpSlotIndex_Type()
)
dsMgcpSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMgcpSlotIndex.setStatus("current")


class _DsMgcpSlotEncodePackageName_Type(Integer32):
    """Custom type dsMgcpSlotEncodePackageName based on Integer32"""
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


_DsMgcpSlotEncodePackageName_Type.__name__ = "Integer32"
_DsMgcpSlotEncodePackageName_Object = MibTableColumn
dsMgcpSlotEncodePackageName = _DsMgcpSlotEncodePackageName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 2),
    _DsMgcpSlotEncodePackageName_Type()
)
dsMgcpSlotEncodePackageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotEncodePackageName.setStatus("current")
_DsMgcpSlotRetransmitStartTimeout_Type = Integer32
_DsMgcpSlotRetransmitStartTimeout_Object = MibTableColumn
dsMgcpSlotRetransmitStartTimeout = _DsMgcpSlotRetransmitStartTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 3),
    _DsMgcpSlotRetransmitStartTimeout_Type()
)
dsMgcpSlotRetransmitStartTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotRetransmitStartTimeout.setStatus("current")
_DsMgcpSlotRetransmitMaxTimeout_Type = Integer32
_DsMgcpSlotRetransmitMaxTimeout_Object = MibTableColumn
dsMgcpSlotRetransmitMaxTimeout = _DsMgcpSlotRetransmitMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 4),
    _DsMgcpSlotRetransmitMaxTimeout_Type()
)
dsMgcpSlotRetransmitMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotRetransmitMaxTimeout.setStatus("current")
_DsMgcpSlotRetransmitLongTimer_Type = Integer32
_DsMgcpSlotRetransmitLongTimer_Object = MibTableColumn
dsMgcpSlotRetransmitLongTimer = _DsMgcpSlotRetransmitLongTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 5),
    _DsMgcpSlotRetransmitLongTimer_Type()
)
dsMgcpSlotRetransmitLongTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMgcpSlotRetransmitLongTimer.setStatus("current")
_DsMgcpSlotRetransmitMaxLifetime_Type = Integer32
_DsMgcpSlotRetransmitMaxLifetime_Object = MibTableColumn
dsMgcpSlotRetransmitMaxLifetime = _DsMgcpSlotRetransmitMaxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 6),
    _DsMgcpSlotRetransmitMaxLifetime_Type()
)
dsMgcpSlotRetransmitMaxLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotRetransmitMaxLifetime.setStatus("current")
_DsMgcpSlotRetransmitMax1_Type = Integer32
_DsMgcpSlotRetransmitMax1_Object = MibTableColumn
dsMgcpSlotRetransmitMax1 = _DsMgcpSlotRetransmitMax1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 7),
    _DsMgcpSlotRetransmitMax1_Type()
)
dsMgcpSlotRetransmitMax1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotRetransmitMax1.setStatus("current")
_DsMgcpSlotRetransmitMax2_Type = Integer32
_DsMgcpSlotRetransmitMax2_Object = MibTableColumn
dsMgcpSlotRetransmitMax2 = _DsMgcpSlotRetransmitMax2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 8),
    _DsMgcpSlotRetransmitMax2_Type()
)
dsMgcpSlotRetransmitMax2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotRetransmitMax2.setStatus("current")
_DsMgcpSlotRestartMaxwait_Type = Integer32
_DsMgcpSlotRestartMaxwait_Object = MibTableColumn
dsMgcpSlotRestartMaxwait = _DsMgcpSlotRestartMaxwait_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 9),
    _DsMgcpSlotRestartMaxwait_Type()
)
dsMgcpSlotRestartMaxwait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotRestartMaxwait.setStatus("current")
_DsMgcpSlotDisconnectInit_Type = Integer32
_DsMgcpSlotDisconnectInit_Object = MibTableColumn
dsMgcpSlotDisconnectInit = _DsMgcpSlotDisconnectInit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 10),
    _DsMgcpSlotDisconnectInit_Type()
)
dsMgcpSlotDisconnectInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotDisconnectInit.setStatus("current")
_DsMgcpSlotDisconnectMin_Type = Integer32
_DsMgcpSlotDisconnectMin_Object = MibTableColumn
dsMgcpSlotDisconnectMin = _DsMgcpSlotDisconnectMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 11),
    _DsMgcpSlotDisconnectMin_Type()
)
dsMgcpSlotDisconnectMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotDisconnectMin.setStatus("current")
_DsMgcpSlotDisconnectMax_Type = Integer32
_DsMgcpSlotDisconnectMax_Object = MibTableColumn
dsMgcpSlotDisconnectMax = _DsMgcpSlotDisconnectMax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 12),
    _DsMgcpSlotDisconnectMax_Type()
)
dsMgcpSlotDisconnectMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotDisconnectMax.setStatus("current")


class _DsMgcpSlotCaAddr1_Type(DisplayString):
    """Custom type dsMgcpSlotCaAddr1 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpSlotCaAddr1_Type.__name__ = "DisplayString"
_DsMgcpSlotCaAddr1_Object = MibTableColumn
dsMgcpSlotCaAddr1 = _DsMgcpSlotCaAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 13),
    _DsMgcpSlotCaAddr1_Type()
)
dsMgcpSlotCaAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaAddr1.setStatus("current")


class _DsMgcpSlotCaAddr2_Type(DisplayString):
    """Custom type dsMgcpSlotCaAddr2 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpSlotCaAddr2_Type.__name__ = "DisplayString"
_DsMgcpSlotCaAddr2_Object = MibTableColumn
dsMgcpSlotCaAddr2 = _DsMgcpSlotCaAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 14),
    _DsMgcpSlotCaAddr2_Type()
)
dsMgcpSlotCaAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaAddr2.setStatus("current")


class _DsMgcpSlotCaAddr3_Type(DisplayString):
    """Custom type dsMgcpSlotCaAddr3 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpSlotCaAddr3_Type.__name__ = "DisplayString"
_DsMgcpSlotCaAddr3_Object = MibTableColumn
dsMgcpSlotCaAddr3 = _DsMgcpSlotCaAddr3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 15),
    _DsMgcpSlotCaAddr3_Type()
)
dsMgcpSlotCaAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaAddr3.setStatus("current")


class _DsMgcpSlotCaAddr4_Type(DisplayString):
    """Custom type dsMgcpSlotCaAddr4 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpSlotCaAddr4_Type.__name__ = "DisplayString"
_DsMgcpSlotCaAddr4_Object = MibTableColumn
dsMgcpSlotCaAddr4 = _DsMgcpSlotCaAddr4_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 16),
    _DsMgcpSlotCaAddr4_Type()
)
dsMgcpSlotCaAddr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaAddr4.setStatus("current")


class _DsMgcpSlotCaAddr5_Type(DisplayString):
    """Custom type dsMgcpSlotCaAddr5 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpSlotCaAddr5_Type.__name__ = "DisplayString"
_DsMgcpSlotCaAddr5_Object = MibTableColumn
dsMgcpSlotCaAddr5 = _DsMgcpSlotCaAddr5_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 17),
    _DsMgcpSlotCaAddr5_Type()
)
dsMgcpSlotCaAddr5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaAddr5.setStatus("current")


class _DsMgcpSlotCaAddr6_Type(DisplayString):
    """Custom type dsMgcpSlotCaAddr6 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpSlotCaAddr6_Type.__name__ = "DisplayString"
_DsMgcpSlotCaAddr6_Object = MibTableColumn
dsMgcpSlotCaAddr6 = _DsMgcpSlotCaAddr6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 18),
    _DsMgcpSlotCaAddr6_Type()
)
dsMgcpSlotCaAddr6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaAddr6.setStatus("current")


class _DsMgcpSlotCaAddr7_Type(DisplayString):
    """Custom type dsMgcpSlotCaAddr7 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpSlotCaAddr7_Type.__name__ = "DisplayString"
_DsMgcpSlotCaAddr7_Object = MibTableColumn
dsMgcpSlotCaAddr7 = _DsMgcpSlotCaAddr7_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 19),
    _DsMgcpSlotCaAddr7_Type()
)
dsMgcpSlotCaAddr7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaAddr7.setStatus("current")


class _DsMgcpSlotCaAddr8_Type(DisplayString):
    """Custom type dsMgcpSlotCaAddr8 based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpSlotCaAddr8_Type.__name__ = "DisplayString"
_DsMgcpSlotCaAddr8_Object = MibTableColumn
dsMgcpSlotCaAddr8 = _DsMgcpSlotCaAddr8_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 20),
    _DsMgcpSlotCaAddr8_Type()
)
dsMgcpSlotCaAddr8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaAddr8.setStatus("current")
_DsMgcpSlotCaPort1_Type = Integer32
_DsMgcpSlotCaPort1_Object = MibTableColumn
dsMgcpSlotCaPort1 = _DsMgcpSlotCaPort1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 21),
    _DsMgcpSlotCaPort1_Type()
)
dsMgcpSlotCaPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaPort1.setStatus("current")
_DsMgcpSlotCaPort2_Type = Integer32
_DsMgcpSlotCaPort2_Object = MibTableColumn
dsMgcpSlotCaPort2 = _DsMgcpSlotCaPort2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 22),
    _DsMgcpSlotCaPort2_Type()
)
dsMgcpSlotCaPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaPort2.setStatus("current")
_DsMgcpSlotCaPort3_Type = Integer32
_DsMgcpSlotCaPort3_Object = MibTableColumn
dsMgcpSlotCaPort3 = _DsMgcpSlotCaPort3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 23),
    _DsMgcpSlotCaPort3_Type()
)
dsMgcpSlotCaPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaPort3.setStatus("current")
_DsMgcpSlotCaPort4_Type = Integer32
_DsMgcpSlotCaPort4_Object = MibTableColumn
dsMgcpSlotCaPort4 = _DsMgcpSlotCaPort4_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 24),
    _DsMgcpSlotCaPort4_Type()
)
dsMgcpSlotCaPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaPort4.setStatus("current")
_DsMgcpSlotCaPort5_Type = Integer32
_DsMgcpSlotCaPort5_Object = MibTableColumn
dsMgcpSlotCaPort5 = _DsMgcpSlotCaPort5_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 25),
    _DsMgcpSlotCaPort5_Type()
)
dsMgcpSlotCaPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaPort5.setStatus("current")
_DsMgcpSlotCaPort6_Type = Integer32
_DsMgcpSlotCaPort6_Object = MibTableColumn
dsMgcpSlotCaPort6 = _DsMgcpSlotCaPort6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 26),
    _DsMgcpSlotCaPort6_Type()
)
dsMgcpSlotCaPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaPort6.setStatus("current")
_DsMgcpSlotCaPort7_Type = Integer32
_DsMgcpSlotCaPort7_Object = MibTableColumn
dsMgcpSlotCaPort7 = _DsMgcpSlotCaPort7_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 27),
    _DsMgcpSlotCaPort7_Type()
)
dsMgcpSlotCaPort7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaPort7.setStatus("current")
_DsMgcpSlotCaPort8_Type = Integer32
_DsMgcpSlotCaPort8_Object = MibTableColumn
dsMgcpSlotCaPort8 = _DsMgcpSlotCaPort8_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 28),
    _DsMgcpSlotCaPort8_Type()
)
dsMgcpSlotCaPort8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotCaPort8.setStatus("current")


class _DsMgcpSlotMgAddr_Type(DisplayString):
    """Custom type dsMgcpSlotMgAddr based on DisplayString"""
    defaultValue = OctetString("1.1.1.1")


_DsMgcpSlotMgAddr_Type.__name__ = "DisplayString"
_DsMgcpSlotMgAddr_Object = MibTableColumn
dsMgcpSlotMgAddr = _DsMgcpSlotMgAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 29),
    _DsMgcpSlotMgAddr_Type()
)
dsMgcpSlotMgAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotMgAddr.setStatus("current")
_DsMgcpSlotMgPort_Type = Integer32
_DsMgcpSlotMgPort_Object = MibTableColumn
dsMgcpSlotMgPort = _DsMgcpSlotMgPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 1, 1, 1, 1, 30),
    _DsMgcpSlotMgPort_Type()
)
dsMgcpSlotMgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMgcpSlotMgPort.setStatus("current")
_DsAccGwyMgcpMonitor_ObjectIdentity = ObjectIdentity
dsAccGwyMgcpMonitor = _DsAccGwyMgcpMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 2)
)
_DsAccGwyMonitorMgcpSlot_ObjectIdentity = ObjectIdentity
dsAccGwyMonitorMgcpSlot = _DsAccGwyMonitorMgcpSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 2, 1)
)
_DsAccGwyMonitorMgcpSlotTable_Object = MibTable
dsAccGwyMonitorMgcpSlotTable = _DsAccGwyMonitorMgcpSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyMonitorMgcpSlotTable.setStatus("current")
_DsAccGwyMonitorMgcpSlotEntry_Object = MibTableRow
dsAccGwyMonitorMgcpSlotEntry = _DsAccGwyMonitorMgcpSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 2, 1, 1, 1)
)
dsAccGwyMonitorMgcpSlotEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-MGCP-MIB", "dsMgcpSlotIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyMonitorMgcpSlotEntry.setStatus("current")
_DsMgcpMonitorMgcpStatus_Type = DisplayString
_DsMgcpMonitorMgcpStatus_Object = MibTableColumn
dsMgcpMonitorMgcpStatus = _DsMgcpMonitorMgcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 2, 2, 1, 1, 1, 1),
    _DsMgcpMonitorMgcpStatus_Type()
)
dsMgcpMonitorMgcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMgcpMonitorMgcpStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-ACCESS-SLOT-MGCP-MIB",
    **{"dasanAccessMib": dasanAccessMib,
       "dasanAccGatewayMIBObjects": dasanAccGatewayMIBObjects,
       "dsAccGwyMgcp": dsAccGwyMgcp,
       "dsAccGwyMgcpConfiguration": dsAccGwyMgcpConfiguration,
       "dsAccGwyConfigMgcpSlot": dsAccGwyConfigMgcpSlot,
       "dsAccGwyConfigMgcpSlotTable": dsAccGwyConfigMgcpSlotTable,
       "dsAccGwyConfigMgcpSlotEntry": dsAccGwyConfigMgcpSlotEntry,
       "dsMgcpSlotIndex": dsMgcpSlotIndex,
       "dsMgcpSlotEncodePackageName": dsMgcpSlotEncodePackageName,
       "dsMgcpSlotRetransmitStartTimeout": dsMgcpSlotRetransmitStartTimeout,
       "dsMgcpSlotRetransmitMaxTimeout": dsMgcpSlotRetransmitMaxTimeout,
       "dsMgcpSlotRetransmitLongTimer": dsMgcpSlotRetransmitLongTimer,
       "dsMgcpSlotRetransmitMaxLifetime": dsMgcpSlotRetransmitMaxLifetime,
       "dsMgcpSlotRetransmitMax1": dsMgcpSlotRetransmitMax1,
       "dsMgcpSlotRetransmitMax2": dsMgcpSlotRetransmitMax2,
       "dsMgcpSlotRestartMaxwait": dsMgcpSlotRestartMaxwait,
       "dsMgcpSlotDisconnectInit": dsMgcpSlotDisconnectInit,
       "dsMgcpSlotDisconnectMin": dsMgcpSlotDisconnectMin,
       "dsMgcpSlotDisconnectMax": dsMgcpSlotDisconnectMax,
       "dsMgcpSlotCaAddr1": dsMgcpSlotCaAddr1,
       "dsMgcpSlotCaAddr2": dsMgcpSlotCaAddr2,
       "dsMgcpSlotCaAddr3": dsMgcpSlotCaAddr3,
       "dsMgcpSlotCaAddr4": dsMgcpSlotCaAddr4,
       "dsMgcpSlotCaAddr5": dsMgcpSlotCaAddr5,
       "dsMgcpSlotCaAddr6": dsMgcpSlotCaAddr6,
       "dsMgcpSlotCaAddr7": dsMgcpSlotCaAddr7,
       "dsMgcpSlotCaAddr8": dsMgcpSlotCaAddr8,
       "dsMgcpSlotCaPort1": dsMgcpSlotCaPort1,
       "dsMgcpSlotCaPort2": dsMgcpSlotCaPort2,
       "dsMgcpSlotCaPort3": dsMgcpSlotCaPort3,
       "dsMgcpSlotCaPort4": dsMgcpSlotCaPort4,
       "dsMgcpSlotCaPort5": dsMgcpSlotCaPort5,
       "dsMgcpSlotCaPort6": dsMgcpSlotCaPort6,
       "dsMgcpSlotCaPort7": dsMgcpSlotCaPort7,
       "dsMgcpSlotCaPort8": dsMgcpSlotCaPort8,
       "dsMgcpSlotMgAddr": dsMgcpSlotMgAddr,
       "dsMgcpSlotMgPort": dsMgcpSlotMgPort,
       "dsAccGwyMgcpMonitor": dsAccGwyMgcpMonitor,
       "dsAccGwyMonitorMgcpSlot": dsAccGwyMonitorMgcpSlot,
       "dsAccGwyMonitorMgcpSlotTable": dsAccGwyMonitorMgcpSlotTable,
       "dsAccGwyMonitorMgcpSlotEntry": dsAccGwyMonitorMgcpSlotEntry,
       "dsMgcpMonitorMgcpStatus": dsMgcpMonitorMgcpStatus}
)
