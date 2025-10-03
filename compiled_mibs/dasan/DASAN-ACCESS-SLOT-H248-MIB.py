# SNMP MIB module (DASAN-ACCESS-SLOT-H248-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-ACCESS-SLOT-H248-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:54 2025
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



class MediaGatewayId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_DasanAccGatewayMIBObjects_ObjectIdentity = ObjectIdentity
dasanAccGatewayMIBObjects = _DasanAccGatewayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2)
)
_DsAccGwyH248_ObjectIdentity = ObjectIdentity
dsAccGwyH248 = _DsAccGwyH248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3)
)
_DsAccGwyH248Configuration_ObjectIdentity = ObjectIdentity
dsAccGwyH248Configuration = _DsAccGwyH248Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1)
)
_DsAccGwyConfigH248Slot_ObjectIdentity = ObjectIdentity
dsAccGwyConfigH248Slot = _DsAccGwyConfigH248Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 1)
)
_DsAccGwyConfigH248Vgw_ObjectIdentity = ObjectIdentity
dsAccGwyConfigH248Vgw = _DsAccGwyConfigH248Vgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2)
)
_DsAccGwyConfigH248VgwTable_Object = MibTable
dsAccGwyConfigH248VgwTable = _DsAccGwyConfigH248VgwTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyConfigH248VgwTable.setStatus("current")
_DsAccGwyConfigH248VgwEntry_Object = MibTableRow
dsAccGwyConfigH248VgwEntry = _DsAccGwyConfigH248VgwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1)
)
dsAccGwyConfigH248VgwEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-H248-MIB", "dsH248VgwIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyConfigH248VgwEntry.setStatus("current")
_DsH248VgwIndex_Type = Integer32
_DsH248VgwIndex_Object = MibTableColumn
dsH248VgwIndex = _DsH248VgwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 1),
    _DsH248VgwIndex_Type()
)
dsH248VgwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248VgwIndex.setStatus("current")
_DsH248VgwGatewayID_Type = DisplayString
_DsH248VgwGatewayID_Object = MibTableColumn
dsH248VgwGatewayID = _DsH248VgwGatewayID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 2),
    _DsH248VgwGatewayID_Type()
)
dsH248VgwGatewayID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248VgwGatewayID.setStatus("current")
_DsH248VgwGatewayPhyTerminationStart_Type = Integer32
_DsH248VgwGatewayPhyTerminationStart_Object = MibTableColumn
dsH248VgwGatewayPhyTerminationStart = _DsH248VgwGatewayPhyTerminationStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 3),
    _DsH248VgwGatewayPhyTerminationStart_Type()
)
dsH248VgwGatewayPhyTerminationStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayPhyTerminationStart.setStatus("current")
_DsH248VgwGatewayPhyTerminationEnd_Type = Integer32
_DsH248VgwGatewayPhyTerminationEnd_Object = MibTableColumn
dsH248VgwGatewayPhyTerminationEnd = _DsH248VgwGatewayPhyTerminationEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 4),
    _DsH248VgwGatewayPhyTerminationEnd_Type()
)
dsH248VgwGatewayPhyTerminationEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayPhyTerminationEnd.setStatus("current")
_DsH248VgwGatewayMediaPortStart_Type = Integer32
_DsH248VgwGatewayMediaPortStart_Object = MibTableColumn
dsH248VgwGatewayMediaPortStart = _DsH248VgwGatewayMediaPortStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 5),
    _DsH248VgwGatewayMediaPortStart_Type()
)
dsH248VgwGatewayMediaPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayMediaPortStart.setStatus("current")
_DsH248VgwGatewayMediaPortEnd_Type = Integer32
_DsH248VgwGatewayMediaPortEnd_Object = MibTableColumn
dsH248VgwGatewayMediaPortEnd = _DsH248VgwGatewayMediaPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 6),
    _DsH248VgwGatewayMediaPortEnd_Type()
)
dsH248VgwGatewayMediaPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayMediaPortEnd.setStatus("current")
_DsH248VgwGatewayAddr_Type = DisplayString
_DsH248VgwGatewayAddr_Object = MibTableColumn
dsH248VgwGatewayAddr = _DsH248VgwGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 7),
    _DsH248VgwGatewayAddr_Type()
)
dsH248VgwGatewayAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsH248VgwGatewayAddr.setStatus("current")


class _DsH248VgwGatewayPort_Type(Integer32):
    """Custom type dsH248VgwGatewayPort based on Integer32"""
    defaultValue = 2944

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsH248VgwGatewayPort_Type.__name__ = "Integer32"
_DsH248VgwGatewayPort_Object = MibTableColumn
dsH248VgwGatewayPort = _DsH248VgwGatewayPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 8),
    _DsH248VgwGatewayPort_Type()
)
dsH248VgwGatewayPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayPort.setStatus("current")


