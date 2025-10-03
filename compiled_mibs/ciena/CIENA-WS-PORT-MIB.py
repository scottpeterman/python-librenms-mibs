# SNMP MIB module (CIENA-WS-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-PORT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:11 2025
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

(Decimal1Dig,
 DescriptionString,
 EnabledDisabledEnum,
 MacString,
 PortId,
 PortName,
 ServiceDomainIdx,
 ServiceIdx,
 XcvrType) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "Decimal1Dig",
    "DescriptionString",
    "EnabledDisabledEnum",
    "MacString",
    "PortId",
    "PortName",
    "ServiceDomainIdx",
    "ServiceIdx",
    "XcvrType")

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

cienaWsPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7)
)
if mibBuilder.loadTexts:
    cienaWsPortMIB.setRevisions(
        ("2017-07-07 00:00",
         "2017-03-02 00:00",
         "2016-12-12 00:00",
         "2016-05-30 00:00",
         "2016-02-23 00:00",
         "2015-09-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortOperationalState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("invalid", 0),
          ("up", 1),
          ("down", 2),
          ("notauthenticated", 3),
          ("loopbacktx", 4),
          ("loopbackrx", 5),
          ("unequipped", 6))
    )



class PortSpeed(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              10000000,
              40000000,
              100000000)
        )
    )
    namedValues = NamedValues(
        *(("speedauto", -1),
          ("speed10gig", 10000000),
          ("speed40gig", 40000000),
          ("speed100gig", 100000000))
    )



class PortTypeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 5),
          ("ethernet10gig", 6),
          ("ethernet40gig", 7),
          ("ethernet100gig", 8))
    )



# MIB Managed Objects in the order of their OIDs

_CienaWsPortObjects_ObjectIdentity = ObjectIdentity
cienaWsPortObjects = _CienaWsPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 1)
)
_CienaWsPortConformance_ObjectIdentity = ObjectIdentity
cienaWsPortConformance = _CienaWsPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 2)
)
_CienaWsPortGroups_ObjectIdentity = ObjectIdentity
cienaWsPortGroups = _CienaWsPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 2, 1)
)
_CienaWsPortCompliances_ObjectIdentity = ObjectIdentity
cienaWsPortCompliances = _CienaWsPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 2, 2)
)
_CwsPortPortsTable_Object = MibTable
cwsPortPortsTable = _CwsPortPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 3)
)
if mibBuilder.loadTexts:
    cwsPortPortsTable.setStatus("current")
_CwsPortPortsEntry_Object = MibTableRow
cwsPortPortsEntry = _CwsPortPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 3, 1)
)
cwsPortPortsEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
)
if mibBuilder.loadTexts:
    cwsPortPortsEntry.setStatus("current")


class _CwsPortPortsPortId_Type(Integer32):
    """Custom type cwsPortPortsPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortPortsPortId_Type.__name__ = "Integer32"
_CwsPortPortsPortId_Object = MibTableColumn
cwsPortPortsPortId = _CwsPortPortsPortId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 3, 1, 1),
    _CwsPortPortsPortId_Type()
)
cwsPortPortsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortPortsPortId.setStatus("current")
_CwsPortIdTable_Object = MibTable
cwsPortIdTable = _CwsPortIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 4)
)
if mibBuilder.loadTexts:
    cwsPortIdTable.setStatus("current")
_CwsPortIdEntry_Object = MibTableRow
cwsPortIdEntry = _CwsPortIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 4, 1)
)
cwsPortIdEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortIdEntry.setStatus("current")


class _CwsPortIdTableSnmpKey_Type(Integer32):
    """Custom type cwsPortIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortIdTableSnmpKey_Object = MibTableColumn
cwsPortIdTableSnmpKey = _CwsPortIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 4, 1, 1),
    _CwsPortIdTableSnmpKey_Type()
)
cwsPortIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortIdTableSnmpKey.setStatus("current")
_CwsPortIdName_Type = PortName
_CwsPortIdName_Object = MibTableColumn
cwsPortIdName = _CwsPortIdName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 4, 1, 2),
    _CwsPortIdName_Type()
)
cwsPortIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortIdName.setStatus("current")
_CwsPortIdDescription_Type = DescriptionString
_CwsPortIdDescription_Object = MibTableColumn
cwsPortIdDescription = _CwsPortIdDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 4, 1, 3),
    _CwsPortIdDescription_Type()
)
cwsPortIdDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortIdDescription.setStatus("current")
_CwsPortIdPortType_Type = PortTypeEnum
_CwsPortIdPortType_Object = MibTableColumn
cwsPortIdPortType = _CwsPortIdPortType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 4, 1, 4),
    _CwsPortIdPortType_Type()
)
cwsPortIdPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortIdPortType.setStatus("current")
_CwsPortIdMacAddress_Type = MacString
_CwsPortIdMacAddress_Object = MibTableColumn
cwsPortIdMacAddress = _CwsPortIdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 4, 1, 5),
    _CwsPortIdMacAddress_Type()
)
cwsPortIdMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortIdMacAddress.setStatus("current")


class _CwsPortIdInterfaceType_Type(Integer32):
    """Custom type cwsPortIdInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inni", 0),
          ("uni", 1),
          ("enni", 2))
    )


_CwsPortIdInterfaceType_Type.__name__ = "Integer32"
_CwsPortIdInterfaceType_Object = MibTableColumn
cwsPortIdInterfaceType = _CwsPortIdInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 4, 1, 6),
    _CwsPortIdInterfaceType_Type()
)
cwsPortIdInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortIdInterfaceType.setStatus("current")
_CwsPortStateTable_Object = MibTable
cwsPortStateTable = _CwsPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 5)
)
if mibBuilder.loadTexts:
    cwsPortStateTable.setStatus("current")
_CwsPortStateEntry_Object = MibTableRow
cwsPortStateEntry = _CwsPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 5, 1)
)
cwsPortStateEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortStateEntry.setStatus("current")


class _CwsPortStateTableSnmpKey_Type(Integer32):
    """Custom type cwsPortStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortStateTableSnmpKey_Object = MibTableColumn
cwsPortStateTableSnmpKey = _CwsPortStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 5, 1, 1),
    _CwsPortStateTableSnmpKey_Type()
)
cwsPortStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortStateTableSnmpKey.setStatus("current")


class _CwsPortStateAdminState_Type(Integer32):
    """Custom type cwsPortStateAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CwsPortStateAdminState_Type.__name__ = "Integer32"
_CwsPortStateAdminState_Object = MibTableColumn
cwsPortStateAdminState = _CwsPortStateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 5, 1, 2),
    _CwsPortStateAdminState_Type()
)
cwsPortStateAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortStateAdminState.setStatus("current")
_CwsPortStateOperationalState_Type = PortOperationalState
_CwsPortStateOperationalState_Object = MibTableColumn
cwsPortStateOperationalState = _CwsPortStateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 5, 1, 3),
    _CwsPortStateOperationalState_Type()
)
cwsPortStateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortStateOperationalState.setStatus("current")


class _CwsPortStateOperationalStateDuration_Type(OctetString):
    """Custom type cwsPortStateOperationalStateDuration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CwsPortStateOperationalStateDuration_Type.__name__ = "OctetString"
_CwsPortStateOperationalStateDuration_Object = MibTableColumn
cwsPortStateOperationalStateDuration = _CwsPortStateOperationalStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 5, 1, 4),
    _CwsPortStateOperationalStateDuration_Type()
)
cwsPortStateOperationalStateDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortStateOperationalStateDuration.setStatus("current")
_CwsPortCapabilitiesTable_Object = MibTable
cwsPortCapabilitiesTable = _CwsPortCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 6)
)
if mibBuilder.loadTexts:
    cwsPortCapabilitiesTable.setStatus("current")
_CwsPortCapabilitiesEntry_Object = MibTableRow
cwsPortCapabilitiesEntry = _CwsPortCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 6, 1)
)
cwsPortCapabilitiesEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortCapabilitiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortCapabilitiesEntry.setStatus("current")


class _CwsPortCapabilitiesTableSnmpKey_Type(Integer32):
    """Custom type cwsPortCapabilitiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortCapabilitiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortCapabilitiesTableSnmpKey_Object = MibTableColumn
cwsPortCapabilitiesTableSnmpKey = _CwsPortCapabilitiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 6, 1, 1),
    _CwsPortCapabilitiesTableSnmpKey_Type()
)
cwsPortCapabilitiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortCapabilitiesTableSnmpKey.setStatus("current")


class _CwsPortCapabilitiesPortSpeeds_Type(Bits):
    """Custom type cwsPortCapabilitiesPortSpeeds based on Bits"""
    namedValues = NamedValues(
        *(("ethernet10gig", 3),
          ("ethernet40gig", 4),
          ("ethernet100gig", 5))
    )

_CwsPortCapabilitiesPortSpeeds_Type.__name__ = "Bits"
_CwsPortCapabilitiesPortSpeeds_Object = MibTableColumn
cwsPortCapabilitiesPortSpeeds = _CwsPortCapabilitiesPortSpeeds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 6, 1, 2),
    _CwsPortCapabilitiesPortSpeeds_Type()
)
cwsPortCapabilitiesPortSpeeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCapabilitiesPortSpeeds.setStatus("current")


class _CwsPortCapabilitiesDuplex_Type(Bits):
    """Custom type cwsPortCapabilitiesDuplex based on Bits"""
    namedValues = NamedValues(
        *(("half", 0),
          ("full", 1))
    )

_CwsPortCapabilitiesDuplex_Type.__name__ = "Bits"
_CwsPortCapabilitiesDuplex_Object = MibTableColumn
cwsPortCapabilitiesDuplex = _CwsPortCapabilitiesDuplex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 6, 1, 3),
    _CwsPortCapabilitiesDuplex_Type()
)
cwsPortCapabilitiesDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCapabilitiesDuplex.setStatus("current")


class _CwsPortCapabilitiesAutoNegotiation_Type(Bits):
    """Custom type cwsPortCapabilitiesAutoNegotiation based on Bits"""
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )

_CwsPortCapabilitiesAutoNegotiation_Type.__name__ = "Bits"
_CwsPortCapabilitiesAutoNegotiation_Object = MibTableColumn
cwsPortCapabilitiesAutoNegotiation = _CwsPortCapabilitiesAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 6, 1, 4),
    _CwsPortCapabilitiesAutoNegotiation_Type()
)
cwsPortCapabilitiesAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCapabilitiesAutoNegotiation.setStatus("current")


class _CwsPortCapabilitiesFlowControl_Type(Bits):
    """Custom type cwsPortCapabilitiesFlowControl based on Bits"""
    namedValues = NamedValues(
        *(("off", 0),
          ("atx", 1),
          ("arx", 2),
          ("symmetric", 3))
    )

_CwsPortCapabilitiesFlowControl_Type.__name__ = "Bits"
_CwsPortCapabilitiesFlowControl_Object = MibTableColumn
cwsPortCapabilitiesFlowControl = _CwsPortCapabilitiesFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 6, 1, 5),
    _CwsPortCapabilitiesFlowControl_Type()
)
cwsPortCapabilitiesFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCapabilitiesFlowControl.setStatus("current")
_CwsPortCapabilitiesFecSupport_Type = EnabledDisabledEnum
_CwsPortCapabilitiesFecSupport_Object = MibTableColumn
cwsPortCapabilitiesFecSupport = _CwsPortCapabilitiesFecSupport_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 6, 1, 6),
    _CwsPortCapabilitiesFecSupport_Type()
)
cwsPortCapabilitiesFecSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCapabilitiesFecSupport.setStatus("current")
_CwsPortPropertiesTable_Object = MibTable
cwsPortPropertiesTable = _CwsPortPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 7)
)
if mibBuilder.loadTexts:
    cwsPortPropertiesTable.setStatus("current")
_CwsPortPropertiesEntry_Object = MibTableRow
cwsPortPropertiesEntry = _CwsPortPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 7, 1)
)
cwsPortPropertiesEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortPropertiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortPropertiesEntry.setStatus("current")


class _CwsPortPropertiesTableSnmpKey_Type(Integer32):
    """Custom type cwsPortPropertiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortPropertiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortPropertiesTableSnmpKey_Object = MibTableColumn
cwsPortPropertiesTableSnmpKey = _CwsPortPropertiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 7, 1, 1),
    _CwsPortPropertiesTableSnmpKey_Type()
)
cwsPortPropertiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortPropertiesTableSnmpKey.setStatus("current")


class _CwsPortPropertiesLoopback_Type(Integer32):
    """Custom type cwsPortPropertiesLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("rx", 1),
          ("tx", 2))
    )


_CwsPortPropertiesLoopback_Type.__name__ = "Integer32"
_CwsPortPropertiesLoopback_Object = MibTableColumn
cwsPortPropertiesLoopback = _CwsPortPropertiesLoopback_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 7, 1, 2),
    _CwsPortPropertiesLoopback_Type()
)
cwsPortPropertiesLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortPropertiesLoopback.setStatus("current")
_CwsPortPropertiesServiceIndex_Type = ServiceIdx
_CwsPortPropertiesServiceIndex_Object = MibTableColumn
cwsPortPropertiesServiceIndex = _CwsPortPropertiesServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 7, 1, 3),
    _CwsPortPropertiesServiceIndex_Type()
)
cwsPortPropertiesServiceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortPropertiesServiceIndex.setStatus("current")
_CwsPortPropertiesServiceDomainIndex_Type = ServiceDomainIdx
_CwsPortPropertiesServiceDomainIndex_Object = MibTableColumn
cwsPortPropertiesServiceDomainIndex = _CwsPortPropertiesServiceDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 7, 1, 4),
    _CwsPortPropertiesServiceDomainIndex_Type()
)
cwsPortPropertiesServiceDomainIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortPropertiesServiceDomainIndex.setStatus("current")
_CwsPortPropertiesXcvrType_Type = XcvrType
_CwsPortPropertiesXcvrType_Object = MibTableColumn
cwsPortPropertiesXcvrType = _CwsPortPropertiesXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 7, 1, 5),
    _CwsPortPropertiesXcvrType_Type()
)
cwsPortPropertiesXcvrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortPropertiesXcvrType.setStatus("current")
_CwsPortEthernetTable_Object = MibTable
cwsPortEthernetTable = _CwsPortEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 8)
)
if mibBuilder.loadTexts:
    cwsPortEthernetTable.setStatus("current")
_CwsPortEthernetEntry_Object = MibTableRow
cwsPortEthernetEntry = _CwsPortEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 8, 1)
)
cwsPortEthernetEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortEthernetTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortEthernetEntry.setStatus("current")


class _CwsPortEthernetTableSnmpKey_Type(Integer32):
    """Custom type cwsPortEthernetTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortEthernetTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortEthernetTableSnmpKey_Object = MibTableColumn