class _DsH248VgwGatewayEncodingScheme_Type(Integer32):
    """Custom type dsH248VgwGatewayEncodingScheme based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("text", 1),
          ("binary", 2))
    )


_DsH248VgwGatewayEncodingScheme_Type.__name__ = "Integer32"
_DsH248VgwGatewayEncodingScheme_Object = MibTableColumn
dsH248VgwGatewayEncodingScheme = _DsH248VgwGatewayEncodingScheme_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 9),
    _DsH248VgwGatewayEncodingScheme_Type()
)
dsH248VgwGatewayEncodingScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248VgwGatewayEncodingScheme.setStatus("current")


class _DsH248VgwGatewayProtocol_Type(Integer32):
    """Custom type dsH248VgwGatewayProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("megacov1", 1),
          ("megacov2", 2))
    )


_DsH248VgwGatewayProtocol_Type.__name__ = "Integer32"
_DsH248VgwGatewayProtocol_Object = MibTableColumn
dsH248VgwGatewayProtocol = _DsH248VgwGatewayProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 10),
    _DsH248VgwGatewayProtocol_Type()
)
dsH248VgwGatewayProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248VgwGatewayProtocol.setStatus("current")


class _DsH248VgwGatewaySignalingTptProtocol_Type(Integer32):
    """Custom type dsH248VgwGatewaySignalingTptProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("sctp", 3))
    )


_DsH248VgwGatewaySignalingTptProtocol_Type.__name__ = "Integer32"
_DsH248VgwGatewaySignalingTptProtocol_Object = MibTableColumn
dsH248VgwGatewaySignalingTptProtocol = _DsH248VgwGatewaySignalingTptProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 11),
    _DsH248VgwGatewaySignalingTptProtocol_Type()
)
dsH248VgwGatewaySignalingTptProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248VgwGatewaySignalingTptProtocol.setStatus("current")
_DsH248VgwGatewayControllerIPAddress1_Type = DisplayString
_DsH248VgwGatewayControllerIPAddress1_Object = MibTableColumn
dsH248VgwGatewayControllerIPAddress1 = _DsH248VgwGatewayControllerIPAddress1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 12),
    _DsH248VgwGatewayControllerIPAddress1_Type()
)
dsH248VgwGatewayControllerIPAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayControllerIPAddress1.setStatus("current")
_DsH248VgwGatewayControllerIPAddress2_Type = DisplayString
_DsH248VgwGatewayControllerIPAddress2_Object = MibTableColumn
dsH248VgwGatewayControllerIPAddress2 = _DsH248VgwGatewayControllerIPAddress2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 13),
    _DsH248VgwGatewayControllerIPAddress2_Type()
)
dsH248VgwGatewayControllerIPAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayControllerIPAddress2.setStatus("current")
_DsH248VgwGatewayControllerIPAddress3_Type = DisplayString
_DsH248VgwGatewayControllerIPAddress3_Object = MibTableColumn
dsH248VgwGatewayControllerIPAddress3 = _DsH248VgwGatewayControllerIPAddress3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 14),
    _DsH248VgwGatewayControllerIPAddress3_Type()
)
dsH248VgwGatewayControllerIPAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayControllerIPAddress3.setStatus("current")
_DsH248VgwGatewayControllerIPAddress4_Type = DisplayString
_DsH248VgwGatewayControllerIPAddress4_Object = MibTableColumn
dsH248VgwGatewayControllerIPAddress4 = _DsH248VgwGatewayControllerIPAddress4_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 15),
    _DsH248VgwGatewayControllerIPAddress4_Type()
)
dsH248VgwGatewayControllerIPAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayControllerIPAddress4.setStatus("current")
_DsH248VgwGatewayControllerIPAddress5_Type = DisplayString
_DsH248VgwGatewayControllerIPAddress5_Object = MibTableColumn
dsH248VgwGatewayControllerIPAddress5 = _DsH248VgwGatewayControllerIPAddress5_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 16),
    _DsH248VgwGatewayControllerIPAddress5_Type()
)
dsH248VgwGatewayControllerIPAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayControllerIPAddress5.setStatus("current")


class _DsH248VgwGatewayControllerPort1_Type(Integer32):
    """Custom type dsH248VgwGatewayControllerPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsH248VgwGatewayControllerPort1_Type.__name__ = "Integer32"
_DsH248VgwGatewayControllerPort1_Object = MibTableColumn
dsH248VgwGatewayControllerPort1 = _DsH248VgwGatewayControllerPort1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 17),
    _DsH248VgwGatewayControllerPort1_Type()
)
dsH248VgwGatewayControllerPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayControllerPort1.setStatus("current")


class _DsH248VgwGatewayControllerPort2_Type(Integer32):
    """Custom type dsH248VgwGatewayControllerPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsH248VgwGatewayControllerPort2_Type.__name__ = "Integer32"
_DsH248VgwGatewayControllerPort2_Object = MibTableColumn
dsH248VgwGatewayControllerPort2 = _DsH248VgwGatewayControllerPort2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 18),
    _DsH248VgwGatewayControllerPort2_Type()
)
dsH248VgwGatewayControllerPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayControllerPort2.setStatus("current")


class _DsH248VgwGatewayControllerPort3_Type(Integer32):
    """Custom type dsH248VgwGatewayControllerPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsH248VgwGatewayControllerPort3_Type.__name__ = "Integer32"
_DsH248VgwGatewayControllerPort3_Object = MibTableColumn
dsH248VgwGatewayControllerPort3 = _DsH248VgwGatewayControllerPort3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 19),
    _DsH248VgwGatewayControllerPort3_Type()
)
dsH248VgwGatewayControllerPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayControllerPort3.setStatus("current")


class _DsH248VgwGatewayControllerPort4_Type(Integer32):
    """Custom type dsH248VgwGatewayControllerPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsH248VgwGatewayControllerPort4_Type.__name__ = "Integer32"
_DsH248VgwGatewayControllerPort4_Object = MibTableColumn
dsH248VgwGatewayControllerPort4 = _DsH248VgwGatewayControllerPort4_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 20),
    _DsH248VgwGatewayControllerPort4_Type()
)
dsH248VgwGatewayControllerPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayControllerPort4.setStatus("current")


class _DsH248VgwGatewayControllerPort5_Type(Integer32):
    """Custom type dsH248VgwGatewayControllerPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsH248VgwGatewayControllerPort5_Type.__name__ = "Integer32"
_DsH248VgwGatewayControllerPort5_Object = MibTableColumn
dsH248VgwGatewayControllerPort5 = _DsH248VgwGatewayControllerPort5_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 21),
    _DsH248VgwGatewayControllerPort5_Type()
)
dsH248VgwGatewayControllerPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwGatewayControllerPort5.setStatus("current")
_DsH248VgwPropertyRootMaxContexts_Type = Integer32
_DsH248VgwPropertyRootMaxContexts_Object = MibTableColumn
dsH248VgwPropertyRootMaxContexts = _DsH248VgwPropertyRootMaxContexts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 22),
    _DsH248VgwPropertyRootMaxContexts_Type()
)
dsH248VgwPropertyRootMaxContexts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwPropertyRootMaxContexts.setStatus("current")
_DsH248VgwPropertyRootMaxTerminations_Type = Integer32
_DsH248VgwPropertyRootMaxTerminations_Object = MibTableColumn
dsH248VgwPropertyRootMaxTerminations = _DsH248VgwPropertyRootMaxTerminations_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 23),
    _DsH248VgwPropertyRootMaxTerminations_Type()
)
dsH248VgwPropertyRootMaxTerminations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwPropertyRootMaxTerminations.setStatus("current")


class _DsH248VgwTopology_Type(Integer32):
    """Custom type dsH248VgwTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nouse", 0),
          ("use", 1))
    )


_DsH248VgwTopology_Type.__name__ = "Integer32"
_DsH248VgwTopology_Object = MibTableColumn
dsH248VgwTopology = _DsH248VgwTopology_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 24),
    _DsH248VgwTopology_Type()
)
dsH248VgwTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwTopology.setStatus("current")


class _DsH248VgwTimestamp_Type(Integer32):
    """Custom type dsH248VgwTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nouse", 0),
          ("use", 1))
    )