cwsPortEthernetTableSnmpKey = _CwsPortEthernetTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 8, 1, 1),
    _CwsPortEthernetTableSnmpKey_Type()
)
cwsPortEthernetTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortEthernetTableSnmpKey.setStatus("current")
_CwsPortEthernetSpeed_Type = PortSpeed
_CwsPortEthernetSpeed_Object = MibTableColumn
cwsPortEthernetSpeed = _CwsPortEthernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 8, 1, 2),
    _CwsPortEthernetSpeed_Type()
)
cwsPortEthernetSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortEthernetSpeed.setStatus("current")
_CwsPortEthernetMaxFrameSize_Type = Unsigned32
_CwsPortEthernetMaxFrameSize_Object = MibTableColumn
cwsPortEthernetMaxFrameSize = _CwsPortEthernetMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 8, 1, 3),
    _CwsPortEthernetMaxFrameSize_Type()
)
cwsPortEthernetMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortEthernetMaxFrameSize.setStatus("current")


class _CwsPortEthernetPauseProfile_Type(Integer32):
    """Custom type cwsPortEthernetPauseProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("discard", 1)
    )


_CwsPortEthernetPauseProfile_Type.__name__ = "Integer32"
_CwsPortEthernetPauseProfile_Object = MibTableColumn
cwsPortEthernetPauseProfile = _CwsPortEthernetPauseProfile_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 8, 1, 4),
    _CwsPortEthernetPauseProfile_Type()
)
cwsPortEthernetPauseProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortEthernetPauseProfile.setStatus("current")
_CwsPortEthernetForwardErrorCorrection_Type = EnabledDisabledEnum
_CwsPortEthernetForwardErrorCorrection_Object = MibTableColumn
cwsPortEthernetForwardErrorCorrection = _CwsPortEthernetForwardErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 8, 1, 5),
    _CwsPortEthernetForwardErrorCorrection_Type()
)
cwsPortEthernetForwardErrorCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortEthernetForwardErrorCorrection.setStatus("current")
_CwsPortConditioningTable_Object = MibTable
cwsPortConditioningTable = _CwsPortConditioningTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 9)
)
if mibBuilder.loadTexts:
    cwsPortConditioningTable.setStatus("current")
_CwsPortConditioningEntry_Object = MibTableRow
cwsPortConditioningEntry = _CwsPortConditioningEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 9, 1)
)
cwsPortConditioningEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortConditioningTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortConditioningEntry.setStatus("current")


class _CwsPortConditioningTableSnmpKey_Type(Integer32):
    """Custom type cwsPortConditioningTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortConditioningTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortConditioningTableSnmpKey_Object = MibTableColumn
cwsPortConditioningTableSnmpKey = _CwsPortConditioningTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 9, 1, 1),
    _CwsPortConditioningTableSnmpKey_Type()
)
cwsPortConditioningTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortConditioningTableSnmpKey.setStatus("current")


class _CwsPortConditioningType_Type(Integer32):
    """Custom type cwsPortConditioningType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("laseroff", 1),
          ("ethernet", 2))
    )


_CwsPortConditioningType_Type.__name__ = "Integer32"
_CwsPortConditioningType_Object = MibTableColumn
cwsPortConditioningType = _CwsPortConditioningType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 9, 1, 2),
    _CwsPortConditioningType_Type()
)
cwsPortConditioningType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortConditioningType.setStatus("current")


class _CwsPortConditioningHoldoff_Type(Integer32):
    """Custom type cwsPortConditioningHoldoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("ms0", 0),
          ("ms100", 100),
          ("ms200", 200),
          ("ms300", 300),
          ("ms400", 400),
          ("ms500", 500),
          ("ms600", 600),
          ("ms700", 700),
          ("ms800", 800),
          ("ms900", 900),
          ("ms1000", 1000))
    )


_CwsPortConditioningHoldoff_Type.__name__ = "Integer32"
_CwsPortConditioningHoldoff_Object = MibTableColumn
cwsPortConditioningHoldoff = _CwsPortConditioningHoldoff_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 9, 1, 3),
    _CwsPortConditioningHoldoff_Type()
)
cwsPortConditioningHoldoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortConditioningHoldoff.setStatus("current")
_CwsPortCurrentTable_Object = MibTable
cwsPortCurrentTable = _CwsPortCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 10)
)
if mibBuilder.loadTexts:
    cwsPortCurrentTable.setStatus("current")
_CwsPortCurrentEntry_Object = MibTableRow
cwsPortCurrentEntry = _CwsPortCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 10, 1)
)
cwsPortCurrentEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortCurrentTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortCurrentEntry.setStatus("current")


class _CwsPortCurrentTableSnmpKey_Type(Integer32):
    """Custom type cwsPortCurrentTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortCurrentTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortCurrentTableSnmpKey_Object = MibTableColumn
cwsPortCurrentTableSnmpKey = _CwsPortCurrentTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 10, 1, 1),
    _CwsPortCurrentTableSnmpKey_Type()
)
cwsPortCurrentTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortCurrentTableSnmpKey.setStatus("current")
_CwsPortCurrentFrameErrorRatio_Type = Counter64
_CwsPortCurrentFrameErrorRatio_Object = MibTableColumn
cwsPortCurrentFrameErrorRatio = _CwsPortCurrentFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 10, 1, 2),
    _CwsPortCurrentFrameErrorRatio_Type()
)
cwsPortCurrentFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCurrentFrameErrorRatio.setStatus("current")
_CwsPortCurrentRxCountsTable_Object = MibTable
cwsPortCurrentRxCountsTable = _CwsPortCurrentRxCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11)
)
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsTable.setStatus("current")
_CwsPortCurrentRxCountsEntry_Object = MibTableRow
cwsPortCurrentRxCountsEntry = _CwsPortCurrentRxCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1)
)
cwsPortCurrentRxCountsEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsEntry.setStatus("current")


class _CwsPortCurrentRxCountsTableSnmpKey_Type(Integer32):
    """Custom type cwsPortCurrentRxCountsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortCurrentRxCountsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortCurrentRxCountsTableSnmpKey_Object = MibTableColumn
cwsPortCurrentRxCountsTableSnmpKey = _CwsPortCurrentRxCountsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 1),
    _CwsPortCurrentRxCountsTableSnmpKey_Type()
)
cwsPortCurrentRxCountsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsTableSnmpKey.setStatus("current")
_CwsPortCurrentRxCountsBytes_Type = Counter64
_CwsPortCurrentRxCountsBytes_Object = MibTableColumn
cwsPortCurrentRxCountsBytes = _CwsPortCurrentRxCountsBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 2),
    _CwsPortCurrentRxCountsBytes_Type()
)
cwsPortCurrentRxCountsBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsBytes.setStatus("current")
_CwsPortCurrentRxCountsPackets_Type = Counter64
_CwsPortCurrentRxCountsPackets_Object = MibTableColumn
cwsPortCurrentRxCountsPackets = _CwsPortCurrentRxCountsPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 3),
    _CwsPortCurrentRxCountsPackets_Type()
)
cwsPortCurrentRxCountsPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsPackets.setStatus("current")
_CwsPortCurrentRxCountsCrcErroredPackets_Type = Counter64
_CwsPortCurrentRxCountsCrcErroredPackets_Object = MibTableColumn
cwsPortCurrentRxCountsCrcErroredPackets = _CwsPortCurrentRxCountsCrcErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 4),
    _CwsPortCurrentRxCountsCrcErroredPackets_Type()
)
cwsPortCurrentRxCountsCrcErroredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsCrcErroredPackets.setStatus("current")
_CwsPortCurrentRxCountsMulticastPackets_Type = Counter64
_CwsPortCurrentRxCountsMulticastPackets_Object = MibTableColumn
cwsPortCurrentRxCountsMulticastPackets = _CwsPortCurrentRxCountsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 5),
    _CwsPortCurrentRxCountsMulticastPackets_Type()
)
cwsPortCurrentRxCountsMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsMulticastPackets.setStatus("current")
_CwsPortCurrentRxCountsBroadcastPackets_Type = Counter64
_CwsPortCurrentRxCountsBroadcastPackets_Object = MibTableColumn
cwsPortCurrentRxCountsBroadcastPackets = _CwsPortCurrentRxCountsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 6),
    _CwsPortCurrentRxCountsBroadcastPackets_Type()
)
cwsPortCurrentRxCountsBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsBroadcastPackets.setStatus("current")
_CwsPortCurrentRxCountsPausePackets_Type = Counter64
_CwsPortCurrentRxCountsPausePackets_Object = MibTableColumn
cwsPortCurrentRxCountsPausePackets = _CwsPortCurrentRxCountsPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 7),
    _CwsPortCurrentRxCountsPausePackets_Type()
)
cwsPortCurrentRxCountsPausePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsPausePackets.setStatus("current")
_CwsPortCurrentRxCountsUndersizedPackets_Type = Counter64
_CwsPortCurrentRxCountsUndersizedPackets_Object = MibTableColumn
cwsPortCurrentRxCountsUndersizedPackets = _CwsPortCurrentRxCountsUndersizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 8),
    _CwsPortCurrentRxCountsUndersizedPackets_Type()
)
cwsPortCurrentRxCountsUndersizedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsUndersizedPackets.setStatus("current")
_CwsPortCurrentRxCountsOversizedPackets_Type = Counter64
_CwsPortCurrentRxCountsOversizedPackets_Object = MibTableColumn
cwsPortCurrentRxCountsOversizedPackets = _CwsPortCurrentRxCountsOversizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 9),
    _CwsPortCurrentRxCountsOversizedPackets_Type()
)
cwsPortCurrentRxCountsOversizedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsOversizedPackets.setStatus("current")
_CwsPortCurrentRxCountsFragmentPackets_Type = Counter64
_CwsPortCurrentRxCountsFragmentPackets_Object = MibTableColumn
cwsPortCurrentRxCountsFragmentPackets = _CwsPortCurrentRxCountsFragmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 10),
    _CwsPortCurrentRxCountsFragmentPackets_Type()
)
cwsPortCurrentRxCountsFragmentPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsFragmentPackets.setStatus("current")
_CwsPortCurrentRxCountsJabberPackets_Type = Counter64
_CwsPortCurrentRxCountsJabberPackets_Object = MibTableColumn
cwsPortCurrentRxCountsJabberPackets = _CwsPortCurrentRxCountsJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 11),
    _CwsPortCurrentRxCountsJabberPackets_Type()
)
cwsPortCurrentRxCountsJabberPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsJabberPackets.setStatus("current")
_CwsPortCurrentRxCountsLengthOutRangePackets_Type = Counter64
_CwsPortCurrentRxCountsLengthOutRangePackets_Object = MibTableColumn
cwsPortCurrentRxCountsLengthOutRangePackets = _CwsPortCurrentRxCountsLengthOutRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 12),
    _CwsPortCurrentRxCountsLengthOutRangePackets_Type()
)
cwsPortCurrentRxCountsLengthOutRangePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsLengthOutRangePackets.setStatus("current")
_CwsPortCurrentRxCountsPackets64Octet_Type = Counter64
_CwsPortCurrentRxCountsPackets64Octet_Object = MibTableColumn
cwsPortCurrentRxCountsPackets64Octet = _CwsPortCurrentRxCountsPackets64Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 13),
    _CwsPortCurrentRxCountsPackets64Octet_Type()
)
cwsPortCurrentRxCountsPackets64Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsPackets64Octet.setStatus("current")
_CwsPortCurrentRxCountsPackets65127Octet_Type = Counter64
_CwsPortCurrentRxCountsPackets65127Octet_Object = MibTableColumn
cwsPortCurrentRxCountsPackets65127Octet = _CwsPortCurrentRxCountsPackets65127Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 14),
    _CwsPortCurrentRxCountsPackets65127Octet_Type()
)
cwsPortCurrentRxCountsPackets65127Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsPackets65127Octet.setStatus("current")
_CwsPortCurrentRxCountsPackets128255Octet_Type = Counter64
_CwsPortCurrentRxCountsPackets128255Octet_Object = MibTableColumn
cwsPortCurrentRxCountsPackets128255Octet = _CwsPortCurrentRxCountsPackets128255Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 15),
    _CwsPortCurrentRxCountsPackets128255Octet_Type()
)
cwsPortCurrentRxCountsPackets128255Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsPackets128255Octet.setStatus("current")
_CwsPortCurrentRxCountsPackets256511Octet_Type = Counter64
_CwsPortCurrentRxCountsPackets256511Octet_Object = MibTableColumn
cwsPortCurrentRxCountsPackets256511Octet = _CwsPortCurrentRxCountsPackets256511Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 16),
    _CwsPortCurrentRxCountsPackets256511Octet_Type()
)
cwsPortCurrentRxCountsPackets256511Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsPackets256511Octet.setStatus("current")
_CwsPortCurrentRxCountsPackets5121023Octet_Type = Counter64
_CwsPortCurrentRxCountsPackets5121023Octet_Object = MibTableColumn
cwsPortCurrentRxCountsPackets5121023Octet = _CwsPortCurrentRxCountsPackets5121023Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 17),
    _CwsPortCurrentRxCountsPackets5121023Octet_Type()
)
cwsPortCurrentRxCountsPackets5121023Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsPackets5121023Octet.setStatus("current")
_CwsPortCurrentRxCountsPackets10241518Octet_Type = Counter64
_CwsPortCurrentRxCountsPackets10241518Octet_Object = MibTableColumn
cwsPortCurrentRxCountsPackets10241518Octet = _CwsPortCurrentRxCountsPackets10241518Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 18),
    _CwsPortCurrentRxCountsPackets10241518Octet_Type()
)
cwsPortCurrentRxCountsPackets10241518Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsPackets10241518Octet.setStatus("current")
_CwsPortCurrentRxCountsAverageLinkUtilization_Type = Decimal1Dig
_CwsPortCurrentRxCountsAverageLinkUtilization_Object = MibTableColumn
cwsPortCurrentRxCountsAverageLinkUtilization = _CwsPortCurrentRxCountsAverageLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 11, 1, 19),
    _CwsPortCurrentRxCountsAverageLinkUtilization_Type()
)
cwsPortCurrentRxCountsAverageLinkUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentRxCountsAverageLinkUtilization.setStatus("current")
_CwsPortCurrentTxCountsTable_Object = MibTable
cwsPortCurrentTxCountsTable = _CwsPortCurrentTxCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12)
)
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsTable.setStatus("current")
_CwsPortCurrentTxCountsEntry_Object = MibTableRow
cwsPortCurrentTxCountsEntry = _CwsPortCurrentTxCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1)
)
cwsPortCurrentTxCountsEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsEntry.setStatus("current")