_DsH248VgwTimestamp_Type.__name__ = "Integer32"
_DsH248VgwTimestamp_Object = MibTableColumn
dsH248VgwTimestamp = _DsH248VgwTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 25),
    _DsH248VgwTimestamp_Type()
)
dsH248VgwTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwTimestamp.setStatus("current")
_DsH248VgwNamingPhyTermination_Type = DisplayString
_DsH248VgwNamingPhyTermination_Object = MibTableColumn
dsH248VgwNamingPhyTermination = _DsH248VgwNamingPhyTermination_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 26),
    _DsH248VgwNamingPhyTermination_Type()
)
dsH248VgwNamingPhyTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwNamingPhyTermination.setStatus("current")
_DsH248VgwNamingRtpTermination_Type = DisplayString
_DsH248VgwNamingRtpTermination_Object = MibTableColumn
dsH248VgwNamingRtpTermination = _DsH248VgwNamingRtpTermination_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 27),
    _DsH248VgwNamingRtpTermination_Type()
)
dsH248VgwNamingRtpTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwNamingRtpTermination.setStatus("current")
_DsH248VgwPkgList_Type = DisplayString
_DsH248VgwPkgList_Object = MibTableColumn
dsH248VgwPkgList = _DsH248VgwPkgList_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 28),
    _DsH248VgwPkgList_Type()
)
dsH248VgwPkgList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwPkgList.setStatus("current")
_DsH248VgwHeartBeatTime_Type = Integer32
_DsH248VgwHeartBeatTime_Object = MibTableColumn
dsH248VgwHeartBeatTime = _DsH248VgwHeartBeatTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 29),
    _DsH248VgwHeartBeatTime_Type()
)
dsH248VgwHeartBeatTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwHeartBeatTime.setStatus("current")
_DsH248VgwRetransmissionTime_Type = Integer32
_DsH248VgwRetransmissionTime_Object = MibTableColumn
dsH248VgwRetransmissionTime = _DsH248VgwRetransmissionTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 30),
    _DsH248VgwRetransmissionTime_Type()
)
dsH248VgwRetransmissionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwRetransmissionTime.setStatus("current")
_DsH248VgwMaxRetransmissionCount_Type = Integer32
_DsH248VgwMaxRetransmissionCount_Object = MibTableColumn
dsH248VgwMaxRetransmissionCount = _DsH248VgwMaxRetransmissionCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 31),
    _DsH248VgwMaxRetransmissionCount_Type()
)
dsH248VgwMaxRetransmissionCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwMaxRetransmissionCount.setStatus("current")
_DsH248VgwDigitmap_Type = DisplayString
_DsH248VgwDigitmap_Object = MibTableColumn
dsH248VgwDigitmap = _DsH248VgwDigitmap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 32),
    _DsH248VgwDigitmap_Type()
)
dsH248VgwDigitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwDigitmap.setStatus("current")
_DsH248VgwDigitmapLongTime_Type = Integer32
_DsH248VgwDigitmapLongTime_Object = MibTableColumn
dsH248VgwDigitmapLongTime = _DsH248VgwDigitmapLongTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 33),
    _DsH248VgwDigitmapLongTime_Type()
)
dsH248VgwDigitmapLongTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwDigitmapLongTime.setStatus("current")
_DsH248VgwDigitmapShortTime_Type = Integer32
_DsH248VgwDigitmapShortTime_Object = MibTableColumn
dsH248VgwDigitmapShortTime = _DsH248VgwDigitmapShortTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 34),
    _DsH248VgwDigitmapShortTime_Type()
)
dsH248VgwDigitmapShortTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwDigitmapShortTime.setStatus("current")
_DsH248VgwDigitmapStartTime_Type = Integer32
_DsH248VgwDigitmapStartTime_Object = MibTableColumn
dsH248VgwDigitmapStartTime = _DsH248VgwDigitmapStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 35),
    _DsH248VgwDigitmapStartTime_Type()
)
dsH248VgwDigitmapStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwDigitmapStartTime.setStatus("current")
_DsH248VgwDigitmapZTime_Type = Integer32
_DsH248VgwDigitmapZTime_Object = MibTableColumn
dsH248VgwDigitmapZTime = _DsH248VgwDigitmapZTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 36),
    _DsH248VgwDigitmapZTime_Type()
)
dsH248VgwDigitmapZTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwDigitmapZTime.setStatus("current")