class _CwsPortCurrentTxCountsTableSnmpKey_Type(Integer32):
    """Custom type cwsPortCurrentTxCountsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortCurrentTxCountsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortCurrentTxCountsTableSnmpKey_Object = MibTableColumn
cwsPortCurrentTxCountsTableSnmpKey = _CwsPortCurrentTxCountsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 1),
    _CwsPortCurrentTxCountsTableSnmpKey_Type()
)
cwsPortCurrentTxCountsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsTableSnmpKey.setStatus("current")
_CwsPortCurrentTxCountsBytes_Type = Counter64
_CwsPortCurrentTxCountsBytes_Object = MibTableColumn
cwsPortCurrentTxCountsBytes = _CwsPortCurrentTxCountsBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 2),
    _CwsPortCurrentTxCountsBytes_Type()
)
cwsPortCurrentTxCountsBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsBytes.setStatus("current")
_CwsPortCurrentTxCountsPackets_Type = Counter64
_CwsPortCurrentTxCountsPackets_Object = MibTableColumn
cwsPortCurrentTxCountsPackets = _CwsPortCurrentTxCountsPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 3),
    _CwsPortCurrentTxCountsPackets_Type()
)
cwsPortCurrentTxCountsPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsPackets.setStatus("current")
_CwsPortCurrentTxCountsCrcErroredPackets_Type = Counter64
_CwsPortCurrentTxCountsCrcErroredPackets_Object = MibTableColumn
cwsPortCurrentTxCountsCrcErroredPackets = _CwsPortCurrentTxCountsCrcErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 4),
    _CwsPortCurrentTxCountsCrcErroredPackets_Type()
)
cwsPortCurrentTxCountsCrcErroredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsCrcErroredPackets.setStatus("current")
_CwsPortCurrentTxCountsMulticastPackets_Type = Counter64
_CwsPortCurrentTxCountsMulticastPackets_Object = MibTableColumn
cwsPortCurrentTxCountsMulticastPackets = _CwsPortCurrentTxCountsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 5),
    _CwsPortCurrentTxCountsMulticastPackets_Type()
)
cwsPortCurrentTxCountsMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsMulticastPackets.setStatus("current")
_CwsPortCurrentTxCountsBroadcastPackets_Type = Counter64
_CwsPortCurrentTxCountsBroadcastPackets_Object = MibTableColumn
cwsPortCurrentTxCountsBroadcastPackets = _CwsPortCurrentTxCountsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 6),
    _CwsPortCurrentTxCountsBroadcastPackets_Type()
)
cwsPortCurrentTxCountsBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsBroadcastPackets.setStatus("current")
_CwsPortCurrentTxCountsPausePackets_Type = Counter64
_CwsPortCurrentTxCountsPausePackets_Object = MibTableColumn
cwsPortCurrentTxCountsPausePackets = _CwsPortCurrentTxCountsPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 7),
    _CwsPortCurrentTxCountsPausePackets_Type()
)
cwsPortCurrentTxCountsPausePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsPausePackets.setStatus("current")
_CwsPortCurrentTxCountsExcessiveDeferredPackets_Type = Counter64
_CwsPortCurrentTxCountsExcessiveDeferredPackets_Object = MibTableColumn
cwsPortCurrentTxCountsExcessiveDeferredPackets = _CwsPortCurrentTxCountsExcessiveDeferredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 8),
    _CwsPortCurrentTxCountsExcessiveDeferredPackets_Type()
)
cwsPortCurrentTxCountsExcessiveDeferredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsExcessiveDeferredPackets.setStatus("current")
_CwsPortCurrentTxCountsGiantPackets_Type = Counter64
_CwsPortCurrentTxCountsGiantPackets_Object = MibTableColumn
cwsPortCurrentTxCountsGiantPackets = _CwsPortCurrentTxCountsGiantPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 9),
    _CwsPortCurrentTxCountsGiantPackets_Type()
)
cwsPortCurrentTxCountsGiantPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsGiantPackets.setStatus("current")
_CwsPortCurrentTxCountsUnderrunPackets_Type = Counter64
_CwsPortCurrentTxCountsUnderrunPackets_Object = MibTableColumn
cwsPortCurrentTxCountsUnderrunPackets = _CwsPortCurrentTxCountsUnderrunPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 10),
    _CwsPortCurrentTxCountsUnderrunPackets_Type()
)
cwsPortCurrentTxCountsUnderrunPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsUnderrunPackets.setStatus("current")
_CwsPortCurrentTxCountsLengthCheckErrorPackets_Type = Counter64
_CwsPortCurrentTxCountsLengthCheckErrorPackets_Object = MibTableColumn
cwsPortCurrentTxCountsLengthCheckErrorPackets = _CwsPortCurrentTxCountsLengthCheckErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 11),
    _CwsPortCurrentTxCountsLengthCheckErrorPackets_Type()
)
cwsPortCurrentTxCountsLengthCheckErrorPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsLengthCheckErrorPackets.setStatus("current")
_CwsPortCurrentTxCountsLengthOutRangePackets_Type = Counter64
_CwsPortCurrentTxCountsLengthOutRangePackets_Object = MibTableColumn
cwsPortCurrentTxCountsLengthOutRangePackets = _CwsPortCurrentTxCountsLengthOutRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 12),
    _CwsPortCurrentTxCountsLengthOutRangePackets_Type()
)
cwsPortCurrentTxCountsLengthOutRangePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsLengthOutRangePackets.setStatus("current")
_CwsPortCurrentTxCountsAverageLinkUtilization_Type = Decimal1Dig
_CwsPortCurrentTxCountsAverageLinkUtilization_Object = MibTableColumn
cwsPortCurrentTxCountsAverageLinkUtilization = _CwsPortCurrentTxCountsAverageLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 12, 1, 13),
    _CwsPortCurrentTxCountsAverageLinkUtilization_Type()
)
cwsPortCurrentTxCountsAverageLinkUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxCountsAverageLinkUtilization.setStatus("current")
_CwsPortCurrentTxQueueTable_Object = MibTable
cwsPortCurrentTxQueueTable = _CwsPortCurrentTxQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 13)
)
if mibBuilder.loadTexts:
    cwsPortCurrentTxQueueTable.setStatus("current")
_CwsPortCurrentTxQueueEntry_Object = MibTableRow
cwsPortCurrentTxQueueEntry = _CwsPortCurrentTxQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 13, 1)
)
cwsPortCurrentTxQueueEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortCurrentTxQueueTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortCurrentTxQueueEntry.setStatus("current")


class _CwsPortCurrentTxQueueTableSnmpKey_Type(Integer32):
    """Custom type cwsPortCurrentTxQueueTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortCurrentTxQueueTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortCurrentTxQueueTableSnmpKey_Object = MibTableColumn
cwsPortCurrentTxQueueTableSnmpKey = _CwsPortCurrentTxQueueTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 13, 1, 1),
    _CwsPortCurrentTxQueueTableSnmpKey_Type()
)
cwsPortCurrentTxQueueTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortCurrentTxQueueTableSnmpKey.setStatus("current")
_CwsPortCurrentTxQueuePacketDropCountSummary_Type = Counter64
_CwsPortCurrentTxQueuePacketDropCountSummary_Object = MibTableColumn
cwsPortCurrentTxQueuePacketDropCountSummary = _CwsPortCurrentTxQueuePacketDropCountSummary_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 13, 1, 2),
    _CwsPortCurrentTxQueuePacketDropCountSummary_Type()
)
cwsPortCurrentTxQueuePacketDropCountSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxQueuePacketDropCountSummary.setStatus("current")
_CwsPortCurrentTxQueueQ0PacketDropCount_Type = Counter64
_CwsPortCurrentTxQueueQ0PacketDropCount_Object = MibTableColumn
cwsPortCurrentTxQueueQ0PacketDropCount = _CwsPortCurrentTxQueueQ0PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 13, 1, 3),
    _CwsPortCurrentTxQueueQ0PacketDropCount_Type()
)
cwsPortCurrentTxQueueQ0PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxQueueQ0PacketDropCount.setStatus("current")
_CwsPortCurrentTxQueueQ1PacketDropCount_Type = Counter64
_CwsPortCurrentTxQueueQ1PacketDropCount_Object = MibTableColumn
cwsPortCurrentTxQueueQ1PacketDropCount = _CwsPortCurrentTxQueueQ1PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 13, 1, 4),
    _CwsPortCurrentTxQueueQ1PacketDropCount_Type()
)
cwsPortCurrentTxQueueQ1PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxQueueQ1PacketDropCount.setStatus("current")
_CwsPortCurrentTxQueueQ2PacketDropCount_Type = Counter64
_CwsPortCurrentTxQueueQ2PacketDropCount_Object = MibTableColumn
cwsPortCurrentTxQueueQ2PacketDropCount = _CwsPortCurrentTxQueueQ2PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 13, 1, 5),
    _CwsPortCurrentTxQueueQ2PacketDropCount_Type()
)
cwsPortCurrentTxQueueQ2PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxQueueQ2PacketDropCount.setStatus("current")
_CwsPortCurrentTxQueueQ3PacketDropCount_Type = Counter64
_CwsPortCurrentTxQueueQ3PacketDropCount_Object = MibTableColumn
cwsPortCurrentTxQueueQ3PacketDropCount = _CwsPortCurrentTxQueueQ3PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 13, 1, 6),
    _CwsPortCurrentTxQueueQ3PacketDropCount_Type()
)
cwsPortCurrentTxQueueQ3PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxQueueQ3PacketDropCount.setStatus("current")
_CwsPortCurrentTxQueueQ4PacketDropCount_Type = Counter64
_CwsPortCurrentTxQueueQ4PacketDropCount_Object = MibTableColumn
cwsPortCurrentTxQueueQ4PacketDropCount = _CwsPortCurrentTxQueueQ4PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 13, 1, 7),
    _CwsPortCurrentTxQueueQ4PacketDropCount_Type()
)
cwsPortCurrentTxQueueQ4PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxQueueQ4PacketDropCount.setStatus("current")
_CwsPortCurrentTxQueueQ5PacketDropCount_Type = Counter64
_CwsPortCurrentTxQueueQ5PacketDropCount_Object = MibTableColumn
cwsPortCurrentTxQueueQ5PacketDropCount = _CwsPortCurrentTxQueueQ5PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 13, 1, 8),
    _CwsPortCurrentTxQueueQ5PacketDropCount_Type()
)
cwsPortCurrentTxQueueQ5PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxQueueQ5PacketDropCount.setStatus("current")
_CwsPortCurrentTxQueueQ6PacketDropCount_Type = Counter64
_CwsPortCurrentTxQueueQ6PacketDropCount_Object = MibTableColumn
cwsPortCurrentTxQueueQ6PacketDropCount = _CwsPortCurrentTxQueueQ6PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 13, 1, 9),
    _CwsPortCurrentTxQueueQ6PacketDropCount_Type()
)
cwsPortCurrentTxQueueQ6PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxQueueQ6PacketDropCount.setStatus("current")
_CwsPortCurrentTxQueueQ7PacketDropCount_Type = Counter64
_CwsPortCurrentTxQueueQ7PacketDropCount_Object = MibTableColumn
cwsPortCurrentTxQueueQ7PacketDropCount = _CwsPortCurrentTxQueueQ7PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 13, 1, 10),
    _CwsPortCurrentTxQueueQ7PacketDropCount_Type()
)
cwsPortCurrentTxQueueQ7PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentTxQueueQ7PacketDropCount.setStatus("current")
_CwsPortCurrentMacTable_Object = MibTable
cwsPortCurrentMacTable = _CwsPortCurrentMacTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 14)
)
if mibBuilder.loadTexts:
    cwsPortCurrentMacTable.setStatus("obsolete")
_CwsPortCurrentMacEntry_Object = MibTableRow
cwsPortCurrentMacEntry = _CwsPortCurrentMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 14, 1)
)
cwsPortCurrentMacEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortCurrentMacTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortCurrentMacEntry.setStatus("obsolete")


class _CwsPortCurrentMacTableSnmpKey_Type(Integer32):
    """Custom type cwsPortCurrentMacTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortCurrentMacTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortCurrentMacTableSnmpKey_Object = MibTableColumn
cwsPortCurrentMacTableSnmpKey = _CwsPortCurrentMacTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 14, 1, 1),
    _CwsPortCurrentMacTableSnmpKey_Type()
)
cwsPortCurrentMacTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortCurrentMacTableSnmpKey.setStatus("current")
_CwsPortCurrentMacUnavailableSeconds_Type = Counter64
_CwsPortCurrentMacUnavailableSeconds_Object = MibTableColumn
cwsPortCurrentMacUnavailableSeconds = _CwsPortCurrentMacUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 14, 1, 2),
    _CwsPortCurrentMacUnavailableSeconds_Type()
)
cwsPortCurrentMacUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCurrentMacUnavailableSeconds.setStatus("obsolete")
_CwsPortPcsCurrentTable_Object = MibTable
cwsPortPcsCurrentTable = _CwsPortPcsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 15)
)
if mibBuilder.loadTexts:
    cwsPortPcsCurrentTable.setStatus("current")
_CwsPortPcsCurrentEntry_Object = MibTableRow
cwsPortPcsCurrentEntry = _CwsPortPcsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 15, 1)
)
cwsPortPcsCurrentEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortPcsCurrentTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortPcsCurrentEntry.setStatus("current")


class _CwsPortPcsCurrentTableSnmpKey_Type(Integer32):
    """Custom type cwsPortPcsCurrentTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortPcsCurrentTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortPcsCurrentTableSnmpKey_Object = MibTableColumn
cwsPortPcsCurrentTableSnmpKey = _CwsPortPcsCurrentTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 15, 1, 1),
    _CwsPortPcsCurrentTableSnmpKey_Type()
)
cwsPortPcsCurrentTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortPcsCurrentTableSnmpKey.setStatus("current")
_CwsPortPcsCurrentErroredSeconds_Type = Counter64
_CwsPortPcsCurrentErroredSeconds_Object = MibTableColumn
cwsPortPcsCurrentErroredSeconds = _CwsPortPcsCurrentErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 15, 1, 2),
    _CwsPortPcsCurrentErroredSeconds_Type()
)
cwsPortPcsCurrentErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortPcsCurrentErroredSeconds.setStatus("current")
_CwsPortPcsCurrentSeverelyErroredSeconds_Type = Counter64
_CwsPortPcsCurrentSeverelyErroredSeconds_Object = MibTableColumn
cwsPortPcsCurrentSeverelyErroredSeconds = _CwsPortPcsCurrentSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 15, 1, 3),
    _CwsPortPcsCurrentSeverelyErroredSeconds_Type()
)
cwsPortPcsCurrentSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortPcsCurrentSeverelyErroredSeconds.setStatus("current")
_CwsPortPcsCurrentUnavailableSeconds_Type = Counter64
_CwsPortPcsCurrentUnavailableSeconds_Object = MibTableColumn
cwsPortPcsCurrentUnavailableSeconds = _CwsPortPcsCurrentUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 15, 1, 4),
    _CwsPortPcsCurrentUnavailableSeconds_Type()
)
cwsPortPcsCurrentUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortPcsCurrentUnavailableSeconds.setStatus("current")
_CwsPortCurrentPcsSyncHeaderErrorsTable_Object = MibTable
cwsPortCurrentPcsSyncHeaderErrorsTable = _CwsPortCurrentPcsSyncHeaderErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 16)
)
if mibBuilder.loadTexts:
    cwsPortCurrentPcsSyncHeaderErrorsTable.setStatus("current")