class _DsH248VgwStartupType_Type(Integer32):
    """Custom type dsH248VgwStartupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("expedited", 2))
    )


_DsH248VgwStartupType_Type.__name__ = "Integer32"
_DsH248VgwStartupType_Object = MibTableColumn
dsH248VgwStartupType = _DsH248VgwStartupType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 37),
    _DsH248VgwStartupType_Type()
)
dsH248VgwStartupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwStartupType.setStatus("current")
_DsH248VgwConnectionSilencePeriod_Type = Integer32
_DsH248VgwConnectionSilencePeriod_Object = MibTableColumn
dsH248VgwConnectionSilencePeriod = _DsH248VgwConnectionSilencePeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 2, 1, 1, 38),
    _DsH248VgwConnectionSilencePeriod_Type()
)
dsH248VgwConnectionSilencePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248VgwConnectionSilencePeriod.setStatus("current")
_DsAccGwyConfigH248Port_ObjectIdentity = ObjectIdentity
dsAccGwyConfigH248Port = _DsAccGwyConfigH248Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 1, 3)
)
_DsAccGwyH248Monitor_ObjectIdentity = ObjectIdentity
dsAccGwyH248Monitor = _DsAccGwyH248Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2)
)
_DsAccGwyMonitorH248Slot_ObjectIdentity = ObjectIdentity
dsAccGwyMonitorH248Slot = _DsAccGwyMonitorH248Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 1)
)
_DsAccGwyMonitorH248Vgw_ObjectIdentity = ObjectIdentity
dsAccGwyMonitorH248Vgw = _DsAccGwyMonitorH248Vgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2)
)
_DsAccGwyMonitorH248VgwTable_Object = MibTable
dsAccGwyMonitorH248VgwTable = _DsAccGwyMonitorH248VgwTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyMonitorH248VgwTable.setStatus("current")
_DsAccGwyMonitorH248VgwEntry_Object = MibTableRow
dsAccGwyMonitorH248VgwEntry = _DsAccGwyMonitorH248VgwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1)
)
dsAccGwyMonitorH248VgwEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-H248-MIB", "dsH248MonitorVgwIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyMonitorH248VgwEntry.setStatus("current")
_DsH248MonitorVgwIndex_Type = Integer32
_DsH248MonitorVgwIndex_Object = MibTableColumn
dsH248MonitorVgwIndex = _DsH248MonitorVgwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 1),
    _DsH248MonitorVgwIndex_Type()
)
dsH248MonitorVgwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwIndex.setStatus("current")


class _DsH248MonitorVgwGatewayOperStatus_Type(Integer32):
    """Custom type dsH248MonitorVgwGatewayOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_DsH248MonitorVgwGatewayOperStatus_Type.__name__ = "Integer32"
_DsH248MonitorVgwGatewayOperStatus_Object = MibTableColumn
dsH248MonitorVgwGatewayOperStatus = _DsH248MonitorVgwGatewayOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 2),
    _DsH248MonitorVgwGatewayOperStatus_Type()
)
dsH248MonitorVgwGatewayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayOperStatus.setStatus("current")
_DsH248MonitorVgwGatewayNumInMessages_Type = Unsigned32
_DsH248MonitorVgwGatewayNumInMessages_Object = MibTableColumn
dsH248MonitorVgwGatewayNumInMessages = _DsH248MonitorVgwGatewayNumInMessages_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 3),
    _DsH248MonitorVgwGatewayNumInMessages_Type()
)
dsH248MonitorVgwGatewayNumInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayNumInMessages.setStatus("current")
_DsH248MonitorVgwGatewayNumInOctets_Type = Unsigned32
_DsH248MonitorVgwGatewayNumInOctets_Object = MibTableColumn
dsH248MonitorVgwGatewayNumInOctets = _DsH248MonitorVgwGatewayNumInOctets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 4),
    _DsH248MonitorVgwGatewayNumInOctets_Type()
)
dsH248MonitorVgwGatewayNumInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayNumInOctets.setStatus("current")
_DsH248MonitorVgwGatewayNumOutMessage_Type = Unsigned32
_DsH248MonitorVgwGatewayNumOutMessage_Object = MibTableColumn
dsH248MonitorVgwGatewayNumOutMessage = _DsH248MonitorVgwGatewayNumOutMessage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 5),
    _DsH248MonitorVgwGatewayNumOutMessage_Type()
)
dsH248MonitorVgwGatewayNumOutMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayNumOutMessage.setStatus("current")
_DsH248MonitorVgwGatewayNumOutOctets_Type = Unsigned32
_DsH248MonitorVgwGatewayNumOutOctets_Object = MibTableColumn
dsH248MonitorVgwGatewayNumOutOctets = _DsH248MonitorVgwGatewayNumOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 6),
    _DsH248MonitorVgwGatewayNumOutOctets_Type()
)
dsH248MonitorVgwGatewayNumOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayNumOutOctets.setStatus("current")
_DsH248MonitorVgwGatewayNumErrors_Type = Unsigned32
_DsH248MonitorVgwGatewayNumErrors_Object = MibTableColumn
dsH248MonitorVgwGatewayNumErrors = _DsH248MonitorVgwGatewayNumErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 7),
    _DsH248MonitorVgwGatewayNumErrors_Type()
)
dsH248MonitorVgwGatewayNumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayNumErrors.setStatus("current")
_DsH248MonitorVgwGatewayNumTimerRecovery_Type = Unsigned32
_DsH248MonitorVgwGatewayNumTimerRecovery_Object = MibTableColumn
dsH248MonitorVgwGatewayNumTimerRecovery = _DsH248MonitorVgwGatewayNumTimerRecovery_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 8),
    _DsH248MonitorVgwGatewayNumTimerRecovery_Type()
)
dsH248MonitorVgwGatewayNumTimerRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayNumTimerRecovery.setStatus("current")
_DsH248MonitorVgwGatewayTransportNumLosses_Type = Unsigned32
_DsH248MonitorVgwGatewayTransportNumLosses_Object = MibTableColumn
dsH248MonitorVgwGatewayTransportNumLosses = _DsH248MonitorVgwGatewayTransportNumLosses_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 9),
    _DsH248MonitorVgwGatewayTransportNumLosses_Type()
)
dsH248MonitorVgwGatewayTransportNumLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayTransportNumLosses.setStatus("current")
_DsH248MonitorVgwGatewayTransportNumSwitchover_Type = Unsigned32
_DsH248MonitorVgwGatewayTransportNumSwitchover_Object = MibTableColumn
dsH248MonitorVgwGatewayTransportNumSwitchover = _DsH248MonitorVgwGatewayTransportNumSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 10),
    _DsH248MonitorVgwGatewayTransportNumSwitchover_Type()
)
dsH248MonitorVgwGatewayTransportNumSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayTransportNumSwitchover.setStatus("current")
_DsH248MonitorVgwGatewayTransportTotalNumAlarms_Type = Unsigned32
_DsH248MonitorVgwGatewayTransportTotalNumAlarms_Object = MibTableColumn
dsH248MonitorVgwGatewayTransportTotalNumAlarms = _DsH248MonitorVgwGatewayTransportTotalNumAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 11),
    _DsH248MonitorVgwGatewayTransportTotalNumAlarms_Type()
)
dsH248MonitorVgwGatewayTransportTotalNumAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayTransportTotalNumAlarms.setStatus("current")