_CwsPortCurrentPcsSyncHeaderErrorsEntry_Object = MibTableRow
cwsPortCurrentPcsSyncHeaderErrorsEntry = _CwsPortCurrentPcsSyncHeaderErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 16, 1)
)
cwsPortCurrentPcsSyncHeaderErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortCurrentPcsSyncHeaderErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortCurrentPcsSyncHeaderErrorsEntry.setStatus("current")


class _CwsPortCurrentPcsSyncHeaderErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPortCurrentPcsSyncHeaderErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortCurrentPcsSyncHeaderErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortCurrentPcsSyncHeaderErrorsTableSnmpKey_Object = MibTableColumn
cwsPortCurrentPcsSyncHeaderErrorsTableSnmpKey = _CwsPortCurrentPcsSyncHeaderErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 16, 1, 1),
    _CwsPortCurrentPcsSyncHeaderErrorsTableSnmpKey_Type()
)
cwsPortCurrentPcsSyncHeaderErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortCurrentPcsSyncHeaderErrorsTableSnmpKey.setStatus("current")
_CwsPortCurrentPcsSyncHeaderErrorsCount_Type = Counter64
_CwsPortCurrentPcsSyncHeaderErrorsCount_Object = MibTableColumn
cwsPortCurrentPcsSyncHeaderErrorsCount = _CwsPortCurrentPcsSyncHeaderErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 16, 1, 2),
    _CwsPortCurrentPcsSyncHeaderErrorsCount_Type()
)
cwsPortCurrentPcsSyncHeaderErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCurrentPcsSyncHeaderErrorsCount.setStatus("current")
_CwsPortCurrentPcsBlockErrorsTable_Object = MibTable
cwsPortCurrentPcsBlockErrorsTable = _CwsPortCurrentPcsBlockErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 17)
)
if mibBuilder.loadTexts:
    cwsPortCurrentPcsBlockErrorsTable.setStatus("current")
_CwsPortCurrentPcsBlockErrorsEntry_Object = MibTableRow
cwsPortCurrentPcsBlockErrorsEntry = _CwsPortCurrentPcsBlockErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 17, 1)
)
cwsPortCurrentPcsBlockErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortCurrentPcsBlockErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortCurrentPcsBlockErrorsEntry.setStatus("current")


class _CwsPortCurrentPcsBlockErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPortCurrentPcsBlockErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortCurrentPcsBlockErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortCurrentPcsBlockErrorsTableSnmpKey_Object = MibTableColumn
cwsPortCurrentPcsBlockErrorsTableSnmpKey = _CwsPortCurrentPcsBlockErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 17, 1, 1),
    _CwsPortCurrentPcsBlockErrorsTableSnmpKey_Type()
)
cwsPortCurrentPcsBlockErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortCurrentPcsBlockErrorsTableSnmpKey.setStatus("current")
_CwsPortCurrentPcsBlockErrorsCount_Type = Counter64
_CwsPortCurrentPcsBlockErrorsCount_Object = MibTableColumn
cwsPortCurrentPcsBlockErrorsCount = _CwsPortCurrentPcsBlockErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 17, 1, 2),
    _CwsPortCurrentPcsBlockErrorsCount_Type()
)
cwsPortCurrentPcsBlockErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCurrentPcsBlockErrorsCount.setStatus("current")
_CwsPortCurrentPcsMultilaneBipErrorsTable_Object = MibTable
cwsPortCurrentPcsMultilaneBipErrorsTable = _CwsPortCurrentPcsMultilaneBipErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 18)
)
if mibBuilder.loadTexts:
    cwsPortCurrentPcsMultilaneBipErrorsTable.setStatus("current")
_CwsPortCurrentPcsMultilaneBipErrorsEntry_Object = MibTableRow
cwsPortCurrentPcsMultilaneBipErrorsEntry = _CwsPortCurrentPcsMultilaneBipErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 18, 1)
)
cwsPortCurrentPcsMultilaneBipErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortCurrentPcsMultilaneBipErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortCurrentPcsMultilaneBipErrorsEntry.setStatus("current")


class _CwsPortCurrentPcsMultilaneBipErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPortCurrentPcsMultilaneBipErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortCurrentPcsMultilaneBipErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortCurrentPcsMultilaneBipErrorsTableSnmpKey_Object = MibTableColumn
cwsPortCurrentPcsMultilaneBipErrorsTableSnmpKey = _CwsPortCurrentPcsMultilaneBipErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 18, 1, 1),
    _CwsPortCurrentPcsMultilaneBipErrorsTableSnmpKey_Type()
)
cwsPortCurrentPcsMultilaneBipErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortCurrentPcsMultilaneBipErrorsTableSnmpKey.setStatus("current")
_CwsPortCurrentPcsMultilaneBipErrorsCount_Type = Counter64
_CwsPortCurrentPcsMultilaneBipErrorsCount_Object = MibTableColumn
cwsPortCurrentPcsMultilaneBipErrorsCount = _CwsPortCurrentPcsMultilaneBipErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 18, 1, 2),
    _CwsPortCurrentPcsMultilaneBipErrorsCount_Type()
)
cwsPortCurrentPcsMultilaneBipErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCurrentPcsMultilaneBipErrorsCount.setStatus("current")
_CwsPortCurrentFecTable_Object = MibTable
cwsPortCurrentFecTable = _CwsPortCurrentFecTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 19)
)
if mibBuilder.loadTexts:
    cwsPortCurrentFecTable.setStatus("current")
_CwsPortCurrentFecEntry_Object = MibTableRow
cwsPortCurrentFecEntry = _CwsPortCurrentFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 19, 1)
)
cwsPortCurrentFecEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortCurrentFecTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortCurrentFecEntry.setStatus("current")


class _CwsPortCurrentFecTableSnmpKey_Type(Integer32):
    """Custom type cwsPortCurrentFecTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortCurrentFecTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortCurrentFecTableSnmpKey_Object = MibTableColumn
cwsPortCurrentFecTableSnmpKey = _CwsPortCurrentFecTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 19, 1, 1),
    _CwsPortCurrentFecTableSnmpKey_Type()
)
cwsPortCurrentFecTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortCurrentFecTableSnmpKey.setStatus("current")
_CwsPortCurrentFecCorrectedBlockCount_Type = Counter64
_CwsPortCurrentFecCorrectedBlockCount_Object = MibTableColumn
cwsPortCurrentFecCorrectedBlockCount = _CwsPortCurrentFecCorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 19, 1, 2),
    _CwsPortCurrentFecCorrectedBlockCount_Type()
)
cwsPortCurrentFecCorrectedBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCurrentFecCorrectedBlockCount.setStatus("current")
_CwsPortCurrentFecUncorrectedBlockCount_Type = Counter64
_CwsPortCurrentFecUncorrectedBlockCount_Object = MibTableColumn
cwsPortCurrentFecUncorrectedBlockCount = _CwsPortCurrentFecUncorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 19, 1, 3),
    _CwsPortCurrentFecUncorrectedBlockCount_Type()
)
cwsPortCurrentFecUncorrectedBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCurrentFecUncorrectedBlockCount.setStatus("current")
_CwsPortCurrentFecSymbolErrorCount_Type = Counter64
_CwsPortCurrentFecSymbolErrorCount_Object = MibTableColumn
cwsPortCurrentFecSymbolErrorCount = _CwsPortCurrentFecSymbolErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 19, 1, 4),
    _CwsPortCurrentFecSymbolErrorCount_Type()
)
cwsPortCurrentFecSymbolErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortCurrentFecSymbolErrorCount.setStatus("current")
_CwsPortTotalTable_Object = MibTable
cwsPortTotalTable = _CwsPortTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 20)
)
if mibBuilder.loadTexts:
    cwsPortTotalTable.setStatus("current")
_CwsPortTotalEntry_Object = MibTableRow
cwsPortTotalEntry = _CwsPortTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 20, 1)
)
cwsPortTotalEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortTotalTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortTotalEntry.setStatus("current")


class _CwsPortTotalTableSnmpKey_Type(Integer32):
    """Custom type cwsPortTotalTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortTotalTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortTotalTableSnmpKey_Object = MibTableColumn
cwsPortTotalTableSnmpKey = _CwsPortTotalTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 20, 1, 1),
    _CwsPortTotalTableSnmpKey_Type()
)
cwsPortTotalTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortTotalTableSnmpKey.setStatus("current")
_CwsPortTotalFrameErrorRatio_Type = Counter64
_CwsPortTotalFrameErrorRatio_Object = MibTableColumn
cwsPortTotalFrameErrorRatio = _CwsPortTotalFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 20, 1, 2),
    _CwsPortTotalFrameErrorRatio_Type()
)
cwsPortTotalFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortTotalFrameErrorRatio.setStatus("current")
_CwsPortTotalRxCountsTable_Object = MibTable
cwsPortTotalRxCountsTable = _CwsPortTotalRxCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21)
)
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsTable.setStatus("current")
_CwsPortTotalRxCountsEntry_Object = MibTableRow
cwsPortTotalRxCountsEntry = _CwsPortTotalRxCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1)
)
cwsPortTotalRxCountsEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsEntry.setStatus("current")


class _CwsPortTotalRxCountsTableSnmpKey_Type(Integer32):
    """Custom type cwsPortTotalRxCountsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortTotalRxCountsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortTotalRxCountsTableSnmpKey_Object = MibTableColumn
cwsPortTotalRxCountsTableSnmpKey = _CwsPortTotalRxCountsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 1),
    _CwsPortTotalRxCountsTableSnmpKey_Type()
)
cwsPortTotalRxCountsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsTableSnmpKey.setStatus("current")
_CwsPortTotalRxCountsBytes_Type = Counter64
_CwsPortTotalRxCountsBytes_Object = MibTableColumn
cwsPortTotalRxCountsBytes = _CwsPortTotalRxCountsBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 2),
    _CwsPortTotalRxCountsBytes_Type()
)
cwsPortTotalRxCountsBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsBytes.setStatus("current")
_CwsPortTotalRxCountsPackets_Type = Counter64
_CwsPortTotalRxCountsPackets_Object = MibTableColumn
cwsPortTotalRxCountsPackets = _CwsPortTotalRxCountsPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 3),
    _CwsPortTotalRxCountsPackets_Type()
)
cwsPortTotalRxCountsPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsPackets.setStatus("current")
_CwsPortTotalRxCountsCrcErroredPackets_Type = Counter64
_CwsPortTotalRxCountsCrcErroredPackets_Object = MibTableColumn
cwsPortTotalRxCountsCrcErroredPackets = _CwsPortTotalRxCountsCrcErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 4),
    _CwsPortTotalRxCountsCrcErroredPackets_Type()
)
cwsPortTotalRxCountsCrcErroredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsCrcErroredPackets.setStatus("current")
_CwsPortTotalRxCountsMulticastPackets_Type = Counter64
_CwsPortTotalRxCountsMulticastPackets_Object = MibTableColumn
cwsPortTotalRxCountsMulticastPackets = _CwsPortTotalRxCountsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 5),
    _CwsPortTotalRxCountsMulticastPackets_Type()
)
cwsPortTotalRxCountsMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsMulticastPackets.setStatus("current")
_CwsPortTotalRxCountsBroadcastPackets_Type = Counter64
_CwsPortTotalRxCountsBroadcastPackets_Object = MibTableColumn
cwsPortTotalRxCountsBroadcastPackets = _CwsPortTotalRxCountsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 6),
    _CwsPortTotalRxCountsBroadcastPackets_Type()
)
cwsPortTotalRxCountsBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsBroadcastPackets.setStatus("current")
_CwsPortTotalRxCountsPausePackets_Type = Counter64
_CwsPortTotalRxCountsPausePackets_Object = MibTableColumn
cwsPortTotalRxCountsPausePackets = _CwsPortTotalRxCountsPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 7),
    _CwsPortTotalRxCountsPausePackets_Type()
)
cwsPortTotalRxCountsPausePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsPausePackets.setStatus("current")
_CwsPortTotalRxCountsUndersizedPackets_Type = Counter64
_CwsPortTotalRxCountsUndersizedPackets_Object = MibTableColumn
cwsPortTotalRxCountsUndersizedPackets = _CwsPortTotalRxCountsUndersizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 8),
    _CwsPortTotalRxCountsUndersizedPackets_Type()
)
cwsPortTotalRxCountsUndersizedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsUndersizedPackets.setStatus("current")
_CwsPortTotalRxCountsOversizedPackets_Type = Counter64
_CwsPortTotalRxCountsOversizedPackets_Object = MibTableColumn
cwsPortTotalRxCountsOversizedPackets = _CwsPortTotalRxCountsOversizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 9),
    _CwsPortTotalRxCountsOversizedPackets_Type()
)
cwsPortTotalRxCountsOversizedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsOversizedPackets.setStatus("current")
_CwsPortTotalRxCountsFragmentPackets_Type = Counter64
_CwsPortTotalRxCountsFragmentPackets_Object = MibTableColumn
cwsPortTotalRxCountsFragmentPackets = _CwsPortTotalRxCountsFragmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 10),
    _CwsPortTotalRxCountsFragmentPackets_Type()
)
cwsPortTotalRxCountsFragmentPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsFragmentPackets.setStatus("current")
_CwsPortTotalRxCountsJabberPackets_Type = Counter64
_CwsPortTotalRxCountsJabberPackets_Object = MibTableColumn
cwsPortTotalRxCountsJabberPackets = _CwsPortTotalRxCountsJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 11),
    _CwsPortTotalRxCountsJabberPackets_Type()
)
cwsPortTotalRxCountsJabberPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsJabberPackets.setStatus("current")
_CwsPortTotalRxCountsLengthOutRangePackets_Type = Counter64
_CwsPortTotalRxCountsLengthOutRangePackets_Object = MibTableColumn
cwsPortTotalRxCountsLengthOutRangePackets = _CwsPortTotalRxCountsLengthOutRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 12),
    _CwsPortTotalRxCountsLengthOutRangePackets_Type()
)
cwsPortTotalRxCountsLengthOutRangePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsLengthOutRangePackets.setStatus("current")
_CwsPortTotalRxCountsPackets64Octet_Type = Counter64
_CwsPortTotalRxCountsPackets64Octet_Object = MibTableColumn
cwsPortTotalRxCountsPackets64Octet = _CwsPortTotalRxCountsPackets64Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 13),
    _CwsPortTotalRxCountsPackets64Octet_Type()
)
cwsPortTotalRxCountsPackets64Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsPackets64Octet.setStatus("current")
_CwsPortTotalRxCountsPackets65127Octet_Type = Counter64
_CwsPortTotalRxCountsPackets65127Octet_Object = MibTableColumn
cwsPortTotalRxCountsPackets65127Octet = _CwsPortTotalRxCountsPackets65127Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 14),
    _CwsPortTotalRxCountsPackets65127Octet_Type()
)
cwsPortTotalRxCountsPackets65127Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsPackets65127Octet.setStatus("current")
_CwsPortTotalRxCountsPackets128255Octet_Type = Counter64
_CwsPortTotalRxCountsPackets128255Octet_Object = MibTableColumn
cwsPortTotalRxCountsPackets128255Octet = _CwsPortTotalRxCountsPackets128255Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 15),
    _CwsPortTotalRxCountsPackets128255Octet_Type()
)
cwsPortTotalRxCountsPackets128255Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsPackets128255Octet.setStatus("current")
_CwsPortTotalRxCountsPackets256511Octet_Type = Counter64
_CwsPortTotalRxCountsPackets256511Octet_Object = MibTableColumn
cwsPortTotalRxCountsPackets256511Octet = _CwsPortTotalRxCountsPackets256511Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 16),
    _CwsPortTotalRxCountsPackets256511Octet_Type()
)
cwsPortTotalRxCountsPackets256511Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsPackets256511Octet.setStatus("current")
_CwsPortTotalRxCountsPackets5121023Octet_Type = Counter64
_CwsPortTotalRxCountsPackets5121023Octet_Object = MibTableColumn
cwsPortTotalRxCountsPackets5121023Octet = _CwsPortTotalRxCountsPackets5121023Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 17),
    _CwsPortTotalRxCountsPackets5121023Octet_Type()
)
cwsPortTotalRxCountsPackets5121023Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsPackets5121023Octet.setStatus("current")
_CwsPortTotalRxCountsPackets10241518Octet_Type = Counter64
_CwsPortTotalRxCountsPackets10241518Octet_Object = MibTableColumn
cwsPortTotalRxCountsPackets10241518Octet = _CwsPortTotalRxCountsPackets10241518Octet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 18),
    _CwsPortTotalRxCountsPackets10241518Octet_Type()
)
cwsPortTotalRxCountsPackets10241518Octet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsPackets10241518Octet.setStatus("current")
_CwsPortTotalRxCountsAverageLinkUtilization_Type = Decimal1Dig
_CwsPortTotalRxCountsAverageLinkUtilization_Object = MibTableColumn
cwsPortTotalRxCountsAverageLinkUtilization = _CwsPortTotalRxCountsAverageLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 21, 1, 19),
    _CwsPortTotalRxCountsAverageLinkUtilization_Type()
)
cwsPortTotalRxCountsAverageLinkUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalRxCountsAverageLinkUtilization.setStatus("current")
_CwsPortTotalTxCountsTable_Object = MibTable
cwsPortTotalTxCountsTable = _CwsPortTotalTxCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22)
)
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsTable.setStatus("current")
_CwsPortTotalTxCountsEntry_Object = MibTableRow
cwsPortTotalTxCountsEntry = _CwsPortTotalTxCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1)
)
cwsPortTotalTxCountsEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsEntry.setStatus("current")


class _CwsPortTotalTxCountsTableSnmpKey_Type(Integer32):
    """Custom type cwsPortTotalTxCountsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortTotalTxCountsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortTotalTxCountsTableSnmpKey_Object = MibTableColumn