class _DsH248MonitorVgwGatewayTransportLastEvent_Type(Integer32):
    """Custom type dsH248MonitorVgwGatewayTransportLastEvent based on Integer32"""
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
        *(("notApplicable", 1),
          ("other", 2),
          ("linkUp", 3),
          ("linkLoss", 4),
          ("persistentError", 5),
          ("linkShutdown", 6),
          ("switchOver", 7))
    )


_DsH248MonitorVgwGatewayTransportLastEvent_Type.__name__ = "Integer32"
_DsH248MonitorVgwGatewayTransportLastEvent_Object = MibTableColumn
dsH248MonitorVgwGatewayTransportLastEvent = _DsH248MonitorVgwGatewayTransportLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 12),
    _DsH248MonitorVgwGatewayTransportLastEvent_Type()
)
dsH248MonitorVgwGatewayTransportLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayTransportLastEvent.setStatus("current")
_DsH248MonitorVgwGatewayTransportLastEventTime_Type = TimeStamp
_DsH248MonitorVgwGatewayTransportLastEventTime_Object = MibTableColumn
dsH248MonitorVgwGatewayTransportLastEventTime = _DsH248MonitorVgwGatewayTransportLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 13),
    _DsH248MonitorVgwGatewayTransportLastEventTime_Type()
)
dsH248MonitorVgwGatewayTransportLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayTransportLastEventTime.setStatus("current")
_DsH248MonitorVgwGatewayLastStatisticsReset_Type = TimeStamp
_DsH248MonitorVgwGatewayLastStatisticsReset_Object = MibTableColumn
dsH248MonitorVgwGatewayLastStatisticsReset = _DsH248MonitorVgwGatewayLastStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 14),
    _DsH248MonitorVgwGatewayLastStatisticsReset_Type()
)
dsH248MonitorVgwGatewayLastStatisticsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayLastStatisticsReset.setStatus("current")
_DsH248MonitorVgwGatewayContexts_Type = DisplayString
_DsH248MonitorVgwGatewayContexts_Object = MibTableColumn
dsH248MonitorVgwGatewayContexts = _DsH248MonitorVgwGatewayContexts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 2, 1, 1, 15),
    _DsH248MonitorVgwGatewayContexts_Type()
)
dsH248MonitorVgwGatewayContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248MonitorVgwGatewayContexts.setStatus("current")
_DsAccGwyMonitorH248Port_ObjectIdentity = ObjectIdentity
dsAccGwyMonitorH248Port = _DsAccGwyMonitorH248Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 2, 3)
)
_DsAccGwyH248Control_ObjectIdentity = ObjectIdentity
dsAccGwyH248Control = _DsAccGwyH248Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 3)
)
_DsAccGwyControlH248Vgw_ObjectIdentity = ObjectIdentity
dsAccGwyControlH248Vgw = _DsAccGwyControlH248Vgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 3, 1)
)
_DsAccGwyControlH248VgwTable_Object = MibTable
dsAccGwyControlH248VgwTable = _DsAccGwyControlH248VgwTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyControlH248VgwTable.setStatus("current")
_DsAccGwyControlH248VgwEntry_Object = MibTableRow
dsAccGwyControlH248VgwEntry = _DsAccGwyControlH248VgwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 3, 1, 1, 1)
)
dsAccGwyControlH248VgwEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-H248-MIB", "dsH248ControlVgwIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyControlH248VgwEntry.setStatus("current")
_DsH248ControlVgwIndex_Type = Integer32
_DsH248ControlVgwIndex_Object = MibTableColumn
dsH248ControlVgwIndex = _DsH248ControlVgwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 3, 1, 1, 1, 1),
    _DsH248ControlVgwIndex_Type()
)
dsH248ControlVgwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsH248ControlVgwIndex.setStatus("current")


class _DsH248ControlVgwGatewayOperation_Type(Integer32):
    """Custom type dsH248ControlVgwGatewayOperation based on Integer32"""
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
        *(("start", 1),
          ("stop", 2),
          ("restart", 3),
          ("restart-idle", 4))
    )


_DsH248ControlVgwGatewayOperation_Type.__name__ = "Integer32"
_DsH248ControlVgwGatewayOperation_Object = MibTableColumn
dsH248ControlVgwGatewayOperation = _DsH248ControlVgwGatewayOperation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 3, 1, 1, 1, 2),
    _DsH248ControlVgwGatewayOperation_Type()
)
dsH248ControlVgwGatewayOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsH248ControlVgwGatewayOperation.setStatus("current")


class _DsH248ControlVgwGatewayResetStatistics_Type(Integer32):
    """Custom type dsH248ControlVgwGatewayResetStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_DsH248ControlVgwGatewayResetStatistics_Type.__name__ = "Integer32"
_DsH248ControlVgwGatewayResetStatistics_Object = MibTableColumn
dsH248ControlVgwGatewayResetStatistics = _DsH248ControlVgwGatewayResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 3, 3, 1, 1, 1, 3),
    _DsH248ControlVgwGatewayResetStatistics_Type()
)
dsH248ControlVgwGatewayResetStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsH248ControlVgwGatewayResetStatistics.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-ACCESS-SLOT-H248-MIB",
    **{"MediaGatewayId": MediaGatewayId,
       "dasanAccessMib": dasanAccessMib,
       "dasanAccGatewayMIBObjects": dasanAccGatewayMIBObjects,
       "dsAccGwyH248": dsAccGwyH248,
       "dsAccGwyH248Configuration": dsAccGwyH248Configuration,
       "dsAccGwyConfigH248Slot": dsAccGwyConfigH248Slot,
       "dsAccGwyConfigH248Vgw": dsAccGwyConfigH248Vgw,
       "dsAccGwyConfigH248VgwTable": dsAccGwyConfigH248VgwTable,
       "dsAccGwyConfigH248VgwEntry": dsAccGwyConfigH248VgwEntry,
       "dsH248VgwIndex": dsH248VgwIndex,
       "dsH248VgwGatewayID": dsH248VgwGatewayID,
       "dsH248VgwGatewayPhyTerminationStart": dsH248VgwGatewayPhyTerminationStart,
       "dsH248VgwGatewayPhyTerminationEnd": dsH248VgwGatewayPhyTerminationEnd,
       "dsH248VgwGatewayMediaPortStart": dsH248VgwGatewayMediaPortStart,
       "dsH248VgwGatewayMediaPortEnd": dsH248VgwGatewayMediaPortEnd,
       "dsH248VgwGatewayAddr": dsH248VgwGatewayAddr,
       "dsH248VgwGatewayPort": dsH248VgwGatewayPort,
       "dsH248VgwGatewayEncodingScheme": dsH248VgwGatewayEncodingScheme,
       "dsH248VgwGatewayProtocol": dsH248VgwGatewayProtocol,
       "dsH248VgwGatewaySignalingTptProtocol": dsH248VgwGatewaySignalingTptProtocol,
       "dsH248VgwGatewayControllerIPAddress1": dsH248VgwGatewayControllerIPAddress1,
       "dsH248VgwGatewayControllerIPAddress2": dsH248VgwGatewayControllerIPAddress2,
       "dsH248VgwGatewayControllerIPAddress3": dsH248VgwGatewayControllerIPAddress3,
       "dsH248VgwGatewayControllerIPAddress4": dsH248VgwGatewayControllerIPAddress4,
       "dsH248VgwGatewayControllerIPAddress5": dsH248VgwGatewayControllerIPAddress5,
       "dsH248VgwGatewayControllerPort1": dsH248VgwGatewayControllerPort1,
       "dsH248VgwGatewayControllerPort2": dsH248VgwGatewayControllerPort2,
       "dsH248VgwGatewayControllerPort3": dsH248VgwGatewayControllerPort3,
       "dsH248VgwGatewayControllerPort4": dsH248VgwGatewayControllerPort4,
       "dsH248VgwGatewayControllerPort5": dsH248VgwGatewayControllerPort5,
       "dsH248VgwPropertyRootMaxContexts": dsH248VgwPropertyRootMaxContexts,
       "dsH248VgwPropertyRootMaxTerminations": dsH248VgwPropertyRootMaxTerminations,
       "dsH248VgwTopology": dsH248VgwTopology,
       "dsH248VgwTimestamp": dsH248VgwTimestamp,
       "dsH248VgwNamingPhyTermination": dsH248VgwNamingPhyTermination,
       "dsH248VgwNamingRtpTermination": dsH248VgwNamingRtpTermination,
       "dsH248VgwPkgList": dsH248VgwPkgList,
       "dsH248VgwHeartBeatTime": dsH248VgwHeartBeatTime,
       "dsH248VgwRetransmissionTime": dsH248VgwRetransmissionTime,
       "dsH248VgwMaxRetransmissionCount": dsH248VgwMaxRetransmissionCount,
       "dsH248VgwDigitmap": dsH248VgwDigitmap,
       "dsH248VgwDigitmapLongTime": dsH248VgwDigitmapLongTime,
       "dsH248VgwDigitmapShortTime": dsH248VgwDigitmapShortTime,
       "dsH248VgwDigitmapStartTime": dsH248VgwDigitmapStartTime,
       "dsH248VgwDigitmapZTime": dsH248VgwDigitmapZTime,
       "dsH248VgwStartupType": dsH248VgwStartupType,
       "dsH248VgwConnectionSilencePeriod": dsH248VgwConnectionSilencePeriod,
       "dsAccGwyConfigH248Port": dsAccGwyConfigH248Port,
       "dsAccGwyH248Monitor": dsAccGwyH248Monitor,
       "dsAccGwyMonitorH248Slot": dsAccGwyMonitorH248Slot,
       "dsAccGwyMonitorH248Vgw": dsAccGwyMonitorH248Vgw,
       "dsAccGwyMonitorH248VgwTable": dsAccGwyMonitorH248VgwTable,
       "dsAccGwyMonitorH248VgwEntry": dsAccGwyMonitorH248VgwEntry,
       "dsH248MonitorVgwIndex": dsH248MonitorVgwIndex,
       "dsH248MonitorVgwGatewayOperStatus": dsH248MonitorVgwGatewayOperStatus,
       "dsH248MonitorVgwGatewayNumInMessages": dsH248MonitorVgwGatewayNumInMessages,
       "dsH248MonitorVgwGatewayNumInOctets": dsH248MonitorVgwGatewayNumInOctets,
       "dsH248MonitorVgwGatewayNumOutMessage": dsH248MonitorVgwGatewayNumOutMessage,
       "dsH248MonitorVgwGatewayNumOutOctets": dsH248MonitorVgwGatewayNumOutOctets,
       "dsH248MonitorVgwGatewayNumErrors": dsH248MonitorVgwGatewayNumErrors,
       "dsH248MonitorVgwGatewayNumTimerRecovery": dsH248MonitorVgwGatewayNumTimerRecovery,
       "dsH248MonitorVgwGatewayTransportNumLosses": dsH248MonitorVgwGatewayTransportNumLosses,
       "dsH248MonitorVgwGatewayTransportNumSwitchover": dsH248MonitorVgwGatewayTransportNumSwitchover,
       "dsH248MonitorVgwGatewayTransportTotalNumAlarms": dsH248MonitorVgwGatewayTransportTotalNumAlarms,
       "dsH248MonitorVgwGatewayTransportLastEvent": dsH248MonitorVgwGatewayTransportLastEvent,
       "dsH248MonitorVgwGatewayTransportLastEventTime": dsH248MonitorVgwGatewayTransportLastEventTime,
       "dsH248MonitorVgwGatewayLastStatisticsReset": dsH248MonitorVgwGatewayLastStatisticsReset,
       "dsH248MonitorVgwGatewayContexts": dsH248MonitorVgwGatewayContexts,
       "dsAccGwyMonitorH248Port": dsAccGwyMonitorH248Port,
       "dsAccGwyH248Control": dsAccGwyH248Control,
       "dsAccGwyControlH248Vgw": dsAccGwyControlH248Vgw,
       "dsAccGwyControlH248VgwTable": dsAccGwyControlH248VgwTable,
       "dsAccGwyControlH248VgwEntry": dsAccGwyControlH248VgwEntry,
       "dsH248ControlVgwIndex": dsH248ControlVgwIndex,
       "dsH248ControlVgwGatewayOperation": dsH248ControlVgwGatewayOperation,
       "dsH248ControlVgwGatewayResetStatistics": dsH248ControlVgwGatewayResetStatistics}
)