cwsPortTotalTxCountsTableSnmpKey = _CwsPortTotalTxCountsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 1),
    _CwsPortTotalTxCountsTableSnmpKey_Type()
)
cwsPortTotalTxCountsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsTableSnmpKey.setStatus("current")
_CwsPortTotalTxCountsBytes_Type = Counter64
_CwsPortTotalTxCountsBytes_Object = MibTableColumn
cwsPortTotalTxCountsBytes = _CwsPortTotalTxCountsBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 2),
    _CwsPortTotalTxCountsBytes_Type()
)
cwsPortTotalTxCountsBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsBytes.setStatus("current")
_CwsPortTotalTxCountsPackets_Type = Counter64
_CwsPortTotalTxCountsPackets_Object = MibTableColumn
cwsPortTotalTxCountsPackets = _CwsPortTotalTxCountsPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 3),
    _CwsPortTotalTxCountsPackets_Type()
)
cwsPortTotalTxCountsPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsPackets.setStatus("current")
_CwsPortTotalTxCountsCrcErroredPackets_Type = Counter64
_CwsPortTotalTxCountsCrcErroredPackets_Object = MibTableColumn
cwsPortTotalTxCountsCrcErroredPackets = _CwsPortTotalTxCountsCrcErroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 4),
    _CwsPortTotalTxCountsCrcErroredPackets_Type()
)
cwsPortTotalTxCountsCrcErroredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsCrcErroredPackets.setStatus("current")
_CwsPortTotalTxCountsMulticastPackets_Type = Counter64
_CwsPortTotalTxCountsMulticastPackets_Object = MibTableColumn
cwsPortTotalTxCountsMulticastPackets = _CwsPortTotalTxCountsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 5),
    _CwsPortTotalTxCountsMulticastPackets_Type()
)
cwsPortTotalTxCountsMulticastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsMulticastPackets.setStatus("current")
_CwsPortTotalTxCountsBroadcastPackets_Type = Counter64
_CwsPortTotalTxCountsBroadcastPackets_Object = MibTableColumn
cwsPortTotalTxCountsBroadcastPackets = _CwsPortTotalTxCountsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 6),
    _CwsPortTotalTxCountsBroadcastPackets_Type()
)
cwsPortTotalTxCountsBroadcastPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsBroadcastPackets.setStatus("current")
_CwsPortTotalTxCountsPausePackets_Type = Counter64
_CwsPortTotalTxCountsPausePackets_Object = MibTableColumn
cwsPortTotalTxCountsPausePackets = _CwsPortTotalTxCountsPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 7),
    _CwsPortTotalTxCountsPausePackets_Type()
)
cwsPortTotalTxCountsPausePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsPausePackets.setStatus("current")
_CwsPortTotalTxCountsExcessiveDeferredPackets_Type = Counter64
_CwsPortTotalTxCountsExcessiveDeferredPackets_Object = MibTableColumn
cwsPortTotalTxCountsExcessiveDeferredPackets = _CwsPortTotalTxCountsExcessiveDeferredPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 8),
    _CwsPortTotalTxCountsExcessiveDeferredPackets_Type()
)
cwsPortTotalTxCountsExcessiveDeferredPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsExcessiveDeferredPackets.setStatus("current")
_CwsPortTotalTxCountsGiantPackets_Type = Counter64
_CwsPortTotalTxCountsGiantPackets_Object = MibTableColumn
cwsPortTotalTxCountsGiantPackets = _CwsPortTotalTxCountsGiantPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 9),
    _CwsPortTotalTxCountsGiantPackets_Type()
)
cwsPortTotalTxCountsGiantPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsGiantPackets.setStatus("current")
_CwsPortTotalTxCountsUnderrunPackets_Type = Counter64
_CwsPortTotalTxCountsUnderrunPackets_Object = MibTableColumn
cwsPortTotalTxCountsUnderrunPackets = _CwsPortTotalTxCountsUnderrunPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 10),
    _CwsPortTotalTxCountsUnderrunPackets_Type()
)
cwsPortTotalTxCountsUnderrunPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsUnderrunPackets.setStatus("current")
_CwsPortTotalTxCountsLengthCheckErrorPackets_Type = Counter64
_CwsPortTotalTxCountsLengthCheckErrorPackets_Object = MibTableColumn
cwsPortTotalTxCountsLengthCheckErrorPackets = _CwsPortTotalTxCountsLengthCheckErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 11),
    _CwsPortTotalTxCountsLengthCheckErrorPackets_Type()
)
cwsPortTotalTxCountsLengthCheckErrorPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsLengthCheckErrorPackets.setStatus("current")
_CwsPortTotalTxCountsLengthOutRangePackets_Type = Counter64
_CwsPortTotalTxCountsLengthOutRangePackets_Object = MibTableColumn
cwsPortTotalTxCountsLengthOutRangePackets = _CwsPortTotalTxCountsLengthOutRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 12),
    _CwsPortTotalTxCountsLengthOutRangePackets_Type()
)
cwsPortTotalTxCountsLengthOutRangePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsLengthOutRangePackets.setStatus("current")
_CwsPortTotalTxCountsAverageLinkUtilization_Type = Decimal1Dig
_CwsPortTotalTxCountsAverageLinkUtilization_Object = MibTableColumn
cwsPortTotalTxCountsAverageLinkUtilization = _CwsPortTotalTxCountsAverageLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 22, 1, 13),
    _CwsPortTotalTxCountsAverageLinkUtilization_Type()
)
cwsPortTotalTxCountsAverageLinkUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxCountsAverageLinkUtilization.setStatus("current")
_CwsPortTotalTxQueueTable_Object = MibTable
cwsPortTotalTxQueueTable = _CwsPortTotalTxQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 23)
)
if mibBuilder.loadTexts:
    cwsPortTotalTxQueueTable.setStatus("current")
_CwsPortTotalTxQueueEntry_Object = MibTableRow
cwsPortTotalTxQueueEntry = _CwsPortTotalTxQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 23, 1)
)
cwsPortTotalTxQueueEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortTotalTxQueueTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortTotalTxQueueEntry.setStatus("current")


class _CwsPortTotalTxQueueTableSnmpKey_Type(Integer32):
    """Custom type cwsPortTotalTxQueueTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortTotalTxQueueTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortTotalTxQueueTableSnmpKey_Object = MibTableColumn
cwsPortTotalTxQueueTableSnmpKey = _CwsPortTotalTxQueueTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 23, 1, 1),
    _CwsPortTotalTxQueueTableSnmpKey_Type()
)
cwsPortTotalTxQueueTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortTotalTxQueueTableSnmpKey.setStatus("current")
_CwsPortTotalTxQueuePacketDropCountSummary_Type = Counter64
_CwsPortTotalTxQueuePacketDropCountSummary_Object = MibTableColumn
cwsPortTotalTxQueuePacketDropCountSummary = _CwsPortTotalTxQueuePacketDropCountSummary_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 23, 1, 2),
    _CwsPortTotalTxQueuePacketDropCountSummary_Type()
)
cwsPortTotalTxQueuePacketDropCountSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxQueuePacketDropCountSummary.setStatus("current")
_CwsPortTotalTxQueueQ0PacketDropCount_Type = Counter64
_CwsPortTotalTxQueueQ0PacketDropCount_Object = MibTableColumn
cwsPortTotalTxQueueQ0PacketDropCount = _CwsPortTotalTxQueueQ0PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 23, 1, 3),
    _CwsPortTotalTxQueueQ0PacketDropCount_Type()
)
cwsPortTotalTxQueueQ0PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxQueueQ0PacketDropCount.setStatus("current")
_CwsPortTotalTxQueueQ1PacketDropCount_Type = Counter64
_CwsPortTotalTxQueueQ1PacketDropCount_Object = MibTableColumn
cwsPortTotalTxQueueQ1PacketDropCount = _CwsPortTotalTxQueueQ1PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 23, 1, 4),
    _CwsPortTotalTxQueueQ1PacketDropCount_Type()
)
cwsPortTotalTxQueueQ1PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxQueueQ1PacketDropCount.setStatus("current")
_CwsPortTotalTxQueueQ2PacketDropCount_Type = Counter64
_CwsPortTotalTxQueueQ2PacketDropCount_Object = MibTableColumn
cwsPortTotalTxQueueQ2PacketDropCount = _CwsPortTotalTxQueueQ2PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 23, 1, 5),
    _CwsPortTotalTxQueueQ2PacketDropCount_Type()
)
cwsPortTotalTxQueueQ2PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxQueueQ2PacketDropCount.setStatus("current")
_CwsPortTotalTxQueueQ3PacketDropCount_Type = Counter64
_CwsPortTotalTxQueueQ3PacketDropCount_Object = MibTableColumn
cwsPortTotalTxQueueQ3PacketDropCount = _CwsPortTotalTxQueueQ3PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 23, 1, 6),
    _CwsPortTotalTxQueueQ3PacketDropCount_Type()
)
cwsPortTotalTxQueueQ3PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxQueueQ3PacketDropCount.setStatus("current")
_CwsPortTotalTxQueueQ4PacketDropCount_Type = Counter64
_CwsPortTotalTxQueueQ4PacketDropCount_Object = MibTableColumn
cwsPortTotalTxQueueQ4PacketDropCount = _CwsPortTotalTxQueueQ4PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 23, 1, 7),
    _CwsPortTotalTxQueueQ4PacketDropCount_Type()
)
cwsPortTotalTxQueueQ4PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxQueueQ4PacketDropCount.setStatus("current")
_CwsPortTotalTxQueueQ5PacketDropCount_Type = Counter64
_CwsPortTotalTxQueueQ5PacketDropCount_Object = MibTableColumn
cwsPortTotalTxQueueQ5PacketDropCount = _CwsPortTotalTxQueueQ5PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 23, 1, 8),
    _CwsPortTotalTxQueueQ5PacketDropCount_Type()
)
cwsPortTotalTxQueueQ5PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxQueueQ5PacketDropCount.setStatus("current")
_CwsPortTotalTxQueueQ6PacketDropCount_Type = Counter64
_CwsPortTotalTxQueueQ6PacketDropCount_Object = MibTableColumn
cwsPortTotalTxQueueQ6PacketDropCount = _CwsPortTotalTxQueueQ6PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 23, 1, 9),
    _CwsPortTotalTxQueueQ6PacketDropCount_Type()
)
cwsPortTotalTxQueueQ6PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxQueueQ6PacketDropCount.setStatus("current")
_CwsPortTotalTxQueueQ7PacketDropCount_Type = Counter64
_CwsPortTotalTxQueueQ7PacketDropCount_Object = MibTableColumn
cwsPortTotalTxQueueQ7PacketDropCount = _CwsPortTotalTxQueueQ7PacketDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 23, 1, 10),
    _CwsPortTotalTxQueueQ7PacketDropCount_Type()
)
cwsPortTotalTxQueueQ7PacketDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalTxQueueQ7PacketDropCount.setStatus("current")
_CwsPortTotalMacTable_Object = MibTable
cwsPortTotalMacTable = _CwsPortTotalMacTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 24)
)
if mibBuilder.loadTexts:
    cwsPortTotalMacTable.setStatus("obsolete")
_CwsPortTotalMacEntry_Object = MibTableRow
cwsPortTotalMacEntry = _CwsPortTotalMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 24, 1)
)
cwsPortTotalMacEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortTotalMacTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortTotalMacEntry.setStatus("obsolete")


class _CwsPortTotalMacTableSnmpKey_Type(Integer32):
    """Custom type cwsPortTotalMacTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortTotalMacTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortTotalMacTableSnmpKey_Object = MibTableColumn
cwsPortTotalMacTableSnmpKey = _CwsPortTotalMacTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 24, 1, 1),
    _CwsPortTotalMacTableSnmpKey_Type()
)
cwsPortTotalMacTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortTotalMacTableSnmpKey.setStatus("current")
_CwsPortTotalMacUnavailableSeconds_Type = Counter64
_CwsPortTotalMacUnavailableSeconds_Object = MibTableColumn
cwsPortTotalMacUnavailableSeconds = _CwsPortTotalMacUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 24, 1, 2),
    _CwsPortTotalMacUnavailableSeconds_Type()
)
cwsPortTotalMacUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortTotalMacUnavailableSeconds.setStatus("obsolete")
_CwsPortTotalPcsTable_Object = MibTable
cwsPortTotalPcsTable = _CwsPortTotalPcsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 25)
)
if mibBuilder.loadTexts:
    cwsPortTotalPcsTable.setStatus("current")
_CwsPortTotalPcsEntry_Object = MibTableRow
cwsPortTotalPcsEntry = _CwsPortTotalPcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 25, 1)
)
cwsPortTotalPcsEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortTotalPcsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortTotalPcsEntry.setStatus("current")


class _CwsPortTotalPcsTableSnmpKey_Type(Integer32):
    """Custom type cwsPortTotalPcsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortTotalPcsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortTotalPcsTableSnmpKey_Object = MibTableColumn
cwsPortTotalPcsTableSnmpKey = _CwsPortTotalPcsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 25, 1, 1),
    _CwsPortTotalPcsTableSnmpKey_Type()
)
cwsPortTotalPcsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortTotalPcsTableSnmpKey.setStatus("current")
_CwsPortTotalPcsErroredSeconds_Type = Counter64
_CwsPortTotalPcsErroredSeconds_Object = MibTableColumn
cwsPortTotalPcsErroredSeconds = _CwsPortTotalPcsErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 25, 1, 2),
    _CwsPortTotalPcsErroredSeconds_Type()
)
cwsPortTotalPcsErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalPcsErroredSeconds.setStatus("current")
_CwsPortTotalPcsSeverelyErroredSeconds_Type = Counter64
_CwsPortTotalPcsSeverelyErroredSeconds_Object = MibTableColumn
cwsPortTotalPcsSeverelyErroredSeconds = _CwsPortTotalPcsSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 25, 1, 3),
    _CwsPortTotalPcsSeverelyErroredSeconds_Type()
)
cwsPortTotalPcsSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalPcsSeverelyErroredSeconds.setStatus("current")
_CwsPortTotalPcsUnavailableSeconds_Type = Counter64
_CwsPortTotalPcsUnavailableSeconds_Object = MibTableColumn
cwsPortTotalPcsUnavailableSeconds = _CwsPortTotalPcsUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 25, 1, 4),
    _CwsPortTotalPcsUnavailableSeconds_Type()
)
cwsPortTotalPcsUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalPcsUnavailableSeconds.setStatus("current")
_CwsPortTotalPcsSyncHeaderErrorsTable_Object = MibTable
cwsPortTotalPcsSyncHeaderErrorsTable = _CwsPortTotalPcsSyncHeaderErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 26)
)
if mibBuilder.loadTexts:
    cwsPortTotalPcsSyncHeaderErrorsTable.setStatus("current")
_CwsPortTotalPcsSyncHeaderErrorsEntry_Object = MibTableRow
cwsPortTotalPcsSyncHeaderErrorsEntry = _CwsPortTotalPcsSyncHeaderErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 26, 1)
)
cwsPortTotalPcsSyncHeaderErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortTotalPcsSyncHeaderErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortTotalPcsSyncHeaderErrorsEntry.setStatus("current")


class _CwsPortTotalPcsSyncHeaderErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPortTotalPcsSyncHeaderErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortTotalPcsSyncHeaderErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortTotalPcsSyncHeaderErrorsTableSnmpKey_Object = MibTableColumn
cwsPortTotalPcsSyncHeaderErrorsTableSnmpKey = _CwsPortTotalPcsSyncHeaderErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 26, 1, 1),
    _CwsPortTotalPcsSyncHeaderErrorsTableSnmpKey_Type()
)
cwsPortTotalPcsSyncHeaderErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortTotalPcsSyncHeaderErrorsTableSnmpKey.setStatus("current")
_CwsPortTotalPcsSyncHeaderErrorsCount_Type = Counter64
_CwsPortTotalPcsSyncHeaderErrorsCount_Object = MibTableColumn
cwsPortTotalPcsSyncHeaderErrorsCount = _CwsPortTotalPcsSyncHeaderErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 26, 1, 2),
    _CwsPortTotalPcsSyncHeaderErrorsCount_Type()
)
cwsPortTotalPcsSyncHeaderErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortTotalPcsSyncHeaderErrorsCount.setStatus("current")
_CwsPortTotalPcsBlockErrorsTable_Object = MibTable
cwsPortTotalPcsBlockErrorsTable = _CwsPortTotalPcsBlockErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 27)
)
if mibBuilder.loadTexts:
    cwsPortTotalPcsBlockErrorsTable.setStatus("current")
_CwsPortTotalPcsBlockErrorsEntry_Object = MibTableRow
cwsPortTotalPcsBlockErrorsEntry = _CwsPortTotalPcsBlockErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 27, 1)
)
cwsPortTotalPcsBlockErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortTotalPcsBlockErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortTotalPcsBlockErrorsEntry.setStatus("current")


class _CwsPortTotalPcsBlockErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPortTotalPcsBlockErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortTotalPcsBlockErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortTotalPcsBlockErrorsTableSnmpKey_Object = MibTableColumn
cwsPortTotalPcsBlockErrorsTableSnmpKey = _CwsPortTotalPcsBlockErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 27, 1, 1),
    _CwsPortTotalPcsBlockErrorsTableSnmpKey_Type()
)
cwsPortTotalPcsBlockErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortTotalPcsBlockErrorsTableSnmpKey.setStatus("current")
_CwsPortTotalPcsBlockErrorsCount_Type = Counter64
_CwsPortTotalPcsBlockErrorsCount_Object = MibTableColumn
cwsPortTotalPcsBlockErrorsCount = _CwsPortTotalPcsBlockErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 27, 1, 2),
    _CwsPortTotalPcsBlockErrorsCount_Type()
)
cwsPortTotalPcsBlockErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortTotalPcsBlockErrorsCount.setStatus("current")
_CwsPortTotalPcsMultilaneBipErrorsTable_Object = MibTable
cwsPortTotalPcsMultilaneBipErrorsTable = _CwsPortTotalPcsMultilaneBipErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 28)
)
if mibBuilder.loadTexts:
    cwsPortTotalPcsMultilaneBipErrorsTable.setStatus("current")
_CwsPortTotalPcsMultilaneBipErrorsEntry_Object = MibTableRow
cwsPortTotalPcsMultilaneBipErrorsEntry = _CwsPortTotalPcsMultilaneBipErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 28, 1)
)
cwsPortTotalPcsMultilaneBipErrorsEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortTotalPcsMultilaneBipErrorsTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortTotalPcsMultilaneBipErrorsEntry.setStatus("current")


class _CwsPortTotalPcsMultilaneBipErrorsTableSnmpKey_Type(Integer32):
    """Custom type cwsPortTotalPcsMultilaneBipErrorsTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortTotalPcsMultilaneBipErrorsTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortTotalPcsMultilaneBipErrorsTableSnmpKey_Object = MibTableColumn
cwsPortTotalPcsMultilaneBipErrorsTableSnmpKey = _CwsPortTotalPcsMultilaneBipErrorsTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 28, 1, 1),
    _CwsPortTotalPcsMultilaneBipErrorsTableSnmpKey_Type()
)
cwsPortTotalPcsMultilaneBipErrorsTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortTotalPcsMultilaneBipErrorsTableSnmpKey.setStatus("current")
_CwsPortTotalPcsMultilaneBipErrorsCount_Type = Counter64
_CwsPortTotalPcsMultilaneBipErrorsCount_Object = MibTableColumn
cwsPortTotalPcsMultilaneBipErrorsCount = _CwsPortTotalPcsMultilaneBipErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 28, 1, 2),
    _CwsPortTotalPcsMultilaneBipErrorsCount_Type()
)
cwsPortTotalPcsMultilaneBipErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortTotalPcsMultilaneBipErrorsCount.setStatus("current")
_CwsPortTotalFecTable_Object = MibTable
cwsPortTotalFecTable = _CwsPortTotalFecTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 29)
)
if mibBuilder.loadTexts:
    cwsPortTotalFecTable.setStatus("current")
_CwsPortTotalFecEntry_Object = MibTableRow
cwsPortTotalFecEntry = _CwsPortTotalFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 29, 1)
)
cwsPortTotalFecEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortTotalFecTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortTotalFecEntry.setStatus("current")


class _CwsPortTotalFecTableSnmpKey_Type(Integer32):
    """Custom type cwsPortTotalFecTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortTotalFecTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortTotalFecTableSnmpKey_Object = MibTableColumn
cwsPortTotalFecTableSnmpKey = _CwsPortTotalFecTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 29, 1, 1),
    _CwsPortTotalFecTableSnmpKey_Type()
)
cwsPortTotalFecTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortTotalFecTableSnmpKey.setStatus("current")
_CwsPortTotalFecCorrectedBlockCount_Type = Counter64
_CwsPortTotalFecCorrectedBlockCount_Object = MibTableColumn
cwsPortTotalFecCorrectedBlockCount = _CwsPortTotalFecCorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 29, 1, 2),
    _CwsPortTotalFecCorrectedBlockCount_Type()
)
cwsPortTotalFecCorrectedBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortTotalFecCorrectedBlockCount.setStatus("current")
_CwsPortTotalFecUncorrectedBlockCount_Type = Counter64
_CwsPortTotalFecUncorrectedBlockCount_Object = MibTableColumn
cwsPortTotalFecUncorrectedBlockCount = _CwsPortTotalFecUncorrectedBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 29, 1, 3),
    _CwsPortTotalFecUncorrectedBlockCount_Type()
)
cwsPortTotalFecUncorrectedBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortTotalFecUncorrectedBlockCount.setStatus("current")
_CwsPortTotalFecSymbolErrorCount_Type = Counter64
_CwsPortTotalFecSymbolErrorCount_Object = MibTableColumn
cwsPortTotalFecSymbolErrorCount = _CwsPortTotalFecSymbolErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 29, 1, 4),
    _CwsPortTotalFecSymbolErrorCount_Type()
)
cwsPortTotalFecSymbolErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPortTotalFecSymbolErrorCount.setStatus("current")
_CwsPortCurrentOduTable_Object = MibTable
cwsPortCurrentOduTable = _CwsPortCurrentOduTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 30)
)
if mibBuilder.loadTexts:
    cwsPortCurrentOduTable.setStatus("current")
_CwsPortCurrentOduEntry_Object = MibTableRow
cwsPortCurrentOduEntry = _CwsPortCurrentOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 30, 1)
)
cwsPortCurrentOduEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortCurrentOduTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortCurrentOduEntry.setStatus("current")


class _CwsPortCurrentOduTableSnmpKey_Type(Integer32):
    """Custom type cwsPortCurrentOduTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortCurrentOduTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortCurrentOduTableSnmpKey_Object = MibTableColumn
cwsPortCurrentOduTableSnmpKey = _CwsPortCurrentOduTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 30, 1, 1),
    _CwsPortCurrentOduTableSnmpKey_Type()
)
cwsPortCurrentOduTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortCurrentOduTableSnmpKey.setStatus("current")
_CwsPortCurrentOduErroredSeconds_Type = Counter64
_CwsPortCurrentOduErroredSeconds_Object = MibTableColumn
cwsPortCurrentOduErroredSeconds = _CwsPortCurrentOduErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 30, 1, 2),
    _CwsPortCurrentOduErroredSeconds_Type()
)
cwsPortCurrentOduErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentOduErroredSeconds.setStatus("current")
_CwsPortCurrentOduSeverelyErroredSeconds_Type = Counter64
_CwsPortCurrentOduSeverelyErroredSeconds_Object = MibTableColumn
cwsPortCurrentOduSeverelyErroredSeconds = _CwsPortCurrentOduSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 30, 1, 3),
    _CwsPortCurrentOduSeverelyErroredSeconds_Type()
)
cwsPortCurrentOduSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentOduSeverelyErroredSeconds.setStatus("current")
_CwsPortCurrentOduUnavailableSeconds_Type = Counter64
_CwsPortCurrentOduUnavailableSeconds_Object = MibTableColumn
cwsPortCurrentOduUnavailableSeconds = _CwsPortCurrentOduUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 30, 1, 4),
    _CwsPortCurrentOduUnavailableSeconds_Type()
)
cwsPortCurrentOduUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortCurrentOduUnavailableSeconds.setStatus("current")
_CwsPortTotalOduTable_Object = MibTable
cwsPortTotalOduTable = _CwsPortTotalOduTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 31)
)
if mibBuilder.loadTexts:
    cwsPortTotalOduTable.setStatus("current")
_CwsPortTotalOduEntry_Object = MibTableRow
cwsPortTotalOduEntry = _CwsPortTotalOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 31, 1)
)
cwsPortTotalOduEntry.setIndexNames(
    (0, "CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-PORT-MIB", "cwsPortTotalOduTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsPortTotalOduEntry.setStatus("current")


class _CwsPortTotalOduTableSnmpKey_Type(Integer32):
    """Custom type cwsPortTotalOduTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPortTotalOduTableSnmpKey_Type.__name__ = "Integer32"
_CwsPortTotalOduTableSnmpKey_Object = MibTableColumn
cwsPortTotalOduTableSnmpKey = _CwsPortTotalOduTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 31, 1, 1),
    _CwsPortTotalOduTableSnmpKey_Type()
)
cwsPortTotalOduTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsPortTotalOduTableSnmpKey.setStatus("current")
_CwsPortTotalOduErroredSeconds_Type = Counter64
_CwsPortTotalOduErroredSeconds_Object = MibTableColumn
cwsPortTotalOduErroredSeconds = _CwsPortTotalOduErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 31, 1, 2),
    _CwsPortTotalOduErroredSeconds_Type()
)
cwsPortTotalOduErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalOduErroredSeconds.setStatus("current")
_CwsPortTotalOduSeverelyErroredSeconds_Type = Counter64
_CwsPortTotalOduSeverelyErroredSeconds_Object = MibTableColumn
cwsPortTotalOduSeverelyErroredSeconds = _CwsPortTotalOduSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 31, 1, 3),
    _CwsPortTotalOduSeverelyErroredSeconds_Type()
)
cwsPortTotalOduSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalOduSeverelyErroredSeconds.setStatus("current")
_CwsPortTotalOduUnavailableSeconds_Type = Counter64
_CwsPortTotalOduUnavailableSeconds_Object = MibTableColumn
cwsPortTotalOduUnavailableSeconds = _CwsPortTotalOduUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 31, 1, 4),
    _CwsPortTotalOduUnavailableSeconds_Type()
)
cwsPortTotalOduUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPortTotalOduUnavailableSeconds.setStatus("current")

# Managed Objects groups

cienaWsPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 2, 1, 1)
)
cienaWsPortGroup.setObjects(
      *(("CIENA-WS-PORT-MIB", "cwsPortPortsPortId"),
        ("CIENA-WS-PORT-MIB", "cwsPortIdName"),
        ("CIENA-WS-PORT-MIB", "cwsPortIdDescription"),
        ("CIENA-WS-PORT-MIB", "cwsPortIdPortType"),
        ("CIENA-WS-PORT-MIB", "cwsPortIdMacAddress"),
        ("CIENA-WS-PORT-MIB", "cwsPortIdInterfaceType"),
        ("CIENA-WS-PORT-MIB", "cwsPortStateAdminState"),
        ("CIENA-WS-PORT-MIB", "cwsPortStateOperationalState"),
        ("CIENA-WS-PORT-MIB", "cwsPortStateOperationalStateDuration"),
        ("CIENA-WS-PORT-MIB", "cwsPortCapabilitiesPortSpeeds"),
        ("CIENA-WS-PORT-MIB", "cwsPortCapabilitiesDuplex"),
        ("CIENA-WS-PORT-MIB", "cwsPortCapabilitiesAutoNegotiation"),
        ("CIENA-WS-PORT-MIB", "cwsPortCapabilitiesFlowControl"),
        ("CIENA-WS-PORT-MIB", "cwsPortCapabilitiesFecSupport"),
        ("CIENA-WS-PORT-MIB", "cwsPortPropertiesXcvrType"),
        ("CIENA-WS-PORT-MIB", "cwsPortPropertiesLoopback"),
        ("CIENA-WS-PORT-MIB", "cwsPortPropertiesServiceIndex"),
        ("CIENA-WS-PORT-MIB", "cwsPortPropertiesServiceDomainIndex"),
        ("CIENA-WS-PORT-MIB", "cwsPortEthernetSpeed"),
        ("CIENA-WS-PORT-MIB", "cwsPortEthernetMaxFrameSize"),
        ("CIENA-WS-PORT-MIB", "cwsPortEthernetPauseProfile"),
        ("CIENA-WS-PORT-MIB", "cwsPortEthernetForwardErrorCorrection"),
        ("CIENA-WS-PORT-MIB", "cwsPortConditioningType"),
        ("CIENA-WS-PORT-MIB", "cwsPortConditioningHoldoff"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentFrameErrorRatio"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsBytes"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsAverageLinkUtilization"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsCrcErroredPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsMulticastPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsBroadcastPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsPausePackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsUndersizedPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsOversizedPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsFragmentPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsJabberPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsLengthOutRangePackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsPackets64Octet"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsPackets65127Octet"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsPackets128255Octet"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsPackets256511Octet"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsPackets5121023Octet"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentRxCountsPackets10241518Octet"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsBytes"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsAverageLinkUtilization"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsCrcErroredPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsMulticastPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsBroadcastPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsPausePackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsExcessiveDeferredPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsGiantPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsUnderrunPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsLengthCheckErrorPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxCountsLengthOutRangePackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxQueuePacketDropCountSummary"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxQueueQ0PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxQueueQ1PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxQueueQ2PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxQueueQ3PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxQueueQ4PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxQueueQ5PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxQueueQ6PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentTxQueueQ7PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentMacUnavailableSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortPcsCurrentErroredSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortPcsCurrentSeverelyErroredSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortPcsCurrentUnavailableSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentPcsSyncHeaderErrorsCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentPcsBlockErrorsCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentPcsMultilaneBipErrorsCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentOduErroredSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentOduSeverelyErroredSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentOduUnavailableSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentFecCorrectedBlockCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentFecUncorrectedBlockCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortCurrentFecSymbolErrorCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalFrameErrorRatio"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsBytes"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsAverageLinkUtilization"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsCrcErroredPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsMulticastPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsBroadcastPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsPausePackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsUndersizedPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsOversizedPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsFragmentPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsJabberPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsLengthOutRangePackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsPackets64Octet"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsPackets65127Octet"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsPackets128255Octet"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsPackets256511Octet"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsPackets5121023Octet"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalRxCountsPackets10241518Octet"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsBytes"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsAverageLinkUtilization"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsCrcErroredPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsMulticastPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsBroadcastPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsPausePackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsExcessiveDeferredPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsGiantPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsUnderrunPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsLengthCheckErrorPackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxCountsLengthOutRangePackets"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxQueuePacketDropCountSummary"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxQueueQ0PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxQueueQ1PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxQueueQ2PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxQueueQ3PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxQueueQ4PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxQueueQ5PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxQueueQ6PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalTxQueueQ7PacketDropCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalMacUnavailableSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalPcsErroredSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalPcsSeverelyErroredSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalPcsUnavailableSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalPcsSyncHeaderErrorsCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalPcsBlockErrorsCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalPcsMultilaneBipErrorsCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalOduErroredSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalOduSeverelyErroredSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalOduUnavailableSeconds"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalFecCorrectedBlockCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalFecUncorrectedBlockCount"),
        ("CIENA-WS-PORT-MIB", "cwsPortTotalFecSymbolErrorCount"))
)
if mibBuilder.loadTexts:
    cienaWsPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 7, 2, 2, 1)
)
cienaWsPortCompliance.setObjects(
    ("CIENA-WS-PORT-MIB", "cienaWsPortGroup")
)
if mibBuilder.loadTexts:
    cienaWsPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-PORT-MIB",
    **{"PortOperationalState": PortOperationalState,
       "PortSpeed": PortSpeed,
       "PortTypeEnum": PortTypeEnum,
       "cienaWsPortMIB": cienaWsPortMIB,
       "cienaWsPortObjects": cienaWsPortObjects,
       "cienaWsPortConformance": cienaWsPortConformance,
       "cienaWsPortGroups": cienaWsPortGroups,
       "cienaWsPortGroup": cienaWsPortGroup,
       "cienaWsPortCompliances": cienaWsPortCompliances,
       "cienaWsPortCompliance": cienaWsPortCompliance,
       "cwsPortPortsTable": cwsPortPortsTable,
       "cwsPortPortsEntry": cwsPortPortsEntry,
       "cwsPortPortsPortId": cwsPortPortsPortId,
       "cwsPortIdTable": cwsPortIdTable,
       "cwsPortIdEntry": cwsPortIdEntry,
       "cwsPortIdTableSnmpKey": cwsPortIdTableSnmpKey,
       "cwsPortIdName": cwsPortIdName,
       "cwsPortIdDescription": cwsPortIdDescription,
       "cwsPortIdPortType": cwsPortIdPortType,
       "cwsPortIdMacAddress": cwsPortIdMacAddress,
       "cwsPortIdInterfaceType": cwsPortIdInterfaceType,
       "cwsPortStateTable": cwsPortStateTable,
       "cwsPortStateEntry": cwsPortStateEntry,
       "cwsPortStateTableSnmpKey": cwsPortStateTableSnmpKey,
       "cwsPortStateAdminState": cwsPortStateAdminState,
       "cwsPortStateOperationalState": cwsPortStateOperationalState,
       "cwsPortStateOperationalStateDuration": cwsPortStateOperationalStateDuration,
       "cwsPortCapabilitiesTable": cwsPortCapabilitiesTable,
       "cwsPortCapabilitiesEntry": cwsPortCapabilitiesEntry,
       "cwsPortCapabilitiesTableSnmpKey": cwsPortCapabilitiesTableSnmpKey,
       "cwsPortCapabilitiesPortSpeeds": cwsPortCapabilitiesPortSpeeds,
       "cwsPortCapabilitiesDuplex": cwsPortCapabilitiesDuplex,
       "cwsPortCapabilitiesAutoNegotiation": cwsPortCapabilitiesAutoNegotiation,
       "cwsPortCapabilitiesFlowControl": cwsPortCapabilitiesFlowControl,
       "cwsPortCapabilitiesFecSupport": cwsPortCapabilitiesFecSupport,
       "cwsPortPropertiesTable": cwsPortPropertiesTable,
       "cwsPortPropertiesEntry": cwsPortPropertiesEntry,
       "cwsPortPropertiesTableSnmpKey": cwsPortPropertiesTableSnmpKey,
       "cwsPortPropertiesLoopback": cwsPortPropertiesLoopback,
       "cwsPortPropertiesServiceIndex": cwsPortPropertiesServiceIndex,
       "cwsPortPropertiesServiceDomainIndex": cwsPortPropertiesServiceDomainIndex,
       "cwsPortPropertiesXcvrType": cwsPortPropertiesXcvrType,
       "cwsPortEthernetTable": cwsPortEthernetTable,
       "cwsPortEthernetEntry": cwsPortEthernetEntry,
       "cwsPortEthernetTableSnmpKey": cwsPortEthernetTableSnmpKey,
       "cwsPortEthernetSpeed": cwsPortEthernetSpeed,
       "cwsPortEthernetMaxFrameSize": cwsPortEthernetMaxFrameSize,
       "cwsPortEthernetPauseProfile": cwsPortEthernetPauseProfile,
       "cwsPortEthernetForwardErrorCorrection": cwsPortEthernetForwardErrorCorrection,
       "cwsPortConditioningTable": cwsPortConditioningTable,
       "cwsPortConditioningEntry": cwsPortConditioningEntry,
       "cwsPortConditioningTableSnmpKey": cwsPortConditioningTableSnmpKey,
       "cwsPortConditioningType": cwsPortConditioningType,
       "cwsPortConditioningHoldoff": cwsPortConditioningHoldoff,
       "cwsPortCurrentTable": cwsPortCurrentTable,
       "cwsPortCurrentEntry": cwsPortCurrentEntry,
       "cwsPortCurrentTableSnmpKey": cwsPortCurrentTableSnmpKey,
       "cwsPortCurrentFrameErrorRatio": cwsPortCurrentFrameErrorRatio,
       "cwsPortCurrentRxCountsTable": cwsPortCurrentRxCountsTable,
       "cwsPortCurrentRxCountsEntry": cwsPortCurrentRxCountsEntry,
       "cwsPortCurrentRxCountsTableSnmpKey": cwsPortCurrentRxCountsTableSnmpKey,
       "cwsPortCurrentRxCountsBytes": cwsPortCurrentRxCountsBytes,
       "cwsPortCurrentRxCountsPackets": cwsPortCurrentRxCountsPackets,
       "cwsPortCurrentRxCountsCrcErroredPackets": cwsPortCurrentRxCountsCrcErroredPackets,
       "cwsPortCurrentRxCountsMulticastPackets": cwsPortCurrentRxCountsMulticastPackets,
       "cwsPortCurrentRxCountsBroadcastPackets": cwsPortCurrentRxCountsBroadcastPackets,
       "cwsPortCurrentRxCountsPausePackets": cwsPortCurrentRxCountsPausePackets,
       "cwsPortCurrentRxCountsUndersizedPackets": cwsPortCurrentRxCountsUndersizedPackets,
       "cwsPortCurrentRxCountsOversizedPackets": cwsPortCurrentRxCountsOversizedPackets,
       "cwsPortCurrentRxCountsFragmentPackets": cwsPortCurrentRxCountsFragmentPackets,
       "cwsPortCurrentRxCountsJabberPackets": cwsPortCurrentRxCountsJabberPackets,
       "cwsPortCurrentRxCountsLengthOutRangePackets": cwsPortCurrentRxCountsLengthOutRangePackets,
       "cwsPortCurrentRxCountsPackets64Octet": cwsPortCurrentRxCountsPackets64Octet,
       "cwsPortCurrentRxCountsPackets65127Octet": cwsPortCurrentRxCountsPackets65127Octet,
       "cwsPortCurrentRxCountsPackets128255Octet": cwsPortCurrentRxCountsPackets128255Octet,
       "cwsPortCurrentRxCountsPackets256511Octet": cwsPortCurrentRxCountsPackets256511Octet,
       "cwsPortCurrentRxCountsPackets5121023Octet": cwsPortCurrentRxCountsPackets5121023Octet,
       "cwsPortCurrentRxCountsPackets10241518Octet": cwsPortCurrentRxCountsPackets10241518Octet,
       "cwsPortCurrentRxCountsAverageLinkUtilization": cwsPortCurrentRxCountsAverageLinkUtilization,
       "cwsPortCurrentTxCountsTable": cwsPortCurrentTxCountsTable,
       "cwsPortCurrentTxCountsEntry": cwsPortCurrentTxCountsEntry,
       "cwsPortCurrentTxCountsTableSnmpKey": cwsPortCurrentTxCountsTableSnmpKey,
       "cwsPortCurrentTxCountsBytes": cwsPortCurrentTxCountsBytes,
       "cwsPortCurrentTxCountsPackets": cwsPortCurrentTxCountsPackets,
       "cwsPortCurrentTxCountsCrcErroredPackets": cwsPortCurrentTxCountsCrcErroredPackets,
       "cwsPortCurrentTxCountsMulticastPackets": cwsPortCurrentTxCountsMulticastPackets,
       "cwsPortCurrentTxCountsBroadcastPackets": cwsPortCurrentTxCountsBroadcastPackets,
       "cwsPortCurrentTxCountsPausePackets": cwsPortCurrentTxCountsPausePackets,
       "cwsPortCurrentTxCountsExcessiveDeferredPackets": cwsPortCurrentTxCountsExcessiveDeferredPackets,
       "cwsPortCurrentTxCountsGiantPackets": cwsPortCurrentTxCountsGiantPackets,
       "cwsPortCurrentTxCountsUnderrunPackets": cwsPortCurrentTxCountsUnderrunPackets,
       "cwsPortCurrentTxCountsLengthCheckErrorPackets": cwsPortCurrentTxCountsLengthCheckErrorPackets,
       "cwsPortCurrentTxCountsLengthOutRangePackets": cwsPortCurrentTxCountsLengthOutRangePackets,
       "cwsPortCurrentTxCountsAverageLinkUtilization": cwsPortCurrentTxCountsAverageLinkUtilization,
       "cwsPortCurrentTxQueueTable": cwsPortCurrentTxQueueTable,
       "cwsPortCurrentTxQueueEntry": cwsPortCurrentTxQueueEntry,
       "cwsPortCurrentTxQueueTableSnmpKey": cwsPortCurrentTxQueueTableSnmpKey,
       "cwsPortCurrentTxQueuePacketDropCountSummary": cwsPortCurrentTxQueuePacketDropCountSummary,
       "cwsPortCurrentTxQueueQ0PacketDropCount": cwsPortCurrentTxQueueQ0PacketDropCount,
       "cwsPortCurrentTxQueueQ1PacketDropCount": cwsPortCurrentTxQueueQ1PacketDropCount,
       "cwsPortCurrentTxQueueQ2PacketDropCount": cwsPortCurrentTxQueueQ2PacketDropCount,
       "cwsPortCurrentTxQueueQ3PacketDropCount": cwsPortCurrentTxQueueQ3PacketDropCount,
       "cwsPortCurrentTxQueueQ4PacketDropCount": cwsPortCurrentTxQueueQ4PacketDropCount,
       "cwsPortCurrentTxQueueQ5PacketDropCount": cwsPortCurrentTxQueueQ5PacketDropCount,
       "cwsPortCurrentTxQueueQ6PacketDropCount": cwsPortCurrentTxQueueQ6PacketDropCount,
       "cwsPortCurrentTxQueueQ7PacketDropCount": cwsPortCurrentTxQueueQ7PacketDropCount,
       "cwsPortCurrentMacTable": cwsPortCurrentMacTable,
       "cwsPortCurrentMacEntry": cwsPortCurrentMacEntry,
       "cwsPortCurrentMacTableSnmpKey": cwsPortCurrentMacTableSnmpKey,
       "cwsPortCurrentMacUnavailableSeconds": cwsPortCurrentMacUnavailableSeconds,
       "cwsPortPcsCurrentTable": cwsPortPcsCurrentTable,
       "cwsPortPcsCurrentEntry": cwsPortPcsCurrentEntry,
       "cwsPortPcsCurrentTableSnmpKey": cwsPortPcsCurrentTableSnmpKey,
       "cwsPortPcsCurrentErroredSeconds": cwsPortPcsCurrentErroredSeconds,
       "cwsPortPcsCurrentSeverelyErroredSeconds": cwsPortPcsCurrentSeverelyErroredSeconds,
       "cwsPortPcsCurrentUnavailableSeconds": cwsPortPcsCurrentUnavailableSeconds,
       "cwsPortCurrentPcsSyncHeaderErrorsTable": cwsPortCurrentPcsSyncHeaderErrorsTable,
       "cwsPortCurrentPcsSyncHeaderErrorsEntry": cwsPortCurrentPcsSyncHeaderErrorsEntry,
       "cwsPortCurrentPcsSyncHeaderErrorsTableSnmpKey": cwsPortCurrentPcsSyncHeaderErrorsTableSnmpKey,
       "cwsPortCurrentPcsSyncHeaderErrorsCount": cwsPortCurrentPcsSyncHeaderErrorsCount,
       "cwsPortCurrentPcsBlockErrorsTable": cwsPortCurrentPcsBlockErrorsTable,
       "cwsPortCurrentPcsBlockErrorsEntry": cwsPortCurrentPcsBlockErrorsEntry,
       "cwsPortCurrentPcsBlockErrorsTableSnmpKey": cwsPortCurrentPcsBlockErrorsTableSnmpKey,
       "cwsPortCurrentPcsBlockErrorsCount": cwsPortCurrentPcsBlockErrorsCount,
       "cwsPortCurrentPcsMultilaneBipErrorsTable": cwsPortCurrentPcsMultilaneBipErrorsTable,
       "cwsPortCurrentPcsMultilaneBipErrorsEntry": cwsPortCurrentPcsMultilaneBipErrorsEntry,
       "cwsPortCurrentPcsMultilaneBipErrorsTableSnmpKey": cwsPortCurrentPcsMultilaneBipErrorsTableSnmpKey,
       "cwsPortCurrentPcsMultilaneBipErrorsCount": cwsPortCurrentPcsMultilaneBipErrorsCount,
       "cwsPortCurrentFecTable": cwsPortCurrentFecTable,
       "cwsPortCurrentFecEntry": cwsPortCurrentFecEntry,
       "cwsPortCurrentFecTableSnmpKey": cwsPortCurrentFecTableSnmpKey,
       "cwsPortCurrentFecCorrectedBlockCount": cwsPortCurrentFecCorrectedBlockCount,
       "cwsPortCurrentFecUncorrectedBlockCount": cwsPortCurrentFecUncorrectedBlockCount,
       "cwsPortCurrentFecSymbolErrorCount": cwsPortCurrentFecSymbolErrorCount,
       "cwsPortTotalTable": cwsPortTotalTable,
       "cwsPortTotalEntry": cwsPortTotalEntry,
       "cwsPortTotalTableSnmpKey": cwsPortTotalTableSnmpKey,
       "cwsPortTotalFrameErrorRatio": cwsPortTotalFrameErrorRatio,
       "cwsPortTotalRxCountsTable": cwsPortTotalRxCountsTable,
       "cwsPortTotalRxCountsEntry": cwsPortTotalRxCountsEntry,
       "cwsPortTotalRxCountsTableSnmpKey": cwsPortTotalRxCountsTableSnmpKey,
       "cwsPortTotalRxCountsBytes": cwsPortTotalRxCountsBytes,
       "cwsPortTotalRxCountsPackets": cwsPortTotalRxCountsPackets,
       "cwsPortTotalRxCountsCrcErroredPackets": cwsPortTotalRxCountsCrcErroredPackets,
       "cwsPortTotalRxCountsMulticastPackets": cwsPortTotalRxCountsMulticastPackets,
       "cwsPortTotalRxCountsBroadcastPackets": cwsPortTotalRxCountsBroadcastPackets,
       "cwsPortTotalRxCountsPausePackets": cwsPortTotalRxCountsPausePackets,
       "cwsPortTotalRxCountsUndersizedPackets": cwsPortTotalRxCountsUndersizedPackets,
       "cwsPortTotalRxCountsOversizedPackets": cwsPortTotalRxCountsOversizedPackets,
       "cwsPortTotalRxCountsFragmentPackets": cwsPortTotalRxCountsFragmentPackets,
       "cwsPortTotalRxCountsJabberPackets": cwsPortTotalRxCountsJabberPackets,
       "cwsPortTotalRxCountsLengthOutRangePackets": cwsPortTotalRxCountsLengthOutRangePackets,
       "cwsPortTotalRxCountsPackets64Octet": cwsPortTotalRxCountsPackets64Octet,
       "cwsPortTotalRxCountsPackets65127Octet": cwsPortTotalRxCountsPackets65127Octet,
       "cwsPortTotalRxCountsPackets128255Octet": cwsPortTotalRxCountsPackets128255Octet,
       "cwsPortTotalRxCountsPackets256511Octet": cwsPortTotalRxCountsPackets256511Octet,
       "cwsPortTotalRxCountsPackets5121023Octet": cwsPortTotalRxCountsPackets5121023Octet,
       "cwsPortTotalRxCountsPackets10241518Octet": cwsPortTotalRxCountsPackets10241518Octet,
       "cwsPortTotalRxCountsAverageLinkUtilization": cwsPortTotalRxCountsAverageLinkUtilization,
       "cwsPortTotalTxCountsTable": cwsPortTotalTxCountsTable,
       "cwsPortTotalTxCountsEntry": cwsPortTotalTxCountsEntry,
       "cwsPortTotalTxCountsTableSnmpKey": cwsPortTotalTxCountsTableSnmpKey,
       "cwsPortTotalTxCountsBytes": cwsPortTotalTxCountsBytes,
       "cwsPortTotalTxCountsPackets": cwsPortTotalTxCountsPackets,
       "cwsPortTotalTxCountsCrcErroredPackets": cwsPortTotalTxCountsCrcErroredPackets,
       "cwsPortTotalTxCountsMulticastPackets": cwsPortTotalTxCountsMulticastPackets,
       "cwsPortTotalTxCountsBroadcastPackets": cwsPortTotalTxCountsBroadcastPackets,
       "cwsPortTotalTxCountsPausePackets": cwsPortTotalTxCountsPausePackets,
       "cwsPortTotalTxCountsExcessiveDeferredPackets": cwsPortTotalTxCountsExcessiveDeferredPackets,
       "cwsPortTotalTxCountsGiantPackets": cwsPortTotalTxCountsGiantPackets,
       "cwsPortTotalTxCountsUnderrunPackets": cwsPortTotalTxCountsUnderrunPackets,
       "cwsPortTotalTxCountsLengthCheckErrorPackets": cwsPortTotalTxCountsLengthCheckErrorPackets,
       "cwsPortTotalTxCountsLengthOutRangePackets": cwsPortTotalTxCountsLengthOutRangePackets,
       "cwsPortTotalTxCountsAverageLinkUtilization": cwsPortTotalTxCountsAverageLinkUtilization,
       "cwsPortTotalTxQueueTable": cwsPortTotalTxQueueTable,
       "cwsPortTotalTxQueueEntry": cwsPortTotalTxQueueEntry,
       "cwsPortTotalTxQueueTableSnmpKey": cwsPortTotalTxQueueTableSnmpKey,
       "cwsPortTotalTxQueuePacketDropCountSummary": cwsPortTotalTxQueuePacketDropCountSummary,
       "cwsPortTotalTxQueueQ0PacketDropCount": cwsPortTotalTxQueueQ0PacketDropCount,
       "cwsPortTotalTxQueueQ1PacketDropCount": cwsPortTotalTxQueueQ1PacketDropCount,
       "cwsPortTotalTxQueueQ2PacketDropCount": cwsPortTotalTxQueueQ2PacketDropCount,
       "cwsPortTotalTxQueueQ3PacketDropCount": cwsPortTotalTxQueueQ3PacketDropCount,
       "cwsPortTotalTxQueueQ4PacketDropCount": cwsPortTotalTxQueueQ4PacketDropCount,
       "cwsPortTotalTxQueueQ5PacketDropCount": cwsPortTotalTxQueueQ5PacketDropCount,
       "cwsPortTotalTxQueueQ6PacketDropCount": cwsPortTotalTxQueueQ6PacketDropCount,
       "cwsPortTotalTxQueueQ7PacketDropCount": cwsPortTotalTxQueueQ7PacketDropCount,
       "cwsPortTotalMacTable": cwsPortTotalMacTable,
       "cwsPortTotalMacEntry": cwsPortTotalMacEntry,
       "cwsPortTotalMacTableSnmpKey": cwsPortTotalMacTableSnmpKey,
       "cwsPortTotalMacUnavailableSeconds": cwsPortTotalMacUnavailableSeconds,
       "cwsPortTotalPcsTable": cwsPortTotalPcsTable,
       "cwsPortTotalPcsEntry": cwsPortTotalPcsEntry,
       "cwsPortTotalPcsTableSnmpKey": cwsPortTotalPcsTableSnmpKey,
       "cwsPortTotalPcsErroredSeconds": cwsPortTotalPcsErroredSeconds,
       "cwsPortTotalPcsSeverelyErroredSeconds": cwsPortTotalPcsSeverelyErroredSeconds,
       "cwsPortTotalPcsUnavailableSeconds": cwsPortTotalPcsUnavailableSeconds,
       "cwsPortTotalPcsSyncHeaderErrorsTable": cwsPortTotalPcsSyncHeaderErrorsTable,
       "cwsPortTotalPcsSyncHeaderErrorsEntry": cwsPortTotalPcsSyncHeaderErrorsEntry,
       "cwsPortTotalPcsSyncHeaderErrorsTableSnmpKey": cwsPortTotalPcsSyncHeaderErrorsTableSnmpKey,
       "cwsPortTotalPcsSyncHeaderErrorsCount": cwsPortTotalPcsSyncHeaderErrorsCount,
       "cwsPortTotalPcsBlockErrorsTable": cwsPortTotalPcsBlockErrorsTable,
       "cwsPortTotalPcsBlockErrorsEntry": cwsPortTotalPcsBlockErrorsEntry,
       "cwsPortTotalPcsBlockErrorsTableSnmpKey": cwsPortTotalPcsBlockErrorsTableSnmpKey,
       "cwsPortTotalPcsBlockErrorsCount": cwsPortTotalPcsBlockErrorsCount,
       "cwsPortTotalPcsMultilaneBipErrorsTable": cwsPortTotalPcsMultilaneBipErrorsTable,
       "cwsPortTotalPcsMultilaneBipErrorsEntry": cwsPortTotalPcsMultilaneBipErrorsEntry,
       "cwsPortTotalPcsMultilaneBipErrorsTableSnmpKey": cwsPortTotalPcsMultilaneBipErrorsTableSnmpKey,
       "cwsPortTotalPcsMultilaneBipErrorsCount": cwsPortTotalPcsMultilaneBipErrorsCount,
       "cwsPortTotalFecTable": cwsPortTotalFecTable,
       "cwsPortTotalFecEntry": cwsPortTotalFecEntry,
       "cwsPortTotalFecTableSnmpKey": cwsPortTotalFecTableSnmpKey,
       "cwsPortTotalFecCorrectedBlockCount": cwsPortTotalFecCorrectedBlockCount,
       "cwsPortTotalFecUncorrectedBlockCount": cwsPortTotalFecUncorrectedBlockCount,
       "cwsPortTotalFecSymbolErrorCount": cwsPortTotalFecSymbolErrorCount,
       "cwsPortCurrentOduTable": cwsPortCurrentOduTable,
       "cwsPortCurrentOduEntry": cwsPortCurrentOduEntry,
       "cwsPortCurrentOduTableSnmpKey": cwsPortCurrentOduTableSnmpKey,
       "cwsPortCurrentOduErroredSeconds": cwsPortCurrentOduErroredSeconds,
       "cwsPortCurrentOduSeverelyErroredSeconds": cwsPortCurrentOduSeverelyErroredSeconds,
       "cwsPortCurrentOduUnavailableSeconds": cwsPortCurrentOduUnavailableSeconds,
       "cwsPortTotalOduTable": cwsPortTotalOduTable,
       "cwsPortTotalOduEntry": cwsPortTotalOduEntry,
       "cwsPortTotalOduTableSnmpKey": cwsPortTotalOduTableSnmpKey,
       "cwsPortTotalOduErroredSeconds": cwsPortTotalOduErroredSeconds,
       "cwsPortTotalOduSeverelyErroredSeconds": cwsPortTotalOduSeverelyErroredSeconds,
       "cwsPortTotalOduUnavailableSeconds": cwsPortTotalOduUnavailableSeconds}
)
